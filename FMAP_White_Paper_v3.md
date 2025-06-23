# FHFA MORTGAGE ANALYTICS PLATFORM
## Version 3.0
### Released by FHFA, November 2022

---

## Table of Contents
* **1 Release Notes** 
* **2 Executive Summary** 
* **3 Overview** 
    * 3.1 Objective and Purpose 
    * 3.2 Description 
* **4 Data Module** 
    * 4.1 Overview 
    * 4.2 Borrower and Collateral Data 
    * 4.3 Macroeconomic Data 
    * 4.4 Loss Severity Data 
    * 4.5 Simulation Data 
* **5 Behavioral Models Module** 
    * 5.1 Overview 
    * 5.2 Framework Specification 
    * 5.3 Model Specification 
    * 5.4 Sample and Methodology 
    * 5.5 Estimation and Results 
    * 5.6 Model Performance Tracking Results 
* **6 Loss Severity Models Module** 
    * 6.1 Overview 
    * 6.2 Framework Specification 
    * 6.3 Data 
    * 6.4 Credit Losses 
    * 6.5 Charge-off Amounts 
    * 6.6 REO Operating Expense 
    * 6.7 Fit Statistics 
* **7 Simulation Module** 
    * 7.1 Overview 
    * 7.2 Cashflow-based Simulation 
    * 7.3 Markov Chain (Continuous) Simulation 
    * 7.4 Monte Carlo (Discrete) Simulation 
* **8 Reporting Module** 
* **9 Appendix** 
    * 9.1 Behavioral Equations 
    * 9.2 Loss Severity Model 
    * 9.3 Simulation 
    * 9.4 Summary Information 
* **Bibliography** 

---

### List of Tables
* **Table 1.** Transition Table 
* **Table 2.** Summary MPT Results for the June 2014, and December 2016 Portfolios* 
* **Table 3.** Variable Specification for Each Segment and Transition State 
* **Table 4.** Segment: F30 Performing, Enterprise 1, Event: Idq 
* **Table 5.** Segment: F15 Performing, Enterprise 1, Event: Idq 
* **Table 6.** Segment: F30 Performing, Enterprise 1, Event: prepay. 
* **Table 7.** Segment: F15 Performing, Enterprise 1, Event: prepay. 
* **Table 8.** Segment: RPL, Enterprise 1, Event: Idq. 
* **Table 9.** Segment: RPL, Enterprise 1, Event: prepay. 
* **Table 10.** Segment: ARMs Performing, Enterprise 1, Event: Idq 
* **Table 11.** Segment: ARMs Performing, Enterprise 1, Event: prepay 
* **Table 12.** Segment: MRPL, Enterprise 1, Event: Idq 
* **Table 13.** Segment: MRPL, Enterprise 1, Event: prepay 
* **Table 14.** Segment: NRPL, Enterprise 1, Event: Idq 
* **Table 15.** Segment: NRPL, Enterprise 1, Event: prepay 
* **Table 16.** Segment: NPL - Idq, Enterprise 1 
* **Table 17.** Segment: NPL - sdq, Enterprise 1 
* **Table 18.** Segment: NPL - ddq, Enterprise 1 
* **Table 19.** Segment: F30 Performing, Enterprise 2, Event: Idq. 
* **Table 20.** Segment: F15 Performing, Enterprise 2, Event: Idq. 
* **Table 21.** Segment: F30 Performing, Enterprise 2, Event: prepay. 
* **Table 22.** Segment: F15 Performing, Enterprise 2, Event: prepay. 
* **Table 23.** Segment: RPL, Enterprise 2, Event: Idq 
* **Table 24.** Segment: RPL, Enterprise 2, Event: prepay. 
* **Table 25.** Segment: ARMs Performing, Enterprise 2, Event: Idq 
* **Table 26.** Segment: ARMs Performing, Enterprise 2, Event: prepay 
* **Table 27.** Segment: MRPL, Enterprise 2, Event: Idq 
* **Table 28.** Segment: MRPL, Enterprise 2, Event: prepay 
* **Table 29.** Segment: NRPL, Enterprise 2, Event: Idq 
* **Table 30.** Segment: NRPL, Enterprise 2, Event: prepay 
* **Table 31.** Segment: NPL - Idq, Enterprise 2 
* **Table 32.** Segment: NPL - sdq, Enterprise 2 
* **Table 33.** Segment: NPL - ddq, Enterprise 2 
* **Table 34.** Enterprise 1&2 Net Sale Proceeds Coefficients for REO properties only (disposition years 2012-2020) 
* **Table 35.** Enterprise 1 & 2 Net Sale Proceeds Coefficients for Foreclosure Alternative dispositions only (disposition years 2012-2020) 
* **Table 36.** Spline Knot Locations for MTMLTV 
* **Table 37.** Spline Knot Locations for Liquidation UPB 
* **Table 38.** Spline Knot Locations for Number of Delinquent Payments 
* **Table 39.** Expected Net Sale Proceeds Parameter Estimates 
* **Table 40.** Liquidated UPB Categories by Enterprise 
* **Table 41.** Enterprise 1 NPL Note Sales Transaction Costs 
* **Table 42.** Enterprise 2 NPL Note Sales Transaction Costs 
* **Table 43.** Fixed Cost for REO Dispositions (Enterprise 1) 
* **Table 44.** Fixed Cost for REO Dispositions (Enterprise 2) 
* **Table 45.** Fixed Cost for Foreclosure Alternative Dispositions (Enterprise 1) 
* **Table 46.** Fixed Cost for Foreclosure Alternative Dispositions (Enterprise 2) 
* **Table 47.** Fixed Cost (or Transaction Expenses) for Non-Performing Loan Sale Dispositions (Enterprise 1) 
* **Table 48.** Fixed Cost (or Transaction Expenses) for Non-Performing Loan Sale Dispositions (Enterprise 2) 
* **Table 49.** Liquidation UPB-weighted Average Months to REO Disposition, by Enterprise 
* **Table 50.** Loss Severity Module Fields and Definitions 
* **Table 51.** Summary Information 

---

### List of Figures
* **Figure 1.** FMAP v3.0 Structure 
* **Figure 2.** Loan Status Schematic 
* **Figure 3.** Example of Performance Tracking, Fixed-rate Mortgage 30-year and 15-year, LDQ and Prepay 
* **Figure 4.** June 2014 Portfolio MPT - Enterprise 1 
* **Figure 5.** June 2014 Portfolio MPT - Enterprise 2 
* **Figure 6.** December 2016 Portfolio MPT - Enterprise 1 
* **Figure 7.** December 2016 Portfolio MPT - Enterprise 2 
* **Figure 8.** Enterprise 1 RMSE and MAE on Loss Severity between 2012-2020 
* **Figure 9.** Enterprise 1 RMSE and MAE of Total Loss Severity Ratios, 2012-2020 
* **Figure 10.** Enterprise 1 Back-testing Results of Total Loss Severity Ratios by Year 
* **Figure 11.** Enterprise 1 Back-testing Results of Total Loss Severity Ratios by Disposition Type 
* **Figure 12.** Simulation Engine within FMAP 
* **Figure 13.** Enterprise 1 Back-testing Results of Net Sales Proceeds Ratios, 2012-2022 
* **Figure 14.** Enterprise 1 Back-testing Results of Fixed Costs Ratios, 2016-2020 
* **Figure 15.** Enterprise 1 Back-testing Results of Carrying Costs Ratios, 2012-2020 
* **Figure 16.** Enterprise 1 Back-testing Results of MI Proceeds Ratios, 2012-2020 

---

## 1 Release Notes

This white paper incorporates the following major enhancements and updates reflected in the third version of the Single-family FHFA Mortgage Analytics Platform (FMAP v3.0) since version 2.0 of FMAP was released in May 2020:[^1]

* Redesigns and re-estimates loan behavioral equations. 
* Develops and implements a proprietary loss severity model. 
* Uses expanded and more representative loan performance data and more granular level economic data to estimate mortgage performance model. 
* Estimates the behavioral equations via an iterative, out-of-sample, model building process. 

## 2 Executive Summary

FMAP is a proprietary analytic system developed by the Federal Housing Finance Agency (FHFA) to inform Agency policy decisions.  Essentially, the system forecasts mortgage performance of Fannie Mae and Freddie Mac (the Enterprises) loan portfolios under various economic scenarios and time horizons.  These forecasts are based upon historical relationships among borrower, collateral, and macroeconomic information.  This white paper describes the most recent version of FMAP, FMAP v3.0. 

FMAP v3.0, like its predecessors, provides analytic support for Agency policy decisions.  Previous examples of FMAP support include the following: 

* FHFA issued the Enterprise Regulatory Capital Framework Final Rule (ERCF) that establishes credit and market risk capital requirements for the guarantee, whole loan, and retained portfolios of the Enterprises using credit score, loan-to-value, and other loan characteristics.  FMAP informed the ERCF credit risk capital requirements for single-family new acquisitions. 
* The Dodd-Frank Act Stress Test requires certain financial institutions to conduct periodic stress tests to determine whether they have sufficient capital to absorb losses and support operations during adverse economic conditions.  FHFA requires the Enterprises to conduct stress tests pursuant to the Dodd-Frank Act.  FHFA uses FMAP to provide an independent benchmark to compare against the Enterprises' single-family credit loss projections. 
* During and after the 2007-2008 financial crisis, the Enterprises suffered losses due to the failure of insufficiently capitalized counterparties to honor their respective obligations.  As a safety and soundness matter, FHFA established the Private Mortgage Insurance Eligibility Requirements Standards (PMIERS), which mandated financial requirements for mortgage insurers interested in serving as counterparties to the Enterprises.  FMAP provided analytic support in establishing these standards. 

FMAP v3.0 contains a series of major enhancements and upgrades to FMAP v20, the current production version.  These new changes include the redesign and re-estimation of the loan performance model and implementation of an internally developed loss severity model.  The new loan performance model expanded FMAP's ability to model loan performance at a more granular level.  Additionally, FMAP v3.0 loan performance equation were estimated using an out-of-time model building approach and more robust nonlinearity specification, which minimizes model overfitting. 

## 3 Overview

### 3.1 Objective and Purpose

FHFA developed FMAP as an analytic system to independently inform Agency management about the potential performance of the Enterprises' portfolio of loans under various scenarios and time horizons.  FHFA considers forecasted loan performance when developing and evaluating various housing policies.  FHFA benefits from the external forecasts provided by the Enterprises and the vendor platforms to which FHFA subscribes.  Simultaneously, FHFA developed FMAP for several reasons.  First, FMAP provides an independent view of portfolio performance rather than a view informed by external entities.  Second, FHFA develops and maintains FMAP in a manner reflective of Agency priorities and perspectives on how mortgages are expected to perform under various economic conditions and time horizons.  Third, FMAP is accessible and transparent relative to other external analytic systems. 

The objective of this white paper is to provide interested stakeholders with an overview of FMAP.  The distribution of this paper reflects the broader Agency-wide effort to provide transparency on the data and analytical tools used by FHFA for policy support.  This white paper describes version 3.0, the latest version of FMAP as of this paper's publication.  The Agency anticipates updating this document periodically. 

### 3.2 Description

FMAP is constructed and used to forecast mortgage cash flows within the structure depicted below in Figure 1, which describes the inter-relationships of the following five FMAP v3.0 modules: 

* Data module
* Behavioral models module
* Loss severity models module
* Simulation module
* Reporting module

<br>
*Figure 1. FMAP v3.0 Structure* 

Each module of FMAP v3.0 is described in the sections following the Release Notes. 

## 4 Data Module

### 4.1 Overview

FMAP v3.0 requires multiple source data to build the statistical models and simulate mortgage performance; namely, 

* Borrower data 
* Collateral data 
* Macroeconomic data 
* Loss severity data 

### 4.2 Borrower and Collateral Data

Monthly, the Enterprises submit to FHFA historical loan-level data containing borrower and collateral characteristics.  These data consist of static origination information as well as monthly dynamic information.  FMAP v3.0 uses historical Enterprise borrower and collateral data to estimate both the behavioral and loss severity models.  FMAP v3.0 also uses Enterprise borrower and collateral information as of the simulation date to define the set of loans for which to simulate mortgage performance and the initial values for these loans in terms of borrower and collateral characteristics. 

### 4.3 Macroeconomic Data

In addition to borrower and collateral information, FMAP v3.0 requires both historical and forecasted macroeconomic information; namely, house prices, unemployment rates, and certain relevant interest rates.  Historical house price indices (HPIs) are provided by FHFA, while historical unemployment rates and interest rates are provided by a vendor.  Forecasted HPIs, unemployment rates, and interest rates are also provided by a vendor.  Combined with borrower and collateral information, FMAP v3.0 uses macroeconomic historical data to estimate the statistical models and macroeconomic forecast data to simulate loan performance for various economic scenarios and time horizons. 

### 4.4 Loss Severity Data

The input data for the loss severity module come from several sources.  First, the Enterprises provide loss and loan level data.  Second, the monthly loan-level submissions provided by the Enterprises include data for real-estate owned fixed costs and alternatives as well as the transaction costs for non-performing loan sales.  Lastly, house price index data is provided by a vendor. 

### 4.5 Simulation Data

The simulation data is one input into the simulation engine.  The data is created based on borrower, collateral, and macroeconomic data.  These data reflect the portfolio of each Enterprise and contain loan attributes as of the simulation date. 

## 5 Behavioral Models Module

### 5.1 Overview

The behavioral models are statistical equations that vary across the Enterprises and other dimensions.  These models predict a given loan's transition among states. A transition refers to a loan changing to a different state from one period to the next, where a state is defined as a loan performance category e.g. performing or delinquent. 

### 5.2 Framework Specification

In particular, FMAP v3.0 proposes a transition probability methodology to model monthly mortgage performance[^2].  This methodology projects monthly probabilities of a given loan transitioning from one state to another state.  Typically, states include current, 30-, 60-, 90-, 120-, 150- day delinquencies, and 180 or more days in delinquency.  The advantage of the transition methodology is that loan performance can be modeled at a more granular delinquency level and each transition equation can be individually specified and estimated.  In addition, the transition technique is particularly useful if modelers need to predict delinquency status of each loan in a portfolio.  The downside of the transition model is that when the granularity of loan state is high, the number of transition equations become very large and unmanageable, and equations for transitions between certain delinquency states cannot be reasonably estimated because of the low transition frequency.  For this reason, institutions cannot always estimate every transition of interest.  Instead, modelers either group delinquency states or omit some of the transition equations.[^3] 

FMAP v3.0 groups active loans into either performing, re-performing, or nonperforming loan segments to balance the granularity and reliable estimation of the transition equations. The segmentation is conditional on the delinquency or performance and modification status of loans. The portfolio, or simulation, date represents the first date upon which FMAP simulates loan transitions. Depending on the modification history, re-performing loans are further classified into either modified re-performing or non-modified re-performing loans.

The segmentation leads to seven loan states:

1.  **Performing (PER) loans:** Loans neither 1) currently delinquent more than two months, 2) ever delinquent more than two months, nor 3) modified before the portfolio date.
2.  **Modified Re-performing loans (MRPL):** There are two groups of modified re-performing loans. The first group of modified re-performing loans are neither i) currently delinquent more than two months nor ii) ever delinquent more than two months; but have been modified before the portfolio date. The second group of modified-reperforming loans are i) not currently delinquent more than two months, ii) have been delinquent at least three months before the portfolio date, iii) have not been delinquent at least three months since the portfolio date, and iv) have been modified before the portfolio date.
3.  **Non-Modified Re-performing loans (NRPL):** Loans that are i) not currently delinquent more than two months, ii) have been delinquent at least three months in the past, albeit not since the portfolio date, and iii) have not been modified before the portfolio date.
4.  **Re-performing (RPL) loans:** Loans not currently delinquent more than two months but have been delinquent at least three months since the portfolio date.[^4]
5.  **Light delinquent (LDQ) loans:** Loans 3 - 5 months delinquent, inclusive.
6.  **Seriously delinquent (SDQ) loans:** Loans 6 - 11 months delinquent, inclusive.
7.  **Deeply delinquent (DDQ) loans:** Loans 12+ months delinquent, inclusive.

PER loans are further classified by product types; namely, the FRM 30/40-year and 15/20-year product types as well as the ARM product type. The nine transition states comprise the same seven active states along with two termination states.[^5] A termination state is a state from which a loan cannot transition such as:

8.  **Prepay loan (Prepay)**
9.  **Defaulted loan (Default)**

FMAP v3.0 defines default as either real-estate owned (REO), foreclosure alternative (deed-in-lieu, pre-foreclosure sale, and third-party sale), or nonperforming loan sale.

The mutually exclusive nature of the seven loan states is presented in the schematic below:

*Figure 2. Loan Status Schematic*

FMAP v3.0 reflects that some transitions are impossible. For example, a lightly delinquent loan is prohibited from transitioning to a performing state, though it can transition to a reperforming state.

The eligible transition states for each loan, conditional on the current state of a given loan, are given as follows:

**Table 1. Transition Table**
| Current state (t) | <div style="text-align:center">Transition state (t+1)</div> | | | | | | | | |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | PER | MRPL | NRPL | RPL | LDQ | SDQ | DDQ | Prepay | Default |
| **PER** | x | | | | x | | | x | |
| **MRPL** | | x | | | x | | | x | |
| **NRPL** | | | x | | x | | | x | |
| **RPL** | | | | x | x | | | x | |
| **LDQ** | | | | x | x | x | | x | x |
| **SDQ** | | | | x | x | x | x | x | x |
| **DDQ** | | | | x | x | x | x | x | x |

To illustrate, consider the performing loan transitions. FMAP v3.0 selects a sample of performing loans from among all loans to inform the performing loan equations, which estimate the probability of transitioning to either one of the following three states: lightly delinquent, prepay, or remain performing. This same outcome distribution is adopted for each of the seven active states.

### 5.3 Model Specification

Borrower behavior may vary based on the current and subsequent transition states of a given loan. For example, a borrower with a fixed-rate, 30-year mortgage may face different economic incentives to refinance than a borrower with an adjustable-rate mortgage. Given the framework described in the previous section and to account for these different incentives, we allow the model specification to vary by segment type, current state, and transition state. This leaves us with the following nine sets of equations: six sets for performing loans and three sets for nonperforming loans:

1.  **Performing 30/40-year fixed-rate to either LDQ or Prepay:** Predicts probability of transition for performing loans with fixed-rate, either 30- or 40-year mortgages to either LDQ or Prepay using separate equations for each outcome.
2.  **Performing 15/20-year fixed-rate to either LDQ or Prepay:** Predicts probability of transition for performing loans with fixed-rate, either 15- or 20-year mortgages to either LDQ or Prepay using separate equations for each outcome.
3.  **Performing adjustable-rate to LDQ or Prepay:** Predicts probability of transition for performing loans with adjustable-rate mortgages to either LDQ or Prepay using separate equations for each outcome.
4.  **mRPL to either LDQ or Prepay:** Predicts probability of transition for all mRPLs to either LDQ or Prepay using separate equations for each outcome.
5.  **nRPL to either LDQ or Prepay:** Predicts probability of transition for all nRPLs to either LDQ or Prepay using separate equations for each outcome.
6.  **RPL to either LDQ or Prepay:** Predicts probability of transition for all RPLs to either LDQ or Prepay using separate equations for each outcome.
7.  **LDQ to either SDQ, RPL, Prepay, or Default:** Predicts probability of transition for all currently LDQ loans to each outcome (SDQ, RPL, Prepay, or Default) with four separate equations.
8.  **SDQ to either LDQ, DDQ, RPL, Prepay, or Default:** Predicts probability of transition for all currently SDQ loans to each outcome (LDQ, DDQ, RPL, Prepay, or Default) with five separate equations.
9.  **DDQ to either LDQ, SDQ, RPL, Prepay, or Default:** Predicts probability of transition for all currently DDQ loans to each outcome (LDQ, SDQ, RPL, Prepay, or Default) with five separate equations.

Covariates assigned to each equation include two types of independent variables: (i) static loan characteristics such as loan purpose and (ii) dynamic loan characteristics such as age. Covariates are assigned to each specification using an iterative model building process that relied on out-of-time (OOT) fit.[^6] The iterative process begins with a simple base model that contains few variables. Then variables were added iteratively and the OOT fit was checked with each iteration to ensure that every variable added improved OOT fit. OOT fit evaluations are used to assess whether a variable should be added to an equation since doing so improves the generalizability of the model on new mortgage loans, which is the primary objective of FMAP.

To produce OOT fits, the iterative process uses a sliding window for the estimation data and tests OOT fit on each year from 2006 to 2019, inclusive. The sliding window produces OOT fits as the estimation data used to fit for each relevant year is only from years prior. By using a sliding window FMAP v3.0 also minimizes the issue of having significantly older data for 2019 fit estimates versus 2006. For example, data from 2000 through 2006 is used to estimate OOT model fits for 2007, data from 2001 to 2007 is used to estimate OOT model fits for 2008 and so on. The output from this process is multiple OOT fit statistics for each year between 2006 and 2019 which allow for comparison of a base regression to a regression with either new or different variables. With this iterative process, FMAP efficiently searches for the optimal subset of covariates. Consistent with borrower behavior varying based on differences in either incentives or characteristics of their loans, the specifications chosen based on this iterative process are not the same for all segments and states.

This iterative process led to either variables included as standalone variables, interactions, polynomials, or splines. The nonlinearity effects of the continuous covariates on mortgage outcomes are captured through either spline or polynomial functions based on the model fit statistics. The number and location of spline knots were identified using a multivariate adaptive regression spline (MARS) technique. Interactions and polynomials of certain covariates are also based on model OOT fit statistics.

Covariate definitions are provided below. Not all covariates are used in every set of equations. Some equations use differently defined variables. The appendix contains a table presenting covariates included in each equation.

**Age**
Age refers to the number of months since the first payment date, inclusive. FMAP v3.0 includes age (age), its square term (age_sq), and its cubic term (age_cb) in some behavioral equations[^7]. FMAP v3.0 also constructs a set of age splines chosen by MARS to improve model fit in some equations.

**Burnout**
The burnout factor reflects missed refinanced opportunities over the life of the loan. Burnout count (brnt_cnt) represents the number of months of missed refinanced opportunities, where a refinance opportunity occurs whenever the prevailing PMMS (Primary Mortgage Market Survey) rate falls below the PMMS rate at origination by 50 basis points. FMAP v3.0 includes burnout and its splines in the behavioral equations. The number and location of spline knots are selected based the optimal spline locations detected by MARS, given certain parameters.

**Current Unpaid Principal Balance (UPB)**
Current unpaid principal balance (cur_upb_k) is the outstanding principal balance at a given month. FMAP v3.0 also includes its square (cur_upb_k_sq) in the behavioral equations.

**Current UPB to Origination UPB**
The ratio of current UPB to original UPB captures the remaining percentage of the loan amount as a measure of the cost of default. Additionally, FMAP v3.0 also includes the interaction term of current UPB to original UPB ratio with house price appreciation (HPA) percentage change lag 24 months (sunk_cost * HPA with lag).

**Debt-to-Income Ratio (DTI)**
DTI refers to the back-end ratio of the sum of the borrower's monthly payment for principal, interest, taxes, homeowners' association fees and insurance, plus all fixed debts to the total monthly income of all borrowers determined at origination. DTI enters the FMAP v3.0 equations as either the value (debt_ratio) or splines chosen by MARS.

**Documentation**
Documentation is a flag (no_full_doc) for the loans without full documentation. These are low credit quality loans often acquired before 2008 that are more likely to default than full documentation loans.

**House Price Index**
HPI is the FHFA all-transaction house price index. HPI is at the metropolitan statistical area (MSA) level. If the MSA-level HPI value is missing, then the state-level HPI is used. If the MSA-level and state-level HPI are missing, then the national level HPI is used. FMAP v3.0 uses the MSA-level HPI in two ways. First, the HPI is used to derive the mark-to-market loan-to-value (MTMLTV). Second, the HPI is used to capture house price percentage change. Specifically, FMAP v3.0 captures recent house price dynamics using the housing price appreciation over the last 24 months (hpa24).

**IO Loan**
IO loan is a flag (io_loan) for interest only loans.

**Judicial State**
A state legal structure indicator is included to control for variation in state foreclosure laws. In judicial foreclosure states, a lender is required to get a judgment against the borrower and a court order authorizing the sale of the property by an office of the court. The foreclosure timelines in judicial states are longer than non-judicial states. As such, it is necessary to control for the local legal structures when modeling delinquent loan outcomes. The judicial state indicator (judicial_state) equals 1 when the loan is in a judicial state.

**Jumbo Loan**
Generally, the Enterprises are prohibited by law from purchasing single-family loans with an original principal balance above the prevailing conforming loan limit. A jumbo loan is a loan that exceeds the conforming loan limit. Jumbo loans may have tighter underwriting requirements, larger down payment requirements, and higher interest rates. Jumbo loan (jumbo_loan) is an indicator equaling 1 when the loan is a jumbo loan in the NPL behavioral equations.

**Junior Lien**
A junior lien is a debt (HELOC or HELOAN) undertaken by a borrower who already has a primary mortgage. Loans with junior liens are potentially riskier than loans without a junior loan. Junior lien is a flag (junior_lien) equaling 1 indicating the loan is for a mortgage with an attached junior lien.

**Loan Purpose**
Loan purpose reflects the borrower's stated reason for obtaining a mortgage, and is constructed as multiple indicator variables; namely, purchase-only (purchase), cash-out refinance (cashout), and rate/term refinance (raterefi). Purchase only is used as the base value and is omitted from the behavioral equations for identification purposes.

**Mark-to-market Loan-to-value Ratio**
The MTMLTV is the ratio of the prevailing unpaid principal balance to the current market value of the property. The current value market of the property is determined using the HPI. FMAP v3.0 includes the MTMLTV field (mtmltv) and its splines. Additionally, an MTMLTV variable is created separately for cash-out (mtmltv_cashout) and for rate-refi loans (mtmltv_raterefi) which allows the specification to control for an interaction between these variables.

**Months Until Interest Rate is Reset**
For ARMs, the principal and interest payments may change once the initial fixed-rate period expires. This potential payment shock can increase the propensity of a borrower to refinance to either a lower interest rate shortly preceding or immediately after the initial fixed-rate period. The number of months until the interest rate is reset (time_to_arm_reset) is specific to the ARM behavioral equations.

**Occupancy Type**
Occupancy type reflects the borrower's intended use of the property. Occupancy type is captured across multiple fields, with separate flags for whether the property is an investment property (investment), a second home (second_home), or a primary residence (primary_residence). 'Primary residence' serves as the base value and is omitted from the behavioral equations for identification purposes.

**Origination Credit Score**
Origination credit score intends to capture borrower(s) credit worthiness at origination. FMAP v3.0 includes origination credit score (cred_score) and its square (cred_score_sq) term. Additionally, the behavioral equations also interact origination credit score only with an indicator for mortgages without co-borrowers (cred_score_one_borrower).

**Origination LTV**
The origination loan-to-value (LTV) ratio measures the amount of financing to acquire the home. The numerator of the ratio measures loan size at origination, while the denominator of the ratio measures the appraised value at origination. FMAP v3.0 includes both the origination LTV (orig_ltv) field and a field defined as the origination LTV interacted with an indicator for mortgages with a junior lien (orig_ltv_junior_lien).

**Product Type**
Product type is defined by the amortization term of the loan at origination. The origination attribute includes the following product types: FRM 15/20-year, FRM 30/40-year, and all ARMs. Unlike other fields, FMAP v3.0 does not include a product type field in the behavioral equations. Rather, as noted earlier, FMAP v3.0 develops separate behavioral equations for performing loans across the product types. The exception is the treatment of product types in the NPL behavioral equations, which includes indicator fields for each product type.

**Refi Boom - 2001-2003**
The 2001-2003 refinance boom (refi_boom) field is a flag for the refinance boom period of 2001-2003. This variable aims to capture additional reasons individuals refinanced in record numbers during this period such as historically low interest rates and media coverage.

**Refinance Incentive**
Refinance incentive is defined as the level difference between the PMMS at origination and the PMMS in the current month. As the difference increases, the incentive for the borrower to refinance increases. FMAP v3.0 uses the lag 2 months refi-incentive (refi_incentive_level_l2) and its splines in the behavioral equations. The number and location of spline knots are selected based on the optimal spline locations detected by MARS.

**Sole Borrower**
Sole borrower is a flag (one_borrower) for loans without a co-borrower. As described earlier, the behavioral equations also include an interaction (cred_score_one_borrower) of origination credit score and the sole borrower field.

**Seasonality**
Seasonality is represented by indicator fields for each of the 12 months (M1-M12) along with each of the four quarters (q1-q4). The month of December (M12) and the fourth quarter (q4) are omitted from the behavioral equations for identification purposes.

**Spread at Origination (SATO)**
The SATO covariate is defined as the difference between the mortgage rate at origination and the prevailing 30-year PMMS at origination. The SATO field aims to capture other unobservable credit-related factors in the transaction at origination. FMAP v3.0 includes SATO for FRM 30-year mortgages (sato_f30).

**Third-party Origination**
A third-party origination is a loan in which a third-party participates in the origination for a lender. Third-party originators include both brokers and correspondent lenders. Third-party origination is a flag (third_party) equaling 1 when the loan was originated by a third-party originator.

**Unemployment Burnout Count**
Unemployment burnout count is designed to help capture the survival bias in the unemployment coefficients. The field is defined as the number of times the unemployment rate in the MSA (or state if MSA is missing) in which the property is located exceeds a certain threshold since origination. FMAP v3.0 includes multiple fields to represent the unemployment burnout count, specifically the frequencies of the unemployment rate greater than 8% (brnt_cnt_8p), 10% (brnt_cnt_10p) or 12% (brnt_cnt_12p).

**Unemployment Rate**
The unemployment rate serves as a proxy for borrower(s) job loss and MSA-level macroeconomic activity. FMAP v3.0 incorporates either the unemployment rate (unemp_rate) or splines of the unemployment variable, depending upon the behavioral equations.

**Vintage**
Vintage refers to loan origination year. These vintage-specific fixed effects intend to capture time-varying features such as underwriting standards not captured by other fields in the behavioral equations. FMAP v3.0 includes indicators for vintages 2005-2008 (vintage_05_08), 2009-2013 (vintage_09_13), and 2014 onward (vintage_ge_14) to capture vintage effects.

### 5.4 Sample and Methodology

Given the technological constraints on estimating models with the entire portfolios of loans from both Enterprises, FMAP v3.0 samples Fannie Mae and Freddie Mac loans to estimate separate behavioral equations for each Enterprise. The time period for the estimation sample reflects borrower and collateral information from January 2000 to December 2019.

In FMAP v2.0, the performing equations for 30-year and 15-year fixed-rate loans and adjustable-rate 5/1 loans were estimated on samples of loans originated from February 1997 to December 2014. Selected loans were followed from acquisition to either first 90-day delinquency, prepayment, or to December 2014, whichever occurred earliest.

FMAP v3.0 includes several changes to this sampling approach to increase the representativeness and usefulness of the samples. FMAP v3.0 randomly samples loans from each monthly portfolio of loan performance observations for loans with a given starting state. This sample is stratified by age, credit score, origination loan-to-value, and loan status. Different sampling rates were set for the different starting states to ensure a sufficient number of loans for estimation. Sampling rates are one percent for FRM 30/40-year and FRM 15/20-year 10 percent for arms, 50 percent for mRPL and nRPL, 25 percent for RPL, and 80 percent for LDQ, SDQ, and DDQ. For each month, this stratified random sampling method generates a sample of loans more representative of the true Fannie Mae and Freddie Mac portfolios of active loans.

### 5.5 Estimation and Results

Multiple statistical modeling approaches have been used to estimate borrower behavior. Jenkins (1995), Calhoun and Deng (2000), and Clapp et. al. (2001) demonstrate that the multinomial logit approach provides a relatively convenient method for modeling prepayment and delinquency risks as discrete-time, competing risks.[^8] The multinomial approach is also consistent with the approach adopted in the prior version of FMAP.

With the sampled data we estimate binomial and multinomial logistic regressions for each Enterprise separately.[^9] Performing and reperforming equations are estimated using a binomial logistic regression (i.e., one vs. the rest scheme), which estimates the probability a certain transition against all other possible transitions. Taking as an example the performing equation there are three possible transitions: prepay, LDQ, and performing. When we estimate the prepay probability, we estimate the probability of prepaying vs the probability of [LDQ or performing]. Estimating the transition probabilities in this way can cause probabilities to sum greater than one. To combat this, we assume the probability of staying in your starting state (i.e., performing to performing) is equal to one minus the probabilities of transitioning to other states. Nonperforming loan equations were estimated using multinomial logits.

The appendix includes an excel file with the estimation results for all specifications. For performing loans for each Enterprise, segment (e.g., fixed-rate 30-year or ARMs), and event (outcome state) has its own table. For nonperforming loans, each Enterprise and segment has its own table. As the behavioral equations are not focused on identifying why a loan changes state, these coefficients cannot be interpreted causally. Instead, these coefficients can only be used in jointly predicting the probability a loan changes state. Therefore, in reviewing the coefficients the focus should be on whether the sign of the coefficient is reasonable. As many of the variables are represented with polynomials, splines, or included in interactions, the signs on all relevant coefficients should be considered.

### 5.6 Model Performance Tracking Results

In this section, we show excerpts from the model performance tracking report, which compares forecasts to actuals for selected historical single-family loan portfolios. FMAP v3.0 includes two types of performance tracking reports to assess the behavioral equation performance. First, the Component Model Performance Tracking (cMPT) compares monthly predicted transition rates with actual transition rates for each behavioral equation. Second, the Integrated Model Performance Tracking (iMPT) compares predicted loan termination rates, i.e., default and prepay rates with the actual termination rates on past portfolios.

#### 5.6.1 Component Model Performance Tracking Report (cMPT)

The Component Model Performance Tracking (cMPT) report monitors the performance for all 29 behavioral models. The cMPT is performed for the 201606 portfolio with forecast until 202003. Below is the sample report for LDQ and prepay equations for PERF FRM 30yr and PERF FRM 15yr products. The AUC statistics show the model fit for these four equations is reasonable.

*Figure 3. Example of Performance Tracking, Fixed-rate Mortgage 30-year and 15-year, LDQ and Prepay*

#### 5.6.2 Integrated Model Performance Tracking Report

Each MPT report contains approximately 70 graphs designed to assess varying views of model performance. For brevity, in this document we will focus only on select results aggregated at the activity date level for the single-month mortality (SMM), monthly default rate (MDR), Cumulative Prepay, and Cumulative Default metrics. All additional graphs can be found linked in the appendix. To gauge the forecast capabilities of FMAP v3.0, MPT reports for two different portfolios were created: June 2014 and December 2016. Results will be shown in this order.

The table below summarizes results for the four metrics across the two portfolios. As shown in this table, we see model performance is similar between the two Enterprises as can be seen by the similar average errors between the two Enterprises. Additionally, we can see that, as expected, the in-time performance is slightly better than the out-of-time performance, though the difference is minimal.

The first two figures below show the results from the June 2014 MPT reports for Enterprise 1 and Enterprise 2, respectively. These graphs yield several observations. First, fit results by Enterprise are similar, this indicates forecast capability is similar for both Enterprises. Second, the in-time and out-of-time results (out-of-time results use coefficients estimated on data from 2000 to May 2014) are close. The similarity in results indicate minimal over-fitting in the final specification, and that the out-of-time iterative model building worked as intended. For prepayment, ignoring the pandemic as illustrated by the red vertical line, SMM shows the predicted prepayments follow the general shape of the actual prepayments. However, there is some overprediction in the first year and a half (June 2014 to December 2016) of the forecast, though this overprediction is decreased after the large prepayment decrease of December 2016. Looking at the pandemic we see that FMAP v3.0 predicts a large and steep increase in prepayments. However, the magnitude is slightly lacking as both Enterprises show an approximate 0.75 percent under prediction in late 2020. It should be noted that FMAP v3.0 excludes COVID-specific treatments or variables. Additionally, the sample used to create FMAP v3.0 finishes at the end of 2019 and therefore includes no pandemic information.

The MDR graph is more difficult to read due to the "spiky" nature of the default data. These spikes represent NPL loan sales, which refer to large loan sales made at the discretion of the Enterprises. Therefore, their exact timing is difficult to model. Looking past the spikes we see FMAP v3.0 predictions seem to be following the general downward trend of actual defaults over the forecast period. We see the cumulative default graphs that FMAP v3.0 slightly underestimates the number of defaults. Similarly, for the prepay results we can see that for the pandemic FMAP v3.0 correctly estimates a decrease in defaults, though the magnitude of the predicted decrease is slightly less than the actual decrease.

The third and fourth figures below show the results from the December 2016 MPT report for Enterprise 1 and Enterprises 2, respectively. The FMAP v3.0 OOT results are based on coefficients estimated on data from 2000 through 2014. Similarly, to the June 2014 MPT, FMAP 3.0 very accurately forecasts the December 2016 portfolio. The estimated prepay rates very closely match the actual prepay rates with only slight overpredictions for both enterprises. There is slightly more variation in the accuracy of default forecasts, the forecast for Enterprise #2 is very close, with an MAE of 0.0205% and slightly under the actual, while the forecast for Enterprise #1 is slightly worse with an MAE of 0.0343% and over the actual default rate. The error in forecast for Enterprise #1 seems to be a result of a large NPL sale that occurred mid 2018 as can be seen by a large spike in defaults in figure 6 subgraph: Cumulative Default Amt % for act_dte.

**Table 2. Summary MPT Results for the June 2014, and December 2016 Portfolios***

**June 2014 MPT**
| Metric | <div style="text-align:center">Enterprise 1</div> | | <div style="text-align:center">Enterprise 2</div> | |
| :--- | :---: | :---: | :---: | :---: |
| | **3.0 OOT MAE** | **3.0 IT MAE** | **3.0 OOT MAE** | **3.0 IT MAE** |
| SMM | 0.2593% | 0.2139% | 0.2362% | 0.2196% |
| MDR | 0.0169% | 0.0188% | 0.0152% | 0.0087% |
| Cumulative Prepay | 3.5047% | 3.2212% | 2.4372% | 2.5721% |
| Cumulative Default | 0.1350% | 0.1093% | 0.1391% | 0.1370% |

<br>

**December 2016 MPT**
| Metric | <div style="text-align:center">Enterprise 1</div> | | <div style="text-align:center">Enterprise 2</div> | |
| :--- | :---: | :---: | :---: | :---: |
| | **3.0 OOT MAE** | **3.0 IT MAE** | **3.0 OOT MAE** | **3.0 IT MAE** |
| Cumulative Prepay | 0.7743% | 1.2909% | 0.9047% | 1.9370% |
| Cumulative Default | 0.0343% | 0.0466% | 0.0205% | 0.0113% |

*\*OOT refers to out-of-time results use coefficients estimated on data from 2000 to May 2014. IT refers to in-time results use final coefficients estimated.*

<br>

*Figure 4. June 2014 Portfolio MPT - Enterprise 1*

*Figure 5. June 2014 Portfolio MPT - Enterprise 2*

*Figure 6. December 2016 Portfolio MPT - Enterprise 1*

*Figure 7. December 2016 Portfolio MPT - Enterprise 2*

## 6 Loss Severity Models Module

### 6.1 Overview
Loss severity models predict credit loss on defaulted loans. These models are either statistical or relational equations that vary across the Enterprises and other dimensions. The historical data used to estimate the loss severity models include borrower and collateral characteristics, payments and receipts for troubled loans and REOs data, along with house price data.

### 6.2 Framework Specification
Loans predicted to default will transition into the loss severity module, which calculates credit loss. Credit loss can result from one of three outcomes: foreclosure, foreclosure alternative, and nonperforming loan sale.[^10] [^11]

Foreclosure transfers property title from the borrower to the lender. The lender in this analysis is one of the two Enterprises. Once transferred, the Enterprise owns the property, which becomes REO. The Enterprises can then market and sell the property to a new owner. The final credit loss on the loan is calculated after the property is sold from REO inventory.

Foreclosure alternatives is an alternative outcome for a defaulted loan. Foreclosure alternatives consist of three major types: deed-in-lieu, pre-foreclosure sale (short sale), and third-party sale. Deed-in-lieu occurs when the lender (in this case one of the Enterprises) forgives the mortgage debt and takes title to the property. In this case, the property becomes REO and the lender can sell it to recoup credit loss. Another foreclosure alternative is a pre-foreclosure sale. This occurs when the lender agrees to allow the borrower to sell the property for less than the outstanding mortgage debt (sometimes called a short sale) and the lender forgives the mortgage debt. Another foreclosure alternative is a third-party sale. This occurs when a third party buys the property for the outstanding loan balance and expenses at the foreclosure sale. The credit loss is recognized at the completion of the foreclosure sale. The pre-foreclosure sale and third-party sale do not result in the Enterprises owning the property. Consequently, there are no expenses after the completion of the sale.

The last potential outcome is a nonperforming loan (NPL) sale[^12], which occurs when an Enterprise sells a defaulted mortgage within a pool of mortgages to an investor. The investor who purchases the pool of mortgages receives cash flows from the mortgages. Credit loss from a nonperforming loan sale equal the unpaid principal balance plus transaction costs minus expected sale price for the mortgage. This outcome is new in FMAP v3.0.

### 6.3 Data
The models that make up the loss severity module are estimated separately for Fannie Mae and Freddie Mac using the Enterprises' data of borrower and collateral characteristics and payments and receipts for troubled loans and REOs and the Enterprises purchase only HPI data from 2012 to 2020.

### 6.4 Credit Losses
For REO dispositions, four components comprise credit losses: 1) the charge-off amount at the title transfer date (for a foreclosure outcome, the title transfer date is foreclosure completion date for REO and all other foreclosure alternative outcomes this is liquidation date), 2) sale price adjustment, 3) carrying costs and accrued interest, and 4) fixed costs. Details on each are provided below:

* **Charge-off** occurs at foreclosure completion. It equals the unpaid principal balance of the mortgage at the time of default (defaulted UPB) plus any relevant expenses up to the foreclosure date minus predicted sale price at the foreclosure date.
* **Sale price adjustment** occurs monthly from foreclosure completion to REO property disposition. This monthly adjustment is calculated as the difference between the expected sale price every month and the expected sale price at foreclosure completion. These monthly adjustments end when the property is disposed of from REO inventory. The sum of these monthly adjustments equals the entire sale price adjustment from foreclosure completion date to REO property disposition date.
* **Carrying costs** are calculated from foreclosure completion to REO property disposition and include taxes, insurance, and homeowner association (HOA) fees from foreclosure completion to REO property disposition. Accrued interest is calculated from last paid installment to foreclosure completion and is included in carrying costs for that period.
* **Fixed costs** are calculated from foreclosure completion to REO property disposition and include certain liquidation expenses and fees plus utility and repair costs, etc.

For non-REO dispositions, the credit losses are limited to the charge-off amount.

Below are the formulas to calculate the credit loss for each outcome.

$$
Credit\ loss_i = Charge–off_i \\
+ Sale\ price\ adjustment\ from\ foreclosure\ completion\ to\ REO\ property\ disposition_i \\
+ Carrying\ costs\ including\ accrued\ interest\ from\ foreclosure\ completion\ to\ REO\ property\ disposition_i \\
+ Fixed\ costs\ from\ foreclosure\ completion\ to\ REO\ property\ disposition_i \\
\forall\ i \in REO
$$

$$
Credit\ loss_i = Charge–off_i \\
\forall\ i \in Foreclosure\ alternatives,\ NPL\ sales
$$

### 6.5 Charge-off Amounts

For each outcome, the formulas below calculate the charge-off amount, which is equal to the unpaid principal balance at the time of default (defaulted UPB) minus expected net sales proceeds on the liquidation (foreclosure) date plus any relevant expenses up to liquidation (foreclosure) date including Carrying costs from LPI to liquidation date.

$$
Charge–off_i = Defaulted\ unpaid\ principal\ balance_i \\
- Expected\ net\ sale\ proceeds\ at\ liquidation\ date_i \\
+ Carrying\ costs\ including\ accrued\ interest\ from\ LPI\ to\ liquidation\ date_i \\
+ Fixed\ costs\ from\ LPI\ to\ liquidation\ date_i \\
\forall\ i \in REO,\ Foreclosure\ alternatives
$$

$$
Charge–off_i = Defaulted\ unpaid\ principal\ balance_i \\
- Expected\ NPL\ sale\ proceeds\ at\ liquidation\ date_i \\
+ Carrying\ costs\ including\ accrued\ interest\ from\ LPI\ to\ liquidation\ date_i \\
+ Transaction\ costs\ from\ LPI\ to\ liquidation\ date_i \\
\forall\ i \in NPL\ sales
$$

#### 6.5.1 Expected Net Sales Proceeds for REO and Foreclosure Alternatives
Net sale proceeds are the difference between gross property sale proceeds and other relevant expenses, which include sales and other selling expenses, broker fees and borrower closing costs. The expected net sale proceeds for REO and foreclosure alternatives used to calculate charge-offs are estimated using a piecewise linear regression technique with a separate model for each state and disposition type. The technique relates historical actual net sale proceeds with the mark-to-market property value at the time of disposition for properties collateralizing Enterprise loans liquidated between 2012 and 2020.[^13] Specifically, the technique captures the relationship between a defaulted loan *i* of the actual net sale proceeds ($Net\ Sale\ Proceeds_i$) against the mark-to-market property value ($PropValue_i$) with a truncated power function series for each state defined as follows:

$$
Net\ Sale\ Proceeds_i = \\ \beta_0 + \beta_1 * (PropValue_i) + \beta_2 * (PropValue_i - k_1)_+ + \beta_3 * (PropValue_i - k_2)_+ \\ + \beta_4 * (PropValue_i - k_3)_+ + \beta_5 * (PropValue_i - k_4)_+ + \epsilon_i \\ \forall\ i \in REO\ and\ Foreclosure\ alternatives
$$

where

$$
(PropValue_i - k_p)_+ = \begin{cases} 0, & PropValue_i < k_p \\ PropValue_i - k_p, & PropValue_i \ge k_p \end{cases} \\ p = 1\ to\ 4
$$

$$
PropValue_i = \left(\frac{Original\ UPB_i}{Original\ LTV_i}\right) * \left(\frac{HPI\ at\ Disposition_i}{HPI\ at\ Origination_i}\right)
$$

$k_p$ = Spline knots located at the 20th, 40th, 60th, and 80th percentiles of PropValue

#### 6.5.2 Expected NPL Sale Proceeds (Recovery Rate)
NPL sale proceeds are equal to the note sale proceeds minus other relevant expenses, which include sales and other selling expenses, broker fees and borrower closing costs.

$$
NPL\ Sale\ Proceeds_i = \\
\beta_0 + \beta_{11}*(MTMLTV_i) + \beta_{12}*(MTMLTV_i - k_1)_+ + \beta_{13}*(MTMLTV_i - k_2)_+ + \beta_{14}*(MTMLTV_i - k_3)_+ \\
+ \beta_{21}*(Liq\_UPB_i) + \beta_{22}*(Liq\_UPB_i - k_1)_+ + \beta_{23}*(Liq\_UPB_i - k_2)_+ + \beta_{24}*(Liq\_UPB_i - k_3)_+ \\
+ \beta_{31}*(Delinq\_Pmts_i) + \beta_{32}*(Delinq\_Pmts_i - k_1)_+ + \beta_{33}*(Delinq\_Pmts_i - k_2)_+ + \beta_{34}*(Delinq\_Pmts_i - k_3)_+ \\
+ liquidation\ year\ dummies + \epsilon_i \\
\forall\ i \in NPL\ sales
$$

where

$$
(MTMLTV_i - k_m)_+ = \begin{cases} 0, & MTMLTV_i < k_m \\ MTMLTV_i - k_m, & MTMLTV_i \ge k_m \end{cases}, m=1\ to\ 3
$$

$$
(Liq\_UPB_i - k_l)_+ = \begin{cases} 0, & Liq\_UPB_i < k_l \\ Liq\_UPB_i - k_l, & Liq\_UPB_i \ge k_l \end{cases}, l=1\ to\ 3
$$

$$
(Delinq\_Pmts_i - k_d)_+ = \begin{cases} 0, & Delinq\_Pmts_i < k_d \\ Delinq\_Pmts_i - k_d, & Delinq\_Pmts_i \ge k_d \end{cases}, d=1\ to\ 3
$$

$k_m$ = Spline knots located the 25th, 50th, and 75th percentiles of $MTMLTV_i$
$k_l$ = Spline knots located the 25th, 50th, and 75th percentiles of $Liq\_UPB_i$
$k_d$ = Spline knots located at the 25th, 50th, and 75th percentiles of $Delinq\_Pmts_i$

We divide the NPL sale proceeds by liquidation UPB to get the recovery rates, which are defined as follows:

$$
Expected\ NPL\ sale\ proceeds_i = Recovery\ rate * Liquidated\ UPB \\
= \frac{Net\ sale\ proceeds\ from\ loan\ sale}{Liqidation\ UPB}
$$

Expected NPL sale proceeds apply only to NPL sales. The expected NPL sale proceeds used to calculate charge-offs are estimated using a piecewise linear regression model, which relates historical actual NPL sale proceeds with MTMLTV at liquidation date, liquidation unpaid principal balance, number of delinquency payments, and liquidation year. These variables were chosen to approximate factors rationale buyers would use to determine the price of a loan in an NPL sale package. Specifically, the piecewise linear regression model captures the relationship between a defaulted loan i of the actual NPL sale proceeds ($Actual\ NPL\ Sale\ Proceeds_i$) against the MTMLTV ($MTMLTV_i$), liquidation unpaid principal balance ($Liq\_UPB_i$), delinquent payments ($Delinq\_Pmts_i$), with a truncated power function series and with separate liquidation year indicator variables ($liq\_year2015$, $liq\_year2016$, etc). See the appendix for details. Additional details are provided as follows:

* The MTMLTV is calculated using the internal FHFA seasonally adjusted purchase-only house price index at the MSA level. If the MSA is missing, the desired value is replaced with the state value of the internal FHFA purchase-only house price index.
* A set of liquidation year dummies are created. Both Fannie Mae and Freddie Mac regressions set the 2019 and beyond liquidation year coefficient as the base liquidation year. The spans of years are from 2015 to 2019 for Fannie Mae and from 2014 to 2019 for Freddie Mac. Fannie Mae started NPL sales in 2015, while Freddie Mac started its NPL sales program in 2014. So, the regression for Fannie has no 2014 dummy.
* Number of delinquent payments refers to the missing payments from LPI to the liquidation date.

Coefficients are combined with the MTMLTV, liquidation unpaid principal balance, delinquency payments, and liquidation year of the defaulted loan to generate expected NPL sale proceeds.

#### 6.5.3 Carrying Costs
While the carrying costs are identical across disposition types, the way they are aggregated when defining charge-offs differs by disposition type. Specifically, for REO dispositions, these expenses are accumulated between last paid installment date and foreclosure completion date. These expenses for both foreclosure alternatives and NPL sales are accumulated from last paid installment date to title transfer date (liquidation date) and are included in the charge-off amount. Carrying costs included HOA fees, property tax, insurance, and accrued interest. Accrued interest included in the charge off amount for REO, foreclosure alternatives and Nonperforming Loan Sales is calculated by multiplying the defaulted unpaid loan balance by the interest rate multiplied by the time from last paid installment data to title transfer (liquidation date). For REO properties, carrying costs also occur during the time from foreclosure completion to REO disposition.
Carrying costs used to calculate charge-offs are estimated using the look-up tables approach. First, carrying costs are calculated at the loan level for all defaulted loans from 2012 to 2020. Second, the defaulted loans are matched to categories uniquely defined by the combination of the property value at origination group, the state in which the property is located, and the disposition type. See the appendix for the carrying cost equations and the property value at origination groups.

#### 6.5.4 Fixed Costs for REO or Foreclosure Alternative
Fixed costs are calculated from last payment date to foreclosure completion date and include appraisal fees, attorney and trustee fees, other foreclosure expenses, other liquidation expenses, maintenance expenses, property inspection, repairs, and utilities. These costs were estimated using a piecewise linear regression technique with a separate model for each state and disposition type (REO and foreclosure alternatives which comprise deed-in-lieu, short sales and third-party sales). This estimation used Enterprise liquidations from 2016-2020. We didn't use the data from 2012 to 2015 in the estimation, as fixed costs seemed to have experienced regime switching and jumped to a much higher level after 2016. Fixed costs components are calculated using the same formula for the two disposition types. The formula is given as follows:

$$
Fixed\ cost_i = Appraisal\ fees_i + Attorney\ and\ trustee\ fees_i + Other\ foreclosure\ expenses_i \\
+ Other\ liquidiation\ expenses_i + Maintenance\ expenses_i \\
+ Property\ inspection_i + Repairs_i + Utilities_i \\
\forall\ i \in REO, Foreclosure\ alternatives
$$

The regression equation is as follows:

$$
\frac{Fixed\ costs_i}{Liq\_UPB_i}*100 = \\
\beta_0 + \beta_1*Liq\_UPB_i + \beta_2*(Liq\_UPB_i - k_1)_+ + \beta_3*(Liq\_UPB_i - k_2)_+ + \beta_4*(Liq\_UPB_i - k_3)_+ \\
+ \beta_5*(Liq\_UPB_i - k_4)_+ + \epsilon_i \\
\forall\ i \in REO, Foreclosure\ alternatives
$$

where

$$
(Liq\_UPB_i - k_l)_+ = \begin{cases} 0, & Liq\_UPB_i < k_l \\ Liq\_UPB_i - k_l, & Liq\_UPB_i \ge k_l \end{cases}, l=1\ to\ 4
$$

$k_l$ = Spline knots located the 25th, 50th, and 75th percentiles of the liquidation UPB amount The variables k1 to k4 are 20%, 40%, 60% and 80% percentiles of the liquidation UPB amount, respectively. We use the same specification for the two disposition types. But the equations are estimated separately for each disposition and for Enterprise 1 and Enterprise 2 separately.

Even though both disposition types use the same regression equation above to produce the predicted fixed cost ratios, FMAP v3.0 omits maintenance expense from the definition of total fixed cost for REOS before estimating the regression for REO loans. As a result, the coefficients reflect estimated fixed costs without maintenance expense. To compensate for the omission of maintenance expense in the regression, FMAP v3.0 adds monthly HOA, insurance fees as well as taxes between last paid installment dates and liquidation dates (charge-off dates) to get the predicted total fixed cost ratios for REOs that includes maintenance expense. Additionally, FMAP v3.0 assumes that the REOs maintenance expenses occur between charge-off date and REO disposition date.

#### 6.5.5 Transaction Costs for an NPL Sale
Transaction costs (also known as fixed costs or liquidation expenses) for an NPL sale, also known as liquidation expenses, include all expenses associated with an NPL sale such as appraisal fees and attorney and trustee fees. Excluded from transaction costs for a NPL sale are aggregated expenses incurred by the Enterprises to execute the NPL sales. These expenses may include incentives to brokers to facilitate transactions and website maintenance where investors can obtain information regarding the loans offered in the note sale pool. Transaction costs for an NPL sale used to calculate charge-offs are estimated using look-up tables. First, the transaction costs for an NPL sale are calculated at the loan level for all defaulted loans from 2014 to 2020. Second, the defaulted loans are matched to categories uniquely defined by the combination of the Enterprise, liquidated unpaid principal balance group, and the judicial status of the state in which the property is located.

$$
Transaction\ Costs_i = Appraisal\ fees_i + Attorney\ and\ trustee\ fees_i + Other\ foreclosure\ expenses_i \\
+ Other\ liquidiation\ expenses_i + Other\ non\ selling\ expenses_i \\
+ Maintenance\ expenses_i + Property\ inspection_i + Repairs_i + Utilities_i \\
+ Possessory\ and\ eviction\ fees_i + Title\ insurance\ fees_i \\
+ Property\ management\ fees_i + Servicer\ incentive\ payment_i \\
\forall\ i \in NPL\ sales
$$

Transaction costs[^14] are calculated as a percentage of liquidated unpaid principal balance, which were estimated separately for Enterprise 1 and Enterprise 2. Predicted transaction costs are calculated as the liquidation UPB weighted average transaction costs of all NPL note sales from 2014 to 2020 by liquidated unpaid principal loan balance category and judicial versus non-judicial state indicators. For a given loan, if a particular state is missing, then the national average transaction costs by liquidated unpaid principal loan balance categories will be applied. The liquidated unpaid loan balance categories were chosen based on the percentiles of the population. Also, the measures are calculated separately for judicial and non-judicial states. The separation by judicial and non-judicial states is intended to capture the difference in length of delinquency and expenses associated with delinquency. Mortgages in judicial states must go through a lengthy legal process to complete a foreclosure or transfer title. Even though non-performing note sales do not have a foreclosure, these court processes can result in extreme times in delinquency which we hypothesize will impact the sale price for a non-performing loan sale. In contrast, mortgages in non-judicial states moving quickly through the delinquency process resulting in short delinquencies before the non-performing loan sale.

Further, states are considered either judicial or non-judicial. A judicial state is one in which a lender must receive court approval to foreclose on a property. A non-judicial state does not. Judicial states include the following:

Connecticut (CT), Delaware (DE), Florida (FL), Hawaii (HI), Iowa (IA), Illinois (IL), Indiana (IN), Kansas (KS), Kentucky (KY), Louisiana (LA), Maine (ME), North Dakota (ND), New Jersey (NJ), New Mexico (NM), New York (NY), Ohio (OH), Oklahoma (OK), Pennsylvania (PA), South Carolina (SC), Vermont (VT), and Wisconsin (WI).[^15]

All other states are considered non-judicial states.

Once the historical loans have been allocated to the unique combination of the Enterprise, liquidated unpaid principal balance group, and the judicial status of the state in which the property is located, the liquidation unpaid principal balance-weighted average transaction costs for an NPL sale are calculated within each category. The resulting look-up table is used to estimate the transaction costs for an NPL sale of a defaulted loan. Specifically, the Enterprises, liquidated unpaid principal balance, and the judicial status of the state in which the property is located of the defaulted loan is matched to the corresponding Enterprise, liquidated unpaid principal balance group, and the judicial status of the state in which the property is located category in the look-up table and the liquidation unpaid principal balance-weighted average transaction costs for an NPL sale of the matched category represents the estimated transaction costs for an NPL sale of the defaulted loan.

Initially, FMAP v3.0 set fixed cost ratios as constant values within different cohorts grouped based on states. However, the setting did not produce accurate predictions of fixed costs components throughout years. Upon further research, FMAP v3.0 uses spline regressions to improve the estimation results.

#### 6.5.6 Mortgage Insurance (MI) Claim
The MI claim refers to the amount included in the claim submitted by the Enterprises to the mortgage insurance company. An Enterprise can only receive reimbursement for MI claims on loans with mortgage insurance as of the title transfer date. The MI claim amount for defaulted loan i (MI Claim Amount) is defined as follows:

$$
MI\ claim\ amount_i = Liquidated\ unpaid\ principal\ balance_i \\
+ Carrying\ costs\ including\ accrued\ interest\ from\ LPI\ to\ liquidation_i \\
+ Fixed\ costs\ from\ LPI\ to\ liquidation_i \\
\forall\ i \in REO\ with\ MI,\ Foreclosure\ alternatives\ with\ MI
$$

Mortgage insurance companies might also default, failing to reimburse the claimed amount. Therefore, the following formula calculates MI proceeds after accounting for the potential failure of MI companies to honor claims, which is represented by the MI haircut ratios. MI haircuts are differentiated by the credit rating of the mortgage insurer and their level of concentration in the mortgage insurance business, loan performance and loan amortization term.

$$
MI\ proceeds_i = MI\ claim\ amount_i * MI\ coverage_i * (1 - MI\ haircut_i)
$$

### 6.6 REO Operating Expense
For REO properties, there are extra losses between Liquidate Date and Disposition Date, which are described as the REO Operating Expense. When a loan becomes REO at month T, there are subsequent monthly operating expenses in the next few months:

**Fixed Expense**
The fixed expense includes monthly tax, HOA, and insurance expenses.

**Sale Price Adjustment from Foreclosure Completion to REO Property Disposition**
The property value component of charge off is measured by house price at foreclosure date. The house price may decrease further, so the property value, after foreclosure date that incur additional losses. The model tracks property value decrease if it occurs, month by month, between foreclosure and disposition and record as additional losses.

**True Up at Disposition Date**
At disposition date, the house price may increase, the sum of additional recorded losses in step 2 may be overly recorded. Total loss will be adjusted by comparing to property value at disposition date.

### 6.7 Fit Statistics
The Loss Severity Module proposes updated parameters for FMAP v3.0 equations and introduced regression techniques to predict net sales proceeds and fixed costs for all three disposition types as well as recovery rates for NPL sales. To validate and improve model predictions, a standard back-testing technique was implemented. The net losses are defined as follows:

$$
Net\ losses_i = Liquidation\ UPB_i - Net\ sale\ proceeds_i + Liquidation\ expenses_i\ (fixed\ costs) \\
+ Carrying\ costs_i - MI\ proceed_i
$$

To make it consistent for different loans, the total net losses as well as each of the five components are divided by the liquidation unpaid principal balance amounts to obtain the ratios. The actual and predicted values are compared.

Fit statistics used include RMSE (Root Mean Square Error) and MAE (Mean Absolute Error), both of which are weighted by the liquidation unpaid principal balance of all the loans. The loss severity equals net losses divided by liquidation UPB. Each component is considered individually in the appendix. This section covers the in-sample back testing results on the total net losses as percentages of the liquidation unpaid principal balances (loss severity ratios) on Enterprise 1 loans liquidated between 2012 and 2020. Here we took out the mortgage insurance proceeds components, as NPL sales do not have mortgage insurance proceeds and we would like to maintain the comparison consistent between the three disposition types. The figure below summarizes RMSE and MAE for the three disposition types. NPL sales have the lowest RMSE followed by foreclosure alternatives and then REO dispositions.

*Figure 8. Enterprise 1 RMSE and MAE on Loss Severity between 2012-2020*

The figure below shows the trends of RMSE and MAE from 2012 to 2020. Except for the year 2020, the RMSE values fall below 0.45 and the MAEs are under 0.25 for the other years.

*Figure 9. Enterprise 1 RMSE and MAE of Total Loss Severity Ratios, 2012-2020*

The figure below compares the actual values and predicted values of loss severity ratios. The orange line represents the liquidation unpaid principal balances of all loans liquidated in each year. Except for 2019-2020, inclusive, the predicted values track actual loss severity ratios closely. Also, the total liquidation unpaid principal balances of all loans are well under $20 billion except for the years from 2012 to 2014.

*Figure 10. Enterprise 1 Back-testing Results of Total Loss Severity Ratios by Year*

The figure below shows the back-testing results by disposition type. As shown below, the predicted loss severity ratios are the closest to the actual values for NPL sales, followed by foreclosure alternatives, and then REO loans.

*Figure 11. Enterprise 1 Back-testing Results of Total Loss Severity Ratios by Disposition Type*

## 7 Simulation Module

### 7.1 Overview
The simulation module uses statistical models (behavioral models and loss severity models) to simulate cash flows, given a set of loan profiles and forecasted macroeconomic environment.

*Figure 12. Simulation Engine within FMAP*

**Loan Profile**
Given a date, called portfolio date, the loan profile data provides required loan attributes measured as of the portfolio date. In FMAP, the loan profile data are called time-zero (TZ) data.

**Economic Data**
Historical and forecast home price index, unemployment rate, and market rates, commonly used in the mortgage industry, are used to represent macroeconomic environments which may influence loan performance and borrower's behavior.

**Models**
During the simulation, models are invoked according to the simulation algorithm to compute conditional probabilities of potential outcomes in transitioning from one month to the next month.

**Simulation Engine**
FMAP v3.0 implements three simulation techniques: (i) a cashflow-based simulation; (ii) Markov Chain simulation; and (iii) Monte Carlo simulation. Each technique will be described briefly.

* **Cashflow-based Simulation**
This approach has been used in FMAP for many years. Every month, the unpaid principal balance of a loan, scheduled/ unscheduled payment and dollar amount of each loan segments are calculated and tracked.
* **Markov Chain (Continuous) Simulation**
This approach focuses on the marginal probabilities of each loan segment.
* **Monte Carlo (Discrete) Simulation**
This is a widely used simulation method for dealing with large amount of data. This approach uses the conditional probabilities and a random number to provide a deterministic status of a loan at month end.

Theoretically, the cashflow based simulation and Markov Chain simulation techniques produce comparable results. With two simulation techniques, one set of simulation results can be benchmarked against the other. Stated differently, one set of simulation results can serve as a cross validation for the other. This cross-validation feature has proven to be a crucial component for FMAP v3.0 development. Comparing the two approaches of Markov Chain and Monte Carlo, statistical theory warrants the two approaches are comparable for a large pool of loans or sufficient time of simulation runs.

### 7.2 Cashflow-based Simulation
The proposed cashflow-based simulation for FMAP v3.0 is similar to the cashflow projection method used in FMAP v2.0 and based on the following two equations:

$$
UPB_{t-1} = performingUPB_t + schedPrinPaid_t + prepayAmt_t + delinquentAmt_t + defaultAmt_t
$$

$$
UPB_t = UPB_{t-1} - schedPrinPaid_t - prepayAmt_t - defaultAmt_t
$$

This method directly calculates projections for the following cash flows:

* Performing unpaid principal balance
* Paid scheduled principal
* Unscheduled principal
* Prepayment
* Paid scheduled interest
* Delinquent unpaid principal balance: LDQ, SDQ, DDQ
* Default unpaid principal balance
* Credit loss related cash flows, including charge off, foreclosure expense, MI, etc.

Detailed descriptions of cashflow projections can be found in the appendix.

### 7.3 Markov Chain (Continuous) Simulation
In this framework, the behavioral equations provide conditional probabilities from states in a given month to states in the next month. These probabilities feed the transition matrix needed by this framework. With a given conditional distribution of states of a loan at one month, we can calculate the marginal probabilities of states at the next month. The Markov Chain algorithm is described as follows:

**State Space:** In terms of the Markov Chain, the state space is the set of all possible values each loan could take. In our case, state space = {perf, nrpl, mrpl, rpl, ldq, sdq, ddq, prep, default}, where prep and default are absorbing states, as stated previously in the behavioral equation section.

**State Vector:** a vector $SV(t)$ of the following elements:
($P_{perf_t}$, $P_{nrpl_t}$, $P_{mrpl_t}$, $P_{rpl_t}$, $P_{ldq_t}$, $P_{sdq_t}$, $P_{ddq_t}$, $P_{prep_t}$, $P_{def_t}$)
where the subscript represents the state.

These elements are the unconditional probabilities of each state of a loan at month t.

At the portfolio month, when month t = 0, the $SV(0)$ is initialized by the following rules, based on the provided loan characteristics: "Loan Segment":

If Loan Segment is PERF, then $SV(0)=(1, 0, 0, 0, 0, 0, 0, 0, 0)$.
If Loan Segment is NON-MOD RPL, then $SV(0)=(0, 1, 0, 0, 0, 0, 0, 0, 0)$.
If Loan Segment is MOD RPL, then $SV(0)=(0, 0, 1, 0, 0, 0, 0, 0, 0)$.
If Loan Segment is LDQ, then $SV(0)=(0, 0, 0, 0, 1, 0, 0, 0, 0)$.
If Loan Segment is SDQ, then $SV(0)=(0, 0, 0, 0, 0, 1, 0, 0, 0)$.
If Loan Segment is DDQ, then $SV(0)=(0, 0, 0, 0, 0, 0, 1, 0, 0)$.

At month t=0, "Loan Segment" can only be in one of the above mentioned six states. It is impossible to have a scenario to define $SV(0)$ as (0, 0, 0, 1, 0, 0, 0, 0, 0).

**Transition Matrix(t)**
The transition matrix $TM(t)$ is invoked by the behavioral equations for each loan at time t. In the $TM(t)$:

| TM | <div style="text-align:center">Transition to: (next month)</div> | | | | | | | |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | **SURVIVING** | | | | | | | **TERMINATIONS** | |
| **Transition from:** | **PERF** | **mRPL** | **nRPL** | **RPL** | **LDQ** | **SDQ** | **DDQ** | **Prep** | **Deft** |
| PERF | residual | | | | perf_ldq | | | perf_prep | |
| nRPL | | | residual | | nrpl_ldq | | | nrpl_prep | |
| mRPL | | residual | | | mrpl_ldq | | | mrpl_prep | |
| RPL | | | | residual | rpl_ldq | | | rpl_prep | |
| LDQ | | | | ldq_rpl | residual | ldq_sdq | | ldq_prep | ldq_deft |
| SDQ | | | | sdq_rpl | sdq_ldq | residual | sdq_ddq | sdq_prep | sdq_deft |
| DDQ | | | | ddq_rpl | ddq_ldq | ddq_sdq | residual | ddq_prep | ddq_deft |

Calculate State Vector at next month (skipping the last 2 elements of $SV(t-1)$):
$$
SV(t) = SV(t-1) * TM(t-1)
$$
(This is matrix multiplication of a 1x7 row vector and a matrix of 7x9).

Through chain multiplication, we can have: $SV(t) = SV(0) * TM(0) * TM(1) * TM(2) * ... * TM(t-1)$

Once the distribution of future status (or their marginal probabilities) is computed, the cashflow of prepayment, default, and loss can be calculated by combining scheduled amortization.

**Prepayment**
$$
Prepaid\ amount(t) = Prepay\ Prob(t) * Schd\_UPB(t)
$$

**Default**
$$
Default\ amount(t) = Default\ Prob(t) * Schd\_UPB(LPI),\ where\ LPI < t
$$

**Loss and Loss Severity**
When a default is simulated, the LGD models are applied to calculate loss and loss severity. In the LGD module, a default is classified by three types: REO, FA (Foreclosure Alternative including Dee-in-Lieu, Pre-foreclosure Sale, and Third-Party Sale) and NS (NPL Sale), which are used to define formulas for losses. Loss has two parts:

$$
Charge\ Off = Liquidation\ UPB + Fixed\ Cost + Carrying\ Expense\ Including\ Accrued\ Interest - Sale\ Proceed
$$

$$
Operating\ Expense = Applies\ only\ to\ REO\ liquidation.
$$

Loss is further distinguished by gross loss (before considering mortgage insurance) and net Loss (after the mortgage insurance). The relation is as follows:

$$
Net\ Loss = Gross\ Loss - MI\ Proceeds
$$

### 7.4 Monte Carlo (Discrete) Simulation
While the Markov Chain (continuous) method computes the probabilities of several states in each month, the Monte Carlo (discrete) method simulates a single outcome in each month, which would be useful for certain applications. The Monte Carlo algorithm is as follows:

Given the state of the loan at month t, one invokes the corresponding behavior equation to calculate the probabilities of states at month $t+1$, then use a random number to select a state among the several possible states. Statistical theory proves that continuous and discrete simulations produce comparable results for large populations. The results from the simulations using the two approaches are reasonably close.

## 8 Reporting Module

FMAP v3.0 produces the loan-level cash flow components over the remaining life of the loans for different scenarios and time horizons. For example:

* Unpaid principal balance
* Scheduled and unscheduled principal payments
* Prepayment dollar amount
* Default dollar amount
* Dollar amount by loan delinquency status (i.e., LDQ, SDQ, DDQ)
* Credit loss

FMAP v3.0 possesses the capability to aggregate loan-level cash flow reports (e.g., aggregate them by either delinquent status or key risk metrics categories, such as mark-to-market loan-to-value, credit score, etc...).[^16]

## 9 Appendix

### 9.1 Behavioral Equations
The tables below provide context on the behavioral equations along with the results of the separately estimated behavioral equations for each Enterprise-segment-transition state.

**Table 3. Variable Specification for Each Segment and Transition State**
*(Note: This is a wide table; columns represent different model segments.)*
| | Perf(F30/F15) - LDQ | Perf(F30/F15) - Prepay | ARM - LDQ | ARM - Prepay | MRPL - LDQ | MRPL - Prepay | NRPL - LDQ | NRPL - Prepay | RPL - LDQ | RPL - Prepay | NPL (Same Spec) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Refinance Rate** | X | X | X | X | X | X | X | X | X | X | X |
| **Cash Out** | X | X | X | X | X | X | X | X | X | X | X |
| **Investment** | X | X | X | X | X | X | X | X | X | X | X |
| **Second Home** | X | X | X | X | X | X | X | X | X | X | X |
| **Age** | X | X | X | X | X | X | X | X | X | X | X |
| **Age Sq.** | X | X | X | X | X | X | X | X | X | X | |
| **Age Cb.** | X | | X | | X | X | X | X | X | X | |
| **Current UPB (000s)** | X | X | X | X | X | X | X | X | X | X | X |
| **Current UPB (000s) Sq.** | X | X | X | X | X | X | X | X | X | X | X |
| **Credit Score** | X | X | X | X | X | X | X | X | X | X | X |
| **Credit Score Sq.** | X | X | X | X | X | X | X | X | X | X | |
| **Sato-F30** | X | X | X | X | X | X | X | X | X | X | X |
| **Burnout Count** | X | | X | | X | | X | | X | | X |
| **Unemployment Rate** | X | X | X | X | X | X | X | X | X | X | |
| **Unemployment Burnout Count, 8%**| X | X | X | X | X | X | X | X | X | X | |
| **Unemployment Burnout Count, 10%**| X | X | X | X | X | X | X | X | X | X | |
| **Unemployment Burnout Count, 12%**| X | X | X | X | X | X | X | X | X | X | |
| **max(0, mtmltv-79)** | X | | X | | X | | X | | X | | |
| **max(0, 79-mtmltv)** | X | | X | | X | | X | | X | | |
| **max(0, mtmltv-154)** | X | | X | | X | | X | | X | | |
| **max(0, mtmltv-90)** | X | | X | | X | | X | | X | | |
| **max(0, mtmltv-105)** | X | | X | | X | | X | | X | | |
| **max(0, debt_ratio-60)** | X | X | X | X | X | X | X | X | X | X | |
| **max(0, 60-debt_ratio)** | X | X | X | X | X | X | X | X | X | X | |
| **max(0, debt_ratio-30)** | X | X | X | X | X | X | X | X | X | X | |
| **max(0, debt_ratio-95)** | X | X | X | X | X | X | X | X | X | X | |
| **Origination LTV** | X | X | X | X | X | X | X | X | X | X | |
| **Junior Lien Indicator**| X | X | X | X | X | X | X | X | X | X | X |
| **Orig LTV*Jr Lien Ind**| X | X | X | X | X | X | X | X | X | X | |
| **One Borrower Indicator**| X | X | X | X | X | X | X | X | X | X | X |
| **Credit Score*One Borrower**| X | X | X | X | X | X | X | X | X | X | X |
| **No Full Doc Loan** | X | X | X | X | X | X | X | X | X | X | X |
| **Third Party Loan** | X | X | X | X | X | X | X | X | | | |
| **Judicial State** | X | X | X | X | X | X | X | X | X | X | X |
| **Current UPB / Orig UPB**| X | X | X | X | X | X | X | X | | | |
| **HPA with 24 month lag**| X | X | X | X | X | X | X | X | | | |
| **HPA with lag * Sunk Cost**| X | X | X | X | X | X | X | X | | | |
| **MTMLTV*Refinance Rate**| X | X | X | X | X | X | X | X | | | |
| **MTMLTV*Cash Out** | X | X | X | X | X | X | X | X | | | |
| **Q1** | X | X | X | X | X | X | X | X | | | |
| **Q2** | X | X | X | X | X | X | X | X | | | |
| **Q3** | X | X | X | X | X | X | X | X | | | |
| **2005-2008 Indicator** | X | X | X | X | X | X | X | X | X | X | X |
| **2009-2013 Indicator** | X | X | X | X | X | X | X | X | X | X | X |
| **>2014 Indicator** | X | X | X | X | X | X | X | X | X | X | X |
| **max(0,17-age)** | | X | | X | | X | | X | | X | |
| **max(0,age-17)** | | X | | X | | X | | X | | X | |
| **max(0,age-7)** | | X | | X | | X | | X | | X | |
| **max(0,age-93)** | | X | | X | | X | | X | | X | |
| **max(0,age-35)** | | X | | X | | X | | X | | X | |
| **max(0,mtmltv-66)** | | X | | X | | X | | X | | X | |
| **max(0,66-mtmltv)** | | X | | X | | X | | X | | X | |
| **max(0,mtmltv-30)** | | X | | X | | X | | X | | X | |
| **max(0,mtmltv-6)** | | X | | X | | X | | X | | X | |
| **max(0,mtmltv-101)**| | X | | X | | X | | X | | X | |
| **max(0,mtmltv-9)** | | X | | X | | X | | X | | X | |
| **max(0,refi_incentive_level_l2-1.4)** | | X | | X | | X | | X | | X | |
| **max(0,1.4-refi_incentive_level_l2)** | | X | | X | | X | | X | | X | |
| **max(0,refi_incentive_level_l2-0.02)** | | X | | X | | X | | X | | X | |
| **max(0,refi_incentive_level_l2-1.1)** | | X | | X | | X | | X | | X | |
| **max(0,brnt_cnt-1)** | | X | | X | | X | | X | | X | |
| **max(0,brnt_cnt-8)** | | X | | X | | X | | X | | X | |
| **max(0,8-brnt_cnt)** | | X | | X | | X | | X | | X | |
| **max(0,brnt_cnt-50)**| | X | | X | | X | | X | | X | |
| **max(0,brnt_cnt-74)**| | X | | X | | X | | X | | X | |
| **Indicator for 2001-2003 Refi Boom** | | X | | X | | X | | X | | X | |
| **Months until Interest Rate reset** | | | X | X | | | | | | | |
| **Min # of months since Mod or Del** | | | | | X | X | | | | | |
| **min_dt_sq** | | | | | X | X | | | | | |
| **min_dt_cb** | | | | | X | X | | | | | |
| **# of months since last 3+ months delinquent** | | | | | | | X | X | | | |
| **month_from_last_dq_sq** | | | | | | | X | X | | | |
| **month_from_last_dq_cb** | | | | | | | X | X | | | |
| **Debt to Income Ratio** | | | | | | | | | | | X |
| **Fixed Rate Mortgage 40 YR**| | | | | | | | | | | X |
| **Fixed Rate Mortgage 30 YR**| | | | | | | | | | | X |
| **Fixed Rate Mortgage 15 YR**| | | | | | | | | | | X |
| **Non Fixed Rate Mortgage**| | | | | | | | | | | X |
| **Alta Loan Indicator** | | | | | | | | | | | X |
| **IO Loan Indicator** | | | | | | | | | | | X |
| **Jumbo Loan Indicator**| | | | | | | | | | | X |
| **max(0,unemp_rate-9)**| | | | | | | | | | | X |
| **max(0,9-unemp_rate)**| | | | | | | | | | | X |
| **max(0,unemp_rate-7)**| | | | | | | | | | | X |
| **max(0,unemp_rate-3)**| | | | | | | | | | | X |
| **max(0,unemp_rate-5.5)**| | | | | | | | | | | X |
| **max(0,mtmltv-95)** | | | | | | | | | | | X |
| **max(0,95-mtmltv)** | | | | | | | | | | | X |
| **max(0,mtmltv-50)** | | | | | | | | | | | X |
| **max(0,mtmltv-80)** | | | | | | | | | | | X |
| **max(0,mtmltv-30)** | | | | | | | | | | | X |
| **max(0,mtmltv-140)**| | | | | | | | | | | X |
| **max(0,mtmltv-5)** | | | | | | | | | | | X |
| **Refi Incentive with 2 months lag** | | | | | | | | | | | X |
| **January Indicator** | | | | | | | | | | | X |
| **February Indicator**| | | | | | | | | | | X |
| **March Indicator** | | | | | | | | | | | X |
| **April Indicator** | | | | | | | | | | | X |
| **May Indicator** | | | | | | | | | | | X |
| **June Indicator** | | | | | | | | | | | X |
| **July Indicator** | | | | | | | | | | | X |
| **August Indicator** | | | | | | | | | | | X |
| **September Indicator** | | | | | | | | | | | X |
| **October Indicator** | | | | | | | | | | | X |
| **November Indicator** | | | | | | | | | | | X |
| **Number of variables** | 45 | 58 | 46 | 59 | 48 | 61 | 48 | 61 | 45 | 58 | 45 |

**Table 4. Segment: F30 Performing, Enterprise 1, Event: Idq**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -38.2439 | 0.9184 | <.0001 |
| Refinance Rate | 0.2014 | 0.0522 | 0.0001 |
| Cash Out | 0.6437 | 0.0497 | <.0001 |
| Investment | 0.0253 | 0.0232 | 0.2738 |
| Second Home | -0.2218 | 0.0373 | <.0001 |
| Age | 0.0332 | 0.0009 | <.0001 |
| Age Sq. | -0.0003 | 0.0000 | <.0001 |
| Age (Years) Cb. | 0.0012 | 0.0000 | <.0001 |
| Current UPB (000s) | 0.0012 | 0.0002 | <.0001 |
| Current UPB (00000s) Sq. | 0.0028 | 0.0000 | <.0001 |
| Credit Score | 0.0186 | 0.0015 | <.0001 |
| Credit Sq (0s) Sq. | -0.0020 | 0.0000 | <.0001 |
| Sato F30 | 0.3464 | 0.0105 | <.0001 |
| Burnout Count | 0.0056 | 0.0005 | <.0001 |
| Unemployment Rate | 0.1059 | 0.0038 | <.0001 |
| Unemployment Burnout Count, 8% | -0.4291 | 0.0319 | <.0001 |
| Unemployment Burnout Count, 10% | -0.6098 | 0.0438 | <.0001 |
| Unemployment Burnout Count, 12% | -1.0179 | 0.0619 | <.0001 |
| max(0, mtmltv-79) | 0.0320 | 0.0021 | <.0001 |
| max(0, 79-mtmltv) | -0.0203 | 0.0009 | <.0001 |
| max(0, mtmltv-154) | -0.0191 | 0.0025 | <.0001 |
| max(0, mtmltv-90) | -0.0093 | 0.0035 | 0.007 |
| max(0, mtmltv-105) | -0.0128 | 0.0024 | <.0001 |
| max(0,debt_ratio-.60) | -0.7255 | 0.2931 | 0.0133 |
| max(0,.60-debt_ratio) | -0.9295 | 0.1772 | <.0001 |
| max(0,debt_ratio-.30) | 0.5298 | 0.2173 | 0.0148 |
| max(0,debt_ratio-.95) | 0.1939 | 0.1600 | 0.2254 |
| Origination LTV | 0.5353 | 0.0610 | <.0001 |
| Junior Lien Indicator | 0.6868 | 0.0938 | <.0001 |
| Orig. LTV x Junior Lien Ind | -0.5582 | 0.1157 | <.0001 |
| One Borrower Indicator | -1.5515 | 0.1328 | <.0001 |
| Credit Score x One Borrower (00s) | 0.3093 | 0.0002 | <.0001 |
| No Full Doc Loan | 0.4780 | 0.0180 | <.0001 |
| Third Party Loan | 0.1423 | 0.0120 | <.0001 |
| Judicial State | 0.1430 | 0.0119 | <.0001 |
| Current UPB/Origination UPB | 30.4879 | 0.7884 | <.0001 |
| HPA with 24 month lag | 20.4234 | 0.5906 | <.0001 |
| HPA with lag x Sunk Cost | -22.9901 | 0.6168 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.0030 | 0.0006 | 0.956 |
| MTMLTV x Cash Out (00s) | -0.5070 | 0.0006 | <.0001 |
| Q1 | -0.1383 | 0.0157 | <.0001 |
| Q2 | -0.2647 | 0.0162 | <.0001 |
| Q3 | -0.1455 | 0.0157 | <.0001 |
| 2005-2008 Indicator | 0.1088 | 0.0178 | <.0001 |
| 2009-2013 Indicator | -0.5820 | 0.0268 | <.0001 |
| >2014 Indicator | -0.4746 | 0.0339 | <.0001 |

**Table 5. Segment: F15 Performing, Enterprise 1, Event: Idq**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -17.4693 | 1.0186 | <.0001 |
| Refinance Rate | 0.1995 | 0.1001 | 0.0464 |
| Cash Out | 0.3712 | 0.0978 | 0.0001 |
| Investment | 0.0747 | 0.0436 | 0.0862 |
| Second Home | -0.0983 | 0.0815 | 0.2279 |
| Age | 0.0550 | 0.0017 | <.0001 |
| Age Sq. | -0.0004 | 0.0000 | <.0001 |
| Age (Years) Cb. | 0.0020 | 0.0000 | <.0001 |
| Current UPB (000s) | -0.0039 | 0.0004 | <.0001 |
| Current UPB (00000s) Sq. | 0.0903 | 0.0000 | <.0001 |
| Credit Score | 0.0285 | 0.0027 | <.0001 |
| Credit Sq (0s) Sq. | -0.0030 | 0.0000 | <.0001 |
| Sato F30 | 0.0628 | 0.0164 | 0.0001 |
| Burnout Count | 0.0036 | 0.0007 | <.0001 |
| Unemployment Rate | 0.1306 | 0.0069 | <.0001 |
| Unemployment Burnout Count, 8% | -0.2698 | 0.0593 | <.0001 |
| Unemployment Burnout Count, 10% | -0.2052 | 0.0787 | 0.0091 |
| Unemployment Burnout Count, 12% | -0.9642 | 0.1165 | <.0001 |
| max(0, mtmltv-79) | 0.0410 | 0.0065 | <.0001 |
| max(0, 79-mtmltv) | -0.0273 | 0.0020 | <.0001 |
| max(0, mtmltv-154) | -0.0460 | 0.0059 | <.0001 |
| max(0, mtmltv-90) | -0.0263 | 0.0132 | 0.0459 |
| max(0, mtmltv-105) | -0.0004 | 0.0117 | 0.9756 |
| max(0,debt_ratio-.60) | 0.1426 | 0.4809 | 0.7668 |
| max(0,.60-debt_ratio) | -1.0286 | 0.2585 | <.0001 |
| max(0,debt_ratio-.30) | 0.1214 | 0.3475 | 0.7268 |
| max(0,debt_ratio-.95) | -0.2645 | 0.2556 | 0.3006 |
| Origination LTV | -0.3775 | 0.1161 | 0.0011 |
| Junior Lien Indicator | 0.1668 | 0.1379 | 0.2265 |
| Orig. LTV x Junior Lien Ind | 0.1300 | 0.1855 | 0.4836 |
| One Borrower Indicator | -1.7962 | 0.2360 | <.0001 |
| Credit Score x One Borrower (00s) | 0.3594 | 0.0003 | <.0001 |
| No Full Doc Loan | 0.5238 | 0.0414 | <.0001 |
| Third Party Loan | 0.1179 | 0.0227 | <.0001 |
| Judicial State | 0.1804 | 0.0223 | <.0001 |
| Current UPB/Origination UPB | 5.6573 | 0.5657 | <.0001 |
| HPA with 24 month lag | 2.7332 | 0.4209 | <.0001 |
| HPA with lag x Sunk Cost | -3.6433 | 0.5155 | <.0001 |
| MTMLTV x Refinance Rate (00s) | 0.0586 | 0.0016 | 0.7171 |
| MTMLTV x Cash Out (00s) | 0.2611 | 0.0016 | 0.0963 |
| Q1 | -0.2120 | 0.0293 | <.0001 |
| Q2 | -0.3551 | 0.0304 | <.0001 |
| Q3 | -0.2629 | 0.0296 | <.0001 |
| 2005-2008 Indicator | 0.1529 | 0.0350 | <.0001 |
| 2009-2013 Indicator | -0.3077 | 0.0414 | <.0001 |
| >2014 Indicator | 0.0296 | 0.0557 | 0.5945 |

**Table 6. Segment: F30 Performing, Enterprise 1, Event: prepay**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -34.0126 | 0.7351 | <.0001 |
| Refinance Rate | 0.0711 | 0.0150 | <.0001 |
| Cash Out | 0.1086 | 0.0163 | <.0001 |
| Investment | -0.3128 | 0.0080 | <.0001 |
| Second Home | -0.1185 | 0.0099 | <.0001 |
| max(0,17-age) | -0.1650 | 0.0033 | <.0001 |
| max(0,age-17) | 0.1435 | 0.0040 | <.0001 |
| max(0,age-7) | -0.1464 | 0.0039 | <.0001 |
| max(0,age-93) | -0.0044 | 0.0004 | <.0001 |
| max(0,age-35) | -0.0010 | 0.0005 | 0.0491 |
| Current UPB (000s) | 0.0056 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq | -0.0572 | 0.0000 | <.0001 |
| Credit Score | 0.0113 | 0.0007 | <.0001 |
| Credit Sq (0s) Sq. | -0.0007 | 0.0000 | <.0001 |
| Sato F30 | 0.4473 | 0.0045 | <.0001 |
| Unemployment Rate | -0.0465 | 0.0015 | <.0001 |
| Unemployment Burnout Count, 8% | 0.0474 | 0.0102 | <.0001 |
| Unemployment Burnout Count, 10% | 0.2849 | 0.0134 | <.0001 |
| Unemployment Burnout Count, 12% | 0.1611 | 0.0225 | <.0001 |
| max(0,mtmltv-66) | -0.5174 | 0.0108 | <.0001 |
| max(0,66-mtmltv) | 0.4958 | 0.0108 | <.0001 |
| max(0,mtmltv-30) | 0.0048 | 0.0011 | <.0001 |
| max(0,mtmltv-6) | 0.4702 | 0.0252 | <.0001 |
| max(0,mtmltv-101) | 0.0060 | 0.0009 | <.0001 |
| max(0,mtmltv-9) | 0.0223 | 0.0163 | 0.1694 |
| max(0,debt_ratio-.60) | 0.1304 | 0.0984 | 0.1853 |
| max(0,.60-debt_ratio) | -0.2829 | 0.0427 | <.0001 |
| max(0,debt_ratio-.30) | -0.5297 | 0.0596 | <.0001 |
| max(0,debt_ratio-.95) | 0.3993 | 0.0659 | <.0001 |
| Origination LTV | 0.2894 | 0.0249 | <.0001 |
| Junior Lien Indicator | 0.1943 | 0.0295 | <.0001 |
| Orig. LTV x Junior Lien Ind | -0.3202 | 0.0397 | <.0001 |
| One Borrower Indicator | -0.2102 | 0.0484 | <.0001 |
| Credit Score x One Borrower (00s) | 0.0155 | 0.0001 | 0.0195 |
| No Full Doc Loan | -0.1214 | 0.0078 | <.0001 |
| Third Party Loan | 0.0449 | 0.0038 | <.0001 |
| Judicial State | -0.1201 | 0.0040 | <.0001 |
| Current UPB/Origination UPB | -3.1012 | 0.1275 | <.0001 |
| HPA with 24 month lag | -0.6704 | 0.1103 | <.0001 |
| HPA with lag x Sunk Cost | 1.8635 | 0.1166 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.1370 | 0.0002 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.2800 | 0.0003 | <.0001 |
| Q1 | -0.0706 | 0.0053 | <.0001 |
| Q2 | 0.0470 | 0.0052 | <.0001 |
| Q3 | 0.0658 | 0.0052 | <.0001 |
| 2005-2008 Indicator | -0.1741 | 0.0072 | <.0001 |
| 2009-2013 Indicator | -0.4301 | 0.0073 | <.0001 |
| >2014 Indicator | -0.4597 | 0.0092 | <.0001 |
| max(0,refi_incentive_level_l2-1.4) | 0.3549 | 0.0314 | <.0001 |
| max(0,1.4-refi_incentive_level_l2) | -0.5152 | 0.0109 | <.0001 |
| max(0,refi_incentive_level_l2-0.02) | 0.7021 | 0.0163 | <.0001 |
| max(0,refi_incentive_level_l2-1.1) | -0.5290 | 0.0317 | <.0001 |
| max(0, brnt_cnt-1) | -0.1741 | 0.0083 | <.0001 |
| max(0, brnt_cnt-8) | 0.1629 | 0.0083 | <.0001 |
| max(0,8-brnt_cnt) | -0.1609 | 0.0076 | <.0001 |
| max(0, brnt_cnt-50) | -0.0009 | 0.0007 | 0.2053 |
| max(0, brnt_cnt-74) | 0.0037 | 0.0007 | <.0001 |
| Indicator for 2001-2003 Refi Boom | 0.6014 | 0.0064 | <.0001 |

**Table 7. Segment: F15 Performing, Enterprise 1, Event: prepay**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -48.7778 | 0.3720 | <.0001 |
| Refinance Rate | 0.0370 | 0.0127 | 0.0035 |
| Cash Out | 0.0336 | 0.0133 | 0.0116 |
| Investment | -0.1890 | 0.0093 | <.0001 |
| Second Home | -0.0386 | 0.0118 | 0.0011 |
| max(0,17-age) | -0.2016 | 0.0043 | <.0001 |
| max(0,age-17) | 0.1770 | 0.0051 | <.0001 |
| max(0,age-7) | -0.1822 | 0.0050 | <.0001 |
| max(0,age-93) | -0.0004 | 0.0003 | 0.2476 |
| max(0,age-35) | -0.0040 | 0.0006 | <.0001 |
| Current UPB (000s) | 0.0056 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | -0.0606 | 0.0000 | <.0001 |
| Credit Score | 0.0110 | 0.0007 | <.0001 |
| Credit Sq (0s) Sq. | -0.0007 | 0.0000 | <.0001 |
| Sato F30 | 0.2751 | 0.0040 | <.0001 |
| Unemployment Rate | -0.0343 | 0.0016 | <.0001 |
| Unemployment Burnout Count, 8% | 0.0313 | 0.0106 | 0.0032 |
| Unemployment Burnout Count, 10% | 0.2468 | 0.0154 | <.0001 |
| Unemployment Burnout Count, 12% | 0.1119 | 0.0247 | <.0001 |
| max(0,mtmltv-66) | -0.7416 | 0.0039 | <.0001 |
| max(0,66-mtmltv) | 0.7232 | 0.0038 | <.0001 |
| max(0,mtmltv-30) | 0.0222 | 0.0007 | <.0001 |
| max(0,mtmltv-6) | 0.8820 | 0.0092 | <.0001 |
| max(0,mtmltv-101) | -0.0212 | 0.0041 | <.0001 |
| max(0,mtmltv-9) | -0.1936 | 0.0062 | <.0001 |
| max(0,debt_ratio-.60) | -0.1746 | 0.1022 | 0.0876 |
| max(0,.60-debt_ratio) | -0.1403 | 0.0383 | 0.0002 |
| max(0,debt_ratio-.30) | -0.3014 | 0.0593 | <.0001 |
| max(0,debt_ratio-.95) | 0.4762 | 0.0686 | <.0001 |
| Origination LTV | 1.5600 | 0.0222 | <.0001 |
| Junior Lien Indicator | 0.0826 | 0.0228 | 0.0003 |
| Orig. LTV x Junior Lien Ind | -0.0682 | 0.0364 | 0.0609 |
| One Borrower Indicator | -0.1125 | 0.0563 | 0.0458 |
| Credit Score x One Borrower (00s) | 0.0080 | 0.0001 | 0.2899 |
| No Full Doc Loan | -0.0355 | 0.0096 | 0.0002 |
| Third Party Loan | 0.0631 | 0.0042 | <.0001 |
| Judicial State | -0.0713 | 0.0042 | <.0001 |
| Current UPB/Origination UPB | -0.4813 | 0.0736 | <.0001 |
| HPA with 24 month lag | -0.2967 | 0.0491 | <.0001 |
| HPA with lag x Sunk Cost | 0.2178 | 0.0616 | 0.0004 |
| MTMLTV x Refinance Rate (00s) | 0.0046 | 0.0003 | 0.8624 |
| MTMLTV x Cash Out (00s) | 0.0895 | 0.0003 | 0.0015 |
| Q1 | -0.0541 | 0.0058 | <.0001 |
| Q2 | 0.0696 | 0.0056 | <.0001 |
| Q3 | 0.0789 | 0.0056 | <.0001 |
| 2005-2008 Indicator | 0.0646 | 0.0086 | <.0001 |
| 2009-2013 Indicator | -0.1413 | 0.0072 | <.0001 |
| >2014 Indicator | -0.2437 | 0.0108 | <.0001 |
| max(0,refi_incentive_level_l2-1.4) | -0.2175 | 0.0342 | <.0001 |
| max(0,1.4-refi_incentive_level_l2) | -0.3505 | 0.0112 | <.0001 |
| max(0,refi_incentive_level_l2-0.02) | 0.5869 | 0.0168 | <.0001 |
| max(0,refi_incentive_level_l2-1.1) | -0.2129 | 0.0344 | <.0001 |
| max(0, brnt_cnt-1) | -0.1733 | 0.0091 | <.0001 |
| max(0, brnt_cnt-8) | 0.1654 | 0.0091 | <.0001 |
| max(0,8-brnt_cnt) | -0.1696 | 0.0083 | <.0001 |
| max(0, brnt_cnt-50) | -0.0028 | 0.0007 | <.0001 |
| max(0, brnt_cnt-74) | 0.0096 | 0.0007 | <.0001 |
| Indicator for 2001-2003 Refi Boom | 0.7077 | 0.0071 | <.0001 |

**Table 8. Segment: RPL, Enterprise 1, Event: Idq**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -4.1234 | 0.1457 | <.0001 |
| Refinance Rate | 0.0536 | 0.0103 | <.0001 |
| Cash Out | 0.0399 | 0.0093 | <.0001 |
| Investment | 0.1055 | 0.0067 | <.0001 |
| Second Home | 0.0066 | 0.0103 | 0.5216 |
| Age | -0.0367 | 0.0003 | <.0001 |
| Age Sq. | 0.0002 | 0.0000 | <.0001 |
| Age (Years) Cb. | -0.0009 | 0.0000 | <.0001 |
| Current UPB (000s) | -0.0014 | 0.0000 | <.0001 |
| Current UPB (00000s) Sq. | 0.0160 | 0.0000 | <.0001 |
| Credit Score | 0.0066 | 0.0003 | <.0001 |
| Credit Sq (0s) Sq. | -0.0007 | 0.0000 | <.0001 |
| Sato F30 | 0.0010 | 0.0020 | 0.6228 |
| Burnout Count | -0.0024 | 0.0001 | <.0001 |
| Unemployment Rate | 0.0609 | 0.0010 | <.0001 |
| Unemployment Burnout Count, 8% | -0.4410 | 0.0087 | <.0001 |
| Unemployment Burnout Count, 10% | -0.7310 | 0.0115 | <.0001 |
| Unemployment Burnout Count, 12% | -0.6791 | 0.0150 | <.0001 |
| max(0, mtmltv-79) | 0.0002 | 0.0005 | 0.7736 |
| max(0, 79-mtmltv) | 0.0081 | 0.0002 | <.0001 |
| max(0, mtmltv-154) | 0.0017 | 0.0005 | 0.0016 |
| max(0, mtmltv-90) | -0.0088 | 0.0009 | <.0001 |
| max(0, mtmltv-105) | 0.0044 | 0.0006 | <.0001 |
| max(0,debt_ratio-.60) | 0.1833 | 0.0691 | 0.008 |
| max(0,.60-debt_ratio) | -0.2650 | 0.0386 | <.0001 |
| max(0,debt_ratio-.30) | -0.5131 | 0.0479 | <.0001 |
| max(0,debt_ratio-.95) | 0.3299 | 0.0415 | <.0001 |
| Origination LTV | 0.7153 | 0.0144 | <.0001 |
| Junior Lien Indicator | 0.1829 | 0.0267 | <.0001 |
| Orig. LTV x Junior Lien Ind | -0.2053 | 0.0340 | <.0001 |
| One Borrower Indicator | -0.3645 | 0.0294 | <.0001 |
| Credit Score x One Borrower (00s) | 0.0701 | 0.0000 | <.0001 |
| No Full Doc Loan | -0.0176 | 0.0046 | 0.0001 |
| Third Party Loan | -0.0074 | 0.0027 | 0.0067 |
| Judicial State | -0.0203 | 0.0027 | <.0001 |
| Current UPB/Origination UPB | 2.1259 | 0.0979 | <.0001 |
| HPA with 24 month lag | -1.2252 | 0.0866 | <.0001 |
| HPA with lag x Sunk Cost | -0.3342 | 0.0913 | 0.0003 |
| MTMLTV x Refinance Rate (00s) | -0.2620 | 0.0001 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.1820 | 0.0001 | <.0001 |
| Q1 | -0.1019 | 0.0037 | <.0001 |
| Q2 | -0.1663 | 0.0037 | <.0001 |
| Q3 | -0.0597 | 0.0036 | <.0001 |
| 2005-2008 Indicator | -0.0675 | 0.0042 | <.0001 |
| 2009-2013 Indicator | -0.0016 | 0.0069 | 0.8183 |
| >2014 Indicator | -0.2747 | 0.0109 | <.0001 |

**Table 9. Segment: RPL, Enterprise 1, Event: prepay**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -45.4811 | 1.1362 | <.0001 |
| Refinance Rate | 0.0264 | 0.0170 | 0.1209 |
| Cash Out | 0.0095 | 0.0163 | 0.562 |
| Investment | 0.0913 | 0.0119 | <.0001 |
| Second Home | 0.0712 | 0.0170 | <.0001 |
| max(0,17-age) | -0.0829 | 0.0969 | 0.3925 |
| max(0,age-17) | 0.0705 | 0.0986 | 0.4747 |
| max(0,age-7) | -0.0903 | 0.0985 | 0.3591 |
| max(0,age-93) | 0.0025 | 0.0003 | <.0001 |
| max(0,age-35) | 0.0087 | 0.0012 | <.0001 |
| Current UPB (000s) | 0.0075 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | -0.1000 | 0.0000 | <.0001 |
| Credit Score | -0.0047 | 0.0006 | <.0001 |
| Credit Sq (0s) Sq. | 0.0005 | 0.0000 | <.0001 |
| Sato F30 | 0.0911 | 0.0040 | <.0001 |
| Unemployment Rate | -0.0927 | 0.0023 | <.0001 |
| Unemployment Burnout Count, 8% | -0.1923 | 0.0195 | <.0001 |
| Unemployment Burnout Count, 10% | -0.0387 | 0.0251 | 0.1232 |
| Unemployment Burnout Count, 12% | 0.7050 | 0.0298 | <.0001 |
| max(0,mtmltv-66) | -0.7694 | 0.0078 | <.0001 |
| max(0,66-mtmltv) | 0.7450 | 0.0078 | <.0001 |
| max(0,mtmltv-30) | -0.0128 | 0.0012 | <.0001 |
| max(0,mtmltv-6) | 1.0055 | 0.0202 | <.0001 |
| max(0,mtmltv-101) | 0.0172 | 0.0009 | <.0001 |
| max(0,mtmltv-9) | -0.2619 | 0.0136 | <.0001 |
| max(0,debt_ratio-.60) | 0.0753 | 0.1244 | 0.5451 |
| max(0,.60-debt_ratio) | -0.1245 | 0.0666 | 0.0613 |
| max(0,debt_ratio-.30) | -0.2831 | 0.0844 | 0.0008 |
| max(0,debt_ratio-.95) | 0.2000 | 0.0785 | 0.0108 |
| Origination LTV | 0.9290 | 0.0263 | <.0001 |
| Junior Lien Indicator | -0.0038 | 0.0479 | 0.9364 |
| Orig. LTV x Junior Lien Ind | -0.0423 | 0.0624 | 0.4975 |
| One Borrower Indicator | -0.0829 | 0.0527 | 0.1155 |
| Credit Score x One Borrower (00s) | -0.0050 | 0.0001 | 0.5346 |
| No Full Doc Loan | -0.2167 | 0.0083 | <.0001 |
| Third Party Loan | 0.0019 | 0.0050 | 0.7086 |
| Judicial State | -0.0670 | 0.0051 | <.0001 |
| Current UPB/Origination UPB | -3.9341 | 0.1234 | <.0001 |
| HPA with 24 month lag | -0.8143 | 0.0986 | <.0001 |
| HPA with lag x Sunk Cost | 2.6407 | 0.1089 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.2880 | 0.0003 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.3880 | 0.0003 | <.0001 |
| Q1 | -0.0841 | 0.0070 | <.0001 |
| Q2 | 0.0642 | 0.0067 | <.0001 |
| Q3 | 0.0615 | 0.0067 | <.0001 |
| 2005-2008 Indicator | -0.0874 | 0.0086 | <.0001 |
| 2009-2013 Indicator | -0.3867 | 0.0129 | <.0001 |
| >2014 Indicator | -0.4403 | 0.0215 | <.0001 |
| max(0,refi_incentive_level_l2-1.4) | 0.6094 | 0.0452 | <.0001 |
| max(0,1.4-refi_incentive_level_l2) | -0.0766 | 0.0231 | 0.0009 |
| max(0,refi_incentive_level_l2-0.02) | 0.1530 | 0.0317 | <.0001 |
| max(0,refi_incentive_level_l2-1.1) | -0.5121 | 0.0495 | <.0001 |
| max(0, brnt_cnt-1) | -0.0774 | 0.0213 | 0.0003 |
| max(0, brnt_cnt-8) | 0.0821 | 0.0214 | 0.0001 |
| max(0,8-brnt_cnt) | -0.0824 | 0.0194 | <.0001 |
| max(0, brnt_cnt-50) | -0.0074 | 0.0007 | <.0001 |
| max(0, brnt_cnt-74) | 0.0013 | 0.0005 | 0.0169 |
| Indicator for 2001-2003 Refi Boom | 0.4645 | 0.0130 | <.0001 |

**Table 10. Segment: ARMs Performing, Enterprise 1, Event: Idq**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -14.9125 | 0.7112 | <.0001 |
| Refinance Rate | 0.5406 | 0.0463 | <.0001 |
| Cash Out | 0.7660 | 0.0446 | <.0001 |
| Investment | 0.0803 | 0.0175 | <.0001 |
| Second Home | -0.0857 | 0.0207 | <.0001 |
| Age | 0.0202 | 0.0009 | <.0001 |
| Age Sq. | -0.0003 | 0.0000 | <.0001 |
| Age (Years) Cb. | 0.0014 | 0.0000 | <.0001 |
| Current UPB (000s) | 0.0012 | 0.0002 | <.0001 |
| Current UPB (00000s) Sq. | 0.0074 | 0.0000 | <.0001 |
| Credit Score | 0.0034 | 0.0015 | 0.0191 |
| Credit Sq (0s) Sq. | -0.0009 | 0.0000 | <.0001 |
| Sato F30 | 0.1830 | 0.0050 | <.0001 |
| Burnout Count | 0.0018 | 0.0005 | 0.0007 |
| Unemployment Rate | 0.0553 | 0.0035 | <.0001 |
| Unemployment Burnout Count, 8% | -0.3543 | 0.0360 | <.0001 |
| Unemployment Burnout Count, 10% | -0.2637 | 0.0466 | <.0001 |
| Unemployment Burnout Count, 12% | -0.3594 | 0.0626 | <.0001 |
| max(0, mtmltv-79) | 0.0365 | 0.0019 | <.0001 |
| max(0, 79-mtmltv) | -0.0134 | 0.0009 | <.0001 |
| max(0, mtmltv-154) | -0.0473 | 0.0016 | <.0001 |
| max(0, mtmltv-90) | -0.0257 | 0.0030 | <.0001 |
| max(0, mtmltv-105) | -0.0009 | 0.0018 | 0.6216 |
| max(0,debt_ratio-.60) | -0.7123 | 0.3282 | 0.03 |
| max(0,.60-debt_ratio) | -1.1156 | 0.1462 | <.0001 |
| max(0,debt_ratio-.30) | 0.1903 | 0.1887 | 0.3132 |
| max(0,debt_ratio-.95) | 0.5201 | 0.2381 | 0.0289 |
| Origination LTV | 2.0750 | 0.0772 | <.0001 |
| Junior Lien Indicator | 0.6979 | 0.1268 | <.0001 |
| Orig. LTV x Junior Lien Ind | -0.4401 | 0.1619 | 0.0066 |
| One Borrower Indicator | -0.2411 | 0.1352 | 0.0745 |
| Credit Score x One Borrower (00s) | 0.1019 | 0.0002 | <.0001 |
| No Full Doc Loan | 0.5410 | 0.0116 | <.0001 |
| Third Party Loan | 0.0888 | 0.0104 | <.0001 |
| Judicial State | 0.1269 | 0.0114 | <.0001 |
| Current UPB/Origination UPB | 11.6751 | 0.5037 | <.0001 |
| HPA with 24 month lag | 5.7011 | 0.4961 | <.0001 |
| HPA with lag x Sunk Cost | -8.8743 | 0.5058 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.3170 | 0.0005 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.4940 | 0.0005 | <.0001 |
| Q1 | -0.0249 | 0.0140 | 0.0749 |
| Q2 | -0.1144 | 0.0143 | <.0001 |
| Q3 | -0.1069 | 0.0142 | <.0001 |
| 2005-2008 Indicator | 0.2482 | 0.0160 | <.0001 |
| 2009-2013 Indicator | -0.7762 | 0.0448 | <.0001 |
| >2014 Indicator | -0.8717 | 0.0921 | <.0001 |
| Months until Interest Rate is reset | 0.0075 | 0.0003 | <.0001 |

**Table 11. Segment: ARMs Performing, Enterprise 1, Event: prepay**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -32.6130 | 0.5230 | <.0001 |
| Refinance Rate | 0.1736 | 0.0140 | <.0001 |
| Cash Out | 0.2045 | 0.0153 | <.0001 |
| Investment | -0.3190 | 0.0076 | <.0001 |
| Second Home | -0.2154 | 0.0080 | <.0001 |
| max(0,17-age) | -0.1520 | 0.0028 | <.0001 |
| max(0,age-17) | 0.1473 | 0.0035 | <.0001 |
| max(0,age-7) | -0.1426 | 0.0033 | <.0001 |
| max(0,age-93) | 0.0035 | 0.0004 | <.0001 |
| max(0,age-35) | -0.0212 | 0.0005 | <.0001 |
| Current UPB (000s) | 0.0029 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | -0.0297 | 0.0000 | <.0001 |
| Credit Score | 0.0094 | 0.0007 | <.0001 |
| Credit Sq (0s) Sq. | -0.0006 | 0.0000 | <.0001 |
| Sato F30 | 0.1146 | 0.0024 | <.0001 |
| Unemployment Rate | -0.0376 | 0.0015 | <.0001 |
| Unemployment Burnout Count, 8% | 0.1333 | 0.0105 | <.0001 |
| Unemployment Burnout Count, 10% | 0.3550 | 0.0142 | <.0001 |
| Unemployment Burnout Count, 12% | 0.3628 | 0.0260 | <.0001 |
| max(0,mtmltv-66) | -0.4957 | 0.0071 | <.0001 |
| max(0,66-mtmltv) | 0.4726 | 0.0071 | <.0001 |
| max(0,mtmltv-30) | 0.0108 | 0.0010 | <.0001 |
| max(0,mtmltv-6) | 0.4514 | 0.0170 | <.0001 |
| max(0,mtmltv-101) | 0.0085 | 0.0010 | <.0001 |
| max(0,mtmltv-9) | 0.0034 | 0.0114 | 0.7646 |
| max(0,debt_ratio-.60) | 0.3258 | 0.1086 | 0.0027 |
| max(0,.60-debt_ratio) | -0.3381 | 0.0371 | <.0001 |
| max(0,debt_ratio-.30) | -0.5255 | 0.0556 | <.0001 |
| max(0,debt_ratio-.95) | 0.1993 | 0.0813 | 0.0142 |
| Origination LTV | 1.3283 | 0.0264 | <.0001 |
| Junior Lien Indicator | 0.1164 | 0.0261 | <.0001 |
| Orig. LTV x Junior Lien Ind | -0.3315 | 0.0360 | <.0001 |
| One Borrower Indicator | -0.1366 | 0.0506 | 0.007 |
| Credit Score x One Borrower (00s) | 0.0044 | 0.0001 | 0.5222 |
| No Full Doc Loan | -0.0898 | 0.0054 | <.0001 |
| Third Party Loan | 0.0847 | 0.0038 | <.0001 |
| Judicial State | -0.0684 | 0.0041 | <.0001 |
| Current UPB/Origination UPB | -1.0167 | 0.0869 | <.0001 |
| HPA with 24 month lag | -0.7869 | 0.0729 | <.0001 |
| HPA with lag x Sunk Cost | 1.3144 | 0.0764 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.1560 | 0.0002 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.3070 | 0.0002 | <.0001 |
| Q1 | -0.0623 | 0.0054 | <.0001 |
| Q2 | 0.1410 | 0.0052 | <.0001 |
| Q3 | 0.1269 | 0.0052 | <.0001 |
| 2005-2008 Indicator | -0.0849 | 0.0062 | <.0001 |
| 2009-2013 Indicator | -0.2302 | 0.0078 | <.0001 |
| >2014 Indicator | -0.3992 | 0.0116 | <.0001 |
| max(0,refi_incentive_level_l2-1.4) | 0.1781 | 0.0364 | <.0001 |
| max(0,1.4-refi_incentive_level_l2) | -0.2903 | 0.0095 | <.0001 |
| max(0,refi_incentive_level_l2-0.02) | 0.1067 | 0.0149 | <.0001 |
| max(0,refi_incentive_level_l2-1.1) | -0.3401 | 0.0359 | <.0001 |
| max(0, brnt_cnt-1) | -0.1412 | 0.0071 | <.0001 |
| max(0, brnt_cnt-8) | 0.1362 | 0.0072 | <.0001 |
| max(0,8-brnt_cnt) | -0.1379 | 0.0065 | <.0001 |
| max(0, brnt_cnt-50) | 0.0038 | 0.0008 | <.0001 |
| max(0, brnt_cnt-74) | 0.0059 | 0.0007 | <.0001 |
| Indicator for 2001-2003 Refi Boom | 0.4416 | 0.0066 | <.0001 |
| Months until Interest Rate is reset | 0.0056 | 0.0001 | <.0001 |

**Table 12. Segment: MRPL, Enterprise 1, Event: Idq**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -7.7288 | 0.1544 | <.0001 |
| Refinance Rate | -0.0278 | 0.0105 | 0.0082 |
| Cash Out | -0.0680 | 0.0095 | <.0001 |
| Investment | 0.0745 | 0.0078 | <.0001 |
| Second Home | 0.0226 | 0.0115 | 0.0506 |
| Age | -0.0085 | 0.0003 | <.0001 |
| Age Sq. | 0.0001 | 0.0000 | <.0001 |
| Age (Years) Cb. | -0.0004 | 0.0000 | <.0001 |
| Current UPB (000s) | -0.0008 | 0.0000 | <.0001 |
| Current UPB (00000s) Sq. | 0.0079 | 0.0000 | <.0001 |
| Credit Score | 0.0053 | 0.0003 | <.0001 |
| Credit Sq (0s) Sq. | -0.0007 | 0.0000 | <.0001 |
| Sato F30 | 0.0339 | 0.0020 | <.0001 |
| Burnout Count | 0.0019 | 0.0001 | <.0001 |
| Unemployment Rate | -0.0191 | 0.0011 | <.0001 |
| Unemployment Burnout Count, 8% | -0.3047 | 0.0086 | <.0001 |
| Unemployment Burnout Count, 10% | -0.5213 | 0.0115 | <.0001 |
| Unemployment Burnout Count, 12% | -0.0723 | 0.0154 | <.0001 |
| max(0, mtmltv-79) | -0.0022 | 0.0005 | <.0001 |
| max(0, 79-mtmltv) | 0.0064 | 0.0002 | <.0001 |
| max(0, mtmltv-154) | -0.0003 | 0.0004 | 0.5096 |
| max(0, mtmltv-90) | -0.0026 | 0.0009 | 0.0027 |
| max(0, mtmltv-105) | 0.0041 | 0.0005 | <.0001 |
| max(0,debt_ratio-.60) | -0.1127 | 0.0718 | 0.1167 |
| max(0,.60-debt_ratio) | -0.0709 | 0.0443 | 0.1096 |
| max(0,debt_ratio-.30) | -0.2040 | 0.0530 | 0.0001 |
| max(0,debt_ratio-.95) | 0.3166 | 0.0400 | <.0001 |
| Origination LTV | 0.5584 | 0.0143 | <.0001 |
| Junior Lien Indicator | 0.1642 | 0.0262 | <.0001 |
| Orig. LTV x Junior Lien Ind | -0.1665 | 0.0330 | <.0001 |
| One Borrower Indicator | -0.3034 | 0.0295 | <.0001 |
| Credit Score x One Borrower (00s) | 0.0629 | 0.0000 | <.0001 |
| No Full Doc Loan | -0.0473 | 0.0044 | <.0001 |
| Third Party Loan | 0.0273 | 0.0027 | <.0001 |
| Judicial State | -0.0108 | 0.0028 | <.0001 |
| Current UPB/Origination UPB | 5.5720 | 0.1057 | <.0001 |
| HPA with 24 month lag | 2.7824 | 0.0959 | <.0001 |
| HPA with lag x Sunk Cost | -3.9223 | 0.0975 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.1140 | 0.0001 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.0620 | 0.0001 | <.0001 |
| Q1 | -0.1335 | 0.0037 | <.0001 |
| Q2 | -0.2159 | 0.0037 | <.0001 |
| Q3 | -0.0819 | 0.0036 | <.0001 |
| 2005-2008 Indicator | -0.0824 | 0.0045 | <.0001 |
| 2009-2013 Indicator | -0.1277 | 0.0073 | <.0001 |
| >2014 Indicator | -0.4000 | 0.0122 | <.0001 |
| Min# of months since Mod. or Del | -0.0583 | 0.0002 | <.0001 |
| min_dt_sq | 0.0003 | 0.0000 | <.0001 |
| min_dt_cb | 0.0000 | 0.0000 | <.0001 |

**Table 13. Segment: MRPL, Enterprise 1, Event: prepay**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -42.4729 | 1.6101 | <.0001 |
| Refinance Rate | -0.0274 | 0.0194 | 0.1573 |
| Cash Out | -0.0916 | 0.0184 | <.0001 |
| Investment | 0.0820 | 0.0149 | <.0001 |
| Second Home | 0.0335 | 0.0201 | 0.0948 |
| max(0,17-age) | -0.0859 | 0.1399 | 0.5395 |
| max(0,age-17) | 0.0507 | 0.1421 | 0.7211 |
| max(0,age-7) | -0.0771 | 0.1420 | 0.5871 |
| max(0,age-93) | 0.0076 | 0.0004 | <.0001 |
| max(0,age-35) | 0.0090 | 0.0019 | <.0001 |
| Current UPB (000s) | 0.0068 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | -0.1000 | 0.0000 | <.0001 |
| Credit Score | -0.0035 | 0.0007 | <.0001 |
| Credit Sq (0s) Sq. | 0.0004 | 0.0000 | <.0001 |
| Sato F30 | 0.0483 | 0.0041 | <.0001 |
| Unemployment Rate | -0.0940 | 0.0026 | <.0001 |
| Unemployment Burnout Count, 8% | -0.2175 | 0.0192 | <.0001 |
| Unemployment Burnout Count, 10% | -0.2237 | 0.0239 | <.0001 |
| Unemployment Burnout Count, 12% | 0.8128 | 0.0288 | <.0001 |
| max(0,mtmltv-66) | -0.7137 | 0.0107 | <.0001 |
| max(0,66-mtmltv) | 0.6937 | 0.0107 | <.0001 |
| max(0,mtmltv-30) | -0.0206 | 0.0014 | <.0001 |
| max(0,mtmltv-6) | 0.8722 | 0.0272 | <.0001 |
| max(0,mtmltv-101) | 0.0184 | 0.0008 | <.0001 |
| max(0,mtmltv-9) | -0.1762 | 0.0181 | <.0001 |
| max(0,debt_ratio-.60) | 0.0622 | 0.1300 | 0.6322 |
| max(0,.60-debt_ratio) | -0.0658 | 0.0812 | 0.4174 |
| max(0,debt_ratio-.30) | -0.3278 | 0.0973 | 0.0008 |
| max(0,debt_ratio-.95) | 0.2655 | 0.0707 | 0.0002 |
| Origination LTV | 1.0624 | 0.0274 | <.0001 |
| Junior Lien Indicator | 0.1723 | 0.0453 | 0.0001 |
| Orig. LTV x Junior Lien Ind | -0.2466 | 0.0585 | <.0001 |
| One Borrower Indicator | -0.0040 | 0.0536 | 0.941 |
| Credit Score x One Borrower (00s) | -0.0270 | 0.0001 | 0.0006 |
| No Full Doc Loan | -0.2654 | 0.0077 | <.0001 |
| Third Party Loan | 0.0014 | 0.0050 | 0.7804 |
| Judicial State | -0.0563 | 0.0053 | <.0001 |
| Current UPB/Origination UPB | -3.9956 | 0.1741 | <.0001 |
| HPA with 24 month lag | -1.3946 | 0.1425 | <.0001 |
| HPA with lag x Sunk Cost | 2.8463 | 0.1549 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.2650 | 0.0003 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.2800 | 0.0003 | <.0001 |
| Q1 | -0.0860 | 0.0071 | <.0001 |
| Q2 | 0.0780 | 0.0067 | <.0001 |
| Q3 | 0.0785 | 0.0066 | <.0001 |
| 2005-2008 Indicator | -0.1268 | 0.0092 | <.0001 |
| 2009-2013 Indicator | -0.3945 | 0.0140 | <.0001 |
| >2014 Indicator | -0.4221 | 0.0224 | <.0001 |
| max(0,refi_incentive_level_l2-1.4) | 1.0980 | 0.0515 | <.0001 |
| max(0,1.4-refi_incentive_level_l2) | -0.1134 | 0.0286 | <.0001 |
| max(0,refi_incentive_level_l2-0.02) | 0.0279 | 0.0396 | 0.4804 |
| max(0,refi_incentive_level_l2-1.1) | -0.7872 | 0.0563 | <.0001 |
| max(0, brnt_cnt-1) | -0.0398 | 0.0304 | 0.1909 |
| max(0, brnt_cnt-8) | 0.0422 | 0.0305 | 0.167 |
| max(0,8-brnt_cnt) | -0.0382 | 0.0274 | 0.1628 |
| max(0, brnt_cnt-50) | -0.0075 | 0.0008 | <.0001 |
| max(0, brnt_cnt-74) | 0.0013 | 0.0006 | 0.0289 |
| Indicator for 2001-2003 Refi Boom | 0.6885 | 0.0224 | <.0001 |
| Min# of months since Mod or Del | 0.0270 | 0.0003 | <.0001 |
| min_dt_sq | -0.0001 | 0.0000 | <.0001 |
| min_dt_cb | 0.0000 | 0.0000 | <.0001 |

**Table 14. Segment: NRPL, Enterprise 1, Event: Idq**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -4.9498 | 0.1390 | <.0001 |
| Refinance Rate | 0.0954 | 0.0109 | <.0001 |
| Cash Out | 0.1481 | 0.0099 | <.0001 |
| Investment | -0.0712 | 0.0060 | <.0001 |
| Second Home | -0.1574 | 0.0095 | <.0001 |
| Age | -0.0044 | 0.0003 | <.0001 |
| Age Sq. | 0.0000 | 0.0000 | <.0001 |
| Age (Years) Cb. | -0.0001 | 0.0000 | <.0001 |
| Current UPB (000s) | 0.0006 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | 0.0027 | 0.0000 | <.0001 |
| Credit Score | 0.0028 | 0.0003 | <.0001 |
| Credit Sq (0s) Sq. | -0.0004 | 0.0000 | <.0001 |
| Sato F30 | 0.0523 | 0.0020 | <.0001 |
| Burnout Count | 0.0007 | 0.0001 | <.0001 |
| Unemployment Rate | 0.0373 | 0.0009 | <.0001 |
| Unemployment Burnout Count, 8% | -0.2289 | 0.0090 | <.0001 |
| Unemployment Burnout Count, 10% | -0.3231 | 0.0120 | <.0001 |
| Unemployment Burnout Count, 12% | -0.3500 | 0.0149 | <.0001 |
| max(0, mtmltv-79) | 0.0093 | 0.0006 | <.0001 |
| max(0, 79-mtmltv) | 0.0009 | 0.0002 | <.0001 |
| max(0, mtmltv-154) | -0.0013 | 0.0010 | 0.2095 |
| max(0, mtmltv-90) | -0.0087 | 0.0010 | <.0001 |
| max(0, mtmltv-105) | -0.0008 | 0.0008 | 0.2982 |
| max(0,debt_ratio-.60) | -0.0390 | 0.0691 | 0.5719 |
| max(0,.60-debt_ratio) | -0.3096 | 0.0353 | <.0001 |
| max(0,debt_ratio-.30) | -0.1530 | 0.0455 | 0.0008 |
| max(0,debt_ratio-.95) | 0.1919 | 0.0435 | <.0001 |
| Origination LTV | 0.4005 | 0.0152 | <.0001 |
| Junior Lien Indicator | 0.1304 | 0.0271 | <.0001 |
| Orig. LTV x Junior Lien Ind | -0.1214 | 0.0348 | 0.0005 |
| One Borrower Indicator | -0.1842 | 0.0298 | <.0001 |
| Credit Score x One Borrower (00s) | 0.0448 | 0.0000 | <.0001 |
| No Full Doc Loan | 0.0622 | 0.0048 | <.0001 |
| Third Party Loan | 0.0057 | 0.0027 | 0.035 |
| Judicial State | 0.0015 | 0.0028 | 0.5956 |
| Current UPB/Origination UPB | 3.4143 | 0.0905 | <.0001 |
| HPA with 24 month lag | 1.5261 | 0.0755 | <.0001 |
| HPA with lag x Sunk Cost | -2.5608 | 0.0826 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.1740 | 0.0002 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.1970 | 0.0001 | <.0001 |
| Q1 | -0.0934 | 0.0037 | <.0001 |
| Q2 | -0.1839 | 0.0037 | <.0001 |
| Q3 | -0.0609 | 0.0037 | <.0001 |
| 2005-2008 Indicator | 0.0828 | 0.0040 | <.0001 |
| 2009-2013 Indicator | 0.0618 | 0.0068 | <.0001 |
| >2014 Indicator | -0.0261 | 0.0101 | 0.0095 |
| # of months since last 3+ months delinquent | -0.1234 | 0.0004 | <.0001 |
| month_from_last_dq_sq | 0.0015 | 0.0000 | <.0001 |
| month_from_last_dq_cb | 0.0000 | 0.0000 | <.0001 |

**Table 15. Segment: NRPL, Enterprise 1, Event: prepay**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -47.8098 | 0.7915 | <.0001 |
| Refinance Rate | 0.0043 | 0.0155 | 0.7811 |
| Cash Out | -0.0308 | 0.0150 | 0.0402 |
| Investment | 0.0375 | 0.0100 | 0.0002 |
| Second Home | 0.0234 | 0.0148 | 0.1135 |
| max(0,17-age) | -0.0844 | 0.0625 | 0.1764 |
| max(0,age-17) | 0.1144 | 0.0638 | 0.0727 |
| max(0,age-7) | -0.1268 | 0.0637 | 0.0464 |
| max(0,age-93) | 0.0029 | 0.0003 | <.0001 |
| max(0,age-35) | 0.0019 | 0.0010 | 0.0501 |
| Current UPB (000s) | 0.0068 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | -0.1000 | 0.0000 | <.0001 |
| Credit Score | -0.0057 | 0.0006 | <.0001 |
| Credit Sq (0s) Sq. | 0.0006 | 0.0000 | <.0001 |
| Sato F30 | 0.0665 | 0.0037 | <.0001 |
| Unemployment Rate | -0.0746 | 0.0020 | <.0001 |
| Unemployment Burnout Count, 8% | 0.0204 | 0.0195 | 0.2947 |
| Unemployment Burnout Count, 10% | 0.1509 | 0.0261 | <.0001 |
| Unemployment Burnout Count, 12% | 0.4328 | 0.0320 | <.0001 |
| max(0,mtmltv-66) | -0.7985 | 0.0063 | <.0001 |
| max(0,66-mtmltv) | 0.7883 | 0.0063 | <.0001 |
| max(0,mtmltv-30) | 0.0161 | 0.0011 | <.0001 |
| max(0,mtmltv-6) | 1.0351 | 0.0164 | <.0001 |
| max(0,mtmltv-101) | 0.0156 | 0.0011 | <.0001 |
| max(0,mtmltv-9) | -0.2741 | 0.0111 | <.0001 |
| max(0,debt_ratio-.60) | 0.2061 | 0.1204 | 0.0871 |
| max(0,.60-debt_ratio) | -0.2768 | 0.0579 | <.0001 |
| max(0,debt_ratio-.30) | -0.2581 | 0.0772 | 0.0008 |
| max(0,debt_ratio-.95) | 0.0523 | 0.0769 | 0.4966 |
| Origination LTV | 0.7672 | 0.0248 | <.0001 |
| Junior Lien Indicator | -0.0423 | 0.0478 | 0.3767 |
| Orig. LTV x Junior Lien Ind | -0.0641 | 0.0634 | 0.3124 |
| One Borrower Indicator | -0.2335 | 0.0515 | <.0001 |
| Credit Score x One Borrower (00s) | 0.0225 | 0.0001 | 0.0035 |
| No Full Doc Loan | -0.1408 | 0.0090 | <.0001 |
| Third Party Loan | 0.0091 | 0.0049 | 0.0616 |
| Judicial State | -0.0518 | 0.0050 | <.0001 |
| Current UPB/Origination UPB | -4.0426 | 0.1069 | <.0001 |
| HPA with 24 month lag | -1.4260 | 0.0847 | <.0001 |
| HPA with lag x Sunk Cost | 3.8305 | 0.0945 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.0590 | 0.0003 | 0.027 |
| MTMLTV x Cash Out (00s) | -0.0380 | 0.0003 | 0.1373 |
| Q1 | -0.0720 | 0.0069 | <.0001 |
| Q2 | 0.0620 | 0.0066 | <.0001 |
| Q3 | 0.0505 | 0.0067 | <.0001 |
| 2005-2008 Indicator | -0.1260 | 0.0083 | <.0001 |
| 2009-2013 Indicator | -0.3268 | 0.0127 | <.0001 |
| >2014 Indicator | -0.2823 | 0.0207 | <.0001 |
| max(0,refi_incentive_level_l2-1.4) | 0.1751 | 0.0406 | <.0001 |
| max(0,1.4-refi_incentive_level_l2) | -0.0120 | 0.0193 | 0.5345 |
| max(0,refi_incentive_level_l2-0.02) | 0.2277 | 0.0266 | <.0001 |
| max(0,refi_incentive_level_l2-1.1) | -0.2311 | 0.0442 | <.0001 |
| max(0, brnt_cnt-1) | -0.0821 | 0.0170 | <.0001 |
| max(0, brnt_cnt-8) | 0.0879 | 0.0170 | <.0001 |
| max(0,8-brnt_cnt) | -0.0877 | 0.0155 | <.0001 |
| max(0, brnt_cnt-50) | -0.0092 | 0.0006 | <.0001 |
| max(0, brnt_cnt-74) | 0.0024 | 0.0005 | <.0001 |
| Indicator for 2001-2003 Refi Boom | 0.4437 | 0.0101 | <.0001 |
| # of months since last 3+ months delinquent | 0.0180 | 0.0004 | <.0001 |
| month_from_last_dq_sq | -0.0002 | 0.0000 | <.0001 |
| month_from_last_dq_cb | 0.0000 | 0.0000 | <.0001 |

**Table 16. Segment: NPL - Idq, Enterprise 1**
| | <div style="text-align:center">Event: RPL</div> | | | <div style="text-align:center">Event: Prepay</div> | | | <div style="text-align:center">Event: SDQ</div> | | | <div style="text-align:center">Event: Default</div> | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Variable Name** | **Estimate** | **StdErr** | **Probt** | **Estimate** | **StdErr** | **Probt** | **Estimate** | **StdErr** | **Probt** | **Estimate** | **StdErr** | **Probt** |
| Intercept | 7.8211 | 0.5716 | <.0001 | -51.7355 | 0.7248 | <.0001 | -6.5517 | 0.5801 | <.0001 | 23.1044 | 9.9344 | 0.0200 |
| Refinance Rate | -0.1215 | 0.0021 | <.0001 | -0.3180 | 0.0075 | <.0001 | 0.0247 | 0.0018 | <.0001 | 0.1639 | 0.0071 | <.0001 |
| Cash Out | -0.1026 | 0.0020 | <.0001 | -0.3748 | 0.0075 | <.0001 | 0.0330 | 0.0017 | <.0001 | -0.0312 | 0.0073 | <.0001 |
| Investment | -0.1808 | 0.0037 | <.0001 | 0.0436 | 0.0121 | 0.0003 | 0.1787 | 0.0028 | <.0001 | 0.5295 | 0.0091 | <.0001 |
| Second Home | -0.0740 | 0.0057 | <.0001 | 0.1557 | 0.0185 | <.0001 | 0.1331 | 0.0042 | <.0001 | 0.3659 | 0.0151 | <.0001 |
| Age | 0.0005 | 0.0001 | <.0001 | -0.0240 | 0.0002 | <.0001 | -0.0011 | 0.0001 | <.0001 | -0.0002 | 0.0003 | 0.4173 |
| Age Sq. | 0.0000 | | <.0001 | 0.0000 | | <.0001 | 0.0000 | | <.0001 | -0.0001 | | <.0001 |
| Current UPB (000s) | -0.0006 | 0.0000 | <.0001 | 0.0041 | 0.0001 | <.0001 | -0.0004 | 0.0000 | <.0001 | -0.0092 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | 0.0050 | | <.0001 | -0.0885 | | <.0001 | 0.0080 | | <.0001 | 0.1100 | | <.0001 |
| Debt to Income Ratio | 0.0000 | 0.0001 | 0.6899 | -0.0021 | 0.0033 | 0.5328 | 0.0000 | 0.0001 | 0.7260 | -0.2733 | 0.0182 | <.0001 |
| Credit Score | -0.0019 | 0.0000 | <.0001 | 0.0035 | 0.0001 | <.0001 | 0.0010 | 0.0000 | <.0001 | 0.0073 | 0.0001 | <.0001 |
| Burnout Count | 0.0042 | 0.0001 | <.0001 | 0.0051 | 0.0002 | <.0001 | -0.0036 | 0.0001 | <.0001 | 0.0062 | 0.0003 | <.0001 |
| Sato F30 | -0.0370 | 0.0013 | <.0001 | 0.0552 | 0.0048 | <.0001 | 0.0222 | 0.0010 | <.0001 | 0.0331 | 0.0040 | <.0001 |
| Judicial State | -0.0711 | 0.0016 | <.0001 | -0.1361 | 0.0059 | <.0001 | 0.1272 | 0.0014 | <.0001 | -1.5860 | 0.0080 | <.0001 |
| 2005-2008 Indicator | -0.1616 | 0.0022 | <.0001 | -0.6295 | 0.0086 | <.0001 | -0.0602 | 0.0021 | <.0001 | -0.6086 | 0.0082 | <.0001 |
| 2009-2013 Indicator | -0.1404 | 0.0034 | <.0001 | -0.4067 | 0.0105 | <.0001 | -0.0821 | 0.0033 | <.0001 | -0.6889 | 0.0130 | <.0001 |
| >2014 Indicator | -0.1042 | 0.0050 | <.0001 | -0.8181 | 0.0152 | <.0001 | -0.2443 | 0.0053 | <.0001 | -1.7263 | 0.0338 | <.0001 |
| No Full Doc Loan | -0.1036 | 0.0029 | <.0001 | -0.1982 | 0.0113 | <.0001 | 0.0350 | 0.0022 | <.0001 | -0.3097 | 0.0089 | <.0001 |
| Fixed Rate Mortgage 40 YR | 0.0788 | 0.0103 | <.0001 | -0.3803 | 0.0736 | <.0001 | -0.1283 | 0.0073 | <.0001 | -0.3767 | 0.0326 | <.0001 |
| Fixed Rate Mortgage 30 YR | 0.1882 | 0.0033 | <.0001 | -0.1108 | 0.0122 | <.0001 | -0.1092 | 0.0024 | <.0001 | -0.0793 | 0.0095 | <.0001 |
| Fixed Rate Mortgage 15 YR | 0.2102 | 0.0042 | <.0001 | -0.1153 | 0.0140 | <.0001 | -0.1127 | 0.0035 | <.0001 | -0.0965 | 0.0157 | <.0001 |
| Non Fixed Rate Mortgage | 0.0000 | | | 0.0000 | | | 0.0000 | | | 0.0000 | | |
| One Borrower Indicator | -0.0971 | 0.0169 | <.0001 | 0.0764 | 0.0626 | 0.2222 | 0.1437 | 0.0154 | <.0001 | 1.4562 | 0.0653 | <.0001 |
| Credit Score x One Borrower (00s) | 0.0092 | 0.0000 | 0.0003 | -0.0260 | 0.0001 | 0.0045 | -0.0110 | 0.0000 | <.0001 | -0.2130 | 0.0001 | <.0001 |
| Junior Lien Indicator | -0.1424 | 0.0028 | <.0001 | -0.3214 | 0.0118 | <.0001 | 0.0563 | 0.0021 | <.0001 | 0.1715 | 0.0084 | <.0001 |
| Alta Loan Indicator | -0.0255 | 0.0023 | <.0001 | -0.0847 | 0.0097 | <.0001 | -0.0165 | 0.0019 | <.0001 | -0.0002 | 0.0075 | 0.9758 |
| IO Loan Indicator | 0.0000 | | | 0.0000 | | | 0.0000 | | | 0.0000 | | |
| Jumbo Loan Indicator | 0.1335 | 0.0216 | <.0001 | 0.7032 | 0.0616 | <.0001 | -0.0161 | 0.0206 | 0.4344 | -0.3313 | 0.1261 | 0.0086 |
| max(0,unemp_rate-9) | 0.0092 | 0.0147 | 0.5280 | 0.1843 | 0.0392 | <.0001 | 0.0033 | 0.0172 | 0.8514 | 0.3842 | 0.0993 | 0.0001 |
| max(0,9-unemp_rate) | 0.1044 | 0.0144 | <.0001 | 0.0809 | 0.0375 | 0.0312 | -0.0108 | 0.0170 | 0.5246 | -0.3421 | 0.0989 | 0.0005 |
| max(0,unemp_rate-7) | -0.0652 | 0.0036 | <.0001 | -0.1160 | 0.0144 | <.0001 | -0.0010 | 0.0031 | 0.7377 | -0.3296 | 0.0117 | <.0001 |
| max(0,unemp_rate-3) | 0.0428 | 0.0151 | 0.0046 | -0.0387 | 0.0399 | 0.3321 | 0.0147 | 0.0177 | 0.4058 | -0.4447 | 0.1012 | <.0001 |
| max(0,unemp_rate-5.5) | 0.0176 | 0.0034 | <.0001 | -0.0121 | 0.0120 | 0.3115 | -0.0192 | 0.0034 | <.0001 | 0.2659 | 0.0135 | <.0001 |
| max(0,mtmltv-95) | 0.1050 | 0.0062 | <.0001 | -0.5230 | 0.0079 | <.0001 | -0.0499 | 0.0063 | <.0001 | 0.3166 | 0.1099 | 0.0040 |
| max(0,95-mtmltv) | -0.0893 | 0.0062 | <.0001 | 0.5413 | 0.0074 | <.0001 | 0.0493 | 0.0063 | <.0001 | -0.3412 | 0.1099 | 0.0019 |
| max(0,mtmltv-50) | -0.0030 | 0.0003 | <.0001 | -0.0220 | 0.0009 | <.0001 | 0.0048 | 0.0003 | <.0001 | 0.0150 | 0.0020 | <.0001 |
| max(0,mtmltv-80) | -0.0034 | 0.0003 | <.0001 | -0.0439 | 0.0015 | <.0001 | 0.0008 | 0.0002 | 0.0008 | -0.0098 | 0.0010 | <.0001 |
| max(0,mtmltv-30) | -0.0014 | 0.0006 | 0.0145 | 0.0164 | 0.0015 | <.0001 | -0.0002 | 0.0006 | 0.7144 | 0.0026 | 0.0052 | 0.6181 |
| max(0,mtmltv-140) | 0.0037 | 0.0003 | <.0001 | 0.0744 | 0.0042 | <.0001 | -0.0030 | 0.0002 | <.0001 | -0.0088 | 0.0006 | <.0001 |
| max(0,mtmltv-5) | -0.0933 | 0.0064 | <.0001 | 0.5057 | 0.0081 | <.0001 | 0.0491 | 0.0065 | <.0001 | -0.3118 | 0.1111 | 0.0050 |
| Refi Incentive with 2 months lag | -0.0424 | 0.0015 | <.0001 | 0.0501 | 0.0053 | <.0001 | 0.0878 | 0.0014 | <.0001 | -0.1170 | 0.0053 | <.0001 |
| January Indicator | -0.0653 | 0.0037 | <.0001 | -0.2157 | 0.0136 | <.0001 | 0.0175 | 0.0032 | <.0001 | -0.0720 | 0.0133 | <.0001 |
| February Indicator | 0.0726 | 0.0036 | <.0001 | -0.2354 | 0.0137 | <.0001 | 0.0652 | 0.0032 | <.0001 | -0.0617 | 0.0134 | <.0001 |
| March Indicator | 0.2450 | 0.0036 | <.0001 | -0.0104 | 0.0132 | 0.4312 | 0.0913 | 0.0032 | <.0001 | 0.0526 | 0.0133 | <.0001 |
| April Indicator | 0.1139 | 0.0037 | <.0001 | -0.0265 | 0.0136 | 0.0511 | 0.1107 | 0.0032 | <.0001 | 0.0723 | 0.0134 | <.0001 |
| May Indicator | 0.0906 | 0.0038 | <.0001 | 0.0057 | 0.0136 | 0.6766 | 0.0670 | 0.0033 | <.0001 | 0.0403 | 0.0136 | 0.0031 |
| June Indicator | 0.0774 | 0.0038 | <.0001 | 0.0336 | 0.0136 | 0.0135 | 0.0360 | 0.0033 | <.0001 | 0.1736 | 0.0132 | <.0001 |
| July Indicator | 0.0276 | 0.0038 | <.0001 | -0.0032 | 0.0137 | 0.8169 | 0.0285 | 0.0033 | <.0001 | 0.1684 | 0.0132 | <.0001 |
| August Indicator | 0.0360 | 0.0038 | <.0001 | 0.0567 | 0.0134 | <.0001 | 0.0100 | 0.0033 | 0.0018 | 0.1775 | 0.0131 | <.0001 |
| September Indicator | -0.0694 | 0.0038 | <.0001 | -0.0677 | 0.0137 | <.0001 | 0.0217 | 0.0033 | <.0001 | 0.1987 | 0.0129 | <.0001 |
| October Indicator | -0.0281 | 0.0037 | <.0001 | -0.0522 | 0.0135 | 0.0001 | 0.0051 | 0.0033 | 0.1153 | 0.1619 | 0.0129 | <.0001 |
| November Indicator | -0.0948 | 0.0038 | <.0001 | -0.1318 | 0.0137 | <.0001 | 0.0340 | 0.0032 | <.0001 | 0.0442 | 0.0132 | 0.0008 |

**Table 17. Segment: NPL - sdq, Enterprise 1**
| | <div style="text-align:center">Event: RPL</div> | | | <div style="text-align:center">Event: Prepay</div> | | | <div style="text-align:center">Event: LDQ</div> | | | <div style="text-align:center">Event: DDQ</div> | | | <div style="text-align:center">Event: Default</div> | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Variable Name** | **Estimate** | **StdErr** | **Probt** | **Estimate** | **StdErr** | **Probt** | **Estimate** | **StdErr** | **Probt** | **Estimate** | **StdErr** | **Probt** | **Estimate** | **StdErr** | **Probt** |
| Intercept | 16.6756 | 1.2717 | <.0001 | -30.9422 | 0.9585 | <.0001 | 5.6129 | 1.9049 | 0.0032 | -8.9694 | 0.8138 | <.0001 | 35.3743 | 5.5355 | <.0001 |
| Refinance Rate | 0.0033 | 0.0033 | 0.3178 | -0.3529 | 0.0092 | <.0001 | -0.0990 | 0.0061 | <.0001 | 0.0283 | 0.0025 | <.0001 | 0.0829 | 0.0039 | <.0001 |
| Cash Out | 0.0657 | 0.0031 | <.0001 | -0.4150 | 0.0091 | <.0001 | -0.1570 | 0.0059 | <.0001 | 0.0367 | 0.0023 | <.0001 | -0.0078 | 0.0038 | 0.0421 |
| Investment | -0.3347 | 0.0062 | <.0001 | -0.0523 | 0.0151 | 0.0005 | 0.6132 | 0.0124 | <.0001 | 0.1347 | 0.0036 | <.0001 | 0.3415 | 0.0052 | <.0001 |
| Second Home | -0.2342 | 0.0090 | <.0001 | 0.0909 | 0.0228 | <.0001 | -0.4421 | 0.0193 | <.0001 | 0.0751 | 0.0054 | <.0001 | 0.3674 | 0.0077 | <.0001 |
| Age | 0.0076 | 0.0001 | <.0001 | -0.0212 | 0.0003 | <.0001 | 0.0051 | 0.0002 | <.0001 | 0.0059 | 0.0001 | <.0001 | -0.0058 | 0.0002 | <.0001 |
| Age Sq. | 0.0000 | | <.0001 | 0.0000 | | <.0001 | -0.0001 | | <.0001 | 0.0000 | | <.0001 | 0.0000 | | <.0001 |
| Current UPB (000s) | 0.0027 | 0.0000 | <.0001 | 0.0057 | 0.0002 | <.0001 | -0.0016 | 0.0001 | <.0001 | 0.0001 | 0.0000 | 0.0533 | -0.0070 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | -0.0324 | | <.0001 | -0.0810 | | <.0001 | 0.0202 | | <.0001 | 0.0034 | | 0.0003 | 0.0852 | | <.0001 |
| Debt to Income Ratio | -0.0001 | 0.0001 | 0.7406 | -0.0005 | 0.0011 | 0.6163 | 0.0001 | 0.0002 | 0.7530 | 0.0001 | 0.0001 | 0.4039 | -0.0008 | 0.0005 | 0.2542 |
| Credit Score | -0.0017 | 0.0000 | <.0001 | 0.0033 | 0.0001 | <.0001 | -0.0029 | 0.0001 | <.0001 | 0.0002 | 0.0000 | <.0001 | 0.0054 | 0.0000 | <.0001 |
| Burnout Count | 0.0053 | 0.0001 | <.0001 | 0.0042 | 0.0003 | <.0001 | 0.0008 | 0.0002 | <.0001 | -0.0013 | 0.0001 | <.0001 | 0.0032 | 0.0001 | <.0001 |
| Sato F30 | -0.0321 | 0.0019 | <.0001 | 0.0058 | 0.0060 | 0.3373 | -0.0029 | 0.0036 | 0.4257 | 0.0219 | 0.0013 | <.0001 | -0.0135 | 0.0020 | <.0001 |
| Judicial State | -0.2060 | 0.0025 | <.0001 | -0.2565 | 0.0072 | <.0001 | -0.3897 | 0.0047 | <.0001 | 0.2737 | 0.0019 | <.0001 | -1.2323 | 0.0035 | <.0001 |
| 2005-2008 Indicator | -0.0739 | 0.0038 | <.0001 | -0.5323 | 0.0105 | <.0001 | -0.1317 | 0.0066 | <.0001 | 0.0343 | 0.0030 | <.0001 | -0.4189 | 0.0047 | <.0001 |
| 2009-2013 Indicator | -0.1849 | 0.0057 | <.0001 | -0.3401 | 0.0128 | <.0001 | -0.4327 | 0.0119 | <.0001 | 0.1120 | 0.0049 | <.0001 | -0.6318 | 0.0075 | <.0001 |
| >2014 Indicator | 0.5715 | 0.0086 | <.0001 | -0.6681 | 0.0201 | <.0001 | -0.1758 | 0.0184 | <.0001 | 0.0127 | 0.0095 | 0.1824 | -1.1761 | 0.0160 | <.0001 |
| No Full Doc Loan | -0.0631 | 0.0041 | <.0001 | -0.1695 | 0.0134 | <.0001 | 0.0011 | 0.0080 | 0.8922 | 0.0464 | 0.0028 | <.0001 | -0.1628 | 0.0045 | <.0001 |
| Fixed Rate Mortgage 40 YR | 0.3505 | 0.0136 | <.0001 | -0.2602 | 0.0848 | 0.0022 | 0.2466 | 0.0260 | <.0001 | -0.0391 | 0.0092 | <.0001 | -0.4364 | 0.0164 | <.0001 |
| Fixed Rate Mortgage 30 YR | 0.2950 | 0.0049 | <.0001 | -0.0302 | 0.0147 | 0.0405 | 0.3320 | 0.0091 | <.0001 | -0.0583 | 0.0031 | <.0001 | -0.1406 | 0.0048 | <.0001 |
| Fixed Rate Mortgage 15 YR | 0.4832 | 0.0065 | <.0001 | -0.0696 | 0.0168 | <.0001 | 0.0917 | 0.0119 | <.0001 | -0.0434 | 0.0049 | <.0001 | -0.2105 | 0.0084 | <.0001 |
| Non Fixed Rate Mortgage| 0.0000 | | | 0.0000 | | | 0.0000 | | | 0.0000 | | | 0.0000 | | |
| One Borrower Indicator| 0.1320 | 0.0271 | <.0001 | 0.1154 | 0.0778 | 0.1381 | -0.0153 | 0.0485 | 0.7532 | 0.0203 | 0.0213 | 0.3409 | 0.4902 | 0.0351 | <.0001 |
| Credit Score x One Borrower (00s) | -0.0210 | 0.0000 | <.0001 | -0.0320 | 0.0001 | 0.0053 | -0.0140 | 0.0001 | 0.0549 | 0.0062 | 0.0000 | 0.0506 | -0.0860 | 0.0001 | <.0001 |
| Junior Lien Indicator| -0.1586 | 0.0041 | <.0001 | -0.2907 | 0.0135 | <.0001 | -0.0860 | 0.0079 | <.0001 | 0.0485 | 0.0028 | <.0001 | 0.1213 | 0.0043 | <.0001 |
| Alta Loan Indicator | -0.0606 | 0.0035 | <.0001 | -0.0875 | 0.0120 | <.0001 | -0.0156 | 0.0065 | 0.0170 | -0.0161 | 0.0025 | <.0001 | -0.0007 | 0.0040 | 0.8641 |
| IO Loan Indicator | 0.0000 | | | 0.0000 | | | | | | 0.0000 | | | 0.0000 | | |
| Jumbo Loan Indicator| 0.1093 | 0.0279 | <.0001 | 0.2486 | 0.0795 | 0.0018 | -0.0996 | 0.0791 | 0.2080 | -0.0850 | 0.0314 | 0.0069 | -0.5216 | 0.0713 | <.0001 |
| max(0,unemp_rate-9)| -0.0263 | 0.0269 | 0.3281 | 0.0747 | 0.0489 | 0.1265 | -0.1735 | 0.0505 | 0.0006 | 0.0194 | 0.0297 | 0.5143 | 0.1608 | 0.0484 | 0.0009 |
| max(0,9-unemp_rate)| 0.0673 | 0.0266 | 0.0114 | -0.9281 | 0.0470 | <.0001 | 0.1901 | 0.0500 | 0.0001 | -0.0424 | 0.0296 | 0.1517 | -0.0981 | 0.0482 | 0.0417 |
| max(0,unemp_rate-7)| -0.0606 | 0.0056 | <.0001 | -0.0731 | 0.0174 | <.0001 | 0.0207 | 0.0104 | 0.0462 | 0.0020 | 0.0043 | 0.6386 | -0.0071 | 0.0067 | 0.2932 |
| max(0,unemp_rate-3)| 0.0686 | 0.0277 | 0.0134 | 0.0123 | 0.0501 | 0.8054 | 0.3365 | 0.0521 | <.0001 | -0.0050 | 0.0305 | 0.8693 | -0.2205 | 0.0495 | <.0001 |
| max(0,unemp_rate-5.5)| 0.1326 | 0.0058 | <.0001 | 0.0167 | 0.0149 | 0.2622 | 0.0229 | 0.0107 | 0.0328 | -0.0118 | 0.0050 | 0.0176 | 0.0032 | 0.0074 | 0.6684 |
| max(0,mtmltv-95) | 0.2012 | 0.0128 | <.0001 | -0.2488 | 0.0105 | <.0001 | 0.0876 | 0.0208 | <.0001 | -0.0672 | 0.0087 | <.0001 | -0.4544 | 0.0613 | <.0001 |
| max(0,95-mtmltv) | -0.2086 | 0.0128 | <.0001 | 0.3025 | 0.0100 | <.0001 | -0.0865 | 0.0208 | <.0001 | 0.0669 | 0.0087 | <.0001 | -0.4593 | 0.0613 | <.0001 |
| max(0,mtmltv-50) | 0.0070 | 0.0005 | <.0001 | -0.0270 | 0.0011 | <.0001 | -0.0096 | 0.0009 | <.0001 | 0.0022 | 0.0005 | <.0001 | 0.0027 | 0.0010 | 0.0072 |
| max(0,mtmltv-80) | 0.0124 | 0.0004 | <.0001 | -0.0566 | 0.0019 | <.0001 | -0.0026 | 0.0008 | 0.0011 | -0.0002 | 0.0003 | 0.4985 | -0.0119 | 0.0005 | <.0001 |
| max(0,mtmltv-30) | -0.0048 | 0.0010 | <.0001 | 0.0100 | 0.0018 | <.0001 | 0.0016 | 0.0019 | 0.3976 | 0.0026 | 0.0010 | 0.0074 | -0.0065 | 0.0026 | 0.0127 |
| max(0,mtmltv-140) | -0.0013 | 0.0003 | <.0001 | 0.0429 | 0.0084 | <.0001 | 0.0077 | 0.0009 | <.0001 | -0.0016 | 0.0002 | <.0001 | -0.0091 | 0.0003 | <.0001 |
| max(0,mtmltv-5) | -0.2152 | 0.0131 | <.0001 | 0.2664 | 0.0107 | <.0001 | -0.0887 | 0.0213 | <.0001 | 0.0658 | 0.0091 | <.0001 | -0.4255 | 0.0618 | <.0001 |
| Refi Incentive with 2 months lag | -0.0192 | 0.0025 | <.0001 | 0.0150 | 0.0067 | 0.0243 | -0.1488 | 0.0045 | <.0001 | 0.0687 | 0.0020 | <.0001 | -0.0896 | 0.0031 | <.0001 |
| January Indicator | -0.0760 | 0.0061 | <.0001 | -0.1876 | 0.0133 | <.0001 | -0.2978 | 0.0114 | <.0001 | 0.0301 | 0.0045 | <.0001 | 0.0027 | 0.0075 | 0.7224 |
| February Indicator | 0.1167 | 0.0061 | <.0001 | -0.1641 | 0.0136 | <.0001 | -0.1116 | 0.0110 | <.0001 | -0.0221 | 0.0046 | <.0001 | 0.1002 | 0.0073 | <.0001 |
| March Indicator | 0.1060 | 0.0058 | <.0001 | 0.0577 | 0.0160 | 0.0003 | -0.0796 | 0.0105 | <.0001 | -0.0367 | 0.0045 | <.0001 | 0.0944 | 0.0073 | <.0001 |
| April Indicator | 0.0549 | 0.0059 | <.0001 | 0.0618 | 0.0168 | 0.0002 | 0.0978 | 0.0104 | <.0001 | -0.0267 | 0.0045 | <.0001 | 0.0782 | 0.0073 | <.0001 |
| May Indicator | 0.0912 | 0.0058 | <.0001 | 0.1339 | 0.0166 | <.0001 | 0.0223 | 0.0106 | 0.0361 | 0.0200 | 0.0045 | <.0001 | -0.0980 | 0.0073 | <.0001 |
| June Indicator | 0.0347 | 0.0059 | <.0001 | 0.1008 | 0.0168 | <.0001 | -0.1237 | 0.0111 | <.0001 | 0.0646 | 0.0045 | <.0001 | 0.1981 | 0.0072 | <.0001 |
| July Indicator | 0.0629 | 0.0059 | <.0001 | 0.0832 | 0.0170 | <.0001 | -0.0379 | 0.0109 | <.0001 | 0.1034 | 0.0045 | <.0001 | 0.2259 | 0.0072 | <.0001 |
| August Indicator | 0.1695 | 0.0059 | <.0001 | 0.0849 | 0.0172 | <.0001 | -0.0710 | 0.0111 | <.0001 | 0.1499 | 0.0045 | <.0001 | 0.1897 | 0.0073 | <.0001 |
| September Indicator| 0.0092 | 0.0061 | 0.1329 | -0.0146 | 0.0177 | 0.4083 | -0.0681 | 0.0112 | <.0001 | 0.1645 | 0.0045 | <.0001 | 0.1346 | 0.0074 | <.0001 |
| October Indicator | -0.0180 | 0.0061 | 0.0033 | 0.0288 | 0.0175 | 0.0996 | 0.1142 | 0.0113 | <.0001 | 0.1356 | 0.0045 | <.0001 | 0.0828 | 0.0075 | <.0001 |
| November Indicator| -0.0849 | 0.0062 | <.0001 | -0.0743 | 0.0178 | <.0001 | -0.1632 | 0.0114 | <.0001 | 0.0564 | 0.0045 | <.0001 | -0.0307 | 0.0076 | <.0001 |

**Table 18. Segment: NPL - ddq, Enterprise 1**

| | <div style="text-align:center">Event: RPL</div> | | | <div style="text-align:center">Event: Prepay</div> | | | <div style="text-align:center">Event: LDQ</div> | | | <div style="text-align:center">Event: SDQ</div> | | | <div style="text-align:center">Event: Default</div> | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Variable Name** | **Est** | **StdErr** | **Probt** | **Est** | **StdErr** | **Probt** | **Est** | **StdErr** | **Probt** | **Est** | **StdErr** | **Probt** | **Est** | **StdErr** | **Probt** |
| Intercept | 18.8560 | 1.8057 | <.0001 | -16.5612 | 1.0897 | <.0001 | 8.7375 | 4.8591 | 0.0721 | 10.6596 | 2.5967 | <.0001 | 52.4906 | 3.1662 | <.0001 |
| Refinance Rate | 0.2346 | 0.0049 | <.0001 | -0.3538 | 0.0130 | <.0001 | 0.0733 | 0.0204 | 0.0003 | -0.1793 | 0.0192 | <.0001 | 0.0998 | 0.0031 | <.0001 |
| Cash Out | 0.3106 | 0.0043 | <.0001 | -0.4448 | 0.0124 | <.0001 | 0.0793 | 0.0183 | <.0001 | -0.2546 | 0.0093 | <.0001 | 0.0203 | 0.0029 | <.0001 |
| Investment | -0.4878 | 0.0090 | <.0001 | -0.1424 | 0.0199 | <.0001 | -0.3424 | 0.0346 | <.0001 | -0.8104 | 0.0197 | <.0001 | 0.0431 | 0.0041 | <.0001 |
| Second Home | -0.5013 | 0.0134 | <.0001 | 0.0974 | 0.0292 | <.0001 | 0.5497 | 0.0584 | <.0001 | -0.7962 | 0.0338 | <.0001 | 0.1400 | 0.0061 | <.0001 |
| Age | 0.0043 | 0.0002 | <.0001 | -0.0256 | 0.0004 | <.0001 | -0.0077 | 0.0008 | <.0001 | -0.0175 | 0.0004 | <.0001 | -0.0093 | 0.0001 | <.0001 |
| Age Sq. | 0.0000 | | <.0001 | 0.0000 | | <.0001 | 0.0000 | | <.0001 | 0.0000 | | <.0001 | 0.0000 | | <.0001 |
| Current UPB (000s) | 0.0008 | 0.0001 | 0.1952 | 0.0040 | 0.0002 | <.0001 | -0.0073 | 0.0002 | <.0001 | -0.0045 | 0.0001 | <.0001 | -0.0043 | 0.0000 | <.0001 |
| Current UPB (00000s) Sq. | 0.0536 | | <.0001 | -0.0788 | | <.0001 | 0.0697 | | <.0001 | 0.0660 | | <.0001 | 0.0599 | | <.0001 |
| Debt to Income Ratio| 0.0000 | 0.0001 | 0.7681 | -0.0004 | 0.0008 | 0.6460 | -0.0006 | 0.0028 | 0.8220 | 0.0010 | 0.0024 | 0.6805 | 0.0001 | 0.0001 | 0.4625 |
| Credit Score | -0.0023 | 0.0001 | <.0001 | 0.0017 | 0.0001 | <.0001 | -0.0034 | 0.0002 | <.0001 | -0.0032 | 0.0001 | <.0001 | 0.0027 | 0.0000 | <.0001 |
| Burnout Count | -0.0001 | 0.0002 | 0.7457 | 0.0055 | 0.0003 | <.0001 | 0.0028 | 0.0007 | <.0001 | 0.0040 | 0.0003 | <.0001 | 0.0038 | 0.0001 | <.0001 |
| Sato F30 | -0.0297 | 0.0023 | <.0001 | -0.0137 | 0.0078 | 0.0787 | -0.0468 | 0.0097 | <.0001 | -0.0542 | 0.0052 | <.0001 | -0.0110 | 0.0015 | <.0001 |
| Judicial State | -0.6347 | 0.0036 | <.0001 | 0.3887 | 0.0098 | <.0001 | -0.7894 | 0.0152 | <.0001 | -0.7971 | 0.0075 | <.0001 | -0.4259 | 0.0024 | <.0001 |
| 2005-2008 Indicator | -0.5926 | 0.0064 | <.0001 | -0.4850 | 0.0145 | <.0001 | -0.3659 | 0.0255 | <.0001 | -0.3575 | 0.0112 | <.0001 | -0.1251 | 0.0039 | <.0001 |
| 2009-2013 Indicator | -0.1970 | 0.0094 | <.0001 | -0.4294 | 0.0188 | <.0001 | -0.5544 | 0.0438 | <.0001 | -0.8599 | 0.0216 | <.0001 | -0.2336 | 0.0065 | <.0001 |
| >2014 Indicator | 0.3287 | 0.0195 | <.0001 | -0.4396 | 0.0330 | <.0001 | 0.0554 | 0.0716 | 0.4391 | -0.6152 | 0.0389 | <.0001 | -0.4401 | 0.0152 | <.0001 |
| No Full Doc Loan | -0.0962 | 0.0053 | <.0001 | -0.2299 | 0.0177 | <.0001 | -0.0543 | 0.0228 | 0.0171 | 0.1124 | 0.0122 | <.0001 | -0.0982 | 0.0033 | <.0001 |
| Fixed Rate Mortgage 40 YR | 0.0998 | 0.0166 | <.0001 | -0.2664 | 0.1034 | 0.0100 | 0.1488 | 0.0663 | 0.0247 | 0.1323 | 0.0385 | 0.0006 | -0.2132 | 0.0115 | <.0001 |
| Fixed Rate Mortgage 30 YR | 0.3743 | 0.0063 | <.0001 | -0.0547 | 0.0197 | 0.0055 | 0.2284 | 0.0262 | <.0001 | 0.1351 | 0.0137 | <.0001 | -0.0785 | 0.0037 | <.0001 |
| Fixed Rate Mortgage 15 YR | 0.8344 | 0.0092 | <.0001 | 0.1141 | 0.0220 | <.0001 | 0.3971 | 0.0383 | <.0001 | -0.0392 | 0.0188 | 0.0375 | -0.1330 | 0.0063 | <.0001 |
| Non Fixed Rate Mortgage| 0.0000 | | | 0.0000 | | | 0.0000 | | | 0.0000 | | | 0.0000 | | |
| One Borrower Indicator| 0.4370 | 0.0402 | <.0001 | -0.2269 | 0.1056 | 0.0316 | 0.0503 | 0.1634 | 0.7581 | -0.0965 | 0.0783 | 0.2179 | 0.3103 | 0.0276 | <.0001 |
| Credit Score x One Borrower (00s) | -0.0680 | 0.0001 | <.0001 | 0.0146 | 0.0002 | 0.3483 | -0.0210 | 0.0002 | 0.3855 | -0.0070 | 0.0001 | 0.5371 | -0.0610 | 0.0000 | <.0001 |
| Junior Lien Indicator| -0.0704 | 0.0054 | <.0001 | -0.2327 | 0.0178 | <.0001 | -0.0609 | 0.0230 | 0.0081 | 0.1238 | 0.0123 | <.0001 | 0.0630 | 0.0033 | <.0001 |
| Alta Loan Indicator | -0.1088 | 0.0047 | <.0001 | -0.0998 | 0.0165 | <.0001 | -0.0803 | 0.0156 | <.0001 | 0.0275 | 0.0101 | 0.0063 | -0.0130 | 0.0030 | <.0001 |
| IO Loan Indicator | 0.0000 | | | 0.0000 | | | 0.0000 | | | 0.0000 | | | 0.0000 | | |
| Jumbo Loan Indicator| -0.6877 | 0.0487 | <.0001 | 0.2675 | 0.0983 | 0.0064 | -0.7801 | 0.3426 | 0.0227 | -0.2903 | 0.1381 | 0.0355 | -0.3879 | 0.0546 | <.0001 |
| max(0,unemp_rate-9)| -0.0362 | 0.0510 | 0.4774 | 0.3329 | 0.0712 | <.0001 | -0.1425 | 0.2071 | 0.4914 | 0.1689 | 0.0870 | 0.0522 | 0.6186 | 0.0371 | <.0001 |
| max(0,9-unemp_rate)| -0.0306 | 0.0507 | 0.5466 | -0.1006 | 0.0690 | 0.1446 | -0.1825 | 0.2058 | 0.3750 | 0.2158 | 0.0863 | 0.0123 | 0.4683 | 0.0369 | <.0001 |
| max(0,unemp_rate-7)| 0.0431 | 0.0079 | <.0001 | -0.0827 | 0.0231 | 0.0003 | 0.1143 | 0.0337 | 0.0007 | 0.0344 | 0.0166 | 0.0379 | 0.0978 | 0.0051 | <.0001 |
| max(0,unemp_rate-3)| -0.1382 | 0.0523 | 0.0082 | -0.5335 | 0.0730 | <.0001 | -0.3797 | 0.2130 | 0.0746 | 0.0869 | 0.0898 | 0.3335 | -0.6186 | 0.0379 | <.0001 |
| max(0,unemp_rate-5.5)| 0.0607 | 0.0088 | <.0001 | 0.1389 | 0.0203 | <.0001 | 0.3058 | 0.0383 | <.0001 | 0.0992 | 0.0178 | <.0001 | 0.0515 | 0.0055 | <.0001 |
| max(0,mtmltv-95) | 0.2209 | 0.0197 | <.0001 | -0.1008 | 0.0116 | <.0001 | 0.1031 | 0.0517 | 0.0461 | 0.1299 | 0.0280 | <.0001 | 0.5955 | 0.0350 | <.0001 |
| max(0,95-mtmltv) | -0.2370 | 0.0197 | <.0001 | 0.1783 | 0.0108 | <.0001 | 0.1107 | 0.0516 | 0.0320 | -0.1285 | 0.0280 | <.0001 | -0.6350 | 0.0350 | <.0001 |
| max(0,mtmltv-50) | 0.0183 | 0.0008 | <.0001 | -0.0351 | 0.0014 | <.0001 | 0.0062 | 0.0036 | 0.0879 | -0.0114 | 0.0016 | <.0001 | -0.0074 | 0.0007 | <.0001 |
| max(0,mtmltv-80) | 0.0204 | 0.0007 | <.0001 | -0.0377 | 0.0029 | <.0001 | 0.0177 | 0.0028 | <.0001 | 0.0029 | 0.0013 | 0.0290 | -0.0098 | 0.0004 | <.0001 |
| max(0,mtmltv-30) | -0.0125 | 0.0017 | <.0001 | -0.0025 | 0.0021 | 0.2302 | 0.0089 | 0.0065 | 0.1690 | -0.0006 | 0.0031 | 0.8535 | -0.0041 | 0.0016 | 0.0083 |
| max(0,mtmltv-140) | -0.0058 | 0.0008 | <.0001 | 0.0255 | 0.0060 | <.0001 | 0.0003 | 0.0013 | 0.8002 | 0.0043 | 0.0011 | 0.0001 | -0.0018 | 0.0002 | <.0001 |
| max(0,mtmltv-5) | -0.2332 | 0.0201 | <.0001 | 0.1432 | 0.0117 | <.0001 | 0.1282 | 0.0528 | 0.0152 | -0.1317 | 0.0290 | <.0001 | -0.5644 | 0.0353 | <.0001 |
| Refi Incentive with 2 months lag | -0.0883 | 0.0038 | <.0001 | -0.1512 | 0.0095 | <.0001 | -0.2687 | 0.0159 | <.0001 | -0.2354 | 0.0076 | <.0001 | -0.1529 | 0.0024 | <.0001 |
| January Indicator | -0.0463 | 0.0086 | <.0001 | -0.2107 | 0.0245 | <.0001 | -0.0615 | 0.0381 | 0.1063 | -0.2024 | 0.0184 | <.0001 | -0.1233 | 0.0056 | <.0001 |
| February Indicator | -0.1207 | 0.0088 | <.0001 | -0.1951 | 0.0243 | <.0001 | -0.0601 | 0.0378 | 0.1110 | -0.1500 | 0.0180 | <.0001 | -0.1246 | 0.0057 | <.0001 |
| March Indicator | 0.1011 | 0.0083 | <.0001 | -0.0046 | 0.0232 | 0.8442 | 0.0916 | 0.0365 | 0.0120 | -0.0145 | 0.0174 | 0.4048 | -0.0346 | 0.0055 | <.0001 |
| April Indicator | 0.0186 | 0.0085 | 0.0284 | -0.0325 | 0.0232 | 0.4211 | 0.1510 | 0.0359 | <.0001 | 0.0414 | 0.0172 | 0.0160 | -0.0135 | 0.0054 | 0.0129 |
| May Indicator | -0.0026 | 0.0085 | 0.7591 | 0.0918 | 0.0226 | <.0001 | 0.3103 | 0.0347 | <.0001 | 0.2227 | 0.0165 | <.0001 | 0.0127 | 0.0056 | <.0001 |
| June Indicator | -0.0727 | 0.0087 | <.0001 | 0.0581 | 0.0228 | 0.0107 | -0.0732 | 0.0379 | 0.0535 | -0.1397 | 0.0180 | <.0001 | 0.0273 | 0.0054 | <.0001 |
| July Indicator | -0.0364 | 0.0086 | <.0001 | 0.0429 | 0.0228 | 0.0602 | 0.0381 | 0.0370 | 0.3026 | -0.0298 | 0.0177 | 0.0909 | 0.0436 | 0.0054 | <.0001 |
| August Indicator | 0.1556 | 0.0082 | <.0001 | 0.0766 | 0.0226 | 0.0007 | 0.2189 | 0.0354 | <.0001 | 0.0208 | 0.0174 | 0.2313 | 0.0334 | 0.0054 | <.0001 |
| September Indicator| 0.1108 | 0.0083 | <.0001 | 0.0223 | 0.0231 | 0.3347 | -0.0645 | 0.0367 | 0.0784 | 0.1248 | 0.0178 | <.0001 | 0.0414 | 0.0053 | <.0001 |
| October Indicator | 0.1180 | 0.0083 | <.0001 | 0.0116 | 0.0229 | 0.6110 | 0.1662 | 0.0368 | <.0001 | 0.1210 | 0.0178 | <.0001 | 0.0687 | 0.0054 | <.0001 |
| November Indicator| 0.0457 | 0.0084 | <.0001 | -0.1258 | 0.0236 | <.0001 | 0.1280 | 0.0362 | 0.0004 | -0.1240 | 0.0181 | <.0001 | 0.0694 | 0.0056 | <.0001 |

**Table 19. Segment: F30 Performing, Enterprise 2, Event: Idq**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -45.5872 | 2.0991 | <.0001 |
| Refinance Rate | 0.0033 | 0.0947 | 0.9721 |
| Cash Out | 0.2724 | 0.0944 | 0.0039 |
| Investment | -0.1811 | 0.0510 | 0.0004 |
| Second Home | -0.1413 | 0.0619 | 0.0224 |
| Age | 0.0534 | 0.0018 | <.0001 |
| Age Sq. | -0.0003 | 0.0000 | <.0001 |
| Age (Years) Cb. | 0.0016 | 0.0000 | <.0001 |
| Current UPB (000s) | 0.0006 | 0.0004 | 0.1658 |
| Current UPB (00000s) Sq. | 0.0094 | 0.0000 | <.0001 |
| Credit Score | 0.0171 | 0.0027 | <.0001 |
| Credit Sq (0s) Sq. | -0.0020 | 0.0000 | <.0001 |
| Sato F30 | 0.3249 | 0.0272 | <.0001 |
| Burnout Count | 0.0055 | 0.0009 | <.0001 |
| Unemployment Rate | 0.0862 | 0.0076 | <.0001 |
| Unemployment Burnout Count, 8% | -0.2195 | 0.0515 | <.0001 |
| Unemployment Burnout Count, 10% | -0.2853 | 0.0672 | <.0001 |
| Unemployment Burnout Count, 12% | -0.6926 | 0.1046 | <.0001 |
| max(0, mtmltv-79) | 0.0313 | 0.0040 | <.0001 |
| max(0, 79-mtmltv) | -0.0163 | 0.0016 | <.0001 |
| max(0, mtmltv-154) | -0.0141 | 0.0044 | 0.0014 |
| max(0, mtmltv-90) | -0.0129 | 0.0068 | 0.0594 |
| max(0, mtmltv-105) | -0.0105 | 0.0049 | 0.0323 |
| max(0,debt_ratio-.60) | -0.9244 | 0.5159 | 0.0732 |
| max(0,.60-debt_ratio) | -1.0222 | 0.3105 | 0.001 |
| max(0,debt_ratio-.30) | 0.7336 | 0.3982 | 0.0654 |
| max(0,debt_ratio-.95) | 0.1900 | 0.2511 | 0.4493 |
| Origination LTV | 0.2525 | 0.1089 | 0.0204 |
| Junior Lien Indicator | 0.3924 | 0.1335 | 0.0033 |
| Orig. LTV x Junior Lien Ind | -0.2363 | 0.1587 | 0.1366 |
| One Borrower Indicator | -1.3313 | 0.2482 | <.0001 |
| Credit Score x One Borrower (00s) | 0.2733 | 0.0004 | <.0001 |
| No Full Doc Loan | -0.0464 | 0.0728 | 0.5234 |
| Third Party Loan | 0.0589 | 0.0374 | 0.115 |
| Judicial State | 0.1063 | 0.0228 | <.0001 |
| Current UPB/Origination UPB | 38.9118 | 1.9622 | <.0001 |
| HPA with 24 month lag | 23.0431 | 1.6340 | <.0001 |
| HPA with lag x Sunk Cost | -26.2402 | 1.7148 | <.0001 |
| MTMLTV x Refinance Rate (00s) | 0.2688 | 0.0011 | 0.0182 |
| MTMLTV x Cash Out (00s) | 0.0355 | 0.0011 | 0.7514 |
| Q1 | -0.1287 | 0.0298 | <.0001 |
| Q2 | -0.3058 | 0.0312 | <.0001 |
| Q3 | -0.1727 | 0.0300 | <.0001 |
| 2005-2008 Indicator | 0.1438 | 0.0373 | 0.0001 |
| 2009-2013 Indicator | -0.5833 | 0.0459 | <.0001 |
| >2014 Indicator | -0.2895 | 0.0567 | <.0001 |

**Table 19. Segment: F30 Performing, Enterprise 2, Event: Idq**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -45.5872 | 2.0991 | <.0001 |
| Refinance Rate | 0.0033 | 0.0947 | 0.9721 |
| Cash Out | 0.2724 | 0.0944 | 0.0039 |
| Investment | -0.1811 | 0.0510 | 0.0004 |
| Second Home | -0.1413 | 0.0619 | 0.0224 |
| Age | 0.0534 | 0.0018 | <.0001 |
| Age Sq. | -0.0003 | 0.0000 | <.0001 |
| Age (Years) Cb. | 0.0016 | 0.0000 | <.0001 |
| Current UPB (000s) | 0.0006 | 0.0004 | 0.1658 |
| Current UPB (00000s) Sq. | 0.0094 | 0.0000 | <.0001 |
| Credit Score | 0.0171 | 0.0027 | <.0001 |
| Credit Sq (0s) Sq. | -0.0020 | 0.0000 | <.0001 |
| Sato F30 | 0.3249 | 0.0272 | <.0001 |
| Burnout Count | 0.0055 | 0.0009 | <.0001 |
| Unemployment Rate | 0.0862 | 0.0076 | <.0001 |
| Unemployment Burnout Count, 8% | -0.2195 | 0.0515 | <.0001 |
| Unemployment Burnout Count, 10% | -0.2853 | 0.0672 | <.0001 |
| Unemployment Burnout Count, 12% | -0.6926 | 0.1046 | <.0001 |
| max(0, mtmltv-79) | 0.0313 | 0.0040 | <.0001 |
| max(0, 79-mtmltv) | -0.0163 | 0.0016 | <.0001 |
| max(0, mtmltv-154) | -0.0141 | 0.0044 | 0.0014 |
| max(0, mtmltv-90) | -0.0129 | 0.0068 | 0.0594 |
| max(0, mtmltv-105) | -0.0105 | 0.0049 | 0.0323 |
| max(0,debt_ratio-.60) | -0.9244 | 0.5159 | 0.0732 |
| max(0,.60-debt_ratio) | -1.0222 | 0.3105 | 0.001 |
| max(0,debt_ratio-.30) | 0.7336 | 0.3982 | 0.0654 |
| max(0,debt_ratio-.95) | 0.1900 | 0.2511 | 0.4493 |
| Origination LTV | 0.2525 | 0.1089 | 0.0204 |
| Junior Lien Indicator | 0.3924 | 0.1335 | 0.0033 |
| Orig. LTV x Junior Lien Ind | -0.2363 | 0.1587 | 0.1366 |
| One Borrower Indicator | -1.3313 | 0.2482 | <.0001 |
| Credit Score x One Borrower (00s) | 0.2733 | 0.0004 | <.0001 |
| No Full Doc Loan | -0.0464 | 0.0728 | 0.5234 |
| Third Party Loan | 0.0589 | 0.0374 | 0.115 |
| Judicial State | 0.1063 | 0.0228 | <.0001 |
| Current UPB/Origination UPB | 38.9118 | 1.9622 | <.0001 |
| HPA with 24 month lag | 23.0431 | 1.6340 | <.0001 |
| HPA with lag x Sunk Cost | -26.2402 | 1.7148 | <.0001 |
| MTMLTV x Refinance Rate (00s) | 0.2688 | 0.0011 | 0.0182 |
| MTMLTV x Cash Out (00s) | 0.0355 | 0.0011 | 0.7514 |
| Q1 | -0.1287 | 0.0298 | <.0001 |
| Q2 | -0.3058 | 0.0312 | <.0001 |
| Q3 | -0.1727 | 0.0300 | <.0001 |
| 2005-2008 Indicator | 0.1438 | 0.0373 | 0.0001 |
| 2009-2013 Indicator | -0.5833 | 0.0459 | <.0001 |
| >2014 Indicator | -0.2895 | 0.0567 | <.0001 |

**Table 20. Segment: F15 Performing, Enterprise 2, Event: Idq**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -20.7634 | 2.0698 | <.0001 |
| Refinance Rate | 0.1922 | 0.1648 | 0.2434 |
| Cash Out | 0.1039 | 0.1682 | 0.5366 |
| Investment | -0.0061 | 0.0877 | 0.9447 |
| Second Home | -0.2122 | 0.1363 | 0.1195 |
| Age | 0.0619 | 0.0034 | <.0001 |
| Age Sq. | -0.0004 | 0.0000 | <.0001 |
| Age (Years) Cb. | 0.0019 | 0.0000 | <.0001 |
| Current UPB (000s) | -0.0048 | 0.0008 | <.0001 |
| Current UPB (00000s) Sq. | 0.1100 | 0.0000 | <.0001 |
| Credit Score | 0.0345 | 0.0055 | <.0001 |
| Credit Sq (0s) Sq. | -0.0040 | 0.0000 | <.0001 |
| Sato F30 | 0.1462 | 0.0441 | 0.0009 |
| Burnout Count | 0.0032 | 0.0013 | 0.0107 |
| Unemployment Rate | 0.1204 | 0.0124 | <.0001 |
| Unemployment Burnout Count, 8% | -0.1604 | 0.0986 | 0.1036 |
| Unemployment Burnout Count, 10% | -0.2110 | 0.1343 | 0.1163 |
| Unemployment Burnout Count, 12% | -0.8154 | 0.1989 | <.0001 |
| max(0, mtmltv-79) | 0.0333 | 0.0126 | 0.0083 |
| max(0, 79-mtmltv) | -0.0224 | 0.0035 | <.0001 |
| max(0, mtmltv-154) | -0.0166 | 0.0185 | 0.3702 |
| max(0, mtmltv-90) | -0.0147 | 0.0254 | 0.5629 |
| max(0, mtmltv-105) | -0.0049 | 0.0217 | 0.8199 |
| max(0,debt_ratio-.60) | -1.2613 | 0.8642 | 0.1444 |
| max(0,.60-debt_ratio) | -0.9564 | 0.4108 | 0.0199 |
| max(0,debt_ratio-.30) | 0.8269 | 0.5891 | 0.1604 |
| max(0,debt_ratio-.95) | 0.3633 | 0.5351 | 0.4972 |
| Origination LTV | -0.0580 | 0.1945 | 0.7656 |
| Junior Lien Indicator | 0.3117 | 0.2093 | 0.1364 |
| Orig. LTV x Junior Lien Ind | -0.2144 | 0.2809 | 0.4452 |
| One Borrower Indicator | -0.4023 | 0.4430 | 0.3639 |
| Credit Score x One Borrower (00s) | 0.1605 | 0.0006 | 0.0123 |
| No Full Doc Loan | -0.0239 | 0.0989 | 0.8089 |
| Third Party Loan | -0.1353 | 0.0862 | 0.1166 |
| Judicial State | 0.1389 | 0.0389 | 0.0004 |
| Current UPB/Origination UPB | 6.1141 | 1.0248 | <.0001 |
| HPA with 24 month lag | 1.8197 | 0.7436 | 0.0144 |
| HPA with lag x Sunk Cost | -3.0296 | 0.9412 | 0.0013 |
| MTMLTV x Refinance Rate (00s) | -0.1210 | 0.0028 | 0.6652 |
| MTMLTV x Cash Out (00s) | 0.4856 | 0.0028 | 0.0871 |
| Q1 | -0.1371 | 0.0503 | 0.0064 |
| Q2 | -0.3880 | 0.0539 | <.0001 |
| Q3 | -0.2791 | 0.0521 | <.0001 |
| 2005-2008 Indicator | 0.3172 | 0.0645 | <.0001 |
| 2009-2013 Indicator | -0.1373 | 0.0699 | 0.0495 |
| >2014 Indicator | 0.4089 | 0.0867 | <.0001 |

**Table 21. Segment: F30 Performing, Enterprise 2, Event: prepay**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -32.9723 | 1.1235 | <.0001 |
| Refinance Rate | 0.1370 | 0.0228 | <.0001 |
| Cash Out | 0.1156 | 0.0269 | <.0001 |
| Investment | -0.3318 | 0.0139 | <.0001 |
| Second Home | -0.1250 | 0.0149 | <.0001 |
| max(0,17-age) | -0.1788 | 0.0055 | <.0001 |
| max(0,age-17) | 0.1719 | 0.0066 | <.0001 |
| max(0,age-7) | -0.1690 | 0.0064 | <.0001 |
| max(0,age-93) | -0.0055 | 0.0006 | <.0001 |
| max(0,age-35) | -0.0066 | 0.0008 | <.0001 |
| Current UPB (000s) | 0.0053 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | -0.0558 | 0.0000 | <.0001 |
| Credit Score | 0.0131 | 0.0012 | <.0001 |
| Credit Sq (0s) Sq. | -0.0008 | 0.0000 | <.0001 |
| Sato F30 | 0.5480 | 0.0082 | <.0001 |
| Unemployment Rate | -0.0515 | 0.0025 | <.0001 |
| Unemployment Burnout Count, 8% | 0.0296 | 0.0149 | 0.0471 |
| Unemployment Burnout Count, 10% | 0.2731 | 0.0198 | <.0001 |
| Unemployment Burnout Count, 12% | 0.1431 | 0.0335 | <.0001 |
| max(0,mtmltv-66) | -0.4772 | 0.0161 | <.0001 |
| max(0,66-mtmltv) | 0.4566 | 0.0160 | <.0001 |
| max(0,mtmltv-30) | 0.0091 | 0.0017 | <.0001 |
| max(0,mtmltv-6) | 0.4024 | 0.0371 | <.0001 |
| max(0,mtmltv-101) | 0.0073 | 0.0016 | <.0001 |
| max(0,mtmltv-9) | 0.0436 | 0.0239 | 0.0679 |
| max(0,debt_ratio-.60) | 0.3195 | 0.1495 | 0.0325 |
| max(0,.60-debt_ratio) | -0.3130 | 0.0639 | <.0001 |
| max(0,debt_ratio-.30) | -0.6965 | 0.0945 | <.0001 |
| max(0,debt_ratio-.95) | 0.3780 | 0.0948 | <.0001 |
| Origination LTV | 0.5204 | 0.0385 | <.0001 |
| Junior Lien Indicator | 0.1909 | 0.0384 | <.0001 |
| Orig. LTV x Junior Lien Ind | -0.2334 | 0.0513 | <.0001 |
| One Borrower Indicator | -0.2152 | 0.0852 | 0.0115 |
| Credit Score x One Borrower (00s) | 0.0153 | 0.0001 | 0.1854 |
| No Full Doc Loan | 0.0437 | 0.0201 | 0.0294 |
| Third Party Loan | 0.0614 | 0.0083 | <.0001 |
| Judicial State | -0.0787 | 0.0062 | <.0001 |
| Current UPB/Origination UPB | -1.6442 | 0.2141 | <.0001 |
| HPA with 24 month lag | 0.0612 | 0.1841 | 0.7395 |
| HPA with lag x Sunk Cost | 0.7873 | 0.1957 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.2720 | 0.0003 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.2890 | 0.0004 | <.0001 |
| Q1 | -0.1068 | 0.0084 | <.0001 |
| Q2 | 0.0218 | 0.0081 | 0.0071 |
| Q3 | 0.0611 | 0.0080 | <.0001 |
| 2005-2008 Indicator | -0.1326 | 0.0124 | <.0001 |
| 2009-2013 Indicator | -0.3752 | 0.0121 | <.0001 |
| >2014 Indicator | -0.3772 | 0.0142 | <.0001 |
| max(0,refi_incentive_level_l2-1.4) | 0.2291 | 0.0493 | <.0001 |
| max(0,1.4-refi_incentive_level_l2) | -0.5061 | 0.0175 | <.0001 |
| max(0,refi_incentive_level_l2-0.02) | 0.8376 | 0.0257 | <.0001 |
| max(0,refi_incentive_level_l2-1.1) | -0.6157 | 0.0489 | <.0001 |
| max(0, brnt_cnt-1) | -0.1933 | 0.0137 | <.0001 |
| max(0, brnt_cnt-8) | 0.1801 | 0.0138 | <.0001 |
| max(0,8-brnt_cnt) | -0.1720 | 0.0124 | <.0001 |
| max(0, brnt_cnt-50) | 0.0061 | 0.0010 | <.0001 |
| max(0, brnt_cnt-74) | 0.0001 | 0.0012 | 0.9056 |
| Indicator for 2001-2003 Refi Boom | 0.6763 | 0.0110 | <.0001 |

**Table 22. Segment: F15 Performing, Enterprise 2, Event: prepay**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -39.4951 | 0.5856 | <.0001 |
| Refinance Rate | 0.0015 | 0.0185 | 0.934 |
| Cash Out | -0.0112 | 0.0201 | 0.5766 |
| Investment | -0.2492 | 0.0160 | <.0001 |
| Second Home | -0.0282 | 0.0164 | 0.0849 |
| max(0,17-age) | -0.2259 | 0.0062 | <.0001 |
| max(0,age-17) | 0.2011 | 0.0074 | <.0001 |
| max(0,age-7) | -0.2077 | 0.0072 | <.0001 |
| max(0,age-93) | -0.0040 | 0.0005 | <.0001 |
| max(0,age-35) | -0.0030 | 0.0008 | 0.0003 |
| Current UPB (000s) | 0.0050 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | -0.0517 | 0.0000 | <.0001 |
| Credit Score | 0.0104 | 0.0013 | <.0001 |
| Credit Sq (0s) Sq. | -0.0007 | 0.0000 | <.0001 |
| Sato F30 | 0.3885 | 0.0071 | <.0001 |
| Unemployment Rate | -0.0459 | 0.0024 | <.0001 |
| Unemployment Burnout Count, 8% | 0.0377 | 0.0151 | 0.0122 |
| Unemployment Burnout Count, 10% | 0.2679 | 0.0219 | <.0001 |
| Unemployment Burnout Count, 12% | 0.1219 | 0.0370 | 0.001 |
| max(0,mtmltv-66) | -0.6012 | 0.0054 | <.0001 |
| max(0,66-mtmltv) | 0.5801 | 0.0053 | <.0001 |
| max(0,mtmltv-30) | 0.0230 | 0.0010 | <.0001 |
| max(0,mtmltv-6) | 0.6431 | 0.0124 | <.0001 |
| max(0,mtmltv-101) | -0.0136 | 0.0053 | 0.0099 |
| max(0,mtmltv-9) | -0.0951 | 0.0084 | <.0001 |
| max(0,debt_ratio-.60) | -0.0183 | 0.1513 | 0.9036 |
| max(0,.60-debt_ratio) | -0.1502 | 0.0513 | 0.0034 |
| max(0,debt_ratio-.30) | -0.3070 | 0.0866 | 0.0004 |
| max(0,debt_ratio-.95) | 0.3255 | 0.1012 | 0.0013 |
| Origination LTV | 1.3643 | 0.0323 | <.0001 |
| Junior Lien Indicator | 0.0805 | 0.0307 | 0.0088 |
| Orig. LTV x Junior Lien Ind | -0.0600 | 0.0478 | 0.2088 |
| One Borrower Indicator | -0.1226 | 0.0931 | 0.1878 |
| Credit Score x One Borrower (00s) | 0.0093 | 0.0001 | 0.4544 |
| No Full Doc Loan | 0.0673 | 0.0152 | <.0001 |
| Third Party Loan | 0.0910 | 0.0103 | <.0001 |
| Judicial State | -0.0317 | 0.0059 | <.0001 |
| Current UPB/Origination UPB | -0.1923 | 0.1103 | 0.0812 |
| HPA with 24 month lag | 0.1148 | 0.0733 | 0.1174 |
| HPA with lag x Sunk Cost | -0.3499 | 0.0930 | 0.0002 |
| MTMLTV x Refinance Rate (00s) | -0.0480 | 0.0004 | 0.216 |
| MTMLTV x Cash Out (00s) | 0.0387 | 0.0004 | 0.3643 |
| Q1 | -0.0792 | 0.0083 | <.0001 |
| Q2 | 0.0500 | 0.0080 | <.0001 |
| Q3 | 0.0745 | 0.0079 | <.0001 |
| 2005-2008 Indicator | -0.0312 | 0.0132 | 0.0178 |
| 2009-2013 Indicator | -0.1745 | 0.0106 | <.0001 |
| >2014 Indicator | -0.3323 | 0.0149 | <.0001 |
| max(0,refi_incentive_level_l2-1.4) | -0.1810 | 0.0497 | 0.0003 |
| max(0,1.4-refi_incentive_level_l2) | -0.3679 | 0.0165 | <.0001 |
| max(0,refi_incentive_level_l2-0.02) | 0.6041 | 0.0243 | <.0001 |
| max(0,refi_incentive_level_l2-1.1) | -0.2241 | 0.0493 | <.0001 |
| max(0, brnt_cnt-1) | -0.1436 | 0.0130 | <.0001 |
| max(0, brnt_cnt-8) | 0.1330 | 0.0130 | <.0001 |
| max(0,8-brnt_cnt) | -0.1410 | 0.0118 | <.0001 |
| max(0, brnt_cnt-50) | 0.0078 | 0.0010 | <.0001 |
| max(0, brnt_cnt-74) | -0.0001 | 0.0010 | 0.9003 |
| Indicator for 2001-2003 Refi Boom | 0.7301 | 0.0102 | <.0001 |

**Table 23. Segment: RPL, Enterprise 2, Event: Idq**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -4.3820 | 0.2636 | <.0001 |
| Refinance Rate | -0.0791 | 0.0188 | <.0001 |
| Cash Out | -0.0659 | 0.0182 | 0.0003 |
| Investment | 0.0579 | 0.0150 | 0.0001 |
| Second Home | -0.0299 | 0.0183 | 0.1033 |
| Age | -0.0273 | 0.0005 | <.0001 |
| Age Sq. | 0.0002 | 0.0000 | <.0001 |
| Age (Years) Cb. | -0.0005 | 0.0000 | <.0001 |
| Current UPB (000s) | -0.0018 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | 0.0214 | 0.0000 | <.0001 |
| Credit Score | 0.0062 | 0.0006 | <.0001 |
| Credit Sq (0s) Sq. | -0.0006 | 0.0000 | <.0001 |
| Sato F30 | 0.0142 | 0.0052 | 0.0069 |
| Burnout Count | -0.0016 | 0.0002 | <.0001 |
| Unemployment Rate | 0.0546 | 0.0019 | <.0001 |
| Unemployment Burnout Count, 8% | -0.2387 | 0.0164 | <.0001 |
| Unemployment Burnout Count, 10% | -0.5476 | 0.0210 | <.0001 |
| Unemployment Burnout Count, 12% | -0.4928 | 0.0269 | <.0001 |
| max(0, mtmltv-79) | 0.0000 | 0.0011 | 0.9738 |
| max(0, 79-mtmltv) | 0.0082 | 0.0004 | <.0001 |
| max(0, mtmltv-154) | 0.0020 | 0.0014 | 0.1566 |
| max(0, mtmltv-90) | -0.0092 | 0.0019 | <.0001 |
| max(0, mtmltv-105) | 0.0042 | 0.0014 | 0.0031 |
| max(0,debt_ratio-.60) | 0.6040 | 0.1256 | <.0001 |
| max(0,.60-debt_ratio) | -0.3839 | 0.0695 | <.0001 |
| max(0,debt_ratio-.30) | -0.8170 | 0.0912 | <.0001 |
| max(0,debt_ratio-.95) | 0.2129 | 0.0690 | 0.002 |
| Origination LTV | 0.4093 | 0.0265 | <.0001 |
| Junior Lien Indicator | 0.0584 | 0.0405 | 0.1495 |
| Orig. LTV x Junior Lien Ind | -0.1210 | 0.0507 | 0.0171 |
| One Borrower Indicator | -0.1879 | 0.0576 | 0.0011 |
| Credit Score x One Borrower (00s) | 0.0403 | 0.0001 | <.0001 |
| No Full Doc Loan | -0.0534 | 0.0138 | 0.0001 |
| Third Party Loan | -0.0012 | 0.0102 | 0.9099 |
| Judicial State | -0.0184 | 0.0054 | 0.0007 |
| Current UPB/Origination UPB | 2.3630 | 0.1744 | <.0001 |
| HPA with 24 month lag | -0.4653 | 0.1506 | 0.002 |
| HPA with lag x Sunk Cost | -1.0048 | 0.1620 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.1700 | 0.0003 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.0680 | 0.0002 | 0.0036 |
| Q1 | -0.0884 | 0.0073 | <.0001 |
| Q2 | -0.1497 | 0.0073 | <.0001 |
| Q3 | -0.0723 | 0.0072 | <.0001 |
| 2005-2008 Indicator | -0.1470 | 0.0086 | <.0001 |
| 2009-2013 Indicator | -0.0741 | 0.0111 | <.0001 |
| >2014 Indicator | -0.3368 | 0.0171 | <.0001 |

**Table 24. Segment: RPL, Enterprise 2, Event: prepay**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -37.6907 | 2.0413 | <.0001 |
| Refinance Rate | 0.0339 | 0.0307 | 0.2701 |
| Cash Out | -0.0027 | 0.0316 | 0.9322 |
| Investment | 0.0899 | 0.0254 | 0.0004 |
| Second Home | 0.1165 | 0.0288 | <.0001 |
| max(0,17-age) | 0.0167 | 0.1750 | 0.924 |
| max(0,age-17) | -0.0607 | 0.1795 | 0.7355 |
| max(0,age-7) | 0.0407 | 0.1793 | 0.8204 |
| max(0,age-93) | 0.0036 | 0.0006 | <.0001 |
| max(0,age-35) | 0.0082 | 0.0025 | 0.0009 |
| Current UPB (000s) | 0.0059 | 0.0002 | <.0001 |
| Current UPB (00000s) Sq. | -0.1000 | 0.0000 | <.0001 |
| Credit Score | -0.0027 | 0.0012 | 0.0202 |
| Credit Sq (0s) Sq. | 0.0003 | 0.0000 | <.0001 |
| Sato F30 | 0.1402 | 0.0096 | <.0001 |
| Unemployment Rate | -0.0804 | 0.0042 | <.0001 |
| Unemployment Burnout Count, 8% | -0.1751 | 0.0363 | <.0001 |
| Unemployment Burnout Count, 10% | -0.0765 | 0.0461 | 0.0973 |
| Unemployment Burnout Count, 12% | 0.5445 | 0.0547 | <.0001 |
| max(0,mtmltv-66) | -0.5926 | 0.0130 | <.0001 |
| max(0,66-mtmltv) | 0.5725 | 0.0129 | <.0001 |
| max(0,mtmltv-30) | -0.0088 | 0.0020 | <.0001 |
| max(0,mtmltv-6) | 0.6881 | 0.0324 | <.0001 |
| max(0,mtmltv-101) | 0.0184 | 0.0020 | <.0001 |
| max(0,mtmltv-9) | -0.1229 | 0.0218 | <.0001 |
| max(0,debt_ratio-.60) | -0.0292 | 0.2179 | 0.8932 |
| max(0,.60-debt_ratio) | -0.0171 | 0.1156 | 0.8823 |
| max(0,debt_ratio-.30) | -0.2239 | 0.1552 | 0.1492 |
| max(0,debt_ratio-.95) | 0.2519 | 0.1220 | 0.0388 |
| Origination LTV | 0.8111 | 0.0473 | <.0001 |
| Junior Lien Indicator | -0.0354 | 0.0699 | 0.6132 |
| Orig. LTV x Junior Lien Ind | -0.0175 | 0.0898 | 0.8457 |
| One Borrower Indicator | -0.3514 | 0.1042 | 0.0007 |
| Credit Score x One Borrower (00s) | 0.0376 | 0.0002 | 0.0137 |
| No Full Doc Loan | -0.0749 | 0.0252 | 0.003 |
| Third Party Loan | -0.0667 | 0.0177 | 0.0002 |
| Judicial State | -0.0366 | 0.0098 | 0.0002 |
| Current UPB/Origination UPB | -2.4197 | 0.2325 | <.0001 |
| HPA with 24 month lag | 0.0793 | 0.1813 | 0.662 |
| HPA with lag x Sunk Cost | 1.6043 | 0.2044 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.3440 | 0.0005 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.3680 | 0.0005 | <.0001 |
| Q1 | -0.0961 | 0.0135 | <.0001 |
| Q2 | 0.0611 | 0.0128 | <.0001 |
| Q3 | 0.0587 | 0.0127 | <.0001 |
| 2005-2008 Indicator | -0.1433 | 0.0167 | <.0001 |
| 2009-2013 Indicator | -0.3194 | 0.0213 | <.0001 |
| >2014 Indicator | -0.3954 | 0.0320 | <.0001 |
| max(0,refi_incentive_level_l2-1.4) | 0.4215 | 0.0819 | <.0001 |
| max(0,1.4-refi_incentive_level_l2) | -0.1414 | 0.0410 | 0.0006 |
| max(0,refi_incentive_level_l2-0.02) | 0.0813 | 0.0561 | 0.1474 |
| max(0,refi_incentive_level_l2-1.1) | -0.3322 | 0.0890 | 0.0002 |
| max(0, brnt_cnt-1) | -0.0437 | 0.0430 | 0.3095 |
| max(0, brnt_cnt-8) | 0.0480 | 0.0431 | 0.2652 |
| max(0,8-brnt_cnt) | -0.0393 | 0.0386 | 0.3083 |
| max(0, brnt_cnt-50) | -0.0071 | 0.0013 | <.0001 |
| max(0, brnt_cnt-74) | 0.0023 | 0.0010 | 0.0194 |
| Indicator for 2001-2003 Refi Boom | 0.4557 | 0.0249 | <.0001 |

**Table 25. Segment: ARMs Performing, Enterprise 2, Event: Idq**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -23.4132 | 1.3252 | <.0001 |
| Refinance Rate | 0.3032 | 0.0764 | <.0001 |
| Cash Out | 0.5594 | 0.0779 | <.0001 |
| Investment | 0.0515 | 0.0353 | 0.1445 |
| Second Home | -0.0412 | 0.0320 | 0.1975 |
| Age | 0.0249 | 0.0016 | <.0001 |
| Age Sq. | -0.0002 | 0.0000 | <.0001 |
| Age (Years) Cb. | 0.0010 | 0.0000 | <.0001 |
| Current UPB (000s) | 0.0020 | 0.0004 | <.0001 |
| Current UPB (00000s) Sq. | -0.0064 | 0.0000 | <.0001 |
| Credit Score | 0.0090 | 0.0025 | 0.0003 |
| Credit Sq (0s) Sq. | -0.0010 | 0.0000 | <.0001 |
| Sato F30 | 0.3936 | 0.0155 | <.0001 |
| Burnout Count | 0.0027 | 0.0010 | 0.005 |
| Unemployment Rate | 0.0795 | 0.0063 | <.0001 |
| Unemployment Burnout Count, 8% | -0.4851 | 0.0629 | <.0001 |
| Unemployment Burnout Count, 10% | -0.3399 | 0.0786 | <.0001 |
| Unemployment Burnout Count, 12% | -0.4293 | 0.1051 | <.0001 |
| max(0, mtmltv-79) | 0.0294 | 0.0035 | <.0001 |
| max(0, 79-mtmltv) | -0.0132 | 0.0017 | <.0001 |
| max(0, mtmltv-154) | -0.0041 | 0.0027 | 0.1299 |
| max(0, mtmltv-90) | -0.0082 | 0.0054 | 0.1279 |
| max(0, mtmltv-105) | -0.0172 | 0.0032 | <.0001 |
| max(0,debt_ratio-.60) | -0.3649 | 0.4885 | 0.4551 |
| max(0,.60-debt_ratio) | -0.9140 | 0.2460 | 0.0002 |
| max(0,debt_ratio-.30) | 0.2101 | 0.3246 | 0.5176 |
| max(0,debt_ratio-.95) | 0.1495 | 0.3064 | 0.6257 |
| Origination LTV | 1.6377 | 0.1126 | <.0001 |
| Junior Lien Indicator | 0.9656 | 0.2060 | <.0001 |
| Orig. LTV x Junior Lien Ind | -0.9104 | 0.2624 | 0.0005 |
| One Borrower Indicator | -0.5609 | 0.2285 | 0.0141 |
| Credit Score x One Borrower (00s) | 0.1439 | 0.0003 | <.0001 |
| No Full Doc Loan | 0.3044 | 0.0239 | <.0001 |
| Third Party Loan | 0.0920 | 0.0659 | 0.1624 |
| Judicial State | 0.1145 | 0.0198 | <.0001 |
| Current UPB/Origination UPB | 18.0858 | 1.0249 | <.0001 |
| HPA with 24 month lag | 10.6921 | 0.9266 | <.0001 |
| HPA with lag x Sunk Cost | -13.9216 | 0.9505 | <.0001 |
| MTMLTV x Refinance Rate (00s) | 0.0481 | 0.0008 | 0.535 |
| MTMLTV x Cash Out (00s) | -0.2010 | 0.0008 | 0.008 |
| Q1 | -0.0334 | 0.0244 | 0.171 |
| Q2 | -0.1571 | 0.0251 | <.0001 |
| Q3 | -0.1373 | 0.0250 | <.0001 |
| 2005-2008 Indicator | 0.2188 | 0.0319 | <.0001 |
| 2009-2013 Indicator | -0.9802 | 0.0786 | <.0001 |
| >2014 Indicator | -1.2345 | 0.1245 | <.0001 |
| Months until Interest Rate is reset | 0.0025 | 0.0004 | <.0001 |

**Table 26. Segment: ARMs Performing, Enterprise 2, Event: prepay**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -29.5370 | 0.7887 | <.0001 |
| Refinance Rate | 0.0872 | 0.0205 | <.0001 |
| Cash Out | 0.0927 | 0.0232 | <.0001 |
| Investment | -0.4211 | 0.0144 | <.0001 |
| Second Home | -0.2483 | 0.0122 | <.0001 |
| max(0,17-age) | -0.1606 | 0.0050 | <.0001 |
| max(0,age-17) | 0.1731 | 0.0061 | <.0001 |
| max(0,age-7) | -0.1642 | 0.0059 | <.0001 |
| max(0,age-93) | -0.0011 | 0.0006 | 0.0872 |
| max(0,age-35) | -0.0230 | 0.0008 | <.0001 |
| Current UPB (000s) | 0.0023 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | -0.0209 | 0.0000 | <.0001 |
| Credit Score | 0.0079 | 0.0012 | <.0001 |
| Credit Sq (0s) Sq. | -0.0005 | 0.0000 | <.0001 |
| Sato F30 | 0.1714 | 0.0055 | <.0001 |
| Unemployment Rate | -0.0471 | 0.0024 | <.0001 |
| Unemployment Burnout Count, 8% | 0.1316 | 0.0161 | <.0001 |
| Unemployment Burnout Count, 10% | 0.3584 | 0.0223 | <.0001 |
| Unemployment Burnout Count, 12% | 0.4294 | 0.0407 | <.0001 |
| max(0,mtmltv-66) | -0.4556 | 0.0101 | <.0001 |
| max(0,66-mtmltv) | 0.4350 | 0.0101 | <.0001 |
| max(0,mtmltv-30) | 0.0120 | 0.0015 | <.0001 |
| max(0,mtmltv-6) | 0.3766 | 0.0240 | <.0001 |
| max(0,mtmltv-101) | 0.0145 | 0.0013 | <.0001 |
| max(0,mtmltv-9) | 0.0390 | 0.0161 | 0.0152 |
| max(0,debt_ratio-.60) | 0.2999 | 0.1585 | 0.0585 |
| max(0,.60-debt_ratio) | -0.3070 | 0.0592 | <.0001 |
| max(0,debt_ratio-.30) | -0.5596 | 0.0915 | <.0001 |
| max(0,debt_ratio-.95) | 0.2600 | 0.1082 | 0.0163 |
| Origination LTV | 1.2336 | 0.0402 | <.0001 |
| Junior Lien Indicator | 0.0297 | 0.0393 | 0.4503 |
| Orig. LTV x Junior Lien Ind | -0.1594 | 0.0536 | 0.0029 |
| One Borrower Indicator | -0.1370 | 0.0851 | 0.1073 |
| Credit Score x One Borrower (00s) | 0.0029 | 0.0001 | 0.801 |
| No Full Doc Loan | -0.1805 | 0.0131 | <.0001 |
| Third Party Loan | 0.1418 | 0.0109 | <.0001 |
| Judicial State | -0.0294 | 0.0063 | <.0001 |
| Current UPB/Origination UPB | -0.4344 | 0.1425 | 0.0023 |
| HPA with 24 month lag | -0.2867 | 0.1186 | 0.0157 |
| HPA with lag x Sunk Cost | 0.7923 | 0.1259 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.0430 | 0.0003 | 0.1839 |
| MTMLTV x Cash Out (00s) | -0.1740 | 0.0004 | <.0001 |
| Q1 | -0.0965 | 0.0086 | <.0001 |
| Q2 | 0.1163 | 0.0082 | <.0001 |
| Q3 | 0.1148 | 0.0082 | <.0001 |
| 2005-2008 Indicator | -0.1788 | 0.0107 | <.0001 |
| 2009-2013 Indicator | -0.2475 | 0.0123 | <.0001 |
| >2014 Indicator | -0.3885 | 0.0148 | <.0001 |
| max(0,refi_incentive_level_l2-1.4) | -0.0100 | 0.0543 | 0.8543 |
| max(0,1.4-refi_incentive_level_l2) | -0.2243 | 0.0163 | <.0001 |
| max(0,refi_incentive_level_l2-0.02) | 0.3016 | 0.0244 | <.0001 |
| max(0,refi_incentive_level_l2-1.1) | -0.2526 | 0.0539 | <.0001 |
| max(0, brnt_cnt-1) | -0.2006 | 0.0123 | <.0001 |
| max(0, brnt_cnt-8) | 0.1937 | 0.0124 | <.0001 |
| max(0,8-brnt_cnt) | -0.1968 | 0.0112 | <.0001 |
| max(0, brnt_cnt-50) | 0.0045 | 0.0011 | <.0001 |
| max(0, brnt_cnt-74) | 0.0060 | 0.0011 | <.0001 |
| Indicator for 2001-2003 Refi Boom | 0.4408 | 0.0102 | <.0001 |
| Months until Interest Rate is reset | 0.0052 | 0.0001 | <.0001 |

**Table 27. Segment: MRPL, Enterprise 2, Event: Idq**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -9.2683 | 0.3211 | <.0001 |
| Refinance Rate | -0.0534 | 0.0225 | 0.0176 |
| Cash Out | -0.1054 | 0.0218 | <.0001 |
| Investment | 0.0176 | 0.0198 | 0.375 |
| Second Home | -0.0653 | 0.0237 | 0.0059 |
| Age | -0.0070 | 0.0007 | <.0001 |
| Age Sq. | 0.0001 | 0.0000 | <.0001 |
| Age (Years) Cb. | -0.0003 | 0.0000 | <.0001 |
| Current UPB (000s) | -0.0011 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | 0.0106 | 0.0000 | <.0001 |
| Credit Score | 0.0102 | 0.0007 | <.0001 |
| Credit Sq (0s) Sq. | -0.0010 | 0.0000 | <.0001 |
| Sato F30 | 0.0358 | 0.0057 | <.0001 |
| Burnout Count | 0.0014 | 0.0002 | <.0001 |
| Unemployment Rate | 0.0015 | 0.0024 | 0.5292 |
| Unemployment Burnout Count, 8% | -0.3990 | 0.0184 | <.0001 |
| Unemployment Burnout Count, 10% | -0.6510 | 0.0244 | <.0001 |
| Unemployment Burnout Count, 12% | -0.2432 | 0.0314 | <.0001 |
| max(0, mtmltv-79) | 0.0005 | 0.0011 | 0.6639 |
| max(0, 79-mtmltv) | 0.0051 | 0.0004 | <.0001 |
| max(0, mtmltv-154) | -0.0015 | 0.0012 | 0.1977 |
| max(0, mtmltv-90) | -0.0056 | 0.0019 | 0.0025 |
| max(0, mtmltv-105) | 0.0029 | 0.0013 | 0.0197 |
| max(0,debt_ratio-.60) | -0.1219 | 0.1399 | 0.3835 |
| max(0,.60-debt_ratio) | -0.1050 | 0.0857 | 0.2207 |
| max(0,debt_ratio-.30) | -0.2067 | 0.1075 | 0.0547 |
| max(0,debt_ratio-.95) | 0.3276 | 0.0709 | <.0001 |
| Origination LTV | 0.4192 | 0.0288 | <.0001 |
| Junior Lien Indicator | 0.1959 | 0.0432 | <.0001 |
| Orig. LTV x Junior Lien Ind | -0.2632 | 0.0533 | <.0001 |
| One Borrower Indicator | -0.2023 | 0.0631 | 0.0014 |
| Credit Score x One Borrower (00s) | 0.0436 | 0.0001 | <.0001 |
| No Full Doc Loan | -0.0111 | 0.0144 | 0.4399 |
| Third Party Loan | 0.0445 | 0.0109 | <.0001 |
| Judicial State | -0.0130 | 0.0061 | 0.0318 |
| Current UPB/Origination UPB | 5.6106 | 0.2315 | <.0001 |
| HPA with 24 month lag | 2.5929 | 0.2092 | <.0001 |
| HPA with lag x Sunk Cost | -3.8017 | 0.2130 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.1270 | 0.0003 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.0010 | 0.0002 | 0.966 |
| Q1 | -0.1211 | 0.0079 | <.0001 |
| Q2 | -0.2193 | 0.0080 | <.0001 |
| Q3 | -0.0941 | 0.0078 | <.0001 |
| 2005-2008 Indicator | -0.1205 | 0.0099 | <.0001 |
| 2009-2013 Indicator | -0.1528 | 0.0134 | <.0001 |
| >2014 Indicator | -0.5742 | 0.0216 | <.0001 |
| Min# of months since Mod. or Del | -0.0653 | 0.0007 | <.0001 |
| min_dt_sq | 0.0006 | 0.0000 | <.0001 |
| min_dt_cb | 0.0000 | 0.0000 | <.0001 |

**Table 28. Segment: MRPL, Enterprise 2, Event: prepay**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -42.9250 | 7.4085 | <.0001 |
| Refinance Rate | -0.0113 | 0.0406 | 0.7797 |
| Cash Out | -0.0631 | 0.0417 | 0.13 |
| Investment | 0.1727 | 0.0352 | <.0001 |
| Second Home | 0.0295 | 0.0399 | 0.4599 |
| max(0,17-age) | 0.2187 | 0.7170 | 0.7603 |
| max(0,age-17) | -0.2170 | 0.7251 | 0.7648 |
| max(0,age-7) | 0.2139 | 0.7248 | 0.7679 |
| max(0,age-93) | 0.0049 | 0.0008 | <.0001 |
| max(0,age-35) | -0.0118 | 0.0041 | 0.0036 |
| Current UPB (000s) | 0.0056 | 0.0002 | <.0001 |
| Current UPB (00000s) Sq. | -0.1000 | 0.0000 | <.0001 |
| Credit Score | 0.0019 | 0.0013 | 0.1394 |
| Credit Sq (0s) Sq. | -0.0001 | 0.0000 | <.0001 |
| Sato F30 | 0.1105 | 0.0108 | <.0001 |
| Unemployment Rate | -0.0793 | 0.0053 | <.0001 |
| Unemployment Burnout Count, 8% | -0.2980 | 0.0414 | <.0001 |
| Unemployment Burnout Count, 10% | -0.2881 | 0.0513 | <.0001 |
| Unemployment Burnout Count, 12% | 0.6323 | 0.0603 | <.0001 |
| max(0,mtmltv-66) | -0.6186 | 0.0219 | <.0001 |
| max(0,66-mtmltv) | 0.6030 | 0.0218 | <.0001 |
| max(0,mtmltv-30) | -0.0040 | 0.0028 | 0.1489 |
| max(0,mtmltv-6) | 0.6974 | 0.0534 | <.0001 |
| max(0,mtmltv-101) | 0.0151 | 0.0019 | <.0001 |
| max(0,mtmltv-9) | -0.1127 | 0.0350 | 0.0013 |
| max(0,debt_ratio-.60) | -0.0320 | 0.2433 | 0.8953 |
| max(0,.60-debt_ratio) | 0.0875 | 0.1489 | 0.5567 |
| max(0,debt_ratio-.30) | -0.1872 | 0.1881 | 0.3198 |
| max(0,debt_ratio-.95) | 0.2175 | 0.1202 | 0.0703 |
| Origination LTV | 1.2008 | 0.0521 | <.0001 |
| Junior Lien Indicator | 0.0826 | 0.0722 | 0.2521 |
| Orig. LTV x Junior Lien Ind | -0.1627 | 0.0905 | 0.0722 |
| One Borrower Indicator | -0.1839 | 0.1157 | 0.1119 |
| Credit Score x One Borrower (00s) | 0.0006 | 0.0002 | 0.9726 |
| No Full Doc Loan | -0.1234 | 0.0271 | <.0001 |
| Third Party Loan | -0.0392 | 0.0180 | 0.0295 |
| Judicial State | -0.0083 | 0.0111 | 0.4556 |
| Current UPB/Origination UPB | -2.7248 | 0.3575 | <.0001 |
| HPA with 24 month lag | -0.6096 | 0.2908 | 0.036 |
| HPA with lag x Sunk Cost | 2.2975 | 0.3162 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.2670 | 0.0006 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.2790 | 0.0006 | <.0001 |
| Q1 | -0.1251 | 0.0150 | <.0001 |
| Q2 | 0.0769 | 0.0141 | <.0001 |
| Q3 | 0.0741 | 0.0139 | <.0001 |
| 2005-2008 Indicator | -0.2190 | 0.0196 | <.0001 |
| 2009-2013 Indicator | -0.3780 | 0.0274 | <.0001 |
| >2014 Indicator | -0.2301 | 0.0399 | <.0001 |
| max(0,refi_incentive_level_l2-1.4) | 0.9466 | 0.0989 | <.0001 |
| max(0,1.4-refi_incentive_level_l2) | -0.1015 | 0.0476 | 0.0329 |
| max(0,refi_incentive_level_l2-0.02) | 0.0036 | 0.0680 | 0.9576 |
| max(0,refi_incentive_level_l2-1.1) | -0.6698 | 0.1089 | <.0001 |
| max(0, brnt_cnt-1) | -0.0322 | 0.0616 | 0.6013 |
| max(0, brnt_cnt-8) | 0.0370 | 0.0618 | 0.5493 |
| max(0,8-brnt_cnt) | -0.0229 | 0.0546 | 0.6755 |
| max(0, brnt_cnt-50) | -0.0084 | 0.0017 | <.0001 |
| max(0, brnt_cnt-74) | 0.0022 | 0.0012 | 0.0667 |
| Indicator for 2001-2003 Refi Boom | 0.8496 | 0.0395 | <.0001 |
| Min# of months since Mod or Del | 0.0246 | 0.0011 | <.0001 |
| min_dt_sq | -0.0001 | 0.0000 | <.0001 |
| min_dt_cb | 0.0000 | 0.0000 | <.0001 |

**Table 29. Segment: NRPL, Enterprise 2, Event: Idq**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -3.9875 | 0.2393 | <.0001 |
| Refinance Rate | 0.0702 | 0.0177 | <.0001 |
| Cash Out | 0.1112 | 0.0174 | <.0001 |
| Investment | -0.0710 | 0.0125 | <.0001 |
| Second Home | -0.1189 | 0.0155 | <.0001 |
| Age | -0.0012 | 0.0004 | 0.0081 |
| Age Sq. | 0.0000 | 0.0000 | 0.0006 |
| Age (Years) Cb. | 0.0000 | 0.0000 | <.0001 |
| Current UPB (000s) | 0.0003 | 0.0001 | 0.0027 |
| Current UPB (00000s) Sq. | -0.0002 | 0.0000 | <.0001 |
| Credit Score | 0.0039 | 0.0006 | <.0001 |
| Credit Sq (0s) Sq. | -0.0004 | 0.0000 | <.0001 |
| Sato F30 | 0.0487 | 0.0049 | <.0001 |
| Burnout Count | 0.0010 | 0.0001 | <.0001 |
| Unemployment Rate | 0.0270 | 0.0017 | <.0001 |
| Unemployment Burnout Count, 8% | -0.1176 | 0.0148 | <.0001 |
| Unemployment Burnout Count, 10% | -0.2207 | 0.0187 | <.0001 |
| Unemployment Burnout Count, 12% | -0.2340 | 0.0243 | <.0001 |
| max(0, mtmltv-79) | 0.0073 | 0.0011 | <.0001 |
| max(0, 79-mtmltv) | 0.0001 | 0.0003 | 0.8516 |
| max(0, mtmltv-154) | 0.0034 | 0.0021 | 0.111 |
| max(0, mtmltv-90) | -0.0105 | 0.0021 | <.0001 |
| max(0, mtmltv-105) | -0.0012 | 0.0017 | 0.486 |
| max(0,debt_ratio-.60) | -0.0653 | 0.1173 | 0.5781 |
| max(0,.60-debt_ratio) | -0.2676 | 0.0598 | <.0001 |
| max(0,debt_ratio-.30) | -0.1601 | 0.0813 | 0.0489 |
| max(0,debt_ratio-.95) | 0.2263 | 0.0685 | 0.0009 |
| Origination LTV | 0.2414 | 0.0255 | <.0001 |
| Junior Lien Indicator | 0.0801 | 0.0389 | 0.0396 |
| Orig. LTV x Junior Lien Ind | -0.1244 | 0.0492 | 0.0122 |
| One Borrower Indicator | -0.1887 | 0.0536 | 0.0004 |
| Credit Score x One Borrower (00s) | 0.0437 | 0.0001 | <.0001 |
| No Full Doc Loan | -0.0010 | 0.0132 | 0.9395 |
| Third Party Loan | 0.0054 | 0.0097 | 0.5758 |
| Judicial State | -0.0266 | 0.0050 | <.0001 |
| Current UPB/Origination UPB | 2.1535 | 0.1554 | <.0001 |
| HPA with 24 month lag | 0.7169 | 0.1293 | <.0001 |
| HPA with lag x Sunk Cost | -1.6600 | 0.1452 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.1820 | 0.0003 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.1900 | 0.0003 | <.0001 |
| Q1 | -0.0874 | 0.0068 | <.0001 |
| Q2 | -0.1710 | 0.0067 | <.0001 |
| Q3 | -0.0827 | 0.0067 | <.0001 |
| 2005-2008 Indicator | 0.0310 | 0.0078 | <.0001 |
| 2009-2013 Indicator | 0.0044 | 0.0101 | 0.6653 |
| >2014 Indicator | -0.0537 | 0.0147 | 0.0003 |
| # of months since last 3+ months delinquent | -0.1342 | 0.0006 | <.0001 |
| month_from_last_dq_sq | 0.0017 | 0.0000 | <.0001 |
| month_from_last_dq_cb | 0.0000 | 0.0000 | <.0001 |

**Table 30. Segment: NRPL, Enterprise 2, Event: prepay**
| Variable Name | Estimate | StdErr | Probt |
| :--- | :--- | :--- | :--- |
| Intercept | -39.2095 | 1.2872 | <.0001 |
| Refinance Rate | 0.0782 | 0.0254 | 0.0021 |
| Cash Out | -0.0245 | 0.0265 | 0.3553 |
| Investment | 0.0083 | 0.0204 | 0.6839 |
| Second Home | -0.0145 | 0.0237 | 0.5405 |
| max(0,17-age) | 0.0183 | 0.1000 | 0.8549 |
| max(0,age-17) | -0.0007 | 0.1030 | 0.9949 |
| max(0,age-7) | -0.0070 | 0.1028 | 0.9459 |
| max(0,age-93) | 0.0022 | 0.0005 | <.0001 |
| max(0,age-35) | -0.0010 | 0.0019 | 0.6176 |
| Current UPB (000s) | 0.0055 | 0.0002 | <.0001 |
| Current UPB (00000s) Sq. | -0.0873 | 0.0000 | <.0001 |
| Credit Score | -0.0071 | 0.0010 | <.0001 |
| Credit Sq (0s) Sq. | 0.0007 | 0.0000 | <.0001 |
| Sato F30 | 0.0760 | 0.0086 | <.0001 |
| Unemployment Rate | -0.0768 | 0.0036 | <.0001 |
| Unemployment Burnout Count, 8% | -0.0905 | 0.0314 | 0.0039 |
| Unemployment Burnout Count, 10% | 0.0076 | 0.0408 | 0.8528 |
| Unemployment Burnout Count, 12% | 0.2240 | 0.0511 | <.0001 |
| max(0,mtmltv-66) | -0.6241 | 0.0100 | <.0001 |
| max(0,66-mtmltv) | 0.6211 | 0.0100 | <.0001 |
| max(0,mtmltv-30) | 0.0189 | 0.0017 | <.0001 |
| max(0,mtmltv-6) | 0.7632 | 0.0252 | <.0001 |
| max(0,mtmltv-101) | 0.0119 | 0.0018 | <.0001 |
| max(0,mtmltv-9) | -0.1741 | 0.0170 | <.0001 |
| max(0,debt_ratio-.60) | 0.1460 | 0.1947 | 0.4532 |
| max(0,.60-debt_ratio) | 0.0136 | 0.0958 | 0.8871 |
| max(0,debt_ratio-.30) | -0.0396 | 0.1339 | 0.7673 |
| max(0,debt_ratio-.95) | -0.1072 | 0.1130 | 0.3426 |
| Origination LTV | 0.7077 | 0.0410 | <.0001 |
| Junior Lien Indicator | 0.0153 | 0.0609 | 0.8012 |
| Orig. LTV x Junior Lien Ind | -0.1233 | 0.0794 | 0.1203 |
| One Borrower Indicator | -0.2794 | 0.0922 | 0.0025 |
| Credit Score x One Borrower (00s) | 0.0306 | 0.0001 | 0.0242 |
| No Full Doc Loan | -0.0364 | 0.0230 | 0.1137 |
| Third Party Loan | -0.0301 | 0.0169 | 0.0741 |
| Judicial State | -0.0078 | 0.0086 | 0.3643 |
| Current UPB/Origination UPB | -2.6363 | 0.1929 | <.0001 |
| HPA with 24 month lag | -0.6133 | 0.1493 | <.0001 |
| HPA with lag x Sunk Cost | 2.8193 | 0.1709 | <.0001 |
| MTMLTV x Refinance Rate (00s) | -0.1990 | 0.0004 | <.0001 |
| MTMLTV x Cash Out (00s) | -0.1050 | 0.0005 | 0.0227 |
| Q1 | -0.0625 | 0.0120 | <.0001 |
| Q2 | 0.0684 | 0.0114 | <.0001 |
| Q3 | 0.0517 | 0.0114 | <.0001 |
| 2005-2008 Indicator | -0.0791 | 0.0147 | <.0001 |
| 2009-2013 Indicator | -0.2740 | 0.0186 | <.0001 |
| >2014 Indicator | -0.2716 | 0.0283 | <.0001 |
| max(0,refi_incentive_level_l2-1.4) | 0.1392 | 0.0700 | 0.0466 |
| max(0,1.4-refi_incentive_level_l2) | -0.1111 | 0.0353 | 0.0016 |
| max(0,refi_incentive_level_l2-0.02) | 0.1032 | 0.0475 | 0.0298 |
| max(0,refi_incentive_level_l2-1.1) | -0.1047 | 0.0753 | 0.1645 |
| max(0, brnt_cnt-1) | -0.0493 | 0.0338 | 0.1446 |
| max(0, brnt_cnt-8) | 0.0530 | 0.0339 | 0.1181 |
| max(0,8-brnt_cnt) | -0.0463 | 0.0305 | 0.1296 |
| max(0, brnt_cnt-50) | -0.0080 | 0.0011 | <.0001 |
| max(0, brnt_cnt-74) | 0.0041 | 0.0009 | <.0001 |
| Indicator for 2001-2003 Refi Boom | 0.4379 | 0.0193 | <.0001 |
| # of months since last 3+ months delinquent | 0.0079 | 0.0007 | <.0001 |
| month_from_last_dq_sq | 0.0000 | 0.0000 | <.0001 |
| month_from_last_dq_cb | 0.0000 | 0.0000 | <.0001 |

**Table 31. Segment: NPL - Idq, Enterprise 2**

| | <div style="text-align:center">Event: RPL</div> | | | <div style="text-align:center">Event: Prepay</div> | | | <div style="text-align:center">Event: SDQ</div> | | | <div style="text-align:center">Event: Default</div> | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Variable Name** | **Estimate** | **StdErr** | **Probt** | **Estimate** | **StdErr** | **Probt** | **Estimate** | **StdErr** | **Probt** | **Estimate** | **StdErr** | **Probt** |
| Intercept | 9.7283 | 0.9893 | <.0001 | -40.1931 | 1.2767 | <.0001 | -20.8654 | 0.8322 | <.0001 | 0.4165 | 13.0726 | 0.9746 |
| Refinance Rate | -0.1406 | 0.0038 | <.0001 | -0.2265 | 0.0129 | <.0001 | 0.0272 | 0.0035 | <.0001 | 0.1046 | 0.0138 | <.0001 |
| Cash Out | -0.1067 | 0.0039 | <.0001 | -0.2999 | 0.0139 | <.0001 | 0.0260 | 0.0035 | <.0001 | -0.1135 | 0.0154 | <.0001 |
| Investment | -0.1651 | 0.0080 | <.0001 | 0.0630 | 0.0246 | 0.0105 | 0.1807 | 0.0062 | <.0001 | 0.3624 | 0.0218 | <.0001 |
| Second Home | -0.1321 | 0.0098 | <.0001 | 0.1111 | 0.0308 | 0.0003 | 0.1412 | 0.0072 | <.0001 | 0.3379 | 0.0261 | <.0001 |
| Age | 0.0017 | 0.0001 | <.0001 | -0.0192 | 0.0004 | <.0001 | -0.0007 | 0.0001 | <.0001 | -0.0002 | 0.0006 | 0.7433 |
| Age Sq. | 0.0000 | | <.0001 | 0.0000 | | <.0001 | 0.0000 | | <.0001 | -0.0001 | | <.0001 |
| Current UPB (000s) | -0.0007 | 0.0001 | <.0001 | 0.0018 | 0.0002 | <.0001 | -0.0006 | 0.0001 | <.0001 | -0.0102 | 0.0002 | <.0001 |
| Current UPB (00000s) Sq. | 0.0074 | | <.0001 | -0.0400 | | <.0001 | 0.0109 | | <.0001 | 0.1400 | | <.0001 |
| Debt to Income Ratio| -0.0003 | 0.0006 | 0.6049 | 0.0003 | 0.0006 | 0.6144 | -0.0003 | 0.0005 | 0.5592 | -0.0159 | 0.0127 | 0.2090 |
| Credit Score | -0.0019 | 0.0000 | <.0001 | 0.0038 | 0.0001 | <.0001 | 0.0012 | 0.0000 | <.0001 | 0.0073 | 0.0002 | <.0001 |
| Burnout Count | 0.0030 | 0.0001 | <.0001 | 0.0022 | 0.0004 | <.0001 | -0.0031 | 0.0001 | <.0001 | 0.0050 | 0.0005 | <.0001 |
| Sato F30 | -0.0207 | 0.0031 | <.0001 | 0.0640 | 0.0112 | <.0001 | 0.0159 | 0.0028 | <.0001 | 0.0027 | 0.0115 | 0.8162 |
| Judicial State | -0.0690 | 0.0030 | <.0001 | -0.1382 | 0.0104 | <.0001 | 0.1140 | 0.0028 | <.0001 | -1.4940 | 0.0153 | <.0001 |
| 2005-2008 Indicator | -0.1083 | 0.0045 | <.0001 | -0.6500 | 0.0163 | <.0001 | -0.0395 | 0.0043 | <.0001 | -0.8658 | 0.0173 | <.0001 |
| 2009-2013 Indicator | -0.0775 | 0.0055 | <.0001 | -0.4760 | 0.0162 | <.0001 | -0.0114 | 0.0053 | 0.0322 | -0.7784 | 0.0213 | <.0001 |
| >2014 Indicator | -0.0193 | 0.0080 | 0.0155 | -0.8939 | 0.0233 | <.0001 | -0.1932 | 0.0084 | <.0001 | -1.7935 | 0.0516 | <.0001 |
| No Full Doc Loan | -0.0220 | 0.0083 | 0.0077 | -0.1353 | 0.0307 | <.0001 | 0.0031 | 0.0068 | 0.6459 | 0.4508 | 0.0216 | <.0001 |
| Fixed Rate Mortgage 40 YR | 0.0127 | 0.0356 | 0.7220 | -0.1837 | 0.1506 | 0.2228 | -0.1022 | 0.0277 | 0.0002 | -0.7826 | 0.1396 | <.0001 |
| Fixed Rate Mortgage 30 YR | 0.1800 | 0.0063 | <.0001 | -0.0110 | 0.0233 | 0.6367 | -0.0955 | 0.0048 | <.0001 | -0.2060 | 0.0187 | <.0001 |
| Fixed Rate Mortgage 15 YR | 0.2217 | 0.0076 | <.0001 | -0.0437 | 0.0255 | 0.0860 | -0.1135 | 0.0066 | <.0001 | -0.2655 | 0.0288 | <.0001 |
| Non Fixed Rate Mortgage| 0.0000 | | | 0.0000 | | | 0.0000 | | | 0.0000 | | |
| One Borrower Indicator| -0.1342 | 0.0319 | <.0001 | -0.1560 | 0.1158 | 0.1777 | 0.2243 | 0.0304 | <.0001 | 1.1403 | 0.1332 | <.0001 |
| Credit Score x One Borrower (00s) | 0.0130 | 0.0000 | 0.0060 | 0.0110 | 0.0002 | 0.5128 | -0.0240 | 0.0000 | <.0001 | -0.1740 | 0.0002 | <.0001 |
| Junior Lien Indicator| -0.1727 | 0.0049 | <.0001 | -0.2549 | 0.0179 | <.0001 | 0.0560 | 0.0039 | <.0001 | 0.2080 | 0.0155 | <.0001 |
| Alta Loan Indicator | -0.0972 | 0.0079 | <.0001 | -0.2306 | 0.0360 | <.0001 | 0.0373 | 0.0059 | <.0001 | -0.3672 | 0.0258 | <.0001 |
| IO Loan Indicator | 0.0000 | | | 0.0000 | | | 0.0000 | | | 0.0000 | | |
| Jumbo Loan Indicator| 0.1042 | 0.0318 | 0.0011 | 0.4416 | 0.0895 | <.0001 | 0.0152 | 0.0311 | 0.6247 | -0.9934 | 0.2576 | 0.0001 |
| max(0,unemp_rate-9) | 0.1145 | 0.0279 | <.0001 | 0.0369 | 0.0740 | 0.6181 | -0.0632 | 0.0319 | 0.0476 | 1.3248 | 0.2941 | <.0001 |
| max(0,9-unemp_rate) | 0.0295 | 0.0274 | 0.2819 | 0.1679 | 0.0712 | 0.0184 | 0.0516 | 0.0316 | 0.1030 | -1.2489 | 0.2936 | <.0001 |
| max(0,unemp_rate-7) | -0.0963 | 0.0069 | <.0001 | -0.0601 | 0.0253 | 0.0177 | -0.0107 | 0.0062 | 0.0874 | -0.3981 | 0.0232 | <.0001 |
| max(0,unemp_rate-3) | -0.0188 | 0.0287 | 0.5112 | 0.0821 | 0.0752 | 0.2752 | 0.0774 | 0.0328 | 0.0184 | -1.2262 | 0.2975 | <.0001 |
| max(0,unemp_rate-5.5)| 0.0321 | 0.0065 | <.0001 | -0.0757 | 0.0212 | 0.0004 | -0.0075 | 0.0065 | 0.2455 | 0.1815 | 0.0273 | <.0001 |
| max(0,mtmltv-95) | 0.1089 | 0.0108 | <.0001 | -0.3791 | 0.0138 | <.0001 | -0.2033 | 0.0089 | <.0001 | 0.0097 | 0.1432 | 0.9460 |
| max(0,95-mtmltv) | -0.1070 | 0.0108 | <.0001 | 0.4018 | 0.0130 | <.0001 | 0.2021 | 0.0089 | <.0001 | -0.0338 | 0.1432 | 0.8132 |
| max(0,mtmltv-50) | -0.0029 | 0.0005 | <.0001 | -0.0146 | 0.0016 | <.0001 | 0.0059 | 0.0006 | <.0001 | 0.0026 | 0.0037 | 0.4901 |
| max(0,mtmltv-80) | -0.0044 | 0.0006 | <.0001 | -0.0434 | 0.0027 | <.0001 | 0.0012 | 0.0005 | 0.0140 | -0.0093 | 0.0020 | <.0001 |
| max(0,mtmltv-30) | -0.0031 | 0.0009 | 0.0009 | 0.0096 | 0.0025 | 0.0001 | -0.0025 | 0.0011 | 0.0190 | -0.0016 | 0.0102 | 0.8733 |
| max(0,mtmltv-140) | 0.0083 | 0.0007 | <.0001 | 0.0593 | 0.0078 | <.0001 | -0.0034 | 0.0004 | <.0001 | -0.0090 | 0.0011 | <.0001 |
| max(0,mtmltv-5) | -0.1088 | 0.0110 | <.0001 | 0.3720 | 0.0141 | <.0001 | 0.2033 | 0.0093 | <.0001 | 0.0099 | 0.1462 | 0.9461 |
| Refi Incentive with 2 months lag | -0.0388 | 0.0029 | <.0001 | 0.0640 | 0.0095 | <.0001 | 0.0784 | 0.0027 | <.0001 | -0.0980 | 0.0107 | <.0001 |
| January Indicator | -0.0492 | 0.0070 | <.0001 | -0.2058 | 0.0246 | <.0001 | 0.0136 | 0.0063 | 0.0318 | -0.0747 | 0.0269 | 0.0055 |
| February Indicator | 0.1002 | 0.0068 | <.0001 | -0.1996 | 0.0246 | <.0001 | 0.0687 | 0.0063 | <.0001 | -0.0921 | 0.0271 | 0.0007 |
| March Indicator | 0.2638 | 0.0068 | <.0001 | 0.0559 | 0.0235 | 0.0175 | 0.1018 | 0.0063 | <.0001 | 0.0847 | 0.0265 | 0.0014 |
| April Indicator | 0.1135 | 0.0071 | <.0001 | 0.0158 | 0.0243 | 0.5160 | 0.1197 | 0.0064 | <.0001 | 0.0866 | 0.0268 | 0.0013 |
| May Indicator | 0.0747 | 0.0072 | <.0001 | 0.0716 | 0.0242 | 0.0031 | 0.0970 | 0.0065 | <.0001 | 0.0981 | 0.0270 | 0.0003 |
| June Indicator | 0.0789 | 0.0072 | <.0001 | 0.1005 | 0.0242 | <.0001 | 0.0669 | 0.0066 | <.0001 | 0.1337 | 0.0269 | <.0001 |
| July Indicator | 0.0902 | 0.0072 | <.0001 | 0.1030 | 0.0241 | <.0001 | 0.0521 | 0.0066 | <.0001 | 0.2052 | 0.0264 | <.0001 |
| August Indicator | 0.0330 | 0.0072 | <.0001 | 0.1010 | 0.0240 | <.0001 | 0.0438 | 0.0066 | <.0001 | 0.1619 | 0.0265 | <.0001 |
| September Indicator| -0.0726 | 0.0073 | <.0001 | 0.0226 | 0.0243 | 0.3517 | 0.0534 | 0.0065 | <.0001 | 0.1718 | 0.0263 | <.0001 |
| October Indicator | -0.0024 | 0.0072 | 0.7355 | 0.0482 | 0.0239 | 0.0437 | 0.0237 | 0.0065 | 0.0003 | 0.1586 | 0.0261 | <.0001 |
| November Indicator| -0.0655 | 0.0072 | <.0001 | -0.0471 | 0.0243 | 0.0524 | 0.0334 | 0.0064 | <.0001 | 0.0691 | 0.0265 | 0.0091 |

**Table 32. Segment: NPL - sdq, Enterprise 2**

| | <div style="text-align:center">Event: RPL</div> | | | <div style="text-align:center">Event: Prepay</div> | | | <div style="text-align:center">Event: LDQ</div> | | | <div style="text-align:center">Event: DDQ</div> | | | <div style="text-align:center">Event: Default</div> | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Variable Name** | **Est** | **StdErr** | **Probt** | **Est** | **StdErr** | **Probt** | **Est** | **StdErr** | **Probt** | **Est** | **StdErr** | **Probt** | **Est** | **StdErr** | **Probt** |
| Intercept | 12.1270 | 2.0685 | <.0001 | -15.8459 | 1.8931 | <.0001 | 9.0026 | 3.8680 | 0.0199 | -23.0566 | 1.2491 | <.0001 | 48.6970 | 15.3094 | 0.0015 |
| Refinance Rate | -0.0611 | 0.0062 | <.0001 | -0.2563 | 0.0149 | <.0001 | -0.1341 | 0.0115 | <.0001 | 0.0406 | 0.0048 | <.0001 | 0.0487 | 0.0075 | <.0001 |
| Cash Out | -0.1490 | 0.0063 | <.0001 | -0.3952 | 0.0162 | <.0001 | -0.1236 | 0.0116 | <.0001 | 0.0443 | 0.0047 | <.0001 | -0.0961 | 0.0080 | <.0001 |
| Investment | 0.2790 | 0.0131 | <.0001 | -0.1345 | 0.0302 | <.0001 | 0.5528 | 0.0272 | <.0001 | 0.1493 | 0.0080 | <.0001 | 0.1543 | 0.0120 | <.0001 |
| Second Home | -0.2810 | 0.0157 | <.0001 | 0.9319 | 0.0366 | 0.3836 | -0.5281 | 0.0240 | <.0001 | 0.0866 | 0.0091 | <.0001 | 0.3072 | 0.0134 | <.0001 |
| Age | 0.0058 | 0.0002 | <.0001 | -0.0186 | 0.0005 | <.0001 | 0.0020 | 0.0004 | <.0001 | 0.0059 | 0.0002 | <.0001 | -0.0086 | 0.0003 | <.0001 |
| Age Sq. | 0.0000 | | <.0001 | 0.0000 | | <.0001 | 0.0000 | | <.0001 | 0.0000 | | <.0001 | 0.0000 | | <.0001 |
| Current UPB (000s) | 0.0025 | 0.0001 | <.0001 | 0.0031 | 0.0002 | <.0001 | -0.0002 | 0.0002 | 0.3148 | -0.0001 | 0.0001 | 0.3462 | -0.0088 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | -0.0344 | | <.0001 | -0.0610 | | <.0001 | -0.0031 | | 0.4431 | 0.0068 | | <.0001 | 0.1200 | | <.0001 |
| Debt to Income Ratio| 0.0007 | 0.0007 | 0.2955 | 0.0013 | 0.0007 | 0.0889 | 0.0007 | 0.0015 | 0.6322 | -0.0002 | 0.0007 | 0.7789 | -0.0017 | 0.0021 | 0.4193 |
| Credit Score | -0.0014 | 0.0001 | <.0001 | 0.0028 | 0.0002 | <.0001 | -0.0033 | 0.0001 | <.0001 | 0.0003 | 0.0000 | <.0001 | 0.0047 | 0.0001 | <.0001 |
| Burnout Count | 0.0046 | 0.0002 | <.0001 | 0.0014 | 0.0004 | 0.0005 | 0.0046 | 0.0003 | <.0001 | -0.0014 | 0.0002 | <.0001 | -0.0005 | 0.0003 | 0.0686 |
| Sato F30 | -0.0529 | 0.0051 | <.0001 | 0.0316 | 0.0128 | 0.0136 | 0.0141 | 0.0090 | 0.1165 | 0.0285 | 0.0038 | <.0001 | -0.0033 | 0.0061 | 0.5894 |
| Judicial State | 0.2736 | 0.0050 | <.0001 | -0.2907 | 0.0121 | <.0001 | -0.3640 | 0.0092 | <.0001 | 0.2659 | 0.0038 | <.0001 | -1.1195 | 0.0068 | <.0001 |
| 2005-2008 Indicator | -0.0372 | 0.0078 | <.0001 | -0.6980 | 0.0190 | <.0001 | 0.2419 | 0.0133 | <.0001 | 0.0400 | 0.0062 | <.0001 | -0.4657 | 0.0047 | <.0001 |
| 2009-2013 Indicator | 0.0400 | 0.0096 | <.0001 | -0.6041 | 0.0194 | <.0001 | 0.5378 | 0.0182 | <.0001 | 0.1510 | 0.0080 | <.0001 | -0.5152 | 0.0121 | <.0001 |
| >2014 Indicator | 0.4730 | 0.0139 | <.0001 | -0.9199 | 0.0296 | <.0001 | -0.3982 | 0.0291 | <.0001 | 0.0671 | 0.0145 | <.0001 | -1.0405 | 0.0235 | <.0001 |
| No Full Doc Loan | 0.0156 | 0.0131 | 0.2342 | -0.1454 | 0.0355 | <.0001 | -0.0108 | 0.0237 | 0.6486 | -0.0637 | 0.0090 | <.0001 | 0.2924 | 0.0126 | <.0001 |
| Fixed Rate Mortgage 40 YR | 0.2808 | 0.0479 | <.0001 | -0.0605 | 0.1470 | 0.6807 | 0.0338 | 0.0930 | 0.7167 | 0.0151 | 0.0350 | 0.6667 | -0.4345 | 0.0633 | <.0001 |
| Fixed Rate Mortgage 30 YR | 0.2318 | 0.0094 | <.0001 | 0.0077 | 0.0262 | 0.7694 | 0.1302 | 0.0175 | <.0001 | -0.0248 | 0.0062 | <.0001 | -0.1919 | 0.0088 | <.0001 |
| Fixed Rate Mortgage 15 YR | 0.4206 | 0.0120 | <.0001 | -0.1130 | 0.0289 | <.0001 | 0.1404 | 0.0221 | <.0001 | 0.0079 | 0.0091 | 0.3827 | -0.2777 | 0.0156 | <.0001 |
| Non Fixed Rate Mortgage| 0.0000 | | | 0.0000 | | | 0.0000 | | | 0.0000 | | | 0.0000 | | |
| One Borrower Indicator| 0.0363 | 0.0515 | 0.4806 | -0.2984 | 0.1334 | 0.0253 | -0.1079 | 0.0905 | 0.3822 | 0.0837 | 0.0410 | 0.0414 | 0.4020 | 0.0705 | <.0001 |
| Credit Score x One Borrower (00s) | -0.0100 | 0.0001 | 0.1807 | 0.0326 | 0.0002 | 0.0934 | -0.0280 | 0.0001 | 0.0389 | -0.0020 | 0.0001 | 0.6966 | -0.0740 | 0.0001 | <.0001 |
| Junior Lien Indicator| -0.1257 | 0.0083 | <.0001 | -0.2389 | 0.0199 | <.0001 | -0.1355 | 0.0144 | <.0001 | 0.0364 | 0.0052 | <.0001 | 0.0957 | 0.0081 | <.0001 |
| Alta Loan Indicator | 0.1300 | 0.0113 | <.0001 | -0.1581 | 0.0384 | <.0001 | -0.0939 | 0.0210 | <.0001 | 0.0283 | 0.0072 | <.0001 | -0.0048 | 0.0121 | 0.6891 |
| IO Loan Indicator | 0.0000 | | | 0.0000 | | | | | | 0.0000 | | | 0.0000 | | |
| Jumbo Loan Indicator| 0.0490 | 0.0481 | 0.3079 | 0.3866 | 0.1070 | 0.0003 | 0.1141 | 0.1114 | 0.3054 | -0.0740 | 0.0474 | 0.1186 | -1.2237 | 0.1445 | <.0001 |
| max(0,unemp_rate-9)| 0.2033 | 0.0484 | <.0001 | 0.0664 | 0.0896 | 0.4588 | -1.0489 | 0.0961 | 0.6107 | 0.0289 | 0.0532 | 0.5868 | 0.3569 | 0.1041 | 0.0006 |
| max(0,9-unemp_rate)| -0.1095 | 0.0478 | 0.0220 | 0.1766 | 0.0866 | 0.0415 | 0.1058 | 0.0951 | 0.2658 | -0.0460 | 0.0528 | 0.3753 | -0.3157 | 0.1037 | 0.0023 |
| max(0,unemp_rate-7)| 0.0591 | 0.0112 | <.0001 | -0.0353 | 0.0292 | 0.2262 | 0.0092 | 0.0204 | 0.6523 | -0.0244 | 0.0085 | 0.0043 | -0.0209 | 0.0133 | 0.1165 |
| max(0,unemp_rate-3)| 0.1934 | 0.0498 | 0.0001 | 0.0576 | 0.0913 | 0.5276 | 0.0573 | 0.0988 | 0.5621 | -0.0279 | 0.0546 | 0.6092 | -0.3817 | 0.1061 | 0.0003 |
| max(0,unemp_rate-5.5)| 0.0395 | 0.0109 | 0.0003 | -0.0889 | 0.0247 | 0.0003 | -0.0190 | 0.0203 | 0.3484 | 0.0276 | 0.0084 | 0.0011 | -0.0287 | 0.0145 | 0.0486 |
| max(0,mtmltv-95) | 0.1377 | 0.0227 | <.0001 | -0.0770 | 0.0207 | 0.0002 | 0.1172 | 0.0423 | 0.0056 | -0.2248 | 0.0133 | <.0001 | 0.5847 | 0.0608 | <.0001 |
| max(0,95-mtmltv) | -0.1453 | 0.0226 | <.0001 | 0.1414 | 0.0199 | <.0001 | -0.1159 | 0.0423 | 0.0061 | 0.2232 | 0.0133 | <.0001 | -0.5908 | 0.0608 | <.0001 |
| max(0,mtmltv-50) | 0.0038 | 0.0009 | <.0001 | -0.0253 | 0.0018 | <.0001 | -0.0109 | 0.0017 | <.0001 | 0.0029 | 0.0008 | 0.0005 | -0.0056 | 0.0019 | 0.0029 |
| max(0,mtmltv-80) | 0.0099 | 0.0009 | <.0001 | -0.0599 | 0.0034 | <.0001 | -0.0013 | 0.0016 | 0.4437 | 0.0008 | 0.0007 | 0.1976 | -0.0184 | 0.0011 | <.0001 |
| max(0,mtmltv-30) | 0.0012 | 0.0017 | 0.4970 | 0.0131 | 0.0028 | <.0001 | -0.0003 | 0.0032 | 0.9173 | 0.0021 | 0.0016 | 0.1979 | -0.0042 | 0.0049 | 0.3876 |
| max(0,mtmltv-140) | 0.0005 | 0.0008 | 0.5105 | 0.0143 | 0.0179 | 0.4241 | 0.0014 | 0.0021 | 0.5018 | -0.0006 | 0.0004 | 0.1838 | -0.0097 | 0.0007 | <.0001 |
| max(0,mtmltv-5) | -0.1525 | 0.0231 | <.0001 | 0.1060 | 0.0209 | <.0001 | -0.1156 | 0.0431 | 0.0073 | 0.2219 | 0.0138 | <.0001 | 0.5479 | 0.0706 | <.0001 |
| Refi Incentive with 2 months lag | 0.1430 | 0.0048 | <.0001 | 0.0456 | 0.0113 | <.0001 | -0.0007 | 0.0088 | 0.9381 | 0.0904 | 0.0039 | <.0001 | -0.0176 | 0.0062 | 0.0043 |
| January Indicator | -0.0180 | 0.0121 | 0.1372 | -0.1641 | 0.0308 | <.0001 | -0.1737 | 0.0221 | <.0001 | 0.0156 | 0.0090 | 0.0825 | 0.0298 | 0.0148 | 0.0447 |
| February Indicator | 0.0195 | 0.0119 | 0.0999 | -0.1605 | 0.0304 | <.0001 | -0.1221 | 0.0216 | <.0001 | -0.0190 | 0.0090 | 0.0347 | 0.0144 | 0.0148 | 0.3295 |
| March Indicator | 0.1689 | 0.0114 | <.0001 | 0.0926 | 0.0284 | 0.0011 | -0.0819 | 0.0205 | <.0001 | -0.0216 | 0.0089 | 0.0159 | 0.0763 | 0.0145 | <.0001 |
| April Indicator | 0.0677 | 0.0116 | <.0001 | 0.0545 | 0.0285 | 0.0560 | 0.0753 | 0.0205 | 0.0002 | -0.0306 | 0.0089 | 0.0006 | 0.0371 | 0.0146 | 0.0111 |
| May Indicator | 0.0126 | 0.0118 | 0.2858 | 0.1446 | 0.0279 | <.0001 | -0.0925 | 0.0213 | <.0001 | -0.0007 | 0.0089 | 0.9396 | -0.0509 | 0.0146 | 0.0005 |
| June Indicator | 0.1406 | 0.0115 | <.0001 | 0.1055 | 0.0283 | 0.0002 | -0.0381 | 0.0211 | 0.0712 | 0.0350 | 0.0088 | <.0001 | 0.0907 | 0.0145 | <.0001 |
| July Indicator | 0.0664 | 0.0117 | <.0001 | 0.1195 | 0.0284 | <.0001 | 0.0142 | 0.0210 | 0.4983 | 0.0754 | 0.0088 | <.0001 | 0.1330 | 0.0145 | <.0001 |
| August Indicator | 0.1124 | 0.0117 | <.0001 | 0.1064 | 0.0288 | 0.0002 | -0.1040 | 0.0218 | <.0001 | 0.1175 | 0.0088 | <.0001 | 0.1780 | 0.0145 | <.0001 |
| September Indicator| 0.0032 | 0.0120 | 0.7878 | 0.0240 | 0.0295 | 0.4135 | -0.1306 | 0.0220 | <.0001 | 0.1240 | 0.0088 | <.0001 | 0.1210 | 0.0147 | <.0001 |
| October Indicator | -0.0145 | 0.0121 | 0.2303 | 0.0699 | 0.0292 | 0.0164 | -0.1088 | 0.0219 | <.0001 | 0.1032 | 0.0089 | <.0001 | 0.1000 | 0.0148 | <.0001 |
| November Indicator| -0.0250 | 0.0121 | 0.0385 | -0.0718 | 0.0301 | 0.0169 | -0.1593 | 0.0222 | <.0001 | 0.0584 | 0.0089 | <.0001 | -0.0368 | 0.0149 | 0.0137 |

**Table 33. Segment: NPL - ddq, Enterprise 2**

| | <div style="text-align:center">Event: RPL</div> | | | <div style="text-align:center">Event: Prepay</div> | | | <div style="text-align:center">Event: LDQ</div> | | | <div style="text-align:center">Event: SDQ</div> | | | <div style="text-align:center">Event: Default</div> | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Variable Name** | **Est** | **StdErr** | **Probt** | **Est** | **StdErr** | **Probt** | **Est** | **StdErr** | **Probt** | **Est** | **StdErr** | **Probt** | **Est** | **StdErr** | **Probt** |
| Intercept | 9.6821 | 3.3201 | 0.0035 | 3.3402 | 2.9108 | 0.2512 | -11.1738 | 8.4166 | 0.1843 | 9.6171 | 5.6048 | 0.0862 | 29.8447 | 6.8475 | <.0001 |
| Refinance Rate | 0.0921 | 0.0087 | <.0001 | -0.3411 | 0.0209 | <.0001 | 0.0222 | 0.0376 | 0.5531 | -0.1793 | 0.0192 | <.0001 | 0.0786 | 0.0064 | <.0001 |
| Cash Out | 0.1575 | 0.0084 | <.0001 | -0.4499 | 0.0217 | <.0001 | 0.0592 | 0.0363 | 0.1022 | -0.2228 | 0.0190 | <.0001 | -0.0415 | 0.0063 | <.0001 |
| Investment | -0.3405 | 0.0173 | <.0001 | -0.3678 | 0.0420 | <.0001 | -0.3968 | 0.0754 | <.0001 | -0.7562 | 0.0431 | <.0001 | -0.0274 | 0.0100 | 0.0063 |
| Second Home | -0.3858 | 0.0203 | <.0001 | 0.0233 | 0.0472 | 0.6216 | -0.3546 | 0.0903 | <.0001 | 0.5762 | 0.0526 | <.0001 | 0.1408 | 0.0119 | <.0001 |
| Age | 0.0030 | 0.0003 | <.0001 | -0.0272 | 0.0007 | <.0001 | -0.0067 | 0.0014 | <.0001 | -0.0151 | 0.0007 | <.0001 | -0.0063 | 0.0003 | <.0001 |
| Age Sq. | 0.0000 | | <.0001 | 0.0000 | | <.0001 | 0.0000 | | <.0001 | 0.0000 | | <.0001 | 0.0000 | | <.0001 |
| Current UPB (000s) | -0.0011 | 0.0001 | <.0001 | 0.0020 | 0.0003 | <.0001 | -0.0033 | 0.0004 | <.0001 | -0.0041 | 0.0003 | <.0001 | -0.0059 | 0.0001 | <.0001 |
| Current UPB (00000s) Sq. | 0.0572 | | <.0001 | -0.0369 | | <.0001 | 0.0914 | | <.0001 | 0.0595 | | <.0001 | 0.0659 | | <.0001 |
| Debt to Income Ratio| -0.0001 | 0.0008 | 0.9058 | -0.0107 | 0.0132 | 0.4183 | -0.0181 | 0.0329 | 0.5820 | -0.0119 | 0.0141 | 0.4008 | -0.0005 | 0.0009 | 0.6328 |
| Credit Score | -0.0011 | 0.0001 | <.0001 | 0.0022 | 0.0002 | <.0001 | -0.0027 | 0.0003 | <.0001 | -0.0031 | 0.0002 | <.0001 | 0.0025 | 0.0001 | <.0001 |
| Burnout Count | 0.0028 | 0.0003 | <.0001 | 0.0054 | 0.0006 | <.0001 | 0.0017 | 0.0012 | 0.1507 | 0.0043 | 0.0006 | <.0001 | 0.0006 | 0.0002 | 0.0059 |
| Sato F30 | -0.0299 | 0.0067 | <.0001 | 0.0630 | 0.0164 | 0.0001 | -0.0822 | 0.0281 | 0.0034 | -0.0349 | 0.0141 | 0.0134 | -0.0123 | 0.0050 | 0.0137 |
| Judicial State | -0.5271 | 0.0068 | <.0001 | -0.3628 | 0.0163 | <.0001 | -0.6058 | 0.0292 | <.0001 | -0.7353 | 0.0150 | <.0001 | -0.3474 | 0.0051 | <.0001 |
| 2005-2008 Indicator | -0.4593 | 0.0120 | <.0001 | -0.8196 | 0.0258 | <.0001 | -0.4771 | 0.0496 | <.0001 | -0.4198 | 0.0231 | <.0001 | -0.0910 | 0.0088 | <.0001 |
| 2009-2013 Indicator | -0.2507 | 0.0158 | <.0001 | -0.8890 | 0.0284 | <.0001 | -0.5400 | 0.0669 | <.0001 | -0.8507 | 0.0322 | <.0001 | -0.2187 | 0.0118 | <.0001 |
| >2014 Indicator | 0.1713 | 0.0276 | <.0001 | -1.1352 | 0.0495 | <.0001 | -0.1530 | 0.1154 | 0.1928 | -0.7275 | 0.0571 | <.0001 | -0.4278 | 0.0239 | <.0001 |
| No Full Doc Loan | 0.1085 | 0.0168 | <.0001 | -0.0882 | 0.0486 | 0.0698 | -0.1088 | 0.0804 | 0.1756 | 0.2304 | 0.0374 | <.0001 | 0.0816 | 0.0118 | <.0001 |
| Fixed Rate Mortgage 40 YR | 0.0501 | 0.0600 | 0.4043 | 0.1644 | 0.1768 | 0.3535 | 0.2404 | 0.2288 | 0.2935 | -0.0288 | 0.1377 | 0.8345 | -0.2616 | 0.0472 | <.0001 |
| Fixed Rate Mortgage 30 YR | 0.2396 | 0.0114 | <.0001 | 0.1118 | 0.0350 | 0.0014 | 0.2062 | 0.0509 | <.0001 | 0.0247 | 0.0272 | 0.3645 | -0.1102 | 0.0079 | <.0001 |
| Fixed Rate Mortgage 15 YR | 0.5553 | 0.0159 | <.0001 | -0.2076 | 0.0382 | <.0001 | 0.4084 | 0.0691 | <.0001 | -0.0866 | 0.0354 | 0.0144 | -0.1865 | 0.0127 | <.0001 |
| Non Fixed Rate Mortgage| 0.0000 | | | 0.0000 | | | 0.0000 | | | 0.0000 | | | 0.0000 | | |
| One Borrower Indicator| -0.0271 | 0.0704 | 0.6998 | 0.0972 | 0.1741 | 0.5769 | -0.1371 | 0.2885 | 0.6346 | -0.0965 | 0.1454 | 0.7669 | 0.1534 | 0.0566 | 0.0068 |
| Credit Score x One Borrower (00s) | -0.0040 | 0.0001 | 0.7341 | -0.0340 | 0.0003 | 0.1775 | -0.0050 | 0.0004 | 0.9076 | -0.0250 | 0.0002 | 0.2454 | -0.0360 | 0.0000 | <.0001 |
| Junior Lien Indicator| -0.0689 | 0.0096 | <.0001 | -0.2464 | 0.0269 | <.0001 | -0.2042 | 0.0442 | <.0001 | -0.1072 | 0.0230 | <.0001 | 0.0943 | 0.0067 | <.0001 |
| Alta Loan Indicator | -0.1796 | 0.0134 | <.0001 | -0.2430 | 0.0481 | <.0001 | -0.1108 | 0.0586 | 0.0587 | -0.1625 | 0.0323 | <.0001 | -0.0439 | 0.0092 | <.0001 |
| IO Loan Indicator | 0.0000 | | | 0.0000 | | | | | | 0.0000 | | | 0.0000 | | |
| Jumbo Loan Indicator| 0.8943 | 0.0729 | <.0001 | 0.2334 | 0.1408 | 0.0974 | -0.9295 | 0.2987 | 0.0019 | -0.6208 | 0.2216 | 0.0051 | -1.5983 | 0.0969 | <.0001 |
| max(0,unemp_rate-9)| 0.1726 | 0.0801 | 0.0312 | 0.3765 | 0.1324 | 0.0045 | -0.1589 | 0.3282 | 0.6283 | -0.0527 | 0.1601 | 0.7421 | 0.4876 | 0.0784 | <.0001 |
| max(0,9-unemp_rate)| -0.1020 | 0.0794 | 0.1990 | -0.2083 | 0.1290 | 0.1064 | 0.1973 | 0.3250 | 0.5437 | 0.1216 | 0.1584 | 0.4425 | -0.3973 | 0.0780 | <.0001 |
| max(0,unemp_rate-7)| 0.0047 | 0.0146 | 0.7483 | 0.0809 | 0.0386 | 0.0363 | 0.1833 | 0.0634 | 0.0038 | 0.1233 | 0.0330 | 0.0002 | 0.1860 | 0.0108 | <.0001 |
| max(0,unemp_rate-3)| 0.1930 | 0.0821 | 0.0187 | -0.1550 | 0.1351 | 0.2505 | 0.0036 | 0.3367 | 0.9914 | 0.0014 | 0.1644 | 0.9934 | -0.4884 | 0.0799 | <.0001 |
| max(0,unemp_rate-5.5)| -0.0136 | 0.0151 | 0.3644 | -0.0407 | 0.0337 | 0.2276 | -0.2197 | 0.0644 | 0.0006 | -0.0495 | 0.0330 | 0.1339 | -0.1754 | 0.0114 | <.0001 |
| max(0,mtmltv-95) | 0.1239 | 0.0363 | 0.0006 | 0.1059 | 0.0319 | 0.0009 | -0.0822 | 0.0900 | 0.3611 | 0.1175 | 0.0610 | 0.0540 | 0.3575 | 0.0757 | <.0001 |
| max(0,95-mtmltv) | -0.1323 | 0.0363 | 0.0003 | -0.0320 | 0.0308 | 0.2990 | 0.0790 | 0.0898 | 0.3797 | -0.1109 | 0.0610 | 0.0688 | -0.3564 | 0.0757 | <.0001 |
| max(0,mtmltv-50) | 0.0042 | 0.0014 | 0.0034 | -0.0384 | 0.0024 | <.0001 | -0.0123 | 0.0059 | 0.0379 | -0.0175 | 0.0028 | <.0001 | -0.0190 | 0.0014 | <.0001 |
| max(0,mtmltv-80) | 0.0133 | 0.0012 | <.0001 | -0.0504 | 0.0053 | <.0001 | 0.0142 | 0.0052 | 0.0069 | -0.0022 | 0.0027 | 0.4190 | -0.0166 | 0.0009 | <.0001 |
| max(0,mtmltv-30) | -0.0047 | 0.0027 | 0.0761 | 0.0019 | 0.0035 | 0.5803 | 0.0152 | 0.0106 | 0.1541 | 0.0047 | 0.0051 | 0.3562 | 0.0106 | 0.0033 | 0.0011 |
| max(0,mtmltv-140) | -0.0065 | 0.0007 | <.0001 | 0.0348 | 0.0153 | 0.0230 | -0.0075 | 0.0035 | 0.0333 | 0.0005 | 0.0028 | 0.8677 | -0.0023 | 0.0005 | <.0001 |
| max(0,mtmltv-5) | -0.1259 | 0.0370 | 0.0007 | -0.0616 | 0.0319 | 0.0530 | 0.0725 | 0.0934 | 0.4375 | -0.1118 | 0.0624 | 0.0730 | -0.3274 | 0.0764 | <.0001 |
| Refi Incentive with 2 months lag | -0.1977 | 0.0069 | <.0001 | -0.1565 | 0.0159 | <.0001 | 0.0781 | 0.0294 | 0.0079 | -0.2244 | 0.0148 | <.0001 | -0.0980 | 0.0052 | <.0001 |
| January Indicator | 0.0463 | 0.0161 | 0.0039 | -0.2056 | 0.0403 | <.0001 | -0.2617 | 0.0639 | <.0001 | -0.2274 | 0.0354 | <.0001 | -0.0479 | 0.0120 | <.0001 |
| February Indicator | 0.0271 | 0.0161 | 0.0933 | -0.2468 | 0.0406 | <.0001 | -0.3039 | 0.0645 | <.0001 | -0.2142 | 0.0351 | <.0001 | -0.0683 | 0.0120 | <.0001 |
| March Indicator | 0.1333 | 0.0157 | <.0001 | -0.0297 | 0.0384 | 0.4395 | -0.2007 | 0.0627 | 0.0014 | -0.0700 | 0.0338 | 0.0386 | 0.0094 | 0.0118 | 0.4251 |
| April Indicator | 0.0145 | 0.0161 | 0.3657 | 0.0092 | 0.0380 | 0.8083 | -0.3383 | 0.0652 | <.0001 | 0.1151 | 0.0342 | 0.0008 | -0.0578 | 0.0120 | <.0001 |
| May Indicator | 0.0030 | 0.0161 | 0.8505 | 0.0374 | 0.0378 | 0.3213 | -0.1736 | 0.0624 | 0.0054 | -0.1214 | 0.0343 | 0.0004 | 0.1889 | 0.0114 | <.0001 |
| June Indicator | -0.1359 | 0.0157 | <.0001 | 0.0363 | 0.0378 | 0.3362 | -0.2527 | 0.0637 | <.0001 | -0.1544 | 0.0345 | <.0001 | -0.0239 | 0.0119 | 0.0448 |
| July Indicator | -0.0364 | 0.0159 | 0.0221 | 0.0257 | 0.0378 | 0.4963 | -0.4875 | 0.0682 | <.0001 | 0.1049 | 0.0341 | 0.0021 | 0.0464 | 0.0117 | <.0001 |
| August Indicator | 0.0909 | 0.0158 | <.0001 | 0.0256 | 0.0378 | 0.4974 | -0.4500 | 0.0675 | <.0001 | -0.1305 | 0.0343 | 0.0001 | 0.1476 | 0.0115 | <.0001 |
| September Indicator| 0.1108 | 0.0160 | <.0001 | -0.0721 | 0.0385 | 0.0612 | -0.3083 | 0.0645 | <.0001 | 0.1921 | 0.0347 | <.0001 | 0.0248 | 0.0118 | 0.0347 |
| October Indicator | 0.1180 | 0.0159 | <.0001 | 0.0014 | 0.0378 | 0.9713 | -0.2826 | 0.0639 | <.0001 | -0.1278 | 0.0342 | 0.0002 | 0.0154 | 0.0118 | 0.1915 |
| November Indicator| 0.0457 | 0.0162 | 0.0048 | -0.0604 | 0.0383 | 0.1146 | -0.3837 | 0.0656 | <.0001 | -0.2033 | 0.0348 | <.0001 | -0.0641 | 0.0120 | <.0001 |

### 9.2 Loss Severity Model
#### 9.2.1 Net Sales Proceeds

**Table 34. Enterprise 1&2 Net Sale Proceeds Coefficients for REO properties only (disposition years 2012-2020)**
| STATE | Intercept | B1 | B2 | B3 | B4 | B5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US | -12,770 | 0.6100 | 0.4037 | -0.2962 | 0.4257 | -0.7506 |
| AK | -6,629 | 0.5896 | 0.1399 | 0.0817 | -0.0189 | -0.3981 |
| AL | -4,625 | 0.4362 | 0.6206 | -0.2467 | 0.1910 | -0.4823 |
| AR | -6,853 | 0.5092 | 0.3353 | -0.0581 | 0.0036 | -0.2365 |
| AZ | -21,142 | 0.8813 | 0.2741 | -0.4058 | 0.3300 | -0.6441 |
| CA | -24,400 | 0.9065 | 0.1832 | -0.4021 | 0.4324 | -0.8152 |
| CO | -17,019 | 0.7471 | 0.1400 | -0.1218 | -0.1299 | -0.2058 |
| CT | 4,454 | 0.4705 | 0.2142 | 0.0323 | 0.1421 | -0.2392 |
| DC | -204,334 | 1.9612 | -0.8966 | -0.6565 | 1.6885 | -1.5867 |
| DE | -22,316 | 0.6420 | 0.5005 | -0.0440 | -0.1772 | -0.2271 |
| FL | -15,634 | 0.7377 | 0.4177 | -0.3895 | 0.4998 | -0.8587 |
| GA | -13,374 | 0.6745 | 0.3974 | -0.1993 | 0.1257 | -0.4938 |
| HI | -49,182 | 0.7797 | -0.2256 | 0.2252 | 0.1202 | -0.5315 |
| IA | -4,471 | 0.4285 | 0.2619 | 0.0265 | 0.2717 | -0.2937 |
| ID | -14,382 | 0.7768 | 0.3558 | -0.5865 | 0.3144 | -0.5115 |
| IL | -9,810 | 0.5199 | 0.4761 | -0.2639 | 0.4812 | -0.7892 |
| IN | -2,522 | 0.3463 | 0.3673 | 0.0441 | 0.3125 | -0.5105 |
| KS | -1,622 | 0.4087 | 0.3278 | 0.0992 | 0.4764 | -0.6023 |
| KY | -7,191 | 0.4655 | 0.4254 | -0.0057 | 0.0560 | -0.3701 |
| LA | -5,037 | 0.4662 | 0.2961 | -0.0013 | 0.2983 | -0.5261 |
| MA | -11,433 | 0.6190 | 0.1543 | -0.2059 | 0.7204 | -1.1389 |
| MD | -20,018 | 0.6131 | 0.2978 | -0.0508 | -0.0053 | -0.3005 |
| ME | -8,024 | 0.3889 | 0.1687 | 0.1822 | 0.1107 | -0.5415 |
| MI | -7,868 | 0.5110 | 0.4240 | -0.2232 | 0.6625 | -0.9378 |
| MN | -15,567 | 0.6506 | 0.5308 | -0.4883 | 0.4825 | -0.8187 |
| MO | -2,524 | 0.3538 | 0.4809 | -0.0839 | 0.6246 | -0.8867 |
| MS | -2,226 | 0.3811 | 0.4733 | 0.0897 | -0.0627 | -0.3817 |
| MT | -19,052 | 0.6848 | 0.0579 | -0.2007 | 0.1575 | -0.4375 |
| NC | -8,053 | 0.5369 | 0.3975 | -0.1080 | 0.0404 | -0.4089 |
| ND | -6,887 | 0.4572 | 0.5572 | -0.9104 | 1.3295 | -1.2491 |
| NE | -3,621 | 0.4825 | 0.1923 | 0.4157 | -0.2405 | -0.0997 |
| NH | -7,224 | 0.5523 | 0.2285 | -0.1163 | 0.2773 | -0.5377 |
| NJ | -14,445 | 0.5891 | 0.1074 | -0.0834 | 0.4658 | -0.6003 |
| NM | -20,386 | 0.7801 | 0.0645 | -0.1154 | -0.0016 | -0.2471 |
| NV | -18,959 | 0.9179 | 0.3429 | -0.3622 | 0.2919 | -0.6829 |
| NY | -2,431 | 0.4159 | 0.2092 | 0.0949 | 0.2198 | -0.2972 |
| OH | -3,262 | 0.3570 | 0.3436 | 0.0194 | 0.4084 | -0.4390 |
| OK | -4,697 | 0.4578 | 0.3087 | 0.0407 | 0.0175 | -0.2276 |
| OR | -27,713 | 0.8434 | 0.1366 | -0.1530 | -0.0017 | -0.4396 |
| PA | -3,775 | 0.4049 | 0.3180 | -0.1013 | 0.2682 | -0.3375 |
| PR | -7,975 | 0.7121 | -0.0190 | -0.0285 | -0.0194 | -0.2714 |
| RI | -10,096 | 0.5592 | 0.2087 | -0.1637 | 0.2259 | -0.2738 |
| SC | -10,251 | 0.5703 | 0.4202 | -0.1738 | 0.1019 | -0.4257 |
| SD | -10,164 | 0.5620 | 0.2202 | -0.2154 | 0.6774 | -0.7411 |
| TN | -15,612 | 0.6565 | 0.1536 | -0.0193 | 0.1773 | -0.4686 |
| TX | -7,780 | 0.6338 | 0.4151 | -0.6397 | 1.2427 | -1.5674 |
| UT | -23,482 | 0.8670 | 0.2005 | -0.4450 | 0.4129 | -0.6626 |
| VA | -16,643 | 0.6402 | 0.5021 | -0.4499 | 0.5944 | -1.0209 |
| VT | 4,386 | 0.2613 | 0.5016 | -0.0410 | 0.0947 | -0.6198 |
| WA | -21,531 | 0.7457 | 0.2502 | -0.1796 | 0.2995 | -0.7615 |
| WI | -6,424 | 0.4697 | 0.3741 | -0.2192 | 0.7870 | -1.1130 |
| WV | -4,826 | 0.3933 | 0.2396 | -0.0793 | 0.8209 | -1.1347 |
| WY | -12,197 | 0.6273 | 0.1832 | -0.1092 | -0.0658 | -0.1365 |

**Table 35. Enterprise 1 & 2 Net Sale Proceeds Coefficients for Foreclosure Alternative dispositions only (disposition years 2012-2020)**
| STATE | Intercept | B1 | B2 | B3 | B4 | B5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US | -12,937 | 0.6320 | 0.3170 | -0.2145 | 0.1795 | -0.4911 |
| AK | -68,471 | 1.0266 | -0.6896 | 0.4820 | 0.0220 | -0.5137 |
| AL | -4,841 | 0.4824 | 0.5270 | -0.1712 | 0.0240 | -0.3841 |
| AR | -5,739 | 0.5242 | 0.5302 | -0.3051 | 0.0035 | -0.2281 |
| AZ | -16,815 | 0.8481 | 0.2330 | -0.4189 | 0.3095 | -0.6320 |
| CA | -14,483 | 0.8291 | 0.2472 | -0.4792 | 0.2734 | -0.4455 |
| CO | -13,550 | 0.6898 | 0.1636 | -0.2747 | -0.0072 | -0.2686 |
| CT | -2,192 | 0.5489 | 0.1337 | 0.1194 | 0.0443 | -0.3845 |
| DC | 74,260 | 0.0593 | 1.0922 | -1.1669 | 1.3033 | -0.6736 |
| DE | 4,279 | 0.3450 | 1.0827 | -0.6356 | 0.4246 | -0.7439 |
| FL | -11,980 | 0.7111 | 0.4263 | -0.2612 | 0.2199 | -0.6501 |
| GA | -10,438 | 0.6745 | 0.2464 | -0.1737 | 0.2013 | -0.5950 |
| HI | -32,970 | 0.6518 | -0.0271 | 0.3030 | -0.6643 | 0.7487 |
| IA | -6,371 | 0.4959 | 0.2613 | 0.0031 | 0.1500 | -0.2253 |
| ID | -22,693 | 0.8908 | -0.2946 | 0.0305 | 0.1844 | -0.4355 |
| IL | -7,900 | 0.5103 | 0.3440 | -0.0104 | 0.1217 | -0.4532 |
| IN | -3,271 | 0.3991 | 0.3043 | 0.1270 | 0.0969 | -0.4209 |
| KS | -5,059 | 0.4862 | 0.1826 | -0.0833 | 0.8277 | -0.8301 |
| KY | -5,554 | 0.4541 | 0.3863 | 0.0774 | 0.1938 | -0.6880 |
| LA | -12,668 | 0.5804 | 0.0933 | 0.1286 | 0.1549 | -0.5041 |
| MA | -22,948 | 0.7305 | -0.2601 | 0.4076 | -0.1426 | -0.2437 |
| MD | -12,859 | 0.5709 | 0.4052 | -0.2040 | 0.0832 | -0.3182 |
| ME | -4,291 | 0.3651 | 0.5760 | -0.5830 | 0.2589 | -0.1610 |
| MI | -7,791 | 0.5356 | 0.2697 | -0.0978 | 0.3555 | -0.5246 |
| MN | -15,988 | 0.6538 | 0.3340 | -0.4419 | 1.1690 | -1.7260 |
| MO | -7,268 | 0.4520 | 0.3874 | 0.0097 | 0.1893 | -0.4564 |
| MS | -6,438 | 0.4606 | 0.6797 | -0.6163 | 0.6952 | -0.8523 |
| MT | -42,760 | 0.8780 | -0.3375 | -0.0169 | -0.2275 | 0.6137 |
| NC | -14,357 | 0.6331 | 0.3887 | -0.3090 | 0.0301 | -0.4586 |
| ND | 2,584 | 0.2871 | 1.2159 | -1.7264 | 1.1670 | -0.6065 |
| NE | 305 | 0.4178 | 0.4166 | -0.1881 | 0.4295 | -0.6463 |
| NH | -17,563 | 0.5884 | 0.0860 | -0.0849 | 0.3545 | -0.4330 |
| NJ | -18,338 | 0.6594 | 0.0980 | -0.2615 | 0.6348 | -0.7978 |
| NM | -31,814 | 0.9430 | -0.2885 | -0.0935 | 0.4370 | -0.6968 |
| NV | -9,116 | 0.8163 | 0.4322 | -0.2957 | -0.0043 | -0.4066 |
| NY | -8,927 | 0.4864 | 0.1744 | 0.0525 | 0.2968 | -0.5528 |
| OH | -6,956 | 0.4647 | 0.2601 | -0.1354 | 0.5204 | -0.5291 |
| OK | 928 | 0.3120 | 0.6845 | -0.2928 | 0.1616 | -0.3447 |
| OR | -38,353 | 0.9563 | -0.1255 | -0.1358 | -0.1202 | -0.1499 |
| PA | -5,794 | 0.4521 | 0.3631 | -0.2032 | 0.1649 | -0.1843 |
| PR | -4,320 | 0.6793 | -0.0873 | 0.0298 | -0.0651 | -0.2615 |
| RI | -47,395 | 0.8176 | -0.2674 | 0.2152 | 0.0902 | -0.4470 |
| SC | -22,490 | 0.7866 | 0.2130 | -0.1084 | -0.2170 | -0.2344 |
| SD | -7,824 | 0.4734 | 0.3574 | -0.2233 | 0.3033 | -0.4284 |
| TN | -14,437 | 0.6511 | 0.4374 | -0.2428 | -0.1311 | -0.2371 |
| TX | -9,621 | 0.6561 | 0.2907 | -0.3754 | 0.2648 | -0.3994 |
| UT | -6,463 | 0.7220 | 0.1378 | 0.0098 | -0.1421 | -0.2699 |
| VA | -25,562 | 0.7461 | 0.3102 | -0.2234 | 0.0533 | -0.4796 |
| VT | 34,558 | 0.0548 | 1.0312 | -0.5873 | -0.0926 | -0.0572 |
| WA | -13,445 | 0.6859 | 0.3682 | -0.2751 | 0.2124 | -0.6654 |
| WI | -10,068 | 0.5521 | 0.2209 | -0.0938 | 0.6046 | -1.0043 |
| WV | 6,877 | 0.2878 | 0.7027 | -0.5897 | -0.0158 | 0.5982 |
| WY | -42,640 | 0.9389 | -0.6792 | 0.6230 | -0.1416 | -0.4281 |

**Table 40. Liquidated UPB Categories by Enterprise** 

| Enterprise 1 Liquidated UPB Categories | Enterprise 2 Liquidated UPB Categories |
| :--- | :--- |
| Liquidated UPB < 95924 | Liquidated UPB < 107400 |
| 95924 <= Liquidated UPB < 162645 | 107400 <= Liquidated UPB < 179765 |
| 162645 <= Liquidated UPB < 251689 | 179765 <= Liquidated UPB < 270431 |
| Liquidated UPB >= 251689 | Liquidated UPB >= 270431 |


**Table 45. Fixed Cost for Foreclosure Alternative Dispositions (Enterprise 1)**
| STATE | Intercept | B1 | B2 | B3 | B4 | B5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| KS | 33.7624 | -0.3884 | 0.1981 | 0.0301 | 0.1045 | 0.0339 |
| KY | 61.5472 | -1.0761 | 1.2010 | -0.1312 | -0.1133 | 0.0997 |
| LA | 60.9864 | -0.9412 | 1.0347 | -0.2052 | 0.0724 | 0.0308 |
| MA | 94.0006 | -0.7641 | 0.9490 | -0.2697 | 0.0769 | 0.0052 |
| MD | 43.0862 | -0.3676 | 0.3856 | -0.0668 | 0.0373 | 0.0165 |
| ME | 143.8074 | -1.8460 | 2.5972 | -1.1291 | 0.3972 | -0.0304 |
| MI | 103.1890 | -2.6243 | 3.5366 | -1.2152 | 0.2802 | 0.0016 |
| MN | 28.8041 | -0.2774 | 0.2532 | 0.0275 | -0.0279 | 0.0103 |
| MO | 42.4799 | -0.7529 | 0.9222 | -0.3186 | 0.1248 | 0.0115 |
| MS | 22.0516 | -0.2408 | 0.1308 | 0.0229 | 0.0882 | -0.0138 |
| MT | 16.7987 | -0.1350 | 0.0935 | -0.0390 | 0.1300 | -0.1022 |
| NC | 54.1829 | -0.9110 | 1.0509 | -0.2248 | 0.0448 | 0.0333 |
| ND | 36.5955 | -0.3748 | 0.3284 | -0.0780 | 0.1147 | 0.0263 |
| NE | 22.3685 | -0.1302 | -0.3215 | 0.4346 | -0.0532 | 0.0831 |
| NH | 88.2587 | -0.9076 | 1.1821 | -0.4067 | 0.1403 | -0.0105 |
| NJ | 56.4996 | -0.4669 | 0.5579 | -0.1586 | 0.0594 | 0.0259 |
| NM | 51.7441 | -0.4805 | 0.4720 | -0.0417 | 0.0546 | -0.0307 |
| NV | 24.8223 | -0.1844 | 0.1918 | -0.0212 | 0.0084 | 0.0024 |
| NY | 75.5901 | -0.7698 | 0.7778 | -0.0592 | 0.0427 | 0.0190 |
| OH | 83.7845 | -1.5915 | 2.0193 | -0.6894 | 0.2275 | 0.0205 |
| OK | 68.8996 | -1.3265 | 1.5584 | -0.4137 | 0.1701 | -0.0069 |
| OR | 31.3947 | -0.2198 | 0.1747 | -0.0078 | 0.0538 | -0.0147 |
| PA | 93.2363 | -1.5522 | 1.7927 | -0.4311 | 0.1667 | 0.0148 |
| PR | 24.6676 | -0.0492 | -0.2333 | 0.2742 | -0.0581 | 0.0549 |
| RI | 39.9144 | -0.2982 | 0.5106 | -0.3126 | 0.1035 | -0.0014 |
| SC | 55.7951 | -0.8256 | 0.8879 | -0.1437 | 0.0314 | 0.0428 |
| SD | 13.2115 | 0.1061 | -0.2953 | -0.0359 | 0.1274 | 0.1044 |
| TN | 60.4061 | -1.2919 | 1.6058 | -0.4201 | 0.0839 | 0.0076 |
| TX | 42.0795 | -0.6645 | 0.7953 | -0.2211 | 0.0839 | -0.0046 |
| UT | 90.0846 | -1.0526 | 1.5810 | -0.6195 | 0.0788 | 0.0058 |
| VA | 19.9911 | -0.1639 | 0.1820 | -0.0736 | 0.0471 | 0.0001 |
| VI | 27.9477 | -0.1612 | 0.2209 | 0.2233 | -0.3747 | 0.0889 |
| VT | 16.0225 | 0.1093 | -0.6459 | 0.5505 | -0.0259 | -0.0167 |
| WA | 31.8490 | -0.2731 | 0.2827 | -0.0313 | 0.0088 | 0.0195 |
| WI | 52.9369 | -0.7181 | 0.7772 | -0.1985 | 0.1082 | 0.0182 |
| WV | 36.0211 | -0.4060 | 0.1468 | 0.2371 | 0.0298 | -0.0186 |
| WY | 23.0371 | -0.2509 | 0.3389 | -0.1509 | 0.0361 | 0.0041 |

**Table 46. Fixed Cost for Foreclosure Alternative Dispositions (Enterprise 2)**
| STATE | Intercept | B1 | B2 | B3 | B4 | B5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US | 59.5212 | -0.6263 | -0.1093 | 0.6521 | 0.0408 | 0.0195 |
| AK | 31.8235 | -0.2773 | 0.2119 | 0.0893 | -0.1591 | 0.1391 |
| AL | 47.2413 | -0.6647 | -0.0539 | 0.6679 | -0.0131 | 0.0462 |
| AR | 16.4704 | 0.0295 | -0.2539 | 0.3968 | -0.2518 | 0.0395 |
| AZ | 33.7405 | -0.2156 | 0.2497 | -0.2145 | 0.1711 | 0.0004 |
| CA | 20.5509 | -0.0674 | 0.0306 | 0.0547 | -0.0840 | 0.0506 |
| CO | 27.7726 | -0.1249 | 0.2333 | -0.0882 | -0.0171 | -0.0308 |
| CT | 41.6334 | -0.2099 | 0.1597 | 0.0851 | -0.0899 | 0.0295 |
| DC | 954.5213 | -8.4789 | 8.3527 | 0.0000 | 0.2492 | 0.0000 |
| DE | 62.6938 | -0.6230 | 0.7157 | 0.3926 | -0.6354 | 0.1712 |
| FL | 41.8567 | -0.2374 | 0.1620 | 0.0413 | 0.0029 | 0.0111 |
| GA | 55.7654 | -0.5034 | 0.4603 | 0.0508 | -0.1334 | 0.1210 |
| HI | 324.7684 | -2.0498 | 2.0492 | -0.3799 | 0.3863 | -0.0113 |
| IA | 63.2919 | -1.0005 | 1.0564 | -0.0369 | -0.0967 | 0.0960 |
| ID | 33.3678 | -0.1970 | 0.3156 | -0.0362 | -0.2609 | 0.1936 |
| IL | 93.0373 | -1.1886 | 1.5371 | -0.5807 | 0.1830 | 0.0210 |
| IN | 50.6721 | -0.7646 | 0.8314 | -0.5480 | 0.6174 | -0.1748 |
| KS | 36.5250 | -0.3005 | 0.6722 | -0.1428 | -0.4278 | 0.1721 |
| KY | 60.7447 | -0.8977 | 0.8410 | 0.2245 | -0.3585 | 0.1407 |
| LA | 32.4736 | -0.2916 | 0.4120 | -0.0638 | -0.1474 | 0.0535 |
| MA | 18.3947 | -0.0087 | 0.0734 | -0.0909 | -0.0163 | 0.0295 |
| MD | 38.4352 | -0.1928 | 0.1404 | 0.0199 | -0.0008 | 0.0060 |
| ME | 41.9006 | -0.1386 | 0.6700 | -0.5029 | -0.1219 | 0.0355 |
| MI | 77.0202 | -1.0953 | 1.0396 | -0.0873 | 0.0143 | 0.0961 |
| MN | 63.6950 | -0.0107 | 0.5426 | -0.5855 | -0.0130 | 0.0549 |
| MO | 33.0767 | -0.2277 | 0.4610 | -0.2976 | 0.0592 | -0.0349 |
| MS | 38.0896 | 0.3688 | -0.4247 | 0.2872 | -0.3067 | 0.0687 |
| MT | 50.9950 | -0.6112 | 0.6708 | -0.1622 | 0.1366 | -0.0730 |
| NC | 52.0286 | -0.4798 | 0.4360 | -0.0465 | 0.0634 | -0.0056 |
| ND | 68.3336 | -0.8943 | 0.9229 | -0.0464 | 0.0117 | 0.0684 |
| NE | -89.1849 | 3.0877 | 1.4480 | -4.5025 | -0.2429 | 0.3629 |
| NH | -20.1635 | 0.3912 | -0.4236 | -0.0963 | 0.0826 | 0.0141 |
| NJ | 47.9133 | -0.2435 | 0.2657 | -0.1061 | 0.0530 | 0.0074 |
| NM | 72.6396 | -0.7141 | 0.7645 | -0.1489 | 0.0493 | 0.0361 |
| NV | 18.2384 | -0.0539 | 0.7581 | -0.0847 | -0.7308 | 0.1337 |
| NY | 121.8580 | -1.3284 | 1.0955 | 0.1398 | 0.0880 | -0.0325 |
| OH | 60.1167 | 0.3590 | -0.7175 | 0.4293 | -0.2770 | 0.1799 |
| OK | 50.6357 | -0.9560 | -0.8312 | 1.3103 | 0.4728 | -0.0418 |
| OR | 57.0231 | -0.3379 | -0.1851 | 0.4216 | 0.0227 | 0.0475 |
| PA | 65.7722 | -0.5479 | 0.2824 | 0.1931 | 0.0212 | 0.0009 |
| PR | 46.0253 | 0.6009 | -0.2424 | -0.4831 | 0.1139 | 0.0370 |
| RI | 38.7495 | 0.3836 | -0.2728 | -0.2187 | 0.1405 | -0.0500 |
| SC | 35.4251 | -0.1931 | 0.4187 | -0.2097 | -0.1237 | 0.0714 |
| SD | 19.4031 | -0.0404 | -0.0033 | 0.0000 | 0.0000 | 0.0000 |
| TN | 55.1561 | -0.6919 | -0.5386 | 0.8324 | 0.4584 | -0.1113 |
| TX | 85.3453 | -0.2364 | 1.1157 | -1.0108 | 0.0780 | 0.0610 |
| UT | 26.9843 | 0.4962 | -0.1201 | -0.2490 | -0.1393 | -0.0211 |
| VA | 14.5760 | 0.0418 | 0.1728 | -0.2181 | -0.0357 | 0.0128 |
| VI | 1.7625 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| VT | -67.5559 | 0.7940 | 0.1750 | -0.9457 | -0.0949 | 0.0957 |
| WA | 37.0203 | 0.0246 | 0.2021 | -0.2278 | -0.0828 | 0.0663 |
| WI | 35.5584 | -0.5903 | 0.4086 | -0.2687 | 0.4319 | -0.0044 |
| WV | 44.4562 | 0.5511 | -0.5284 | -0.0315 | -0.0233 | 0.0068 |
| WY | -16.3683 | 0.1493 | -0.2120 | 0.0000 | -0.0235 | 0.0000 |

**Table 47. Fixed Cost (or Transaction Expenses) for Non-Performing Loan Sale Dispositions (Enterprise 1)**
| STATE | Intercept | B1 | B2 | B3 | B4 | B5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US | 29.39081 | -0.26216 | 0.26404 | -0.03274 | 0.018987 | 0.021296 |
| AK | 19.4426 | -0.13974 | 0.194466 | -0.15224 | 0.100766 | 0.005111 |
| AL | 25.48085 | -0.30231 | 0.23058 | 0.057084 | -0.00839 | 0.007202 |
| AR | 29.18113 | -0.46256 | 0.491023 | -0.12037 | 0.078855 | 0.00265 |
| AZ | 14.09432 | -0.1058 | 0.090947 | -0.0017 | 0.008403 | 0.011397 |
| CA | 11.88882 | -0.06661 | 0.070025 | -0.00858 | 0.008864 | 0.006868 |
| CO | 15.30777 | -0.10816 | 0.086874 | 0.012867 | -0.00078 | 0.015905 |
| CT | 25.05863 | -0.16659 | 0.180383 | -0.02971 | 0.016395 | 0.009551 |
| DC | 25.44852 | -0.18049 | 0.171383 | 0.016537 | -0.01722 | 0.00614 |
| DE | 20.01625 | -0.13586 | 0.07047 | 0.042779 | 0.022852 | 0.00226 |
| FL | 34.06473 | -0.28523 | 0.293704 | -0.03816 | 0.019716 | 0.024328 |
| GA | 29.80606 | -0.37491 | 0.475945 | -0.15385 | 0.053041 | -0.0074 |
| HI | 23.81148 | -0.11879 | 0.121415 | -0.02311 | 0.013511 | 0.00874 |
| IA | 33.28467 | -0.4693 | 0.517336 | -0.10679 | 0.10968 | -0.07769 |
| ID | 24.56054 | -0.28486 | 0.329444 | -0.12083 | 0.082779 | -0.0209 |
| IL | 27.9051 | -0.23216 | 0.229945 | -0.01809 | 0.012983 | 0.020793 |
| IN | 34.69314 | -0.54205 | 0.540965 | -0.05263 | 0.013456 | 0.036876 |
| KS | 29.14582 | -0.46562 | 0.486553 | -0.14911 | 0.168912 | -0.02678 |
| KY | 46.56793 | -0.70409 | 0.687709 | -0.03083 | 0.021072 | 0.005886 |
| LA | 38.44814 | -0.51371 | 0.510341 | -0.02422 | 0.051807 | -0.04448 |
| MA | 21.76046 | -0.13449 | 0.147923 | -0.02943 | 0.008404 | 0.018292 |
| MD | 18.60948 | -0.12413 | 0.11758 | -0.01184 | 0.011126 | 0.021358 |
| ME | 25.93898 | -0.22552 | 0.210255 | -0.00687 | 0.004638 | 0.017213 |
| MI | 53.2339 | -0.95747 | 1.197252 | -0.33969 | 0.101638 | -0.00815 |
| MN | 37.40145 | -0.39742 | 0.571436 | -0.22204 | 0.045523 | 0.003525 |
| MO | 29.51481 | -0.47289 | 0.622711 | -0.18237 | -0.00973 | 0.038544 |
| MS | 27.61974 | -0.40215 | 0.328605 | 0.093332 | -0.05621 | 0.039406 |
| MT | 25.3058 | -0.18027 | 0.106116 | 0.108087 | -0.08646 | 0.065491 |
| NC | 20.46653 | -0.19896 | 0.133103 | 0.047768 | -0.00877 | 0.020596 |
| ND | 35.15197 | -0.50413 | 0.08844 | 0.884303 | -0.70479 | 0.217986 |
| NE | 33.27652 | -0.43716 | 0.413482 | -0.01238 | 0.063305 | -0.02305 |
| NH | 37.36032 | -0.36301 | 0.404052 | -0.09433 | 0.087075 | -0.03028 |
| NJ | 33.49279 | -0.21322 | 0.22248 | -0.03411 | 0.008888 | 0.034182 |
| NM | 33.48826 | -0.34451 | 0.389316 | -0.10637 | 0.0399 | 0.018768 |
| NV | 11.29515 | -0.07211 | 0.074769 | -0.01505 | 0.014996 | 0.000646 |
| NY | 35.68663 | -0.23526 | 0.21127 | 0.011226 | 0.003352 | 0.025791 |
| OH | 39.73075 | -0.56135 | 0.503186 | -0.0447 | 0.094699 | 0.000973 |
| OK | 39.56837 | -0.66576 | 0.550855 | 0.051062 | 0.052374 | -0.00154 |
| OR | 22.42751 | -0.14541 | 0.15373 | -0.06742 | 0.042772 | 0.020893 |
| PA | 43.72884 | -0.55586 | 0.487228 | 0.031266 | -0.00691 | 0.050942 |
| PR | 22.14992 | -0.39628 | 0.390993 | -0.0176 | 0.030013 | -0.0208 |
| RI | 13.20695 | -0.06846 | 0.071438 | 0.006686 | -0.00282 | 0.000431 |
| SC | 32.29118 | -0.35418 | 0.294409 | 0.040026 | -0.01591 | 0.020521 |
| SD | -6.09134 | 0.261987 | -0.3474 | -0.01803 | 0.192619 | -0.119 |
| TN | 27.50024 | -0.39916 | 0.376061 | 0.034334 | -0.04849 | 0.039482 |
| TX | 22.69102 | -0.24325 | 0.237922 | 0.0017 | 0.000384 | 0.005992 |
| UT | 15.59645 | -0.10866 | 0.109657 | -0.01088 | 0.011508 | -0.0101 |
| VA | 15.42962 | -0.10944 | 0.077502 | 0.014246 | 0.005703 | 0.02688 |
| VI | 5.112422 | -0.00792 | 0 | 0 | 0 | 0 |
| VT | 19.03838 | -0.09468 | 0.011512 | 0.031093 | 0.04375 | -0.00333 |
| WA | 22.69898 | -0.18739 | 0.188943 | -0.00909 | -0.00472 | 0.01917 |
| WI | 26.68847 | -0.28133 | 0.336691 | -0.11792 | 0.056367 | 0.00968 |
| WV | 16.50412 | -0.15424 | -0.04931 | 0.203155 | -0.04184 | 0.042401 |
| WY | 7.680851 | -0.00475 | -0.13832 | 0.18366 | -0.09588 | 0.076708 |

**Table 48. Fixed Cost (or Transaction Expenses) for Non-Performing Loan Sale Dispositions (Enterprise 2)**
| STATE | Intercept | B1 | B2 | B3 | B4 | B5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US | 19.0708 | -0.1735 | 0.1822 | -0.0266 | 0.0108 | 0.0038 |
| AK | 3.8319 | -0.0343 | 0.2917 | -0.6639 | 0.4125 | 0.0158 |
| AL | 18.1130 | 0.1326 | -0.2300 | 0.0667 | 0.0109 | 0.0164 |
| AR | 35.9577 | -0.8189 | 1.0359 | -0.3167 | 0.0610 | 0.0368 |
| AZ | 4.8769 | 0.0139 | -0.0180 | 0.0070 | -0.0097 | -0.0057 |
| CA | 22.6999 | -0.1283 | 0.1859 | -0.0773 | 0.0176 | 0.0016 |
| CO | 7.7053 | -0.0151 | -0.0602 | 0.0703 | -0.0259 | 0.0360 |
| CT | 15.1129 | -0.1050 | 0.1281 | -0.0359 | 0.0071 | 0.0025 |
| DC | 3.9214 | -0.0078 | 0.0227 | -0.0197 | -0.0180 | 0.0198 |
| DE | 10.1418 | -0.0727 | 0.0659 | 0.0086 | -0.0037 | -0.0091 |
| FL | 30.2605 | -0.2809 | 0.3160 | -0.0627 | 0.0180 | 0.0033 |
| GA | 9.6381 | -0.0722 | 0.0309 | 0.0186 | 0.0165 | 0.0014 |
| HI | 14.9187 | -0.0591 | 0.0583 | -0.0001 | -0.0086 | 0.0056 |
| IA | 5.9781 | -0.0519 | 0.0948 | -0.0625 | 0.0010 | 0.0068 |
| ID | 14.6004 | -0.1561 | 0.3085 | -0.2789 | 0.1290 | -0.0085 |
| IL | 24.4571 | -0.2598 | 0.2977 | -0.0580 | 0.0137 | 0.0023 |
| IN | 9.0174 | -0.1044 | 0.1678 | -0.1316 | 0.0561 | 0.0075 |
| KS | 22.2138 | 0.6131 | -0.4683 | -0.3844 | 0.2574 | -0.0221 |
| KY | 100.0934 | -2.1444 | 3.5029 | -1.5619 | 0.1956 | -0.0012 |
| LA | 14.7683 | -0.1561 | 0.1731 | -0.0593 | 0.0086 | 0.0324 |
| MA | 10.7001 | -0.0517 | 0.0507 | -0.0011 | -0.0102 | 0.0070 |
| MD | 13.0964 | -0.0907 | 0.0963 | -0.0194 | 0.0102 | 0.0032 |
| ME | 35.4116 | -0.3545 | 0.2775 | 0.1123 | -0.0565 | 0.0148 |
| MI | 14.5730 | -0.1874 | 0.1381 | 0.0261 | 0.0180 | 0.0006 |
| MN | 7.1098 | -0.0329 | -0.0150 | 0.0634 | -0.0165 | -0.0085 |
| MO | 20.6054 | 0.3460 | -0.3504 | -0.0254 | 0.0251 | 0.0010 |
| MS | 7.5533 | -0.0636 | 0.0997 | -0.0788 | 0.0112 | 0.0264 |
| MT | 20.1671 | -0.2085 | 0.2104 | -0.0896 | 0.1296 | -0.0460 |
| NC | 26.6363 | -0.3759 | 0.4659 | -0.1475 | 0.0535 | -0.0010 |
| ND | -2.8644 | 0.5464 | -0.5922 | -0.2765 | 0.3295 | -0.0146 |
| NE | 23.3240 | -0.3050 | 0.2774 | 0.0763 | -0.1449 | 0.1059 |
| NH | 5.0810 | -0.0165 | 0.0479 | -0.0898 | 0.0213 | 0.0472 |
| NJ | 16.8384 | -0.0945 | 0.0930 | -0.0177 | 0.0134 | 0.0007 |
| NM | 15.7203 | -0.1105 | 0.0750 | 0.0354 | -0.0383 | 0.0363 |
| NV | 7.2220 | -0.0249 | 0.0055 | 0.0165 | -0.0039 | 0.0030 |
| NY | 23.5023 | -0.1594 | 0.1586 | -0.0082 | 0.0052 | 0.0016 |
| OH | 20.2435 | -0.2939 | 0.2387 | 0.0467 | -0.0048 | 0.0051 |
| OK | 11.4625 | -0.0746 | -0.1983 | 0.3678 | -0.1912 | 0.0884 |
| OR | 8.7982 | -0.0408 | 0.0526 | 0.0029 | -0.0414 | 0.0243 |
| PA | 25.4541 | -0.3355 | 0.3414 | -0.0551 | 0.0399 | 0.0037 |
| PR | -2.1136 | 0.1070 | -0.1363 | 0.0436 | -0.1580 | 0.1431 |
| RI | -1.2780 | -0.0923 | 0.0376 | 0.1679 | -0.1961 | 0.0866 |
| SC | 19.8291 | -0.2508 | 0.2245 | -0.0214 | 0.0346 | 0.0113 |
| SD | 3.4610 | -0.0164 | -0.0805 | 0.1749 | -0.0694 | -0.0076 |
| TN | 22.6046 | -0.3676 | 0.3302 | 0.0871 | -0.0789 | 0.0234 |
| TX | 27.6189 | 0.3244 | -0.3320 | -0.0019 | -0.0042 | 0.0106 |
| UT | -6.9436 | 0.0809 | -0.1487 | 0.1077 | -0.0673 | 0.0227 |
| VA | 10.6915 | -0.0889 | 0.1094 | -0.0243 | -0.0143 | 0.0173 |
| VI | 0.2724 | 0.0009 | -0.0172 | 0.0174 | -0.0008 | 0.0000 |
| VT | 2.2661 | 0.0243 | 0.0011 | -0.0924 | 0.0831 | -0.0259 |
| WA | 10.9757 | -0.0638 | 0.0634 | -0.0325 | 0.0386 | -0.0117 |
| WI | 25.1053 | -0.3660 | 0.5381 | -0.2103 | 0.0204 | 0.0123 |
| WV | 18.8994 | 0.3291 | -0.3100 | -0.0461 | -0.0037 | 0.0321 |
| WY | -19.8514 | 0.1882 | -0.2073 | 0.0046 | 0.0165 | 0.1918 |
*Many fixed cost categories are zero for NPL sales.*

#### 9.2.4 Carrying Costs
Carrying costs for defaulted loan i ($Carrying\ Costs_i$) are defined as carrying costs times the number of months from last paid installment date to REO liquidation date. For foreclosure alternatives carrying costs are calculated from last paid installment date to title transfer date (liquidation).

$$
Carrying\ Costs_i = (Property\ taxes_i + Property\ insurance_i + HOA\ fees_i + Condominimum\ fees_i \\
+ Maintenance\ fees_i) * Number\ of\ months\ from\ Last\ Paid\ Installment\ Rate\ to\ REO\ liquidation \\
\forall\ i \in REO
$$

$$
Carrying\ Costs_i = (Property\ taxes_i + Property\ insurance_i + HOA\ fees_i + Condominimum\ fees_i \\
+ Maintenance\ fees_i) * Number\ of\ months\ from\ Last\ Paid\ Installment\ Date\ to\ title\ transfer\ date \\
\forall\ i \in Foreclosure\ alternative
$$

**Months from Foreclosure to REO Property Disposition**
The number of months from foreclosure to property disposition is estimated for both Enterprises for REOs that have completed their disposition between 2012 and 2020. This measure is the liquidated UPB weighted average months from foreclosure completion date to property disposition date. Months from foreclosure date to property disposition date are multiplied by calculated monthly carrying costs to create total for REO dispositions. See table below for weighted average months by Enterprise.

**Table 49. Liquidation UPB-weighted Average Months to REO Disposition, by Enterprise**

| State | <div style="text-align:center">Enterprise 1</div> | <div style="text-align:center">Enterprise 2</div> |
| :--- | :---: | :---: |
| | **Liquidation UPB Weighted Average Months to REO Disposition** | **Liquidation UPB Weighted Average Months to REO Disposition** |
| US | 8.6 | 8.4 |
| AK | 8.6 | 9.9 |
| AL | 7.3 | 7.6 |
| AR | 6.4 | 7.1 |
| AZ | 5.8 | 5.5 |
| CA | 8.2 | 7.6 |
| CO | 7.2 | 7.3 |
| CT | 9.4 | 9.1 |
| DC | 12.6 | 16.7 |
| DE | 8.2 | 9.0 |
| FL | 7.1 | 7.0 |
| GA | 6.8 | 6.8 |
| HI | 14.7 | 16.6 |
| IA | 6.3 | 6.6 |
| ID | 7.0 | 6.4 |
| IL | 10.8 | 10.6 |
| IN | 6.3 | 5.2 |
| KS | 8.3 | 8.8 |
| KY | 8.9 | 8.6 |
| LA | 7.0 | 7.8 |
| MA | 10.0 | 11.6 |
| MD | 12.4 | 13.9 |
| ME | 6.6 | 7.7 |
| MI | 10.6 | 11.7 |
| MN | 10.9 | 11.7 |
| MO | 6.8 | 6.5 |
| MS | 6.8 | 7.3 |
| MT | 8.0 | 7.0 |
| NC | 6.7 | 6.7 |
| ND | 11.9 | 11.8 |
| NE | 6.2 | 6.2 |
| NH | 8.7 | 8.9 |
| NJ | 11.1 | 10.9 |
| NM | 10.5 | 11.2 |
| NV | 6.7 | 6.6 |
| NY | 11.1 | 12.7 |
| OH | 7.9 | 8.6 |
| OK | 6.9 | 7.7 |
| OR | 12.2 | 8.9 |
| PA | 8.0 | 8.4 |
| PR | 11.5 | 13.8 |
| RI | 7.4 | 9.8 |
| SC | 6.8 | 7.2 |
| SD | 10.3 | 12.9 |
| TN | 7.2 | 6.7 |
| TX | 7.4 | 7.4 |
| UT | 6.0 | 6.2 |
| VA | 7.8 | 7.3 |
| VT | 11.7 | 11.4 |
| WA | 7.7 | 7.0 |
| WI | 8.0 | 7.9 |
| WV | 9.8 | 7.7 |
| WY | 12.0 | 10.9 |

#### 9.2.5 Loss Severity Module Variable Definition
Loss Severity Module involves numerous definitions and variables. Below is a table summarizing the major variables in the module.

**Table 50. Loss Severity Module Fields and Definitions**

**Accounting transaction types**
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

**Other Loss severity data**
* **Foreclosure date** - the date when the foreclosure is completed and the title has been transferred from borrower to the Enterprises.
* **Disposition date** - the date the REO property is sold from REO inventory
* **Sale price at liquidation** - the sale price of the property at liquidation date for foreclosure alternatives (third party sale and short sale)
* **Dummy variable Judicial state** - this dummy identifies the states that have foreclosures go through the courts. These are states Connecticut (CT), Delaware (DE), Florida (FL), Hawaii (HI), Iowa (IA), Illinois (IL), Indiana (IN), Kansas (KS), Kentucky (KY), Louisiana (LA), Maine (ME), North Dakota (ND), New Jersey (NJ), New Mexico (NM), New York (NY), Ohio (OH), Oklahoma (OK), Pennsylvania (PA), South Carolina (SC), Vermont (VT), and Wisconsin (WI).
* **Dummy variable non-Judicial state** - all other states do not have court proceedings to complete the foreclosure.
* **Net sale proceeds** = Gross sale proceeds or note sale proceeds minus the sum of sales expense - other selling expense - broker fees - borrower closing costs
* **Fixed costs for foreclosure and foreclosure alternatives** = the sum of appraisal fees + attorney and trustee fees + other foreclosure expenses + other liquidation expenses + maintenance expense + property inspection + repairs + utilities.
* **Fixed costs ratio for foreclosure and foreclosure alternatives** = (fixed costs/liquidated upb)*100
* **Monthly condo fee** = (condo fee per day*360)/12
* **Monthly insurance fee** = (insurance fee per day*360)/12
* **Monthly property taxes** = (property taxes per day*360)/12
* **Marked to market loans to value ratio at liquidation** = original LTV * (liquidate unpaid amount/original unpaid loan amount) * (original house price index/liquidation house price index)
* **Original sale price** = original unpaid loan balance/original loan to value ratio

#### 9.2.6 Loss Severity Module Back-testing of Each Component
In this section, we look at the first component of net losses, which is the net sales proceeds on three different disposition types. We divide net sales proceeds by the liquidation unpaid principal balance to obtain the net sale proceed ratios. Overall, predicted values track actual values throughout the years with the largest discrepancies for years 2012 to 2013 as well as 2020. See the figure below. Here the net sales proceeds are calculated as follows:

$$
Net\ sale\ proceeds_i = Gross\ property\ sale\ proceeds_i - Sales\ expense_i - Other\ selling\ expense_i \\ - Broker\ fees_i - Borrower\ closing\ costs_i \\
\forall i\ for\ REOs\ or\ foreclosure\ alternatives
$$

$$
Net\ sale\ proceeds_i = NPL\ sale\ proceeds_i - Sales\ expense_i - Other\ selling\ expense_i - Broker\ fees_i \\ - Borrower\ closing\ costs_i \\
\forall i\ for\ NPL\ sales
$$

*Figure 13. Enterprise 1 Back-testing Results of Net Sales Proceeds Ratios, 2012-2022*

#### 9.2.7 Fixed Costs Ratios
The figure below compares the predicted fixed costs ratios with actual cost ratios, both scaled by liquidation unpaid principal balance. We divide fixed costs by the liquidation unpaid principal balance to get the fixed costs ratios. As shown in the figure below, before year 2017 the predicted values consistently overestimate fixed cost ratios. However, the predicted values underestimated the ratios since 2017. It seems that there is still some recent upward shifting trend in fixed costs being missed in predicting the fixed costs component. Below is the formula for calculating fixed costs for REOs and foreclosure alternatives:

$$
Fixed\ costs_i = Appraisal\ Fees_i + Attorney\ and\ Trustee\ Fees_i \\
+ Other\ Foreclosure\ Expenses_i + Other\ Liquidation\ Expenses_i \\
+ Maintenance\ Expenses_i + Property\ Inspection\ Fees_i + Repairs_i \\
+ Utilities\ costs_i \\
\forall i\ for\ REOs\ or\ foreclosure\ alternatives
$$

The fixed costs on NPL sales are also called liquidation expenses and they are calculated as follows[^18]:

$$
Fixed\ costs_i = Appraisal\ Fees_i + Attorney\ and\ Trustee\ Fees_i \\
+ Other\ Foreclosure\ Expenses_i + Other\ Liquidation\ Expenses_i \\
+ Other\ Non\ Selling\ Expenses_i + Maintenance\ Expenses_i \\
+ Property\ Inspection\ Fees_i + Repairs_i + Utilities\ costs_i \\
+ Possessory\ and\ Eviction\ Fees_i + Title\ Insurance\ Fees_i \\
+ Property\ Management\ Expenses_i + Servicer\ Incentive\ Payments_i \\
\forall i\ for\ NPL\ sales
$$

*Figure 14. Enterprise 1 Back-testing Results of Fixed Costs Ratios, 2016-2020*

#### 9.2.8 Carrying Costs Ratios
Carrying costs consist of five components: (1) insurance fees, (2) taxes, (3) HOA, (4) condo fees, and (5) accrued interests before disposition. As with other items, carrying cost ratios, which equals carrying costs divided by liquidation unpaid balance amount, are also reasonably well predicted in aggregate across all loans (see figure below). Though not shown below, the predictions match well with actuals also across different cohorts by disposition types, and by judicial or non-judicial states.

*Figure 15. Enterprise 1 Back-testing Results of Carrying Costs Ratios, 2012-2020*

#### 9.2.9 Mortgage Insurance Proceeds Ratios
Mortgage insurance proceeds ratios are calculated by dividing mortgage insurance proceeds by the liquidation unpaid principal balance to get mortgage insurance proceed ratios. Mortgage insurance proceeds ratios have the second largest discrepancy between predicted and actual values after fixed costs ratios (see the figure below). However, other than the last year considered (2020), most other years seem to have reasonable predictions.

*Figure 16. Enterprise 1 Back-testing Results of MI Proceeds Ratios, 2012-2020*

### 9.3 Simulation
#### 9.3.1 Markov Chain Simulation Framework Implementation
In the main context, we illustrate the Markov Chain in terms of matrix operations. Here we are presenting how it is implemented.

**Problem:** Given that, at time t, the probability in each state is known, how to compute the probability of each state at time t+1.

**Solution:**
1. Use behavioral equations to get transition rate from time t to time t+1.
    * x_perf_ldq, x_perf_prep, x_perf_perf
    * x_nrpl_ldq, x_nrpl_prep, x_nrpl_nrpl
    * x_mrpl_ldq, x_mrpl_prep, x_mrpl_mrpl
    * x_rpl_ldq, x_rpl_prep, x_rpl_rpl
    * x_ldq_ldq, x_ldq_prep, x_ldq_def, x_ldq_sdq, x_ldq_rpl
    * x_sdq_sdq, x_sdq_prep, x_sdq_def, x_sdq_ldq, x_sdq_rpl, x_sdq_ddq
    * x_ddq_ddq, x_ddq_prep, x_ddq_def, x_ddq_sdq, x_ddq_rpl, x_ddq_ldq

2. Compute the marginal probabilities at time t+1, which is the weighted average of transition rates weighted by the probabilities of each state at time t.
    * `next_SProb_perf = SProb_perf * x_perf_perf;`
    * `next_SProb_nrpl = SProb_nrpl * x_nrpl_nrpl;`
    * `next_SProb_mrpl = SProb_mrpl * x_mrpl_mrpl;`
    * `next_SProb_rpl = SProb_rpl * x_rpl_rpl + SProb_ldq * x_ldq_rpl + SProb_sdq * x_sdq_rpl + SProb_ddq * x_ddq_rpl;`
    * `next_SProb_ldq = SProb_perf * x_perf_ldq + SProb_nrpl * x_nrpl_ldq + SProb_mrpl * x_mrpl_ldq + SProb_rpl * x_rpl_ldq + SProb_ldq * x_ldq_ldq + SProb_sdq * x_sdq_ldq + SProb_ddq * x_ddq_ldq;`
    * `next_SProb_sdq = SProb_ldq * x_ldq_sdq + SProb_sdq * x_sdq_sdq + SProb_ddq * x_ddq_sdq;`
    * `next_SProb_ddq = SProb_sdq * x_sdq_ddq + SProb_ddq * x_ddq_ddq;`
    * `next_SProb_P = SProb_perf * x_perf_prep + SProb_nrpl * x_nrpl_prep + SProb_mrpl * x_mrpl_prep + SProb_rpl * x_rpl_prep + SProb_ldq * x_ldq_prep + SProb_sdq * x_sdq_prep + SProb_ddq * x_ddq_prep;`
    * `next_SProb_D = SProb_ldq * x_ldq_def + SProb_sdq * x_sdq_def + SProb_ddq * x_ddq_def;`

#### 9.3.2 Monte Carlo Simulation Framework Implementation
Based on the state of the loan at month t, one invokes the corresponding behavior equation to calculate the probabilities of states at month t+1, then use a random number to select a state among the several possible states.

Here is a pseudo-code example for the PERF loan status:

```
For each simulation scenario
  for each loan
    for each month (t)
      Draw a uniform random number, U, in the range of (0, 1)
      Select LOAN_STATUS:
        case PERF:
          Invoke PERF models to computing the probabilities of LDQ, Prepay and PERF, which are denoted as x_perf_ldq, x_perf_prep and x_perf_perf.
          if (U <= x_perf_perf) then
            NEXT_LOAN_STATUS = PERF
          else if (U <= x_perf_perf + x_perf_ldq) then
            NEXT_LOAN_STATUS = LDQ
          else
            NEXT_LOAN_STATUS = PREPAY
END of month
END of loan
END of scenario
```

#### 9.3.3 Cash Flow-Based Simulation
##### 9.3.3.1 Performing and Nonperforming Unpaid Principal Balance
In general, for a particular month, a given loan can either perform (i.e., pay as scheduled per terms of the loan contract) or fail to perform (i.e., not pay as scheduled per terms of the loan contract) or prepay. If a loan performs, then its unpaid principal balance (i.e., the amount contractually owed) is characterized as a performing unpaid principal balance. If a given loan fails to perform, then it is considered delinquent, and its unpaid principal balance is characterized as a nonperforming unpaid principal balance. Performing unpaid principal balance at a current point in time, say month t, equals a sum of two parts. The first part reflects the amount of performing unpaid principal balance from the prior period, say the previous month t-1, that remains performing at month t. The second part reflects the amount of the delinquent unpaid principal balance from a prior period that transitions to performing status at month t.

To calculate the projected performing unpaid principal balance for month t, consider the following two steps. First, the projected performing unpaid principal balance, at month t, equals the performing unpaid principal balance from the prior period, month t-1, minus the projected scheduled principal payment. Second, this projected performing unpaid principal balance is multiplied by the likelihood (i.e., conditional probability) of transitioning from the performing status in the prior period to the performing status in month t.

For a delinquent loan to be reclassified as performing at month t, the borrower(s) must pay the sum of two amounts: what was owed (i.e., the unpaid scheduled principal owed from last paid installment date in the previous period) and what is due (i.e., scheduled principal due currently). To calculate the projected performing unpaid principal balance for a delinquent loan for the month t, consider again the following two steps. First, the projected performing unpaid principal balance from the prior period delinquency equals the delinquent unpaid principal balance from the prior period minus what was owed (i.e., the unpaid scheduled principal from the last paid installment date to the previous period) and what is due (i.e., the scheduled principal due in the current period), multiplied by the likelihood of performing from the prior period delinquency.

##### 9.3.3.2 Prepayment Amount (Unscheduled Principal)
The projection of prepayment amount is similar to the projection of performing unpaid principal balance described previously. Prepayment amount in a current period, say at month t, equals the sum of the following: the amount of performing unpaid principal balance from a previous period, say month t-1, that prepays in the current period plus the amount of the delinquent unpaid principal balance from the previous period that prepays in the current period. For a performing loan to prepay at month t, the borrower(s) must pay scheduled principal due at month t. The projected prepaid amount for the current period performing in the previous period is the performing unpaid principal balance in the previous period minus the projected scheduled principal payment in the current period. This differential is multiplied by the likelihood (e.g., conditional probability) transitioning from the performing status in the previous period to prepay in the current period. For a delinquent loan to prepay in the current period, the borrower(s) must pay the sum of two amounts: what was owed (i.e., the unpaid scheduled principal owed from last paid installment date in the previous period) and what is due (i.e., scheduled principal due currently). The projected prepay amount in the current period that is delinquent at the previous period equals the delinquent unpaid principal balance from the prior period minus what was owed and what is due multiplied by the likelihood of prepaying in the current period given the previous period delinquency.

##### 9.3.3.3 Delinquent Amount
Delinquent amount at month t is the sum of LDQ (3-5 months delinquent) amount, SDQ (6-11 month of delinquent) amount, and DDQ (12 or more month of delinquent) amount. A loan that is LDQ at month t may result from the following: transition from performing loan at month t-1; remains LDQ from prior month LDQ loan; transition from a SDQ loan at prior month; or transition from DDQ loan at prior month. A SDQ loan at month t may: transition from a LDQ loan at month t-1; remains SDQ status from prior month SDQ status; or transition from a DDQ loan at prior month. A DDQ loan at month t may result from the following: transition from a SDQ loan at month t-1; or remains DDQ from a DDQ loan at prior month. In order for a loan to transition from higher delinquency status to lower delinquency status, for example, SDQ, to LDQ, DDQ to LDQ, DDQ to SDQ, the loan is expected to pay a portion of unpaid principal.

LDQ amount at month t is the sum of the following: performing UPB at month t-1 multiplied by the likelihood of transition to LDQ from performing at t-1; the LDQ amount at month t-1 multiplied by the likelihood of transition to LDQ from LDQ at t-1; the SDQ amount at month t-1 minus the portion of unpaid (owed) scheduled principal balance, multiplied by the likelihood of transition to LDQ from SDQ at month t-1; and DDQ amount at month t-1 minus the portion of unpaid (owed) scheduled principal balance, multiplied by the likelihood of transition to LDQ from DDQ at month t-1.

SDQ amount at month t is projected as the sum of the following: the LDQ amount at month t-1 multiplied by the likelihood of transition to SDQ status from LDQ at t-1; the SDQ amount at month t-1, multiplied by the likelihood of transition to SDQ from SDQ at month t-1; and DDQ amount at month t-1 minus the portion of unpaid (owed) scheduled principal balance, multiplied by the likelihood of transition to SDQ status from DDQ at month t-1.

DDQ amount at month t is the sum of the SDQ amount at month t-1 multiplied by the likelihood of transition to DDQ from SDQ at month t-1; and DDQ amount at month t-1 multiplied by the likelihood of transition to DDQ from DDQ at month t - 1.

##### 9.3.3.4 Default Unpaid Principal Balance
Projected default amount at month t is the amount of delinquent UPB at month t-1 defaults at month t. This amount is equal to delinquent UPB at month t-1 multiplies the conditional probabilities of default at month t given delinquency at t-1.

#### 9.3.4 Cashflow-based Simulation vs. Markov Chain Simulation
Markov chain approach is focusing on the unconditional probabilities first (without the cashflow consideration), then using scheduled UPB to derive the prepay amount and using weighted lagged scheduled UPB to derive the default amount. Cashflow based simulation first calculates conditional probabilities, and then uses the projected UPB in the prior period to derive cash flows. As an example, consider the calculation of prepayment amount.

In Markov chain approach,
$$
Prepaid\ amount(t) = Prep\_prob(t) * Schd\_UPB(t)
$$

In cash flow-based approach, this amount is calculated as the sum of:
* Prepay amount transition from performing UPB at t-1; `perf_prep(t) * Perf_UPB(t-1)`, subtract scheduled principal payment (amount due)
* Prepay amount transition from LDQ at t-1: `ldq_prep(t) * LDQ_UPB(t-1)`, subtract scheduled principal payment (amount due), and amount owe from LPI to t-1
* Prepay amount transition from SDQ at t-1; `sdq_prep(t) * SDQ_UPB(t-1)`, subtract scheduled principal payment (amount due), and amount owe from LPI to t-1
* Prepay amount transition from DDQ at t-1: `ddq_prep(t) * DDQ_UPB(t-1)`, subtract scheduled principal payment (amount due), and amount owe from LPI to t-1, where `perf_prep(t)`, `ldq_prep(t)`, `sdq_prep(t)` are conditional probabilities of prepay.

Although the difference seems obvious in formulation, the actual differences (both formulation and numerical) are small.

### 9.4 Summary Information
Below is summary information provided in compliance with FHFA's Information Quality Guidelines.

**Table 51. Summary Information**
| Requirement | Response |
| :--- | :--- |
| **1. Describe the underlying source of any data used to create the product, including whether FHFA or a different agency collected the data.** | Single-Family Mortgage Analytics Platform (SF FMAP) consists of two separate sets of underlying data, which vary depending on the type of SF FMAP equation: behavioral equations or loss severity equations. For the behavioral equations, the underlying data come from three sources; namely, (i) Mortgage Loan Integrated System (MLIS); (ii) FHFA-produced House Price Index (HPI); and (iii) a vendor. Regarding MLIS, each month, Fannie Mae and Freddie Mac provide FHFA with borrower and collateral information on their mortgage holdings. Regarding FHFA-produced HPI, the Office of Capital Policy receives HPI information from the Division of Research and Statistics of the Agency. The vendor provides historical and forecast house price, market rates, and unemployment rates. For the loss severity equations, the underlying source data come from multiple sources as well. First, Fannie Mae and Freddie Mac (The Enterprises) provide monthly loan-level real-estate owned fixed costs data. Second, The Enterprises provide monthly transaction-level costs for non-performing loan sales. Lastly, house price index data is provided by a vendor. Combined, these data serve as the estimation data that feed SF FMAP. |
| **2. Describe the statistical methods or models used to create the product.** | SF FMAP consists of three sets of statistical/quantitative methods embedded within SF FMAP. In the behavioral equations of SF FMAP, the statistical methods include a set of binomial logistic regressions and a set of multinomial logistic regressions. In the loss severity equations of SF FMAP, the statistical method is a set of linear regressions. Lastly, the simulation module of SF FMAP includes a cash flow calculation method, Markov Chain-based method, and Monte Carlo-based method. |
| **3. Describe the intended uses of the product, and if applicable, uses not recommended.** | SF FMAP is a decision support tool used to provide independent analytic support to Agency decision makers on a wide variety of policies such as, but not limited to, Dodd-Frank Act Stress Test, Conservatorship Capital Framework, and the Private Mortgage Insurer Eligibility Requirements. The white paper describes the modeling rationale, theoretical underpinnings, and empirical results from updating and enhancing the production version of SF FMAP. |
| **4. Describe the time period presented in the event or phenomenon reflected in the product.** | SF FMAP consists of several sets of time periods, which vary depending upon the SF FMAP module. For the set of behavioral equations of SF FMAP, the time period for the estimation sample reflects borrower and collateral information from Jan. 2000 to Dec. 2019. For the loss severity equations of SF FMAP, the time period for the loss data sample ranges from Jan. 2011 to Jul. 2022. For the simulation module, the time period for simulated single-family credit loss forecasts can range from one to 40 years. |
| **5. Describe the granularity (i.e., amount of disaggregation) of any key estimates.** | SF FMAP consists of several levels of granularity, which vary depending upon the SF FMAP module. For the set of behavioral equations of SF FMAP, the level of granularity is threefold: (i) loan-level for behavioral and collateral data; (ii) metropolitan level for house price and unemployment rate; and (iii) national-level for market rates. For the set of loss severity equations of SF FMAP, the level of granularity is loan-level varies from loan-level to aggregate-levels of various dimensions. For the simulation module of SF FMAP, the level of granularity varies from loan-level to aggregate-levels of various dimensions (e.g., loan characteristic, geography, book-level, etc....) |
| **6. Where applicable, describe any known major or significant errors in the underlying source data used to create the product.** | The loan level data used for the model fitting is from the historical loan-level database of mortgage, property, and borrower characteristics (excluding Personally Identifiable Information) submitted by the Enterprises. The Enterprises perform data validation for each submission.. Since FMAP is estimated using a sample of loans from the historical loan-level database, loans with errors (missing or unreasonable values) are filtered out from the sample to ensure that data used for model estimation is clean. |
| **7. Where applicable, describe how users can estimate errors, such as errors from sampling.** | To estimate errors, users need to repeat the sampling and estimation process that were done in the update and collect the errors from the estimation. To estimate sampling error, users need to calculate the summary statistics of the sample and population and calculate the difference of the two sets of summary statistics. |
| **8. Where applicable, describe the consistency or comparability with estimates contained in other products published by FHFA.** | The document describes a model that is an update to the predecessor model described in the prior version of the document. Since the equations have been re-estimated since the prior model, the estimates themselves are incomparable. There is no other products published by FHFA that has same intended uses as SF FMAP. |
| **9. Where applicable, describe the steps taken to ensure the product protects the privacy and confidentiality of underlying entity (e.g., borrower, business) reflected in the source data, where applicable.** | FHFA staff do not disclose any private or confidential information in the working paper. At the individual loan level, the analysis relies upon the historical loan-level database of mortgage, property, and borrower characteristics submitted by the Enterprises. The database omits private or confidential information. At the Enterprise level, FHFA staff anonymize the Enterprises rather than reveal their names when appropriate. |
| **10. Where applicable, describe the verification and validation steps taken to ensure errors are not introduced in the production process.** | FHFA staff continually review the working paper until it has been posted. In particular, (i) FHFA SF FMAP model risk personnel series of collaboration/meetings, (ii) external review of FHFA non-SF-FMAP personnel, (iii) external presentation and review by FHFA Office of Financial Analysis and Division of Research and Statistics personnel, and (iv) executive-level review. |
| **11. Where applicable, describe the “chain of custody” of the product from its verification and validation to when it is posted on the website.** | After posting of the working paper, FHFA staff intends to perform a check to ensure the file posted matches the file intended for posting. |

### Bibliography
Begg, Colin B. and Robert Gray. “Calculation of Polychotomous Logistic Regression Parameters Using Individualized Regressions”. Biometrika. Volume 71, Number 1. April 1984.

BlackRock Solutions. The BRS v6.1 Agency Credit Model. October 2020. Internal document.

Calhoun, C. A. and Y Deng (2002), “A Dynamic Analysis of Fixed- and Adjustable- Rate Mortgage Terminations,” Journal of Real Estate Finance and Economics, 24 (1/2): 9-33.

Clapp, John M., Goldberg, Gerson M., Harding, John P., and Michael LaCour-Little (2001), “Movers and Shuckers: Interdependent Prepayment Decisions,” Real Estate Economics, Vol. 29, No. 3: 411-450

Fannie Mae. CCFA Borrower Behavioral Models. Whitepaper. 2019Q3. Internal document.

Federal Housing Finance Agency, Division of Research and Statistics. Mortgage Insight 2020-03 – State Foreclosure Timelines, pg 3. 2020. Internal document.

Jenkins, Stephen P. (1995) "Easy Estimation Methods for Discrete-Time Duration Models." Oxford Bulletin of Economics and Statistics, Vol. 57, No. 1: 129–136.

Milliman. Milliman Mortgage Platform for Investments and Reinsurance (M-PIRe). January 19, 2020. Internal document.



[^1]: The FMAP v2.0 White Paper is located at https://www.fhfa.gov/PolicyProgramsResearch/Research/PaperDocuments/FHFA_MortgageAnalyticsPlatform_Whitepaper_V2.0.pdf. 
[^2]: For example, BlackRock (2020), Fannie Mae (2019), and Milliman (2020). 
[^3]: For example, BlackRock (2020) omitted transitions from 120+ day delinquencies to reperforming status.  This omission may incorrectly predict what happens to some seriously delinquent loans as it does not allow for a seriously delinquent loan to be cured when the loan is given a modification.
[^4]: An RPL loan is a loan that transitions from one of the nonperforming states to the performing state in the simulation. In the simulation, a loan cannot transition to either modified or non-modified re-performing as FMAP v3.0 does not specify if the transition is due to a modification. Also, the only re-performing loans that exist at the start of the simulation are modified and non-modified re-performing loans.
[^5]: Separate models are also estimated by Enterprise.
[^6]: An out-of-time fit is a particular type of out-of-sample fit where the model predictions are tested on data outside of the sample the model was estimated on. Specifically, an out-of-time fit relies on testing the fit of predictions of a model on data that is from a different time period than the sample the model was estimated on.
[^7]: In the loss forecast, loan age in the behavioral equations is capped at 240 months to prevent the predicted probability from being unreasonably high.
[^8]: Discrete-time refers to the fact that borrower behavior is generally observed discretely such as monthly rather than at a more granular frequency more closely associated with continuous-time.
[^9]: Estimating binomial logits in place of multinomial logits follows Begg, Colin B. and Robert Gray. "Calculation of Polychotomous Logistic Regression Parameters Using Individualized Regression." Biometrika, 71, no. 1 (1984): 11-18. For computational expediency, multinomial logits were estimated in instances where all the models within the same multinomial framework contained the same set of regressors. For example, the nonperforming loan equations all contained the same regressors and hence were estimated within a single multinomial logit rather than across multiple binomial logits.
[^10]: FMAP v3.0 omits repurchase and RPL sales as terminal outcomes.
[^11]: The behavioral equations do not allocate loans across the three outcomes separately. Hence, for loss severity the amount of a loan predicted to be defaulted is divided into three portions associated with the three default outcomes using the following percentages:
| Judicial State | REO | Foreclosure Alternative | NPL Sale |
| :--- | :---: | :---: | :---: |
| TRUE | 48% | 26% | 26% |
| FALSE | 50% | 32% | 18% |
[^12]: Nonperforming loan (NPL) sales have been used by the Enterprises to sell severely delinquent mortgages from their portfolios. This reduces the losses to the Enterprises. A particular group of servicers are approved to participate in NPL sales with the stipulation they will work out the loans once purchased.
[^13]: The time of disposition equates to REO property disposition for REO resolutions, and the time of disposition equates to the title transfer for foreclosure alternatives.
[^14]: Many of the components of fixed costs are zero for non-performing loan sales.
[^15]: Federal Housing Finance Agency, Division of Research and Statistics (2020).
[^16]: Additional information about the information used, provided, and reported can be found in the appendix.
[^17]: The liquidated loan balance categories were chosen based on the percentiles of the population.
[^18]: Many of the fixed cost components are zero for Nonperforming Loan (NPL) Sales.
