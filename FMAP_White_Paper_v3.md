# FHFA MORTGAGE ANALYTICS PLATFORM

**Version 3.0**

[cite_start]**Released by FHFA, November 2022** 

***

## Table of Contents

* [cite_start]**List of Tables** 
* [cite_start]**List of Figures** 
* **1 Release Notes** 
* [cite_start]**2 Executive Summary** 
* [cite_start]**3 Overview** 
    * 3.1 Objective and Purpose 
    * [cite_start]3.2 Description 
* [cite_start]**4 Data Module** 
    * 4.1 Overview 
    * [cite_start]4.2 Borrower and Collateral Data 
    * [cite_start]4.3 Macroeconomic Data 
    * 4.4 Loss Severity Data 
    * [cite_start]4.5 Simulation Data 
* [cite_start]**5 Behavioral Models Module** 
    * 5.1 Overview 
    * [cite_start]5.2 Framework Specification 
    * [cite_start]5.3 Model Specification 
    * 5.4 Sample and Methodology 
    * [cite_start]5.5 Estimation and Results 
    * [cite_start]5.6 Model Performance Tracking Results 
* **6 Loss Severity Models Module** 
    * [cite_start]6.1 Overview 
    * [cite_start]6.2 Framework Specification 
    * 6.3 Data 
    * [cite_start]6.4 Credit Losses 
    * [cite_start]6.5 Charge-off Amounts 
    * 6.6 REO Operating Expense 
    * [cite_start]6.7 Fit Statistics 
* [cite_start]**7 Simulation Module** 
    * 7.1 Overview 
    * [cite_start]7.2 Cashflow-based Simulation 
    * [cite_start]7.3 Markov Chain (Continuous) Simulation 
    * 7.4 Monte Carlo (Discrete) Simulation 
* [cite_start]**8 Reporting Module** 
* [cite_start]**9 Appendix** 
    * 9.1 Behavioral Equations 
    * [cite_start]9.2 Loss Severity Model 
    * [cite_start]9.3 Simulation 
    * 9.4 Summary Information 
* [cite_start]**Bibliography** 

***

## 1 Release Notes

This white paper incorporates the following major enhancements and updates reflected in the third version of the Single-family FHFA Mortgage Analytics Platform (FMAP v3.0) since version 2.0 of FMAP was released in May 2020: 

* [cite_start]Redesigns and re-estimates loan behavioral equations. 
* [cite_start]Develops and implements a proprietary loss severity model. 
* Uses expanded and more representative loan performance data and more granular level economic data to estimate mortgage performance model. 
* [cite_start]Estimates the behavioral equations via an iterative, out-of-sample, model building process. 

## 2 Executive Summary

[cite_start]FMAP is a proprietary analytic system developed by the Federal Housing Finance Agency (FHFA) to inform Agency policy decisions.  [cite_start]Essentially, the system forecasts mortgage performance of Fannie Mae and Freddie Mac (the Enterprises) loan portfolios under various economic scenarios and time horizons.  [cite_start]These forecasts are based upon historical relationships among borrower, collateral, and macroeconomic information.  [cite_start]This white paper describes the most recent version of FMAP, FMAP v3.0.  [cite_start]FMAP v3.0, like its predecessors, provides analytic support for Agency policy decisions.  [cite_start]Previous examples of FMAP support include the following: 

* [cite_start]FHFA issued the Enterprise Regulatory Capital Framework Final Rule (ERCF) that establishes credit and market risk capital requirements for the guarantee, whole loan, and retained portfolios of the Enterprises using credit score, loan-to-value, and other loan characteristics.  [cite_start]FMAP informed the ERCF credit risk capital requirements for single-family new acquisitions. 
* [cite_start]The Dodd-Frank Act Stress Test requires certain financial institutions to conduct periodic stress tests to determine whether they have sufficient capital to absorb losses and support operations during adverse economic conditions.  [cite_start]FHFA requires the Enterprises to conduct stress tests pursuant to the Dodd-Frank Act.  [cite_start]FHFA uses FMAP to provide an independent benchmark to compare against the Enterprises' single-family credit loss projections. 
* During and after the 2007-2008 financial crisis, the Enterprises suffered losses due to the failure of insufficiently capitalized counterparties to honor their respective obligations.  As a safety and soundness matter, FHFA established the Private Mortgage Insurance Eligibility Requirements Standards (PMIERS), which mandated financial requirements for mortgage insurers interested in serving as counterparties to the Enterprises.  FMAP provided analytic support in establishing these standards. 

FMAP v3.0 contains a series of major enhancements and upgrades to FMAP v2.0, the current production version.  These new changes include the redesign and re-estimation of the loan performance model and implementation of an internally developed loss severity model.  The new loan performance model expanded FMAP's ability to model loan performance at a more granular level.  Additionally, FMAP v3.0 loan performance equation were estimated using an out-of-time model building approach and more robust nonlinearity specification, which minimizes model overfitting. 

## 3 Overview

### 3.1 Objective and Purpose

FHFA developed FMAP as an analytic system to independently inform Agency management about the potential performance of the Enterprises' portfolio of loans under various scenarios and time horizons.  FHFA considers forecasted loan performance when developing and evaluating various housing policies.  FHFA benefits from the external forecasts provided by the Enterprises and the vendor platforms to which FHFA subscribes.  Simultaneously, FHFA developed FMAP for several reasons.  First, FMAP provides an independent view of portfolio performance rather than a view informed by external entities.  Second, FHFA develops and maintains FMAP in a manner reflective of Agency priorities and perspectives on how mortgages are expected to perform under various economic conditions and time horizons.  Third, FMAP is accessible and transparent relative to other external analytic systems.  The objective of this white paper is to provide interested stakeholders with an overview of FMAP.  The distribution of this paper reflects the broader Agency-wide effort to provide transparency on the data and analytical tools used by FHFA for policy support.  This white paper describes version 3.0, the latest version of FMAP as of this paper's publication.  The Agency anticipates updating this document periodically. 

### 3.2 Description

FMAP is constructed and used to forecast mortgage cash flows within the structure depicted below in Figure 1, which describes the inter-relationships of the following five FMAP v3.0 modules: 

* Data module
* Behavioral models module
* Loss severity models module
* Simulation module
* Reporting module

[cite_start]*Figure 1. FMAP v3.0 Structure* 

[cite_start]Each module of FMAP v3.0 is described in the sections following the Release Notes. 

## 4 Data Module

### 4.1 Overview

[cite_start]FMAP v3.0 requires multiple source data to build the statistical models and simulate mortgage performance; namely, 

* [cite_start]Borrower data 
* Collateral data 
* [cite_start]Macroeconomic data 
* [cite_start]Loss severity data 

### 4.2 Borrower and Collateral Data

[cite_start]Monthly, the Enterprises submit to FHFA historical loan-level data containing borrower and collateral characteristics.  [cite_start]These data consist of static origination information as well as monthly dynamic information.  [cite_start]FMAP v3.0 uses historical Enterprise borrower and collateral data to estimate both the behavioral and loss severity models.  [cite_start]FMAP v3.0 also uses Enterprise borrower and collateral information as of the simulation date to define the set of loans for which to simulate mortgage performance and the initial values for these loans in terms of borrower and collateral characteristics. 

### 4.3 Macroeconomic Data

[cite_start]In addition to borrower and collateral information, FMAP v3.0 requires both historical and forecasted macroeconomic information; namely, house prices, unemployment rates, and certain relevant interest rates.  [cite_start]Historical house price indices (HPIs) are provided by FHFA, while historical unemployment rates and interest rates are provided by a vendor.  [cite_start]Forecasted HPIs, unemployment rates, and interest rates are also provided by a vendor.  [cite_start]Combined with borrower and collateral information, FMAP v3.0 uses macroeconomic historical data to estimate the statistical models and macroeconomic forecast data to simulate loan performance for various economic scenarios and time horizons. 

### 4.4 Loss Severity Data

[cite_start]The input data for the loss severity module come from several sources.  [cite_start]First, the Enterprises provide loss and loan level data.  [cite_start]Second, the monthly loan-level submissions provided by the Enterprises include data for real-estate owned fixed costs and alternatives as well as the transaction costs for non- performing loan sales.  [cite_start]Lastly, house price index data is provided by a vendor. 

### 4.5 Simulation Data

[cite_start]The simulation data is one input into the simulation engine.  [cite_start]The data is created based on borrower, collateral, and macroeconomic data.  [cite_start]These data reflect the portfolio of each Enterprise and contain loan attributes as of the simulation date. 

## 5 Behavioral Models Module

### 5.1 Overview

[cite_start]The behavioral models are statistical equations that vary across the Enterprises and other dimensions.  [cite_start]These models predict a given loan's transition among states.  [cite_start]A transition refers to a loan changing to a different state from one period to the next, where a state is defined as a loan performance category e.g. performing or delinquent. 

### 5.2 Framework Specification

[cite_start]In particular, FMAP v3.0 proposes a transition probability methodology to model monthly mortgage performance.  [cite_start]This methodology projects monthly probabilities of a given loan transitioning from one state to another state.  [cite_start]Typically, states include current, 30-, 60-, 90-, 120-, 150- day delinquencies, and 180 or more days in delinquency.  [cite_start]The advantage of the transition methodology is that loan performance can be modeled at a more granular delinquency level and each transition equation can be individually specified and estimated.  [cite_start]In addition, the transition technique is particularly useful if modelers need to predict delinquency status of each loan in a portfolio.  [cite_start]The downside of the transition model is that when the granularity of loan state is high, the number of transition equations become very large and unmanageable, and equations for transitions between certain delinquency states cannot be reasonably estimated because of the low transition frequency.  [cite_start]For this reason, institutions cannot always estimate every transition of interest.  [cite_start]Instead, modelers either group delinquency states or omit some of the transition equations. 

[cite_start]FMAP v3.0 groups active loans into either performing, re-performing, or nonperforming loan segments to balance the granularity and reliable estimation of the transition equations.  [cite_start]The segmentation is conditional on the delinquency or performance and modification status of loans.  [cite_start]The portfolio, or simulation, date represents the first date upon which FMAP simulates loan transitions.  [cite_start]Depending on the modification history, re-performing loans are further classified into either modified re-performing or non-modified re-performing loans.  [cite_start]The segmentation leads to seven loan states: 

1.  [cite_start]**Performing (PER) loans**: Loans neither 1) currently delinquent more than two months, 2) ever delinquent more than two months, nor 3) modified before the portfolio date. 
2.  [cite_start]**Modified Re-performing loans (MRPL)**: There are two groups of modified re-performing loans.  [cite_start]The first group of modified re-performing loans are neither i) currently delinquent more than two months nor ii) ever delinquent more than two months; but have been modified before the portfolio date.  [cite_start]The second group of modified-reperforming loans are i) not currently delinquent more than two months, ii) have been delinquent at least three months before the portfolio date, iii) have not been delinquent at least three months since the portfolio date, and iv) have been modified before the portfolio date. 
3.  [cite_start]**Non-Modified Re-performing loans (NRPL)**: Loans that are i) not currently delinquent more than two months, ii) have been delinquent at least three months in the past, albeit not since the portfolio date, and iii) have not been modified before the portfolio date. 
4.  [cite_start]**Re-performing (RPL) loans**: Loans not currently delinquent more than two months but have been delinquent at least three months since the portfolio date. 
5.  [cite_start]**Light delinquent (LDQ) loans**: Loans 3 - 5 months delinquent, inclusive. 
6.  [cite_start]**Seriously delinquent (SDQ) loans**: Loans 6 - 11 months delinquent, inclusive. 
7.  [cite_start]**Deeply delinquent (DDQ) loans**: Loans 12+ months delinquent, inclusive. 

[cite_start]PER loans are further classified by product types; namely, the FRM 30/40-year and 15/20-year product types as well as the ARM product type.  [cite_start]The nine transition states comprise the same seven active states along with two termination states.  [cite_start]A termination state is a state from which a loan cannot transition such as: 

8.  [cite_start]Prepay loan (Prepay) 
9.  [cite_start]Defaulted loan (Default) 

[cite_start]FMAP v3.0 defines default as either real-estate owned (REO), foreclosure alternative (deed-in-lieu, pre-foreclosure sale, and third-party sale), or nonperforming loan sale.  [cite_start]The mutually exclusive nature of the seven loan states is presented in the schematic below: 

[cite_start]*Figure 2. Loan Status Schematic* 

[cite_start]FMAP v3.0 reflects that some transitions are impossible.  [cite_start]For example, a lightly delinquent loan is prohibited from transitioning to a performing state, though it can transition to a reperforming state.  [cite_start]The eligible transition states for each loan, conditional on the current state of a given loan, are given as follows: 

| Current state (t) | PER | MRPL | NRPL | RPL | LDQ | SDQ | DDQ | Prepay | Default |
| :--- | :-: | :--: | :--: | :-: | :-: | :-: | :-: | :----: | :-----: |
| PER | X | | | | X | | | X | |
| MRPL | | X | | | X | | | X | |
| NRPL | | | X | | X | | | X | |
| RPL | | | | X | X | | | X | |
| LDQ | | | | X | X | X | | X | X |
| SDQ | | | | X | X | X | X | X | |
| DDQ | | | | X | X | X | X | X | X |

[cite_start]*Table 1. Transition Table* 

[cite_start]To illustrate, consider the performing loan transitions.  [cite_start]FMAP v3.0 selects a sample of performing loans from among all loans to inform the performing loan equations, which estimate the probability of transitioning to either one of the following three states: lightly delinquent, prepay, or remain performing.  [cite_start]This same outcome distribution is adopted for each of the seven active states. 

### 5.3 Model Specification

[cite_start]Borrower behavior may vary based on the current and subsequent transition states of a given loan.  [cite_start]For example, a borrower with a fixed-rate, 30-year mortgage may face different economic incentives to refinance than a borrower with an adjustable-rate mortgage.  [cite_start]Given the framework described in the previous section and to account for these different incentives, we allow the model specification to vary by segment type, current state, and transition state.  [cite_start]This leaves us with the following nine sets of equations: six sets for performing loans and three sets for nonperforming loans: 

1.  [cite_start]**Performing 30/40-year fixed-rate to either LDQ or Prepay**: Predicts probability of transition for performing loans with fixed-rate, either 30- or 40-year mortgages to either LDQ or Prepay using separate equations for each outcome. 
2.  [cite_start]**Performing 15/20 year fixed-rate to either LDQ or Prepay**: Predicts probability of transition for performing loans with fixed-rate, either 15- or 20-year mortgages to either LDQ or Prepay using separate equations for each outcome. 
3.  [cite_start]**Performing adjustable-rate to LDQ or Prepay**: Predicts probability of transition for performing loans with adjustable-rate mortgages to either LDQ or Prepay using separate equations for each outcome. 
4.  [cite_start]**mRPL to either LDQ or Prepay**: Predicts probability of transition for all mRPLs to either LDQ or Prepay using separate equations for each outcome. 
5.  [cite_start]**nRPL to either LDQ or Prepay**: Predicts probability of transition for all nRPLs to either LDQ or Prepay using separate equations for each outcome. 
6.  [cite_start]**RPL to either LDQ or Prepay**: Predicts probability of transition for all RPLs to either LDQ or Prepay using separate equations for each outcome. 
7.  [cite_start]**LDQ to either SDQ, RPL, Prepay, or Default**: Predicts probability of transition for all currently LDQ loans to each outcome (SDQ, RPL, Prepay, or Default) with four separate equations. 
8.  [cite_start]**SDQ to either LDQ, DDQ, RPL, Prepay, or Default**: Predicts probability of transition for all currently SDQ loans to each outcome (LDQ, DDQ, RPL, Prepay, or Default) with five separate equations. 
9.  [cite_start]**DDQ to either LDQ, SDQ, RPL, Prepay, or Default**: Predicts probability of transition for all currently DDQ loans to each outcome (LDQ, SDQ, RPL, Prepay, or Default) with five separate equations. 

[cite_start]Covariates assigned to each equation include two types of independent variables: (i) static loan characteristics such as loan purpose and (ii) dynamic loan characteristics such as age.  [cite_start]Covariates are assigned to each specification using an iterative model building process that relied on out-of-time (OOT) fit.  [cite_start]The iterative process begins with a simple base model that contains few variables.  [cite_start]Then variables were added iteratively and the OOT fit was checked with each iteration to ensure that every variable added improved OOT fit.  [cite_start]OOT fit evaluations are used to assess whether a variable should be added to an equation since doing so improves the generalizability of the model on new mortgage loans, which is the primary objective of FMAP.  [cite_start]To produce OOT fits, the iterative process uses a sliding window for the estimation data and tests OOT fit on each year from 2006 to 2019, inclusive.  [cite_start]The sliding window produces OOT fits as the estimation data used to fit for each relevant year is only from years prior.  [cite_start]By using a sliding window FMAP v3.0 also minimizes the issue of having significantly older data for 2019 fit estimates versus 2006.  [cite_start]For example, data from 2000 through 2006 is used to estimate OOT model fits for 2007, data from 2001 to 2007 is used to estimate OOT model fits for 2008 and so on.  [cite_start]The output from this process is multiple OOT fit statistics for each year between 2006 and 2019 which allow for comparison of a base regression to a regression with either new or different variables.  [cite_start]With this iterative process, FMAP efficiently searches for the optimal subset of covariates.  [cite_start]Consistent with borrower behavior varying based on differences in either incentives or characteristics of their loans, the specifications chosen based on this iterative process are not the same for all segments and states.  [cite_start]This iterative process led to either variables included as standalone variables, interactions, polynomials, or splines.  [cite_start]The nonlinearity effects of the continuous covariates on mortgage outcomes are captured through either spline or polynomial functions based on the model fit statistics.  [cite_start]The number and location of spline knots were identified using a multivariate adaptive regression spline (MARS) technique.  [cite_start]Interactions and polynomials of certain covariates are also based on model OOT fit statistics. 

[cite_start]Covariate definitions are provided below.  [cite_start]Not all covariates are used in every set of equations.  [cite_start]Some equations use differently defined variables.  [cite_start]The appendix contains a table presenting covariates included in each equation. 

### 5.4 Sample and Methodology

[cite_start]Given the technological constraints on estimating models with the entire portfolios of loans from both Enterprises, FMAP v3.0 samples Fannie Mae and Freddie Mac loans to estimate separate behavioral equations for each Enterprise.  [cite_start]The time period for the estimation sample reflects borrower and collateral information from January 2000 to December 2019. 

[cite_start]In FMAP v2.0, the performing equations for 30-year and 15-year fixed-rate loans and adjustable-rate 5/1 loans were estimated on samples of loans originated from February 1997 to December 2014.  [cite_start]Selected loans were followed from acquisition to either first 90-day delinquency, prepayment, or to December 2014, whichever occurred earliest.  [cite_start]FMAP v3.0 includes several changes to this sampling approach to increase the representativeness and usefulness of the samples.  [cite_start]FMAP v3.0 randomly samples loans from each monthly portfolio of loan performance observations for loans with a given starting state.  [cite_start]This sample is stratified by age, credit score, origination loan-to-value, and loan status.  [cite_start]Different sampling rates were set for the different starting states to ensure a sufficient number of loans for estimation.  [cite_start]Sampling rates are one percent for FRM 30/40-year and FRM 15/20-year 10 percent for arms, 50 percent for mRPL and nRPL, 25 percent for RPL, and 80 percent for LDQ, SDQ, and DDQ.  [cite_start]For each month, this stratified random sampling method generates a sample of loans more representative of the true Fannie Mae and Freddie Mac portfolios of active loans. 

### 5.5 Estimation and Results

[cite_start]Multiple statistical modeling approaches have been used to estimate borrower behavior. [cite: 226] Jenkins (1995), Calhoun and Deng (2000), and Clapp et. al. [cite_start](2001) demonstrate that the multinomial logit approach provides a relatively convenient method for modeling prepayment and delinquency risks as discrete time, competing risks.  [cite_start]The multinomial approach is also consistent with the approach adopted in the prior version of FMAP.  [cite_start]With the sampled data we estimate binomial and multinomial logistic regressions for each Enterprise separately.  [cite_start]Performing and reperforming equations are estimated using a binomial logistic regression (i.e., one vs. the rest scheme), which estimates the probability a certain transition against all other possible transitions.  [cite_start]Taking as an example the performing equation there are three possible transitions: prepay, LDQ, and performing.  [cite_start]When we estimate the prepay probability, we estimate the probability of prepaying vs the probability of [LDQ or performing].  [cite_start]Estimating the transition probabilities in this way can cause probabilities to sum greater than one.  [cite_start]To combat this, we assume the probability of staying in your starting state (i.e., performing to performing) is equal to one minus the probabilities of transitioning to other states.  [cite_start]Nonperforming loan equations were estimated using multinomial logits. 

[cite_start]The appendix includes an excel file with the estimation results for all specifications.  [cite_start]For performing loans for each Enterprise, segment (e.g., fixed-rate 30-year or ARMs), and event (outcome state) has its own table.  [cite_start]For nonperforming loans, each Enterprise and segment has its own table.  [cite_start]As the behavioral equations are not focused on identifying why a loan changes state, these coefficients cannot be interpreted causally.  [cite_start]Instead, these coefficients can only be used in jointly predicting the probability a loan changes state.  [cite_start]Therefore, in reviewing the coefficients the focus should be on whether the sign of the coefficient is reasonable.  [cite_start]As many of the variables are represented with polynomials, splines, or included in interactions, the signs on all relevant coefficients should be considered. 

### 5.6 Model Performance Tracking Results

[cite_start]In this section, we show excerpts from the model performance tracking report, which compares forecasts to actuals for selected historical single-family loan portfolios.  [cite_start]FMAP v3.0 includes two types of performance tracking reports to assess the behavioral equation performance.  [cite_start]First, the Component Model Performance Tracking (cMPT) compares monthly predicted transition rates with actual transition rates for each behavioral equation.  [cite_start]Second, the Integrated Model Performance Tracking (iMPT) compares predicted loan termination rates, i.e., default and prepay rates with the actual termination rates on past portfolios. 

#### 5.6.1 Component Model Performance Tracking Report (CMPT)

[cite_start]The Component Model Performance Tracking (CMPT) report monitors the performance for all 29 behavioral models.  [cite_start]The CMPT is performed for the 201606 portfolio with forecast until 202003.  [cite_start]Below is the sample report for LDQ and prepay equations for PERF FRM 30yr and PERF FRM 15yr products.  [cite_start]The AUC statistics show the model fit for these four equations is reasonable. 

#### 5.6.2 Integrated Model Performance Tracking Report

[cite_start]Each MPT report contains approximately 70 graphs designed to assess varying views of model performance.  [cite_start]For brevity, in this document we will focus only on select results aggregated at the activity date level for the single-month mortality (SMM), monthly default rate (MDR), Cumulative Prepay, and Cumulative Default metrics.  [cite_start]To gauge the forecast capabilities of FMAP v3.0, MPT reports for two different portfolios were created: June 2014 and December 2016.  [cite_start]Results will be shown in this order.  [cite_start]The table below summarizes results for the four metrics across the two portfolios.  [cite_start]As shown in this table, we see model performance is similar between the two Enterprises as can be seen by the similar average errors between the two Enterprises.  [cite_start]Additionally, we can see that, as expected, the in-time performance is slightly better than the out-of-time performance, though the difference is minimal. 

[cite_start]The first two figures below show the results from the June 2014 MPT reports for Enterprise 1 and Enterprise 2, respectively.  [cite_start]These graphs yield several observations.  [cite_start]First, fit results by Enterprise are similar, this indicates forecast capability is similar for both Enterprises.  [cite_start]Second, the in-time and out-of- time results (out-of-time results use coefficients estimated on data from 2000 to May 2014) are close.  [cite_start]The similarity in results indicate minimal over-fitting in the final specification, and that the out-of-time iterative model building worked as intended.  [cite_start]For prepayment, ignoring the pandemic as illustrated by the red vertical line, SMM shows the predicted prepayments follow the general shape of the actual prepayments.  [cite_start]However, there is some overprediction in the first year and a half (June 2014 to December 2016) of the forecast, though this overprediction is decreased after the large prepayment decrease of December 2016.  [cite_start]Looking at the pandemic we see that FMAP v3.0 predicts a large and steep increase in prepayments.  [cite_start]However, the magnitude is slightly lacking as both Enterprises show an approximate 0.75 percent under prediction in late 2020.  [cite_start]It should be noted that FMAP v3.0 excludes COVID-specific treatments or variables.  [cite_start]Additionally, the sample used to create FMAP v3.0 finishes at the end of 2019 and therefore includes no pandemic information. 

[cite_start]The MDR graph is more difficult to read due to the "spiky" nature of the default data.  [cite_start]These spikes represent NPL loan sales, which refer to large loan sales made at the discretion of the Enterprises.  [cite_start]Therefore, their exact timing is difficult to model.  [cite_start]Looking past the spikes we see FMAP v3.0 predictions seem to be following the general downward trend of actual defaults over the forecast period.  [cite_start]We see the cumulative default graphs that FMAP v3.0 slightly underestimates the number of defaults.  [cite_start]Similarly, for the prepay results we can see that for the pandemic FMAP v3.0 correctly estimates a decrease in defaults, though the magnitude of the predicted decrease is slightly less than the actual decrease. 

[cite_start]The third and fourth figures below show the results from the December 2016 MPT report for Enterprise 1 and Enterprises 2, respectively.  [cite_start]The FMAP v3.0 OOT results are based on coefficients estimated on data from 2000 through 2014.  [cite_start]Similarly, to the June 2014 MPT, FMAP 3.0 very accurately forecasts the December 2016 portfolio.  [cite_start]The estimated prepay rates very closely match the actual prepay rates with only slight overpredictions for both enterprises.  [cite_start]There is slightly more variation in the accuracy of default forecasts, the forecast for Enterprise #2 is very close, with an MAE of 0.0205% and slightly under the actual, while the forecast for Enterprise #1 is slightly worse with an MAE of 0.0343% and over the actual default rate.  [cite_start]The error in forecast for Enterprise #1 seems to be a result of a large NPL sale that occurred mid 2018 as can be seen by a large spike in defaults in figure 6 subgraph: Cumulative Default Amt % for act_dte. 

## 6 Loss Severity Models Module

### 6.1 Overview

[cite_start]Loss severity models predict credit loss on defaulted loans.  [cite_start]These models are either statistical or relational equations that vary across the Enterprises and other dimensions.  [cite_start]The historical data used to estimate the loss severity models include borrower and collateral characteristics, payments and receipts for troubled loans and REOs data, along with house price data. 

### 6.2 Framework Specification

[cite_start]Loans predicted to default will transition into the loss severity module, which calculates credit loss.  [cite_start]Credit loss can result from one of three outcomes: foreclosure, foreclosure alternative, and nonperforming loan sale. 

[cite_start]Foreclosure transfers property title from the borrower to the lender.  [cite_start]The lender in this analysis is one of the two Enterprises.  [cite_start]Once transferred, the Enterprise owns the property, which becomes REO.  [cite_start]The Enterprises can then market and sell the property to a new owner.  [cite_start]The final credit loss on the loan is calculated after the property is sold from REO inventory. 

[cite_start]Foreclosure alternatives is an alternative outcome for a defaulted loan.  [cite_start]Foreclosure alternatives consist of three major types: deed-in-lieu, pre-foreclosure sale (short sale), and third-party sale.  [cite_start]Deed-in-lieu occurs when the lender (in this case one of the Enterprises) forgives the mortgage debt and takes title to the property.  [cite_start]In this case, the property becomes REO and the lender can sell it to recoup credit loss.  [cite_start]Another foreclosure alternative is a pre-foreclosure sale.  [cite_start]This occurs when the lender agrees to allow the borrower to sell the property for less than the outstanding mortgage debt (sometimes called a short sale) and the lender forgives the mortgage debt.  [cite_start]Another foreclosure alternative is a third-party sale.  [cite_start]This occurs when a third party buys the property for the outstanding loan balance and expenses at the foreclosure sale.  [cite_start]The credit loss is recognized at the completion of the foreclosure sale.  [cite_start]The pre-foreclosure sale and third-party sale do not result in the Enterprises owning the property.  [cite_start]Consequently, there are no expenses after the completion of the sale. 

[cite_start]The last potential outcome is a nonperforming loan (NPL) sale, which occurs when an Enterprise sells a defaulted mortgage within a pool of mortgages to an investor.  [cite_start]The investor who purchases the pool of mortgages receives cash flows from the mortgages.  [cite_start]Credit loss from a nonperforming loan sale equal the unpaid principal balance plus transaction costs minus expected sale price for the mortgage.  [cite_start]This outcome is new in FMAP v3.0. 

### 6.3 Data

[cite_start]The models that make up the loss severity module are estimated separately for Fannie Mae and Freddie Mac using the Enterprises' data of borrower and collateral characteristics and payments and receipts for troubled loans and REOs and the Enterprises purchase only HPI data from 2012 to 2020. 

### 6.4 Credit Losses

[cite_start]For REO dispositions, four components comprise credit losses: 1) the charge-off amount at the title transfer date (for a foreclosure outcome, the title transfer date is foreclosure completion date for REO and all other foreclosure alternative outcomes this is liquidation date), 2) sale price adjustment, 3) carrying costs and accrued interest, and 4) fixed costs.  [cite_start]Details on each are provided below: 

[cite_start]Charge-off occurs at foreclosure completion.  [cite_start]It equals the unpaid principal balance of the mortgage at the time of default (defaulted UPB) plus any relevant expenses up to the foreclosure date minus predicted sale price at the foreclosure date.  [cite_start]Sale price adjustment occurs monthly from foreclosure completion to REO property disposition.  [cite_start]This monthly adjustment is calculated as the difference between the expected sale price every month and the expected sale price at foreclosure completion.  [cite_start]These monthly adjustments end when the property is disposed of from REO inventory.  [cite_start]The sum of these monthly adjustments equals the entire sale price adjustment from foreclosure completion date to REO property disposition date. 

[cite_start]Carrying costs are calculated from foreclosure completion to REO property disposition and include taxes, insurance, and homeowner association (HOA) fees from foreclosure completion to REO property disposition.  [cite_start]Accrued interest is calculated from last paid installment to foreclosure completion and is included in carrying costs for that period.  [cite_start]Fixed costs are calculated from foreclosure completion to REO property disposition and include certain liquidation expenses and fees plus utility and repair costs, etc. 

[cite_start]For non-REO dispositions, the credit losses are limited to the charge-off amount.  [cite_start]Below are the formulas to calculate the credit loss for each outcome. 
*Credit loss~i~ = Charge off~i~ + Sale price adjustment from foreclosure completion to REO property disposition~i~ + Carrying costs including accrued interest from foreclosure completion to REO property disposition + Fixed costs from foreclosure completion to REO property disposition*
[cite_start]*∀ i ∈ REO* 

*Credit loss~i~ = Charge-off~i~*
[cite_start]*∀ i ∈ Foreclosure alternatives, NPL sales* 

### 6.5 Charge-off Amounts

[cite_start]For each outcome, the formulas below calculate the charge-off amount, which is equal to the unpaid principal balance at the time of default (defaulted UPB) minus expected net sales proceeds on the liquidation (foreclosure) date plus any relevant expenses up to liquidation (foreclosure) date including Carrying costs from LPI to liquidation date. 

*Charge off~i~ = Defaulted unpaid principal balance - Expected net sale proceeds at liquidation date + Carrying costs including accrued interest from LPI to liquidation date + Fixed costs from LPI to liquidation date*
[cite_start]*∀ i ∈ REO, Foreclosure alternatives* 

*Charge off~i~ = Defaulted unpaid principal balance - Expected NPL sale proceeds at liquidation date + Carrying costs including accrued interest from LPI to liquidation date + Transaction costs from LPI to liquidation date*
[cite_start]*∀ i ∈ NPL sales* 

#### 6.5.1 Expected Net Sales Proceeds for REO and Foreclosure Alternatives

[cite_start]Net sale proceeds are the difference between gross property sale proceeds and other relevant expenses, which include sales and other selling expenses, broker fees and borrower closing costs.  [cite_start]The expected net sale proceeds for REO and foreclosure alternatives used to calculate charge-offs are estimated using a piecewise linear regression technique with a separate model for each state and disposition type.  [cite_start]The technique relates historical actual net sale proceeds with the mark-to-market property value at the time of disposition for properties collateralizing Enterprise loans liquidated between 2012 and 2020.  [cite_start]Specifically, the technique captures the relationship between a defaulted loan i of the actual net sale proceeds (Net Sale Proceeds~i~) against the mark-to-market property value (PropValue) with a truncated power function series for each state defined as follows: 

Net Sale Proceeds~i~ = β~0~ + β~1~ \* (PropValue~i~) + β~2~ \* (PropValue~i~ - k~1~)~+~ + β~3~ \* (PropValue~i~ - k~2~)~+~ + β~4~ \* (PropValue~i~ - k~3~)~+~ + β~5~ \* (PropValue~i~ - k~4~)~+~ + ε~i~
*∀ i ∈ REO and Foreclosure alternatives* 
where p=1 to 4 

#### 6.5.2 Expected NPL Sale Proceeds (Recovery Rate)

NPL sale proceeds are equal to the note sale proceeds minus other relevant expenses, which include sales and other selling expenses, broker fees and borrower closing costs. 

*NPL Sale Proceeds~i~ = β~0~ + β~11~ \* (MTMLTV~i~) + β~12~ \* (MTMLTV~i~ - k~1~)~+~ + β~13~ \* (MTMLTV~i~ - k~2~)~+~ + β~14~ \* (MTMLTV~i~ - k~3~)~+~ + β~21~ \* (Liq~UPB~i~) + β~22~ \* (Liq~UPB~i~ - k~1~)~+~ + β~23~ \* (Liq~UPB~i~ - k~2~)~+~ + β~24~ \* (Liq~UPB~i~ - k~3~)~+~ + β~31~ \* (Delinq~Pmts~i~) + β~32~ \* (Delinq~Pmts~i~ - k~1~)~+~ + β~33~ \* (Delinq~Pmts~i~ - k~2~)~+~ + β~34~ \* (Delinq~Pmts~i~ - k~3~)~+~ + liquidation year dummies + E~i~*
*∀ i ∈ NPL sales* 

We divide the NPL sale proceeds by liquidation UPB to get the recovery rates, which are defined as follows: 

*Expected NPL sale proceeds~i~ = Recovery rate \* Liquidated UPB*
[cite_start]*Net sale proceeds from loan sale / Liqidation UPB* 

[cite_start]Expected NPL sale proceeds apply only to NPL sales.  [cite_start]The expected NPL sale proceeds used to calculate charge-offs are estimated using a piecewise linear regression model, which relates historical actual NPL sale proceeds with MTMLTV at liquidation date, liquidation unpaid principal balance, number of delinquency payments, and liquidation year.  [cite_start]These variables were chosen to approximate factors rationale buyers would use to determine the price of a loan in an NPL sale package.  [cite_start]Specifically, the piecewise linear regression model captures the relationship between a defaulted loan i of the actual NPL sale proceeds (Actual NPL Sale Proceeds~i~) against the MTMLTV (MTMLTV~i~), liquidation unpaid principal balance (Liq~UPB~i~), delinquent payments (Delinq~Pmts~i~), with a truncated power function series and with separate liquidation year indicator variables (liq~year2015~, liq~year2016~, etc). 

#### 6.5.3 Carrying Costs

[cite_start]While the carrying costs are identical across disposition types, the way they are aggregated when defining charge-offs differs by disposition type.  [cite_start]Specifically, for REO dispositions, these expenses are accumulated between last paid installment date and foreclosure completion date.  [cite_start]These expenses for both foreclosure alternatives and NPL sales are accumulated from last paid installment date to title transfer date (liquidation date) and are included in the charge-off amount.  [cite_start]Carrying costs included HOA fees, property tax, insurance, and accrued interest.  [cite_start]Accrued interest included in the charge off amount for REO, foreclosure alternatives and Nonperforming Loan Sales is calculated by multiplying the defaulted unpaid loan balance by the interest rate multiplied by the time from last paid installment data to title transfer (liquidation date).  [cite_start]For REO properties, carrying costs also occur during the time from foreclosure completion to REO disposition.  [cite_start]Carrying costs used to calculate charge-offs are estimated using the look-up tables approach.  [cite_start]First, carrying costs are calculated at the loan level for all defaulted loans from 2012 to 2020.  [cite_start]Second, the defaulted loans are matched to categories uniquely defined by the combination of the property value at origination group, the state in which the property is located, and the disposition type. 

#### 6.5.4 Fixed Costs for REO or Foreclosure Alternative

[cite_start]Fixed costs are calculated from last payment date to foreclosure completion date and include appraisal fees, attorney and trustee fees, other foreclosure expenses, other liquidation expenses, maintenance expenses, property inspection, repairs, and utilities.  [cite_start]These costs were estimated using a piecewise linear regression technique with a separate model for each state and disposition type (REO and foreclosure alternatives which comprise deed-in-lieu, short sales and third-party sales).  [cite_start]This estimation used Enterprise liquidations from 2016-2020.  [cite_start]We didn't use the data from 2012 to 2015 in the estimation, as fixed costs seemed to have experienced regime switching and jumped to a much higher level after 2016.  [cite_start]Fixed costs components are calculated using the same formula for the two disposition types. 

#### 6.5.5 Transaction Costs for an NPL Sale

[cite_start]Transaction costs (also known as fixed costs or liquidation expenses) for an NPL sale, also known as liquidation expenses, include all expenses associated with an NPL sale such as appraisal fees and attorney and trustee fees.  [cite_start]Excluded from transaction costs for a NPL sale are aggregated expenses incurred by the Enterprises to execute the NPL sales.  [cite_start]These expenses may include incentives to brokers to facilitate transactions and website maintenance where investors can obtain information regarding the loans offered in the note sale pool.  [cite_start]Transaction costs for an NPL sale used to calculate charge-offs are estimated using look-up tables.  [cite_start]First, the transaction costs for an NPL sale are calculated at the loan level for all defaulted loans from 2014 to 2020.  [cite_start]Second, the defaulted loans are matched to categories uniquely defined by the combination of the Enterprise, liquidated unpaid principal balance group, and the judicial status of the state in which the property is located. 

#### 6.5.6 Mortgage Insurance (MI) Claim

[cite_start]The MI claim refers to the amount included in the claim submitted by the Enterprises to the mortgage insurance company.  [cite_start]An Enterprise can only receive reimbursement for MI claims on loans with mortgage insurance as of the title transfer date.  [cite_start]The MI claim amount for defaulted loan i (MI Claim Amount) is defined as follows: 

MI claim amount = Liquidated unpaid principal balance + Carrying costs including accrued interest from LPI to liquidation + Fixed costs from LPI to liquidation
[cite_start]*∀ i ∈ REO with MI, Foreclosure alternatives with MI* 

[cite_start]Mortgage insurance companies might also default, failing to reimburse the claimed amount.  [cite_start]Therefore, the following formula calculates MI proceeds after accounting for the potential failure of MI companies to honor claims, which is represented by the MI haircut ratios.  [cite_start]MI haircuts are differentiated by the credit rating of the mortgage insurer and their level of concentration in the mortgage insurance business, loan performance and loan amortization term. 

[cite_start]*MI proceeds~i~ = MI claim amount~i~ \* MI coverage~i~ \* (1 - MI haircut~i~)* 

### 6.6 REO Operating Expense

[cite_start]For REO properties, there are extra losses between Liquidate Date and Disposition Date, which are described as the REO Operating Expense.  [cite_start]When a loan becomes REO at month T, there are subsequent monthly operating expenses in the next few months: 

**Fixed Expense**

[cite_start]The fixed expense includes monthly tax, HOA, and insurance expenses. 

**Sale Price Adjustment from Foreclosure Completion to REO Property Disposition**

[cite_start]The property value component of charge off is measured by house price at foreclosure date.  [cite_start]The house price may decrease further, so the property value, after foreclosure date that incur additional losses.  [cite_start]The model tracks property value decrease if it occurs, month by month, between foreclosure and disposition and record as additional losses. 

**True Up at Disposition Date**

[cite_start]At disposition date, the house price may increase, the sum of additional recorded losses in step 2 may be overly recorded.  [cite_start]Total loss will be adjusted by comparing to property value at disposition date. 

### 6.7 Fit Statistics

[cite_start]The Loss Severity Module proposes updated parameters for FMAP v3.0 equations and introduced regression techniques to predict net sales proceeds and fixed costs for all three disposition types as well as recovery rates for NPL sales.  [cite_start]To validate and improve model predictions, a standard back-testing technique was implemented.  [cite_start]The net losses are defined as follows: 

[cite_start]*Net losses~i~ = Liquidation UPB~i~ - Net sale proceeds + Liquidation expenses (fixed costs) + Carrying costs MI proceed* 

[cite_start]To make it consistent for different loans, the total net losses as well as each of the five components are divided by the liquidation unpaid principal balance amounts to obtain the ratios.  [cite_start]The actual and predicted values are compared. 

[cite_start]Fit statistics used include RMSE (Root Mean Square Error) and MAE (Mean Absolute Error), both of which are weighted by the liquidation unpaid principal balance of all the loans.  [cite_start]The loss severity equals net losses divided by liquidation UPB.  [cite_start]This section covers the in-sample back testing results on the total net losses as percentages of the liquidation unpaid principal balances (loss severity ratios) on Enterprise 1 loans liquidated between 2012 and 2020.  [cite_start]Here we took out the mortgage insurance proceeds components, as NPL sales do not have mortgage insurance proceeds and we would like to maintain the comparison consistent between the three disposition types.  [cite_start]The figure below summarizes RMSE and MAE for the three disposition types.  [cite_start]NPL sales have the lowest RMSE followed by foreclosure alternatives and then REO dispositions. 

## 7 Simulation Module

### 7.1 Overview

[cite_start]The simulation module uses statistical models (behavioral models and loss severity models) to simulate cash flows, given a set of loan profiles and forecasted macroeconomic environment. 

### 7.2 Cashflow-based Simulation

[cite_start]The proposed cashflow-based simulation for FMAP v3.0 is similar to the cashflow projection method used in FMAP v2.0 and based on the following two equations: 

[cite_start]*UPB~t-1~ = performingUPB~t~ + schedPrinPaid~t~ + prepayAmt~t~ + delinquentAmt~t~ + defaultAmt~t~* 

[cite_start]*UPB~t~ = UPB~t-1~ - schedPrinPaid - prepayAmt - defaultAmt~t~* 

[cite_start]This method directly calculates projections for the following cash flows: 

* Performing unpaid principal balance
* Paid scheduled principal
* Unscheduled principal
* Prepayment
* Paid scheduled interest
* Delinquent unpaid principal balance: LDQ, SDQ, DDQ
* Default unpaid principal balance
* Credit loss related cash flows, including charge off, foreclosure expense, MI, etc.

### 7.3 Markov Chain (Continuous) Simulation

[cite_start]In this framework, the behavioral equations provide conditional probabilities from states in a given month to states in the next month.  [cite_start]These probabilities feed the transition matrix needed by this framework.  [cite_start]With a given conditional distribution of states of a loan at one month, we can calculate the marginal probabilities of states at the next month.  [cite_start]The Markov Chain algorithm is described as follows: 

[cite_start]**State Space**: In terms of the Markov Chain, the state space is the set of all possible values each loan could take.  [cite_start]In our case, state space = {perf, nrpl, mrpl, rpl, Idq, sdq, ddq, prep, default}, where prep and default are absorbing states, as stated previously in the behavioral equation section. 

**State Vector**: a vector SV(t) of the following elements:
(P~perf~, P~nrpl~, P~mrpl~, P~rpl~, P~ldq~, P~sdq~, P~ddq~, P~prep~, P~def~)
[cite_start]where the subscript represents the state. 

[cite_start]These elements are the unconditional probabilities of each state of a loan at month t. 

[cite_start]At month t=0, "Loan Segment" can only be in one of the above mentioned six states.  [cite_start]It is impossible to have a scenario to define SV(0) as (0, 0, 0, 1, 0, 0, 0, 0, 0). 

**Transition Matrix(t)**

[cite_start]The transition matrix TM(t) is invoked by the behavioral equations for each loan at time t. 

### 7.4 Monte Carlo (Discrete) Simulation

[cite_start]While the Markov Chain (continuous) method computes the probabilities of several states in each month, the Monte Carlo (discrete) method simulates a single outcome in each month, which would be useful for certain applications.  [cite_start]The Monte Carlo algorithm is as follows: 

[cite_start]Given the state of the loan at month t, one invokes the corresponding behavior equation to calculate the probabilities of states at month t+1, then use a random number to select a state among the several possible states.  [cite_start]Statistical theory proves that continuous and discrete simulations produce comparable results for large populations.  [cite_start]The results from the simulations using the two approaches are reasonably close. 

## 8 Reporting Module

[cite_start]FMAP v3.0 produces the loan-level cash flow components over the remaining life of the loans for different scenarios and time horizons.  [cite_start]For example: 

* Unpaid principal balance 
* [cite_start]Scheduled and unscheduled principal payments 
* [cite_start]Prepayment dollar amount 
* Default dollar amount 
* [cite_start]Dollar amount by loan delinquency status (i.e., LDQ, SDQ, DDQ) 
* [cite_start]Credit loss 

[cite_start]FMAP v3.0 possesses the capability to aggregate loan-level cash flow reports (e.g., aggregate them by either delinquent status or key risk metrics categories, such as mark-to-market loan-to-value, credit score, etc.). 

## 9 Appendix

### 9.1 Behavioral Equations

[cite_start]The tables below provide context on the behavioral equations along with the results of the separately estimated behavioral equations for each Enterprise-segment-transition state. 

| | Perf(F30/F15) - LDQ | Perf(F30/F15) - Prepay | ARM - LDO | ARM - Prepay | MRPL - LDO | MRPL - Prepay | RPL - LDO | RPL - Prepay | NRPL - LDO | NRPL - Prepay | NPL - Same Spec for All |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Refinance Rate** | X | X | X | X | X | X | X | X | X | X | |
| **Cash Out** | X | | X | | X | | X | | X | | |
| **Investment** | X | X | | X | | X | | | | | X |
| **Second Home** | | X | | X | | X | | X | | X | X |
| **Age** | | X | | X | | X | | | | | X |
| **Age Sq.** | X | X | | X | | X | | | | | |
| **Age Cb.** | | X | | X | | X | | | | | |
| **Current UPB (000s)** | X | X | | | | | | | | | X |
| **Current UPB (000s) Sq.** | | | | | | | | | | | |
| **Credit Score** | X | X | X | X | X | X | X | X | X | X | X |
| **Credit Score Sq.** | X | X | X | X | X | X | X | X | X | X | |
| **Sato-F30** | X | X | X | X | X | X | X | X | X | X | X |
| **Burnout Count** | X | | X | | X | | X | | X | | X |
| **Unemployment Rate** | X | X | X | X | X | X | X | X | X | X | |
| **Unemployment Burnout Count, 8%** | X | X | X | X | X | X | X | X | X | X | |
| **Unemployment Burnout Count, 10%** | X | X | X | X | X | X | X | X | X | X | |
| **Unemployment Burnout Count, 12%** | X | X | X | X | X | X | X | X | X | X | |
| **max(0, mtmltv - 79)** | X | | X | | X | | X | | X | | |
| **max(0, 79 - mtmltv)** | X | | X | | X | | X | | X | | |
| **max(0, mtmltv - 154)** | X | | X | | X | | X | | X | | |
| **max(0, mtmltv - 90)** | X | | X | | X | | X | | X | | |
| **max(0, mtmltv - 105)** | X | | X | | X | | X | | X | | |
| **max(0, debt_ratio - 60)** | X | | X | | X | | X | | X | | |
| **max(0, 60 - debt_ratio)** | | | | | | | | | | | |
| **max(0, debt_ratio - 30)** | X | | X | | X | | X | | X | | |
| **max(0, debt_ratio - 95)** | | | | | | | | | | | |
| **Origination LTV** | | | | | | | | | | | |
| **Junior Lien Indicator** | X | X | X | X | X | X | X | X | X | X | X |
| **Orig LTV x Jr Lien Ind** | X | X | X | X | X | X | X | X | X | X | |
| **One Borrower Indicator** | X | X | X | X | X | X | X | X | X | X | X |
| **Credit Score x One Borrower** | X | X | X | X | X | X | X | X | X | X | X |
| **No Full Doc Loan** | X | X | X | X | X | X | X | X | X | X | X |
| **Third Party Loan** | X | X | X | X | X | X | X | X | X | X | |
| **Judicial State** | X | X | X | X | X | X | X | X | X | X | X |
| **HPA with 24 month lag** | X | X | X | X | X | X | X | X | X | X | |
| **HPA with lag x Sunk Cost** | X | X | X | X | X | X | X | X | X | X | |
| **MTMLTV x Refinance Rate** | X | X | X | X | X | X | X | X | X | X | |
| **MTMLTV x Cash Out** | X | X | X | X | X | X | X | X | X | X | |
| **Q1** | X | X | X | X | X | X | X | X | X | X | |
| **Q2** | X | X | X | X | X | X | X | X | X | X | |
| **Q3** | X | X | X | X | X | X | X | X | X | X | |
| **2005-2008 Indicator** | X | X | X | X | X | X | X | X | X | X | X |
| **2009-2013 Indicator** | X | X | X | X | X | X | X | X | X | X | X |
| **>2014 Indicator** | X | X | X | X | X | X | X | X | X | X | X |
| **max(0, age - 17)** | | X | | X | | X | | X | | X | |
| **max(0, 17 - age)** | | X | | X | | X | | X | | X | |
| **max(0, age - 7)** | | X | | X | | X | | X | | X | |
| **max(0, age - 93)** | | X | | X | | X | | X | | X | |
| **max(0, age - 35)** | | X | | X | | X | | X | | X | |
| **max(0, mtmltv - 66)** | | X | | X | | X | | X | | X | |
| **max(0, 66 - mtmltv)** | | X | | X | | X | | X | | X | |
| **max(0, mtmltv - 30)** | | X | | X | | X | | X | | X | |
| **max(0, mtmltv - 6)** | | X | | X | | X | | X | | X | |
| **max(0, mtmltv - 101)** | | X | | X | | X | | X | | X | |
| **max(0, mtmltv - 9)** | | X | | X | | X | | X | | X | |
| **max(0, refi_incentive_level_12 - 1.4)** | | X | | X | | X | | X | | X | |
| **max(0, 1.4 - refi_incentive_level_12)** | | X | | X | | X | | X | | X | |
| **max(0, refi_incentive_level_12 - 0.02)** | | X | | X | | X | | X | | X | |
| **max(0, refi_incentive_level_12 - 1.1)** | | X | | X | | X | | X | | X | |
| **max(0, brnt_cnt - 1)** | | X | | X | | X | | X | | X | |
| **max(0, brnt_cnt - 8)** | | X | | X | | X | | X | | X | |
| **max(0, 8 - brnt_cnt)** | | X | | X | | X | | X | | X | |
| **max(0, brnt_cnt - 50)** | | X | | X | | X | | X | | X | |
| **max(0, brnt_cnt - 74)** | | X | | X | | X | | X | | X | |
| **Indicator for 2001-2003 Refi Boom** | | X | | X | | X | | X | | X | |
| **Months until Interest Rate reset** | | | X | X | | | | | | | |
| **Min # of months since Mod. or Del.** | | | | | X | X | | | | | |
| **min_dt sq.** | | | | | X | X | | | | | |
| **min_dt cb.** | | | | | X | X | | | | | |
| **# of months since last 3+ months delinquent** | | | | | | | | | X | X | |
| **month_from_last_dq sq.** | | | | | | | | | X | X | |
| **month_from_last_dq cb.** | | | | | | | | | X | X | |
| **Debt to Income Ratio** | | | | | | | | | | | X |
| **Fixed Rate Mortgage 40 YR** | | | | | | | | | | | X |
| **Fixed Rate Mortgage 30 YR** | | | | | | | | | | | X |
| **Fixed Rate Mortgage 15 YR** | | | | | | | | | | | X |
| **Non Fixed Rate Mortgage** | | | | | | | | | | | X |
| **Alta Loan Indicator** | | | | | | | | | | | X |
| **IO Loan Indicator** | | | | | | | | | | | X |
| **Jumbo Loan Indicator** | | | | | | | | | | | X |
| **max(0, unemp_rate - 9)** | | | | | | | | | | | X |
| **max(0, 9 - unemp_rate)** | | | | | | | | | | | X |
| **max(0, unemp_rate - 7)** | | | | | | | | | | | X |
| **max(0, unemp_rate - 3)** | | | | | | | | | | | X |
| **max(0, unemp_rate - 5.5)** | | | | | | | | | | | X |
| **max(0, mtmltv - 95)** | | | | | | | | | | | X |
| **max(0, 95 - mtmltv)** | | | | | | | | | | | X |
| **max(0, mtmltv - 50)** | | | | | | | | | | | X |
| **max(0, mtmltv - 80)** | | | | | | | | | | | X |
| **max(0, mtmltv - 30)** | | | | | | | | | | | X |
| **max(0, mtmltv - 140)** | | | | | | | | | | | X |
| **max(0, mtmltv - 5)** | | | | | | | | | | | X |
| **Refi Incentive with 2 months lag** | | | | | | | | | | | X |
| **January Indicator** | | | | | | | | | | | X |
| **February Indicator** | | | | | | | | | | | X |
| **March Indicator** | | | | | | | | | | | X |
| **April Indicator** | | | | | | | | | | | X |
| **May Indicator** | | | | | | | | | | | X |
| **June Indicator** | | | | | | | | | | | X |
| **July Indicator** | | | | | | | | | | | X |
| **August Indicator** | | | | | | | | | | | X |
| **September Indicator** | | | | | | | | | | | X |
| **October Indicator** | | | | | | | | | | | X |
| **November Indicator** | | | | | | | | | | | X |
| **Number of variables (not including server)** | 45 | 59 | 46 | 60 | 48 | 62 | 45 | 59 | 48 | 62 | 45 |

[cite_start]*Table 3. Variable Specification for Each Segment and Transition State* 

### 9.2 Loss Severity Model

#### 9.2.1 Net Sales Proceeds

| STATE | Intercept | B1 | B2 | B3 | B4 | B5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **US** | -12,770 | 0.6100 | 0.4037 | -0.2962 | 0.4257 | -0.7506 |
| **AK** | -6,629 | 0.5896 | 0.1399 | 0.0817 | -0.0189 | -0.3981 |
| **AL** | -4,625 | 0.4362 | 0.6206 | -0.2467 | 0.1910 | -0.4823 |
| **AR** | -6,853 | 0.5092 | 0.3353 | -0.0581 | 0.0036 | -0.2365 |
| **AZ** | -21,142 | 0.8813 | 0.2741 | -0.4058 | 0.3300 | -0.6441 |
| **CA** | -24,400 | 0.9065 | 0.1832 | -0.4021 | 0.4324 | -0.8152 |
| **CO** | -17,019 | 0.7471 | 0.1400 | -0.1218 | -0.1299 | -0.2058 |
| **CT** | 4,454 | 0.4705 | 0.2142 | 0.0323 | 0.1421 | -0.2392 |
| **DC** | -204,334 | 1.9612 | -0.8966 | -0.6565 | 1.6885 | -1.5867 |
| **DE** | -22,316 | 0.6420 | 0.5005 | -0.0440 | -0.1772 | -0.2271 |
| **FL** | -15,634 | 0.7377 | 0.4177 | -0.3895 | 0.4998 | -0.8587 |
| **GA** | -13,374 | 0.6745 | 0.3974 | -0.1993 | 0.1257 | -0.4938 |
| **HI** | -49,182 | 0.7797 | -0.2256 | 0.2252 | 0.1202 | -0.5315 |
| **IA** | -4,471 | 0.4285 | 0.2619 | 0.0265 | 0.2717 | -0.2937 |
| **ID** | -14,382 | 0.7768 | 0.3558 | -0.5865 | 0.3144 | -0.5115 |
| **IL** | -9,810 | 0.5199 | 0.4761 | -0.2639 | 0.4812 | -0.7892 |
| **IN** | -2,522 | 0.3463 | 0.3673 | 0.0441 | 0.3125 | -0.5105 |
| **KS** | -1,622 | 0.4087 | 0.3278 | 0.0992 | 0.4764 | -0.6023 |
| **KY** | -7,191 | 0.4655 | 0.4254 | -0.0057 | 0.0560 | -0.3701 |
| **LA** | -5,037 | 0.4662 | 0.2961 | -0.0013 | 0.2983 | -0.5261 |
| **MA** | -11,433 | 0.6190 | 0.1543 | -0.2059 | 0.7204 | -1.1389 |
| **MD** | -20,018 | 0.6131 | 0.2978 | -0.0508 | -0.0053 | -0.3005 |
| **ME** | -8,024 | 0.3889 | 0.1687 | 0.1822 | 0.1107 | -0.5415 |
| **MI** | -7,868 | 0.5110 | 0.4240 | -0.2232 | 0.6625 | -0.9378 |
| **MN** | -15,567 | 0.6506 | 0.5308 | -0.4883 | 0.4825 | -0.8187 |
| **MO** | -2,524 | 0.3538 | 0.4809 | -0.0839 | 0.6246 | -0.8867 |
| **MS** | -2,226 | 0.3811 | 0.4733 | 0.0897 | -0.0627 | -0.3817 |
| **MT** | -19,052 | 0.6848 | 0.0579 | -0.2007 | 0.1575 | -0.4375 |
| **NC** | -8,053 | 0.5369 | 0.3975 | -0.1080 | 0.0404 | -0.4089 |
| **ND** | -6,887 | 0.4572 | 0.5572 | -0.9104 | 1.3295 | -1.2491 |
| **NE** | -3,621 | 0.4825 | 0.1923 | 0.4157 | -0.2405 | -0.0997 |
| **NH** | -7,224 | 0.5523 | 0.2285 | -0.1163 | 0.2773 | -0.5377 |

[cite_start]*Table 34. Enterprise 1&2 Net Sale Proceeds Coefficients for REO properties only (disposition years 2012-2020)* 

| STATE | Intercept | B1 | B2 | B3 | B4 | B5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **NJ** | -14,445 | 0.5891 | 0.1074 | -0.0834 | 0.4658 | -0.6003 |
| **NM** | -20,386 | 0.7801 | 0.0645 | -0.1154 | -0.0016 | -0.2471 |
| **NV** | -18,959 | 0.9179 | 0.3429 | -0.3622 | 0.2919 | -0.6829 |
| **NY** | -2,431 | 0.4159 | 0.2092 | 0.0949 | 0.2198 | -0.2972 |
| **OH** | -3,262 | 0.3570 | 0.3436 | 0.0194 | 0.4084 | -0.4390 |
| **OK** | -4,697 | 0.4578 | 0.3087 | 0.0407 | 0.0175 | -0.2276 |
| **OR** | -27,713 | 0.8434 | 0.1366 | -0.1530 | -0.0017 | -0.4396 |
| **PA** | -3,775 | 0.4049 | 0.3180 | -0.1013 | 0.2682 | -0.3375 |
| **PR** | -7,975 | 0.7121 | -0.0190 | -0.0285 | -0.0194 | -0.2714 |
| **RI** | -10,096 | 0.5592 | 0.2087 | -0.1637 | 0.2259 | -0.2738 |
| **SC** | -10,251 | 0.5703 | 0.4202 | -0.1738 | 0.1019 | -0.4257 |
| **SD** | -10,164 | 0.5620 | 0.2202 | -0.2154 | 0.6774 | -0.7411 |
| **TN** | -15,612 | 0.6565 | 0.1536 | -0.0193 | 0.1773 | -0.4686 |
| **TX** | -7,780 | 0.6338 | 0.4151 | -0.6397 | 1.2427 | -1.5674 |
| **UT** | -23,482 | 0.8670 | 0.2005 | -0.4450 | 0.4129 | -0.6626 |
| **VA** | -16,643 | 0.6402 | 0.5021 | -0.4499 | 0.5944 | -1.0209 |
| **VT** | 4,386 | 0.2613 | 0.5016 | -0.0410 | 0.0947 | -0.6198 |
| **WA** | -21,531 | 0.7457 | 0.2502 | -0.1796 | 0.2995 | -0.7615 |
| **WI** | -6,424 | 0.4697 | 0.3741 | -0.2192 | 0.7870 | -1.1130 |
| **WV** | -4,826 | 0.3933 | 0.2396 | -0.0793 | 0.8209 | -1.1347 |
| **WY** | -12,197 | 0.6273 | 0.1832 | -0.1092 | -0.0658 | -0.1365 |

[cite_start]*Table 35. Enterprise 1 & 2 Net Sale Proceeds Coefficients for Foreclosure Alternative dispositions only (disposition years 2012-2020)* 

#### 9.2.2 Transaction Costs for an NPL Sale

[cite_start]The transaction costs for an NPL sale i (Transaction costs for an NPL sale~i~) are defined as follows: 

*Transaction costs for an NPL sale~i~ = Appraisal fees + Attorney and trustee fees + Other foreclosure expense + Other liquidiation expenses + Other non selling expense~i~ + Property inspection + Maintenance expense + Utilities + Possessory and eviction fees + Repairs + Title insurance fees + Property management expense + Servicer incentive payment~i~*
[cite_start]*∀ i ∈ NPL sales* 

Most NPL sales doesn't have values for the following components: (1) possessory and eviction fees; (2) repairs; (3) title insurance fees; [cite_start](4) service incentive payment, and (5) Property_Management_Expense. 

| Enterprise 1 Liquidated UPB Categories | Enterprise 2 Liquidated UPB Categories |
| :--- | :--- |
| Liquidated UPB < 95924 | Liquidated UPB < 179765 |
| 95924 <= Liquidated UPB < 162645 | 107400 <= Liquidated UPB < 179765 |
| 162645 <= Liquidated UPB < 251689 | 179765 <= Liquidated UPB < 270431 |
| Liquidated UPB => 251689 | Liquidated UPB >= 270431 |

[cite_start]*Table 40. Liquidated UPB Categories by Enterprise* 

| liq_upb_group | Judicial state | trans_cost_w |
| :--- | :--- | :--- |
| All | Entire | 6.4760 |
| Liquidated UPB <95924 | Entire | 11.7498 |
| 95924<=Liquidated UPB <162645 | Entire | 7.5359 |
| 162645<=Liquidated UPB <251689 | Entire | 5.8004 |
| Liquidated UPB>=251689 | Entire | 5.5275 |
| Liquidated UPB <95924 | Non-Judicial | 8.4810 |
| Liquidated UPB <95924 | Judicial | 13.3240 |
| 95924<=Liquidated UPB <162645 | Non-Judicial | 5.7777 |
| 95924<=Liquidated UPB <162645 | Judicial | 8.3994 |
| 162645<=Liquidated UPB <251689 | Non-Judicial | 4.3930 |
| 162645<=Liquidated UPB <251689 | Judicial | 6.4754 |
| Liquidated UPB>=251689 | Non-Judicial | 4.0830 |
| Liquidated UPB>=251689 | Judicial | 6.0537 |

[cite_start]*Table 41. Enterprise 1 NPL Note Sales Transaction Costs* 

| liq_upb_group | Judicial state | trans_cost_w |
| :--- | :--- | :--- |
| All | Entire | 2.7557 |
| Liquidated UPB <107400 | Entire | 6.4614 |
| 107400<=Liquidated UPB <179765 | Entire | 3.6052 |
| 179765<=Liquidated UPB <270431 | Entire | 2.5703 |
| Liquidated UPB>=270431 | Entire | 1.8093 |
| Liquidated UPB <107400 | Non-Judicial | 4.8332 |
| Liquidated UPB <107400 | Judicial | 7.2157 |
| 107400<=Liquidated UPB <179765 | Non-Judicial | 2.9401 |
| 107400<=Liquidated UPB <179765 | Judicial | 3.9719 |
| 179765<=Liquidated UPB <270431 | Non-Judicial | 2.1510 |
| 179765<=Liquidated UPB <270431 | Judicial | 2.8002 |
| Liquidated UPB>=270431 | Non-Judicial | 1.5142 |
| Liquidated UPB>=270431 | Judicial | 1.9388 |

[cite_start]*Table 42. Enterprise 2 NPL Note Sales Transaction Costs* 

#### 9.2.3 Fixed Costs

[cite_start]The table below presents the results for REO fixed costs using data for liquidation dates from 2016-2020. 

| STATE | Intercept | B1 | B2 | B3 | B4 | B5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **US** | 62.15438 | 0.960884 | -0.81129 | -0.23366 | 0.055273 | 0.017983 |
| **AK** | 17.2172 | -0.07538 | -0.0393 | 0.194558 | -0.13164 | 0.046234 |
| **AL** | 45.52273 | 0.74622 | -0.68285 | -0.08351 | -0.03542 | 0.027185 |
| **AR** | 50.84624 | -0.90275 | 1.082902 | -0.23006 | 0.021381 | 0.009975 |
| **AZ** | 17.77514 | -0.10524 | -0.01663 | 0.131037 | -0.02567 | 0.001724 |
| **CA** | 25.39388 | -0.10908 | 0.137152 | -0.06406 | 0.010242 | 0.03445 |
| **CO** | 41.78155 | -0.46414 | 0.449543 | 0.012064 | -0.02087 | 0.012878 |
| **CT** | 212.4139 | -2.07243 | 3.092698 | -1.33104 | 0.321759 | -0.00882 |
| **DC** | 20.34779 | -0.04948 | -0.02712 | -0.0241 | 0.107145 | 0.000371 |
| **DE** | 42.68649 | 0.324705 | -0.26832 | -0.17881 | 0.175152 | -0.08823 |
| **FL** | 60.15516 | -0.51858 | 0.58568 | -0.13554 | 0.049322 | 0.013847 |
| **GA** | 34.25614 | -0.37566 | 0.503163 | -0.1732 | 0.029372 | 0.002176 |
| **HI** | 73.93931 | -0.3718 | 0.431651 | -0.1185 | 0.035263 | 0.012605 |
| **IA** | 56.84247 | -0.97621 | 0.775079 | 0.447421 | -0.3477 | 0.084003 |
| **ID** | 10.43044 | 0.1507 | -0.38734 | 0.123158 | 0.069131 | 0.0262 |
| **IL** | 57.54701 | -0.67405 | 0.698755 | -0.10389 | 0.069907 | 0.012388 |
| **IN** | 56.54632 | 1.002276 | -0.97632 | -0.0613 | 0.027309 | 0.003174 |
| **KS** | 44.68834 | -0.66924 | 0.340629 | 0.497289 | -0.14883 | -0.03281 |
| **KY** | 61.35904 | -0.89819 | 1.00929 | -0.18856 | 0.057181 | -0.02518 |
| **LA** | 59.93409 | -0.7547 | 0.882484 | -0.26408 | 0.12515 | -0.01314 |
| **MA** | 84.48434 | -0.61951 | 0.79657 | -0.24319 | 0.05026 | 0.006185 |
| **MD** | 65.87139 | 0.590166 | -0.53194 | -0.10506 | 0.010914 | 0.036022 |
| **ME** | 56.31967 | 0.697897 | -0.62403 | -0.17105 | 0.027081 | 0.042339 |
| **MI** | 63.01637 | -1.12864 | 1.393842 | -0.35296 | 0.145884 | -0.07379 |
| **MN** | 36.07118 | -0.25068 | 0.127144 | 0.182041 | -0.15005 | 0.07606 |
| **MO** | 51.84551 | -0.91029 | 1.145894 | -0.32901 | 0.083769 | -0.01035 |
| **MS** | 50.74813 | 1.376872 | -0.92879 | -0.52876 | 0.051888 | -0.00411 |
| **MT** | 16.96773 | -0.11792 | 0.003681 | -0.07363 | 0.209869 | -0.06472 |
| **NC** | 43.59939 | -0.49796 | 0.595517 | -0.14482 | -0.01442 | 0.037181 |
| **ND** | 68.90828 | -0.8488 | 1.269247 | -0.63887 | 0.183677 | 0.012822 |
| **NE** | 41.34585 | 0.439329 | -0.68334 | 0.298702 | 0.016064 | -0.10585 |
| **NH** | 22.39889 | -0.10296 | 0.134657 | -0.06839 | 0.030689 | -0.01621 |
| **NJ** | 54.06007 | -0.34307 | 0.371452 | -0.05937 | -0.00749 | 0.051732 |
| **NM** | 45.52069 | -0.35938 | 0.39768 | -0.13745 | 0.061827 | 0.003249 |
| **NV** | 20.62588 | 0.00889 | -0.05372 | 0.094873 | -0.12768 | 0.078015 |

[cite_start]*Table 43. Fixed Cost for REO Dispositions (Enterprise 1)* 

#### 9.2.4 Carrying Costs

[cite_start]Carrying costs for defaulted loan i (Carrying Costs~i~) are defined as carrying costs times the number of months from last paid installment date to REO liquidation date.  [cite_start]For foreclosure alternatives carrying costs are calculated from last paid installment date to title transfer date (liquidation). 

*Carrying Costs~i~ = (Property taxes + Property insurance + HOA fees + Condominimum fees~i~ + Maintenance fees~i~) \* Number of months from Last Paid Installment Rate to REO liquidation*
*∀ i ∈ REO* 

*Carrying Costs~i~ = (Property taxes + Property insurance + HOA fees~i~ + Condominimum fees~i~ + Maintenance fees~i~) \* Number of months from Last Paid Installment Date to title transfer date*
[cite_start]*∀ i ∈ Foreclosure alternative* 

**Months from Foreclosure to REO Property Disposition**

[cite_start]The number of months from foreclosure to property disposition is estimated for both Enterprises for REOs that have completed their disposition between 2012 and 2020.  [cite_start]This measure is the liquidated UPB weighted average months from foreclosure completion date to property disposition date.  [cite_start]Months from foreclosure date to property disposition date are multiplied by calculated monthly carrying costs to create total for REO dispositions.  [cite_start]See table below for weighted average months by Enterprise. 

| State | Enterprise 1 Liquidation UPB Weighted Average Months to REO Disposition | Enterprise 2 Liquidation UPB Weighted Average Months to REO Disposition |
| :--- | :--- | :--- |
| **US** | 8.6 | 8.4 |
| **AK** | 8.6 | 9.9 |
| **AL** | 7.3 | 7.6 |
| **AR** | 6.4 | 7.1 |
| **AZ** | 5.8 | 5.5 |
| **CA** | 8.2 | 7.6 |
| **CO** | 7.2 | 7.3 |
| **CT** | 9.4 | 9.1 |
| **DC** | 12.6 | 16.7 |
| **DE** | 8.2 | 9.0 |
| **FL** | 7.1 | 7.0 |
| **GA** | 6.8 | 6.8 |
| **HI** | 14.7 | 16.6 |
| **IA** | 6.3 | 6.6 |
| **ID** | 7.0 | 6.4 |
| **IL** | 10.8 | 10.6 |
| **IN** | 6.3 | 5.2 |
| **KS** | 8.3 | 8.8 |
| **KY** | 8.9 | 8.6 |
| **LA** | 7.0 | 7.8 |
| **MA** | 10.0 | 11.6 |
| **MD** | 12.4 | 13.9 |
| **ME** | 6.6 | 7.7 |

[cite_start]*Table 49. Liquidation UPB-weighted Average Months to REO Disposition, by Enterprise* 

#### 9.2.5 Loss Severity Module Variable Definition

[cite_start]Loss Severity Module involves numerous definitions and variables.  [cite_start]Below is a table summarizing the major variables in the module. 

* **Accounting transaction types**
* Appraisal Fees
* Attorney and Trustee Fees
* Borrower Closing Costs
* Broker Fees
* Credit Enhancement Proceeds
* Discount Points
* Gross Property Sale Price
* HOA and Condo Fees
* Insurance
* Maintenance Expense
* MI Proceeds
* Other Foreclosure Expense
* Other Income
* Other Liquidation Expenses
* Other Non-Selling Expense
* Possessory and Eviction Fees
* Property Rental Income
* Property Inspection
* Property Management Expense
* Repairs
* Sales Expense
* Seller Closing Expense
* Seller Loan Repair Amount
* Taxes
* Title Insurance Fee
* Utilities
* Reps and Warrants Proceeds
* Incentive Payment
* Net Sales Proceeds
* **Other Loss severity data**
* [cite_start]**Foreclosure date** - the date when the foreclosure is completed and the title has been transferred from borrower to the Enterprises. 
* [cite_start]**Disposition date** - the date the REO property is sold from REO inventory 
* **Sale price at liquidation** - the sale price of the property at liquidation date for foreclosure alternatives (third party sale and short sale) 
* [cite_start]**Dummy variable Judicial state** - this dummy identifies the states that have foreclosures go through the courts.  [cite_start]These are states Connecticut (CT), Delaware (DE), Florida (FL), Hawaii (HI), Iowa (IA), Illinois (IL), Indiana (IN), Kansas (KS), Kentucky (KY), Louisiana (LA), Maine (ME), North Dakota (ND), New Jersey (NJ), New Mexico (NM), New York (NY), Ohio (OH), Oklahoma (OK), Pennsylvania (PA), South Carolina (SC), Vermont (VT), and Wisconsin (WI). 
* **Dummy variable non-Judicial state** - all other states do not have court proceedings to complete the foreclosure. 

*Table 50. Loss Severity Module Fields and Definitions* 

#### 9.2.6 Loss Severity Module Back-testing of Each Component

In this section, we look at the first component of net losses, which is the net sales proceeds on three different disposition types.  We divide net sales proceeds by the liquidation unpaid principal balance to obtain the net sale proceed ratios.  Overall, predicted values track actual values throughout the years with the largest discrepancies for years 2012 to 2013 as well as 2020.  Here the net sales proceeds are calculated as follows: 

*Net sale proceeds~i~ = Gross property sale proceeds - Sales expense - Other selling expense - Broker fees~i~ - Borrower closing costs~i~*
*∀ i for REOs or foreclosure alternatives* 

*Net sale proceeds~i~ = NPL sale proceeds - Sales expense - Other selling expense - Broker fees~i~ - Borrower closing costs~i~*
*∀ i for NPL sales* 

#### 9.2.7 Fixed Costs Ratios

The figure below compares the predicted fixed costs ratios with actual cost ratios, both scaled by liquidation unpaid principal balance.  We divide fixed costs by the liquidation unpaid principal balance to get the fixed costs ratios.  As shown in the figure below, before year 2017 the predicted values consistently overestimate fixed cost ratios.  However, the predicted values underestimated the ratios since 2017.  It seems that there is still some recent upward shifting trend in fixed costs being missed in predicting the fixed costs component.  Below is the formula for calculating fixed costs for REOs and foreclosure alternatives: 

*Fixed costs = Appraisal Fees + Attorney and Trustee Fees~i~ + Other Foreclosure Expenses + Other Liquidation Expenses~i~ + Maintenance Expenses + Property Inspection Fees + Repairs~i~ + Utilities costs~i~*
*∀ i for REOs or foreclosure alternatives* 

The fixed costs on NPL sales are also called liquidation expenses and they are calculated as follows: 

*Fixed costs~i~ = Appraisal Fees + Attorney and Trustee Fees~i~ + Other Foreclosure Expenses + Other Liquidation Expenses~i~ + Other Non Selling Expenses + Maintenance Expenses~i~ + Property Inspection Fees + Repairs + Utilities costs + Possessory and Eviction Fees + Title Insurance Fees~i~ + Property Management Expenses + Servicer Incentive Payments~i~*
*∀ i for NPL sales* 

#### 9.2.8 Carrying Costs Ratios

Carrying costs consist of five components: (1) insurance fees, (2) taxes, (3) HOA, (4) condo fees, and (5) accrued interests before disposition.  As with other items, carrying cost ratios, which equals carrying costs divided by liquidation unpaid balance amount, are also reasonably well predicted in aggregate across all loans.  Though not shown below, the predictions match well with actuals also across different cohorts by disposition types, and by judicial or non-judicial states. 

#### 9.2.9 Mortgage Insurance Proceeds Ratios

Mortgage insurance proceeds ratios are calculated by dividing mortgage insurance proceeds by the liquidation unpaid principal balance to get mortgage insurance proceed ratios.  Mortgage insurance proceeds ratios have the second largest discrepancy between predicted and actual values after fixed costs ratios.  However, other than the last year considered (2020), most other years seem to have reasonable predictions. 

### 9.3 Simulation

#### 9.3.1 Markov Chain Simulation Framework Implementation

In the main context, we illustrate the Markov Chain in terms of matrix operations.  Here we are presenting how it is implemented. 

**Problem**: Given that, at time t, the probability in each state is known, how to compute the probability of each state at time t+1. 

**Solution**: 

1.  Use behavioral equations to get transition rate from time t to time t+1. 
2.  Compute the marginal probabilities at time t+1, which is the weighted average of transition rates weighted by the probabilities of each state at time t. 

#### 9.3.2 Monte Carlo Simulation Framework Implementation

Based on the state of the loan at month t, one invokes the corresponding behavior equation to calculate the probabilities of states at month t+1, then use a random number to select a state among the several possible states. 

#### 9.3.3 Cash Flow-Based Simulation

#### 9.3.3.1 Performing and Nonperforming Unpaid Principal Balance

In general, for a particular month, a given loan can either perform (i.e., pay as scheduled per terms of the loan contract) or fail to perform (i.e., not pay as scheduled per terms of the loan contract) or prepay.  If a loan performs, then its unpaid principal balance (i.e., the amount contractually owed) is characterized as a performing unpaid principal balance.  If a given loan fails to perform, then it is considered delinquent, and its unpaid principal balance is characterized as a nonperforming unpaid principal balance. 

Performing unpaid principal balance at a current point in time, say month t, equals a sum of two parts.  The first part reflects the amount of performing unpaid principal balance from the prior period, say the previous month t-1, that remains performing at month t.  The second part reflects the amount of the delinquent unpaid principal balance from a prior period that transitions to performing status at month t. 

#### 9.3.3.2 Prepayment Amount (Unscheduled Principal)

The projection of prepayment amount is similar to the projection of performing unpaid principal balance described previously.  Prepayment amount in a current period, say at month t, equals the sum of the following: the amount of performing unpaid principal balance from a previous period, say month t-1, that prepays in the current period plus the amount of the delinquent unpaid principal balance from the previous period that prepays in the current period. 

#### 9.3.3.3 Delinquent Amount

Delinquent amount at month t is the sum of LDQ (3-5 months delinquent) amount, SDQ (6-11 month of delinquent) amount, and DDQ (12 or more month of delinquent) amount.  A loan that is LDQ at month t may result from the following: transition from performing loan at month t-1 remains LDQ from prior month LDQ loan; transition from a SDQ loan at prior month; or transition from DDQ loan at prior month.  A SDQ loan at month t may: transition from a LDQ loan at month t-1; remains SDQ status from prior month SDQ status; or transition from a DDQ loan at prior month.  A DDQ loan at month t may result from the following: transition from a SDQ loan at month t-1; or remains DDQ from a DDQ loan at prior month. 

#### 9.3.3.4 Default Unpaid Principal Balance

Projected default amount at month t is the amount of delinquent UPB at month t-1 defaults at month t.  This amount is equal to delinquent UPB at month t-1 multiplies the conditional probabilities of default at month t given delinquency at t-1. 

#### 9.3.4 Cashflow-based Simulation vs. Markov Chain Simulation

Markov chain approach is focusing on the unconditional probabilities first (without the cashflow consideration), then using scheduled UPB to derive the prepay amount and using weighted lagged scheduled UPB to derive the default amount.  Cashflow based simulation first calculates conditional probabilities, and then uses the projected UPB in the prior period to derive cash flows.  As an example, consider the calculation of prepayment amount. 

In Markov chain approach,

*Prepaid amount (t) = Prep_prob(t) \* Schd_UPB(t)* 

In cash flow-based approach, this amount is calculated as the sum of: 

* [cite_start]Prepay amount transition from performing UPB at t-1; perf_prep(t) \* Perf_UPB(t-1), subtract scheduled principal payment (amount due) 
* [cite_start]Prepay amount transition from LDQ at t-1: ldq_prep(t) \* LDQ_UPB(t-1), subtract scheduled principal payment (amount due), and amount owe from LPI to t-1 
* [cite_start]Prepay amount transition from SDQ at t-1; sdq_prep(t) \* SDQ_UPB(t-1), subtract scheduled principal payment (amount due), and amount owe from LPI to t-1 
* [cite_start]Prepay amount transition from DDQ at t-1: ddq_prep(t) \* DDQ_UPB(t-1), subtract scheduled principal payment (amount due), and amount owe from LPI to t-1 

Although the difference seems obvious in formulation, the actual differences (both formulation and numerical) are small. 

### 9.4 Summary Information

Below is summary information provided in compliance with FHFA's Information Quality Guidelines. 

| Requirement | Response |
| :--- | :--- |
| **1. Describe the underlying source of any data used to create the product, including whether FHFA or a different agency collected the data.** | Single-Family Mortgage Analytics Platform (SF FMAP) consists of two separate sets of underlying data, which vary depending on the type of SF FMAP equation: behavioral equations or loss severity equations. For the behavioral equations, the underlying data come from three sources; namely, (i) Mortgage Loan Integrated System (MLIS); (ii) FHFA-produced House Price Index (HPI); and (iii) a vendor. Regarding MLIS, each month, Fannie Mae and Freddie Mac provide FHFA with borrower and collateral information on their mortgage holdings. The vendor provides historical and forecast house price, market rates, and unemployment rates. For the loss severity equations, the underlying source data come from multiple sources as well. First, Fannie Mae and Freddie Mac (The Enterprises) provide monthly loan-level real-estate owned fixed costs data. Second, The Enterprises provide monthly transaction-level costs for non-performing loan sales. Lastly, house price index data is provided by a vendor. Combined, these data serve as the estimation data that feed SF FMAP.  |
| **2. Describe the statistical methods or models used to create the product.** | SF FMAP consists of three sets of statistical/quantitative methods embedded within SF FMAP. In the behavioral equations of SF FMAP, the statistical methods include a set of binomial logistic regressions and a set of multinomial logistic regressions. In the loss severity equations of SF FMAP, the statistical method is a set of linear regressions. Lastly, the simulation module of SF FMAP includes a cash flow calculation method, Markov Chain-based method, and Monte Carlo-based method.  |
| **3. Describe the intended uses of the product, and if applicable, uses not recommended.** | SF FMAP is a decision support tool used to provide independent analytic support to Agency decision makers on a wide variety of policies such as, but not limited to, Dodd-Frank Act Stress Test, Conservatorship Capital Framework, and the Private Mortgage Insurer Eligibility Requirements. The white paper describes the modeling rationale, theoretical underpinnings, and empirical results from updating and enhancing the production version of SF FMAP.  |
| **4. Describe the time period presented in the event or phenomenon reflected in the product.** | SF FMAP consists of several sets of time periods, which vary depending upon the SF FMAP module. For the set of behavioral equations of SF FMAP, the time period for the estimation sample reflects borrower and collateral information from Jan. 2000 to Dec. 2019. For the loss severity equations of SF FMAP, the time period for the loss data sample ranges from Jan. 2011 to Jul. 2022. For the simulation module, the time period for simulated single-family credit loss forecasts can range from one to 40 years.  |
| **5. Describe the granularity (i.e., amount of disaggregation) of any key estimates.** | SF FMAP consists of several levels of granularity, which vary depending upon the SF FMAP module. For the set of behavioral equations of SF FMAP, the level of granularity is threefold: (i) loan-level for behavioral and collateral data; (ii) metropolitan level for house price and unemployment rate; and (iii) national-level for market rates. For the set of loss severity equations of SF FMAP, the level of granularity is loan-level varies from loan-level to aggregate-levels of various dimensions. For the simulation module of SF FMAP, the level of granularity varies from loan-level to aggregate-levels of various dimensions (e.g., loan characteristic, geography, book-level, etc….)  |
| **6. Where applicable, describe any known major or significant errors in the underlying source data used to create the product.** | The loan level data used for the model fitting is from the historical loan-level database of mortgage, property, and borrower characteristics (excluding Personally Identifiable Information) submitted by the Enterprises. The Enterprises perform data validation for each submission. Since FMAP is estimated using a sample of loans from the historical loan-level database, loans with errors (missing or unreasonable values) are filtered out from the sample to ensure that data used for model estimation is clean.  |
| **7. Where applicable, describe how users can estimate errors, such as errors from sampling.** | To estimate errors, users need to repeat the sampling and estimation process that were done in the update and collect the errors from the estimation. To estimate sampling error, users need to calculate the summary statistics of the sample and population and calculate the difference of the two sets of summary statistics.  |
| **8. Where applicable, describe the consistency or comparability with estimates contained in other products published by FHFA.** | The document describes a model that is an update to the predecessor model described in the prior version of the document. Since the equations have been re-estimated since the prior model, the estimates themselves are incomparable. There is no other products published by FHFA that has same intended uses as SF FMAP.  |
| **9. Where applicable, describe the steps taken to ensure the product protects the privacy and confidentiality of underlying entity (e.g., borrower, business) reflected in the source data, where applicable.** | FHFA staff do not disclose any private or confidential information in the working paper. At the individual loan level, the analysis relies upon the historical loan-level database of mortgage, property, and borrower characteristics submitted by the Enterprises. the database omits private or confidential information. At the Enterprise level, FHFA staff anonymize the Enterprises rather than reveal their names when appropriate.  |
| **10. Where applicable, describe the verification and validation steps taken to ensure errors are not introduced in the production process.** | FHFA staff continually review the working paper until it has been posted. In particular, (i) FHFA SF FMAP model risk personnel series of collaboration/meetings, (ii) external review of FHFA non-SF-FMAP personnel, (iii) external presentation and review by FHFA Office of Financial Analysis and Division of Research and Statistics personnel, and (iv) executive-level review.  |
| **11. Where applicable, describe the “chain of custody” of the product from its verification and validation to when it is posted on the website.** | After posting of the working paper, FHFA staff intends to perform a check to ensure the file posted matches the file intended for posting.  |

*Table 51. Summary Information* 

### Bibliography

* Begg, Colin B. and Robert Gray. “Calculation of Polychotomous Logistic Regression Parameters Using Individualized Regressions”. Biometrika. [cite_start]Volume 71, Number 1. April 1984. 
* BlackRock Solutions. The BRS v6.1 Agency Credit Model. [cite_start]October 2020. Internal document. 
* Calhoun, C. A. and Y Deng (2002), “A Dynamic Analysis of Fixed- and Adjustable- Rate Mortgage Terminations,” Journal of Real Estate Finance and Economics, 24 (1/2): 9-33. 
* Clapp, John M., Goldberg, Gerson M., Harding, John P., and Michael LaCour-Little (2001), “Movers and Shuckers: Interdependent Prepayment Decisions,” Real Estate Economics, Vol. [cite_start]29, No. 3: 411-450 
* Fannie Mae. CCFA Borrower Behavioral Models. Whitepaper. 2019Q3. [cite_start]Internal document. 
* Federal Housing Finance Agency, Division of Research and Statistics. Mortgage Insight 2020-03 – State Foreclosure Timelines, pg 3. 2020. Internal document. 
* Jenkins, Stephen P. (1995) "Easy Estimation Methods for Discrete-Time Duration Models." Oxford Bulletin of Economics and Statistics, Vol. [cite_start]57, No. 1: 129–136. 
* Milliman. Milliman Mortgage Platform for Investments and Reinsurance (M-PIRe). [cite_start]January 19, 2020. Internal document.