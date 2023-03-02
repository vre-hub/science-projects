import ROOT
import os
scope="DMsummary.dileptonReinterpretation_14TeV.2018/"

def getDMCrossSection(medType):

    outfilename = scope+"DMCrossSectionGraphs_" + medType
    outfile     = ROOT.TFile("output/"+outfilename+".root","recreate")
    
    mgAcc     = ROOT.TMultiGraph()
    mgXsec    = ROOT.TMultiGraph()
    mgFidXsec = ROOT.TMultiGraph()
    mgWidth   = ROOT.TMultiGraph()
    mgAcc.SetName("mgAcc")
    mgXsec.SetName("mgXsec")
    mgFidXsec.SetName("mgFidXsec")
    mgWidth.SetName("mgWidth")

    infilename = "merged_DM_" + medType + "_ee_gDM_1p0"
    file = ROOT.TFile(infilename + ".root", "read")
    tuple = file.Get("events").Clone()

    statusCond   = "status_l1==23 && status_l2==23"
    twoLepCond   = "(n_l1>0 && n_l2>0)"
    fiducialCond = "(pt_l1>30 && pt_l2>30 && TMath::Abs(eta_l1)<2.5 && TMath::Abs(eta_l2)<2.5 && m_ll>((1000*mass)-(2*width)))"
    binning      = "(11850,0.150.,12.,41,-0.025,2.025)"

    tuple.Draw("massDM:mass>>hWidth"+binning,"100*width/(mass*1000.)","goff")
    tuple.Draw("massDM:mass>>hXsec"+binning,"xsec*1000.","goff")
    nTruthTotal = tuple.Draw("massDM:mass>>hTruth"+binning,"","goff")
    nAccTotal   = tuple.Draw("massDM:mass>>hAcc"+binning,fiducialCond,"goff")

    hWidth = ROOT.gROOT.FindObject("hWidth")
    hXsec  = ROOT.gROOT.FindObject("hXsec")
    hTruth = ROOT.gROOT.FindObject("hTruth")
    hAcc   = ROOT.gROOT.FindObject("hAcc")

    hWidth.Divide(hTruth)
    hXsec.Divide(hTruth)

    print("\n\n\nmass\twidth\tmassDM\txsec_truth\txsec_acc\tacc")

    nY = 0
    for yIndex in range(1,hTruth.GetNbinsY()):
        nY+=1

        acc = []
        xsec = []
        fidXsec = []
        width = []
        mass = []
        massDM = -1.

        nX = 0
        for xIndex in range(1,hTruth.GetNbinsX()):
            nX+=1
            nTruth = hTruth.GetBinContent(xIndex, yIndex)
            nAcc = hAcc.GetBinContent(xIndex, yIndex)
            #print("Truth:",nTruth,"\tAcc:",nAcc)
            if (nTruth < 1 or nAcc < 1): continue
            xsecBin = hXsec.GetBinContent(xIndex,yIndex)

#            print(hTruth.GetXaxis().GetBinCenter(xIndex))
            mass.append(hTruth.GetXaxis().GetBinCenter(xIndex))
            massDM = hTruth.GetYaxis().GetBinCenter(yIndex)
            accBin = (1.*nAcc)/nTruth
            width.append(hWidth.GetBinContent(xIndex,yIndex))
            xsec.append(xsecBin)
            acc.append(accBin)
            fidXsec.append(xsecBin*accBin)
            print("xIndex: ",nX,"\tyIndex: ",nY,"\n")

        print("Mass",mass,"\tLength:",len(mass),"\n\n")

        if ROOT.TMath.Abs(massDM)<0.00001: massDM = 0.
        outfile.cd()

        graphAcc = ROOT.TGraph(len(mass),mass[0],acc[0])
        graphXsec = ROOT.TGraph(len(mass),mass[0],xsec[0])
        graphFidXsec = ROOT.TGraph(len(mass),mass[0],fidXsec[0])
        graphWidth = ROOT.TGraph(len(mass),mass[0],width[0])

        massDMString = (ROOT.TString.Format("%.4f",massDM)).ReplaceAll(".","p")
        print("massDMString: ",massDMString)


def LoadXsecGraph(massDM,finalState):

    #To be replaced when getDMCrossSection() function is completed, for now load from file

    if finalState=="ee": file = ROOT.TFile.Open(scope+"DMCrossSectionGraphs_axial_ee.root","READ")
    else: file = ROOT.TFile.Open(scope+"DMCrossSectionGraphs_axial_mumu.root","READ")

    fidXsec = file.Get("graphFidXsec_"+massDM+"00")

    return fidXsec

def SetArrays(finalState):

    poleMass = []
    Width    = []
    neg95    = []
    neg68    = []
    central  = []
    pos68    = []
    pos95    = []

    if finalState == "ee":
        poleMass = [2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5]
        Width    = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
        neg95    = [1.04031e-05,2.83953e-06,1.40525e-06,1.22429e-06,1.93764e-06,6.58814e-06,2.77217e-05,4.30815e-05,4.53581e-05,4.7677e-05]
        neg68    = [1.34446e-05,3.89499e-06,2.02331e-06,1.67029e-06,2.90514e-06,9.48196e-06,3.94315e-05,5.87383e-05,6.347e-05,6.46488e-05]
        central  = [1.88798e-05,5.63752e-06,2.90367e-06,2.44504e-06,4.31562e-06,1.4725e-05,5.73635e-05,8.10394e-05,8.93357e-05,9.16786e-05]
        pos68    = [2.65541e-05,8.37326e-06,4.2378e-06,3.75409e-06,6.38766e-06,2.37465e-05,8.61154e-05,0.000114161,0.000121193,0.000126887]
        pos95    = [3.78479e-05,1.16504e-05,6.39832e-06,5.50215e-06,9.53352e-06,3.82278e-05,0.000128042,0.00016707,0.000186021,0.00018895]

    elif finalState == 'mumu':
        poleMass = [2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5]
        Width    = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
        neg95    = [1.61917e-05,6.51315e-06,3.81537e-06,3.01525e-06,5.392e-06,1.55101e-05,6.86931e-05,8.03059e-05,8.55459e-05,9.07205e-05]
        neg68    = [2.20171e-05,9.28147e-06,5.31672e-06,4.2708e-06,8.81809e-06,2.51158e-05,9.15622e-05,0.000119728,0.000127277,0.000126067]
        central  = [3.03798e-05,1.30241e-05,7.61418e-06,6.45049e-06,1.36629e-05,3.91601e-05,0.000127654,0.000170966,0.000177079,0.000185776]
        pos68    = [4.4327e-05,1.85039e-05,1.14114e-05,9.73674e-06,2.20711e-05,6.09291e-05,0.000186503,0.000247614,0.000246595,0.000260345]
        pos95    = [5.97339e-05,2.81679e-05,1.63669e-05,1.52416e-05,3.46819e-05,9.97071e-05,0.000287434,0.000348022,0.000335421,0.000347694]

    else:
        poleMass = [2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5]
        Width    = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
        neg95    = [7.85926e-06,2.57093e-06,1.23207e-06,1.1213e-06,1.61091e-06,5.19454e-06,2.33238e-05,3.65479e-05,3.85411e-05,4.27675e-05]
        neg68    = [1.13433e-05,3.60592e-06,1.75137e-06,1.50583e-06,2.41052e-06,7.8052e-06,3.25632e-05,4.96584e-05,5.43096e-05,5.73977e-05]
        central  = [1.60391e-05,5.07399e-06,2.544e-06,2.13902e-06,3.52157e-06,1.1884e-05,4.90778e-05,6.883e-05,7.69767e-05,8.00197e-05]
        pos68    = [2.25132e-05,7.30838e-06,3.98052e-06,3.18756e-06,5.30126e-06,1.9621e-05,7.65786e-05,0.000105856,0.000113159,0.000114257]
        pos95    = [3.24424e-05,1.02573e-05,5.67244e-06,4.61893e-06,8.75688e-06,3.1588e-05,0.000113206,0.000145293,0.000156925,0.000161499]

    return poleMass,Width,neg95,neg68,central,pos68,pos95

def MakeLimit(fOutput,finalState):

    Mass,Width,neg95,neg68,central,pos68,pos95 = SetArrays(finalState)
    expLimit   = ROOT.TGraph()
    expLimit.SetName("ExpLimit_"+finalState)
    for N in range(len(Mass)):
        expLimit.SetPoint(N,Mass[N],1000*central[N])

    expLimit.GetXaxis().SetTitle("Mass Z'")
    expLimit.GetYaxis().SetTitle("fid. xsec")

#    fOutput.mkdir(finalState)
#    fOutput.cd()
#    expLimit.Write()

    return expLimit

def MakeLimit2D(fOutput,finalState):

    Mass,Width,neg95,neg68,central,pos68,pos95 = SetArrays(finalState)
    expLimit2D = ROOT.TGraph2D()
    expLimit2D.SetName("ExpLimit2D_"+finalState)
    for N in range(len(Mass)):
        expLimit2D.SetPoint(N,Mass[N],Width[N],central[N])

    expLimit2D.GetXaxis().SetTitle("Mass Z'")
    expLimit2D.GetYaxis().SetTitle("Width")
    expLimit2D.GetZaxis().SetTitle("fid. xsec")

#    fOutput.mkdir(finalState)
    fOutput.cd()
    expLimit2D.Write()

    return expLimit2D

def MakeCrossing(fOutput,finalState,massDM):

    mDM = massDM.replace('p','.')
    expLimit = MakeLimit(fOutput,finalState)
    fidXsec = LoadXsecGraph(massDM,finalState)
    fidXsec.SetName("graphFidXsec_"+massDM+"_"+finalState)
#    fidXsec.SetTitle("graphFidXsec_"+massDM+"_"+finalState)

    c = ROOT.TCanvas("Crossing DM "+mDM+"Final State "+finalState,"Crossing DM "+mDM+"Final State "+finalState,700,600)
    c.cd()
    c.SetLogy()

    fidXsec.GetXaxis().SetTitle("Mass Z'")
    fidXsec.GetYaxis().SetTitle("fid. xsec")
    expLimit.SetLineColor(2)

    fidXsec.GetYaxis().SetRangeUser(0.0001,10)
    fidXsec.Draw("AC")
    expLimit.Draw("C")

    leg = ROOT.TLegend(0.35, 0.72, 0.85, 0.92, "")
    leg.SetTextSize(0.04)
    leg.SetFillColor(0)
    leg.SetBorderSize(0)

    if finalState == "ee": leg.AddEntry(expLimit,"#font[42]{Expected e^{+}e^{-} limit}","l")
    else: leg.AddEntry(expLimit,"#font[42]{Expected #mu^{+}#mu^{-} limit}","l")
    leg.AddEntry(fidXsec,"#font[42]{Vector Z'_{DM} (m_{#chi}="+mDM+" TeV)}","l")
    leg.Draw()
    ROOT.gPad.RedrawAxis()

    fOutput.cd()
    if mDM == "0.50": expLimit.Write()
    fidXsec.Write()
    c.Write()
    c.SaveAs("plots/Crossing_DM"+massDM+"_fs"+finalState+".png")

    return expLimit,fidXsec

def DrawAllCrossing(fOutput,finalState):

    massDM = ['0p50','1p00','1p50','2p00']

    for mDM in massDM:
        MakeCrossing(fOutput,finalState,mDM)

if __name__ == "__main__":

    ROOT.gROOT.SetBatch(True)
    ROOT.gStyle.SetOptStat(False)
    ROOT.gROOT.SetStyle("ATLAS")

    fOutput = ROOT.TFile(scope+"LimitInterpolator_CL95_14TeV.root","Update")

    #MakeCrossing(fOutput,"ll","1p00")
    DrawAllCrossing(fOutput,"ll")
