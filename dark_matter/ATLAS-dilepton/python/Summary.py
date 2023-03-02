import ROOT
from array import array
import numpy as np

scope="DMsummary.dileptonReinterpretation_14TeV.2018/"

def GetLimit(finalState):

    file = ROOT.TFile.Open(scope+"LimitInterpolator_CL95_14TeV.root", "READ")
    expLimit = file.Get("ExpLimit_"+finalState)

    return expLimit

def GetFidXsec(massDM,finalState):

    file = ROOT.TFile.Open(scope+"LimitInterpolator_CL95_14TeV.root", "READ")
    fidXsec = file.Get("graphFidXsec_"+massDM+"_"+finalState)

    return fidXsec

def GetCrossing(finalState,massDM):

    expLimit = GetLimit(finalState)
    fidXsec = GetFidXsec(massDM,finalState)

    min = 0.0
    max = 10.0
    steps = 10000
    epsilon = 1
    mZp = 0.0

    for i in np.linspace(min,max,steps):
        if ROOT.TMath.Abs(expLimit.Eval(i)-fidXsec.Eval(i))<epsilon:
            epsilon = ROOT.TMath.Abs(expLimit.Eval(i)-fidXsec.Eval(i))
            mZp = i
#            print("Crossing near (",i,expLimit.Eval(i),")\t","epsilon:",epsilon)
#    print("Z prime Limit:",mZp)

    return mZp

def Summarize(finalState):

    massDM = ['0p50','1p00','1p50','2p00']

    mZp_lower,mZp_upper,mDM = array( 'd' ), array( 'd' ), array( 'd' )
    for mass in massDM:
        mDM.append(float(mass.replace('p','.')))
        mZp_upper.append(GetCrossing(finalState,mass))
        mZp_lower.append(0.15)

    exclusionGraph_lower = ROOT.TGraph(len(mDM),mZp_lower,mDM) # From Previous Results
    exclusionGraph_upper = ROOT.TGraph(len(mDM),mZp_upper,mDM)
    exclusionGraph_upper.SetTitle("Upper Limit")
    exclusionGraph_upper.GetXaxis().SetTitle("m_{Z'}_{A} [TeV]")
    exclusionGraph_upper.GetYaxis().SetTitle("m_{#chi} [TeV]")

    c = ROOT.TCanvas("c","c",700,600)
    c.cd()
    exclusionGraph_upper.GetXaxis().SetLimits(0., 6.)
    exclusionGraph_upper.Draw("AC*")
    exclusionGraph_lower.Draw("C*")
    c.Update()
    ROOT.gPad.RedrawAxis()
    # change this path after creating the desired output directory!!!!!

    # c.SaveAs("../plots/summary/DMsummary.pdf")

    return exclusionGraph_upper,exclusionGraph_lower
