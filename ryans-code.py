import json
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# file path to chrome history: C:\Users\ryanf\Downloads\takeout-20250211T161420Z-001.zip\Takeout\Chrome
# Step 1: Load JSON Data
# with open('/Users/ryanf/AppData/Local/Temp/fb788f27-e091-4224-970e-e993bffa4f69_takeout-20250211T161420Z-001.zip.f69/Takeout/Chrome/Hisory.json', 'r') as file:
# #with open(r'C:\Users\ryanf\Downloads\takeout-20250211T161420Z-001\Takeout\Chrome\History', 'r') as file:
#     data = json.load(file)

data = {
    "Browser History": [
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Advisor Agreement - Roth IRA | Dropbox Sign",
            "url": "https://app.hellosign.com/sign/5869bd035c8fc9662753701f56a6101d1cbff465#/complete",
            "time_usec": 1738590839450168,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Advisor Agreement - Roth IRA | Dropbox Sign",
            "url": "https://app.hellosign.com/sign/5869bd035c8fc9662753701f56a6101d1cbff465#/confirm",
            "time_usec": 1738590836965541,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Advisor Agreement - Roth IRA | Dropbox Sign",
            "url": "https://app.hellosign.com/sign/5869bd035c8fc9662753701f56a6101d1cbff465#/sign/component_1235421184_2?validate=False",
            "time_usec": 1738590801486329,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Advisor Agreement - Roth IRA | Dropbox Sign",
            "url": "https://app.hellosign.com/sign/5869bd035c8fc9662753701f56a6101d1cbff465#/sign/component_461407445_1",
            "time_usec": 1738590791745781,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Advisor Agreement - Roth IRA | Dropbox Sign",
            "url": "https://app.hellosign.com/sign/5869bd035c8fc9662753701f56a6101d1cbff465",
            "time_usec": 1738590786537101,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.irs.gov/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.irs.gov/pub/irs-pdf/fw9.pdf",
            "url": "https://www.irs.gov/pub/irs-pdf/fw9.pdf",
            "time_usec": 1738590784463282,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.irs.gov/pub/irs-pdf/fw9.pdf",
            "url": "https://www.irs.gov/pub/irs-pdf/fw9.pdf",
            "time_usec": 1738095009184056,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app02.us.bill.com/onboarding/assets/favicons/favicon.ico?1738095010072",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Business Bill Payment | Pay Online and Get Paid",
            "url": "https://app02.us.bill.com/onboarding/flow/",
            "time_usec": 1738095008666940,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.irs.gov/pub/irs-pdf/fw9.pdf",
            "url": "https://www.irs.gov/pub/irs-pdf/fw9.pdf",
            "time_usec": 1738073767958665,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.ups.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Tracking | UPS - United States",
            "url": "https://www.ups.com/track?loc=en_US&Requester=SBN&tracknum=1Z4051V00399182059&AgreeToTermsAndConditions=yes&WT.z_eCTAid=ct1_eml_Tracking__ct1_eml_tra_eml_auto_missed_delivery&WT.z_edatesent=01162025/trackdetails",
            "time_usec": 1738073767121350,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.ups.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Tracking | UPS - United States",
            "url": "https://www.ups.com/track?loc=en_US&Requester=SBN&tracknum=1Z4051V00399182059&AgreeToTermsAndConditions=yes&WT.z_eCTAid=ct1_eml_Tracking__ct1_eml_tra_eml_auto_missed_delivery&WT.z_edatesent=01162025",
            "time_usec": 1737071857169420,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.ups.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Tracking | UPS - United States",
            "url": "https://www.ups.com/track?loc=en_US&Requester=SBN&tracknum=1Z4051V00399182059&AgreeToTermsAndConditions=yes&WT.z_eCTAid=ct1_eml_Tracking__ct1_eml_tra_eml_auto_missed_delivery&WT.z_edatesent=01162025/trackdetails",
            "time_usec": 1737071855189604,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Tracking | UPS - United States",
            "url": "https://www.ups.com/track?loc=en_US&Requester=SBN&tracknum=1Z4051V00399182059&AgreeToTermsAndConditions=yes&WT.z_eCTAid=ct1_eml_Tracking__ct1_eml_tra_eml_auto_missed_delivery&WT.z_edatesent=01162025/trackdetails",
            "time_usec": 1737057054711379,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Tracking | UPS - United States",
            "url": "https://www.ups.com/track?loc=en_US&Requester=SBN&tracknum=1Z4051V00399182059&AgreeToTermsAndConditions=yes&WT.z_eCTAid=ct1_eml_Tracking__ct1_eml_tra_eml_auto_missed_delivery&WT.z_edatesent=01162025",
            "time_usec": 1737057053190141,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app.pnmvote.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MyVote",
            "url": "https://app.pnmvote.com/",
            "time_usec": 1736958492315652,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app.pnmvote.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MyVote",
            "url": "https://app.pnmvote.com/",
            "time_usec": 1736699260964831,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app.pnmvote.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MyVote",
            "url": "https://app.pnmvote.com/login",
            "time_usec": 1736699238925816,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.purdueglobal.edu/shared/favicon/apple-touch-icon.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Purdue Global - An Accredited Online University",
            "url": "https://www.purdueglobal.edu/?source=SC48413&ve=62296&utm_source=google&utm_medium=display&utm_campaign=pg_demandgen_con_gen-bus-it&utm_content=PG_CON_General_Images&dclid=&wbraid=CloKCQiAjp-7BhDZARJJAJjLeK9BH72Ki3e-QhdVfhQFwhckobC5TjcyDdDPciISyF4wAsk2fFVBCxN8LVqvazrytiYHDG4U_7dNreu1ENrI7wJ-5yigaxoCG4g",
            "time_usec": 1736699191231069,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.fedex.com/images/c/s1/fx-favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Detailed Tracking",
            "url": "https://www.fedex.com/fedextrack/?trknbr=282441444327&trkqual=2460644000~282441444327~FX",
            "time_usec": 1734964476840376,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Purdue Global - An Accredited Online University",
            "url": "https://www.purdueglobal.edu/?source=SC48413&ve=62296&utm_source=google&utm_medium=display&utm_campaign=pg_demandgen_con_gen-bus-it&utm_content=PG_CON_General_Images&dclid=&wbraid=CloKCQiAjp-7BhDZARJJAJjLeK9BH72Ki3e-QhdVfhQFwhckobC5TjcyDdDPciISyF4wAsk2fFVBCxN8LVqvazrytiYHDG4U_7dNreu1ENrI7wJ-5yigaxoCG4g",
            "time_usec": 1734964468160301,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.fedex.com/images/c/s1/fx-favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Detailed Tracking",
            "url": "https://www.fedex.com/fedextrack/?trknbr=282441444327&trkqual=2460644000~282441444327~FX",
            "time_usec": 1733090532221273,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.fedex.com/images/c/s1/fx-favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Detailed Tracking",
            "url": "https://www.fedex.com/wtrk/track/?trknbr=282441444327&sc_src=email_4967189&sc_lid=544755794&sc_uid=iv4JPtKeT7&sc_llid=792375&sc_eh=e1e424bcba971e311&utm_source=Emarsys&utm_medium=email&utm_id=4967189&utm_campaign=shipping%20confirmation&utm_content=transactional&utm_term=CGA",
            "time_usec": 1733090526858476,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Ticketmaster Sign In",
            "url": "https://auth.ticketmaster.com/as/authorization.oauth2?redirect_uri=https%3A%2F%2Fam.ticketmaster.com%2Fmsg%2Fam-sso%3Fdeeplink%3DL21zZy9lbi9teS1ldmVudHMvNjQ3Njg%3D&response_type=code&lang=en-us&integratorId=NAM&placementId=homepage&visualPresets=msg&hideLeftPanel=true&client_id=4c81b8c6f059.web.msg-msg.us&scope=openid%20profile%20phone%20email%20tm",
            "time_usec": 1733090525147289,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Events Landing Page \u2013 Ticket Management | MSG Spo\u2026",
            "url": "https://am.ticketmaster.com/msg/en/my-events/64768",
            "time_usec": 1732485842231824,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Events Landing Page \u2013 Ticket Management | MSG Spo\u2026",
            "url": "https://am.ticketmaster.com/msg/dashboard/invites/b6p32576n3dpug90l48j16mqqoo22hq26pm0ke54qem1du3b",
            "time_usec": 1732485830425438,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://auth.ticketmaster.com/assets/favicon-32x32.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Ticketmaster Sign In",
            "url": "https://auth.ticketmaster.com/as/authorization.oauth2?redirect_uri=https%3A%2F%2Fam.ticketmaster.com%2Fmsg%2Fam-sso%3Fdeeplink%3DL21zZy9pbnZpdGVzL2I2cDMyNTc2bjNkcHVnOTBsNDhqMTZtcXFvbzIyaHEyNnBtMGtlNTRxZW0xZHUzYg%3D%3D&response_type=code&lang=en-us&integratorId=NAM&placementId=homepage&visualPresets=msg&hideLeftPanel=true&client_id=4c81b8c6f059.web.msg-msg.us&scope=openid%20profile%20phone%20email%20tm",
            "time_usec": 1732485813548279,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://s1.s.tmol.io/static/favicon-tm.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Orders",
            "url": "https://my.ticketmaster.com/order/Z7IVgZOxvZ16ke976v4/tickets?eventId=3B006158C64B1D76",
            "time_usec": 1732485811198427,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://my.ticketmaster.com/order/Z7IVgZOxvZ16ke976v4/tickets?eventId=3B006158C64B1D76",
            "url": "https://my.ticketmaster.com/order/Z7IVgZOxvZ16ke976v4/tickets?eventId=3B006158C64B1D76",
            "time_usec": 1732313168007450,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://s1.s.tmol.io/static/favicon-tm.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Orders",
            "url": "https://my.ticketmaster.com/order/Z7IVgZOxvZ16ke976v4/view",
            "time_usec": 1732313162452866,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://s1.s.tmol.io/static/favicon-tm.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Transfer Accept",
            "url": "https://my.ticketmaster.com/transfer/accept?v=CQzPVEeC4Fq5LtdbPRdK3O9UuzcXHHw5erdwpnZ3gvaUhrHQSlieghIljKFqFKgooAyM_90-PcUNEq81_jn62CrQgqjQz7GNN1L9giGVyca_kZ7mYaGDerDv-QLxD6Kaw0qFve-2-xn943ViseQmSOqpuZc5AoLwDkuJsKc&lang=en-us&wt.mc_id=EML_TMNT767759_6634590_0%5BPP_Accept_Ticket&et_cid=TM_767759&et_rid=&efeat_seg=0&utm_source=sfmc&utm_medium=tmemail&utm_campaign=PP_XferRec_Email_NEMSv2.1_v01.5_Prod&utm_term=767759&utm_content=PP_Accept_Ticket&j=767759&l=21_HTML&sfmc_sub=733864742&jb=6634590&mid=7222895&landing=c",
            "time_usec": 1732313147421743,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://auth.ticketmaster.com/assets/favicon-32x32.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Ticketmaster Sign In",
            "url": "https://auth.ticketmaster.com/as/authorization.oauth2?client_id=8bf7204a7e97.web.ticketmaster.us&response_type=code&scope=openid%20profile%20phone%20email%20tm&redirect_uri=https://identity.ticketmaster.com/exchange&visualPresets=tm&lang=en-us&placementId=myAccount&showHeader=true&hideLeftPanel=False&integratorId=prd283.myAccount&intSiteToken=tm-us&TMUO=west_Fe7SODOCjonCFPMHZ60v7wKr0Jc3tyf0lV0Ro5lc5Pw%3D&deviceId=DuLb04fBxrG3s7SzsbOxsbm5s7iRdgTCZMtfEw&doNotTrack=False",
            "time_usec": 1732313120150370,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://career5.successfactors.eu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://career5.successfactors.eu/portalcareer?_s.crb=WAXWHIfDzmElYl3yPT%252bwNSyhBOjN7F8P05MOINStZ0U%253d",
            "url": "https://career5.successfactors.eu/portalcareer?_s.crb=WAXWHIfDzmElYl3yPT%252bwNSyhBOjN7F8P05MOINStZ0U%253d",
            "time_usec": 1732313117234513,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://career5.successfactors.eu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Career Opportunities: Applied to Software Develop\u2026",
            "url": "https://career5.successfactors.eu/portalcareer?_s.crb=WAXWHIfDzmElYl3yPT%252bwNSyhBOjN7F8P05MOINStZ0U%253d",
            "time_usec": 1731588941715678,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://career5.successfactors.eu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Career Opportunities: Sign In",
            "url": "https://career5.successfactors.eu/career?_s.crb=WAXWHIfDzmElYl3yPT%252bwNSyhBOjN7F8P05MOINStZ0U%253d",
            "time_usec": 1731588940700862,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://career5.successfactors.eu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Career Opportunities: Sign In",
            "url": "https://career5.successfactors.eu/career?career_ns=job_application&navBarLevel=JOB_MGMT&subNavBarLevel=JOB_APPLIED&fbja_action=fbja_viewApp&company=ALSTOM&career_job_req_id=472321&fbja_appId=4384403&st=79FA6509ED7F77F69E1692410B1A81C537A5B34A&",
            "time_usec": 1731588925206685,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.elfster.com/apple-touch-icon-180x180.png?v=vMgzWYB3oR",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Delta Shelta Secret Santa (again) | Elfster",
            "url": "https://www.elfster.com/gift-exchanges/dbbc2db7-aaa6-4a3e-8106-f0d08189cc4a/?utm_source=app_email&utm_medium=email&utm_content=CallToActionHtml0&utm_campaign=DrawNotification",
            "time_usec": 1731074035683364,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.elfster.com/apple-touch-icon-180x180.png?v=vMgzWYB3oR",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Delta Shelta Secret Santa (again) | Elfster",
            "url": "https://www.elfster.com/actions/redirect/?redirecturl=%2Fcore%2F%3Fe%3D0195e5a8-cf38-4d30-908a-2649da74a905%26u%3Dhttps%253A%252F%252Fwww.elfster.com%252Fgift-exchanges%252Fdbbc2db7-aaa6-4a3e-8106-f0d08189cc4a%252F%26t%3D2",
            "time_usec": 1731074034777802,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product_ios/3x/gsa_ios_60dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "student financial services - Google Search",
            "url": "https://www.google.com/search?q=student+financial+services&rlz=1CDGOYI_enUS976US998&oq=student+financial+services&gs_lcrp=EgZjaHJvbWUqCggAEAAY4wIYgAQyCggAEAAY4wIYgAQyEAgBEC4YrwEYxwEYgAQYjgUyCggCEAAYsQMYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyDQgGEC4YrwEYxwEYgAQyDQgHEC4YrwEYxwEYgAQyBwgIEAAYgAQyBwgJEAAYgATSAQg0OTkxajBqNKgCAbACAeIDBBgBIF8&hl=en-US&sourceid=chrome-mobile&ie=UTF-8&dlnr=1&sei=MzAqZ7bPBYbk5NoPhru-oAM#ebo=0",
            "time_usec": 1731074033820352,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.google.com/maps/uv?viewerState=lb&pb=!1s0x89b3865ad95ad309:0x1fd9ae158af2caa8&imagekey=!1e10!2sAF1QipM8ohsmzh7myZSBmYUttc5ACuk2TWmBMU0noPWF&cr=tp_14&gsas=1",
            "url": "https://www.google.com/maps/uv?viewerState=lb&pb=!1s0x89b3865ad95ad309:0x1fd9ae158af2caa8&imagekey=!1e10!2sAF1QipM8ohsmzh7myZSBmYUttc5ACuk2TWmBMU0noPWF&cr=tp_14&gsas=1",
            "time_usec": 1730819353434977,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product_ios/3x/gsa_ios_60dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "student financial services - Google Search",
            "url": "https://www.google.com/search?q=student+financial+services&rlz=1CDGOYI_enUS976US998&oq=student+financial+services&gs_lcrp=EgZjaHJvbWUqCggAEAAY4wIYgAQyCggAEAAY4wIYgAQyEAgBEC4YrwEYxwEYgAQYjgUyCggCEAAYsQMYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyDQgGEC4YrwEYxwEYgAQyDQgHEC4YrwEYxwEYgAQyBwgIEAAYgAQyBwgJEAAYgATSAQg0OTkxajBqNKgCAbACAeIDBBgBIF8&hl=en-US&sourceid=chrome-mobile&ie=UTF-8&dlnr=1&sei=MzAqZ7bPBYbk5NoPhru-oAM#ebo=0",
            "time_usec": 1730818105943654,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product_ios/3x/gsa_ios_60dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "student financial services - Google Search",
            "url": "https://www.google.com/search?q=student+financial+services&rlz=1CDGOYI_enUS976US998&oq=student+financial+services&gs_lcrp=EgZjaHJvbWUqCggAEAAY4wIYgAQyCggAEAAY4wIYgAQyEAgBEC4YrwEYxwEYgAQYjgUyCggCEAAYsQMYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyDQgGEC4YrwEYxwEYgAQyDQgHEC4YrwEYxwEYgAQyBwgIEAAYgAQyBwgJEAAYgATSAQg0OTkxajBqNKgCAbACAeIDBBgBIF8&hl=en-US&sourceid=chrome-mobile&ie=UTF-8",
            "time_usec": 1730818099235248,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "SIS Home",
            "url": "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_GN.H_SPRINGBOARD.FieldFormula.IScript_Main?institution=UVA01&",
            "time_usec": 1730817880573170,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "SIS Home",
            "url": "https://sisuva.admin.virginia.edu/psp/ihprd/?cmd=login&languageCd=ENG&",
            "time_usec": 1730817879976884,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://sisuva.admin.virginia.edu/psp/ihprd/?cmd=login&languageCd=ENG&",
            "url": "https://sisuva.admin.virginia.edu/ihprd/signon.html",
            "time_usec": 1730817878765034,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://static.hirevue.com/static/cd8edc3/webclient/bd-learn-more/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "HireVue",
            "url": "https://app.hirevue.com/ui/learn-more/#/interview/Pkyy5pb-g5iskc/",
            "time_usec": 1730817877626479,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://static.hirevue.com/static/cd8edc3/webclient/bd-learn-more/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "HireVue Learn More",
            "url": "https://app.hirevue.com/ui/learn-more/#/interview/Pkyy5pb-g5iskc/",
            "time_usec": 1730207163771119,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Frye Phillip Short Black Harness Moto Biker Boots\u2026",
            "url": "https://www.ebay.com/itm/267036625439?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D264184%26meid%3Df8fdedf5072741a789137a218d244c2a%26pid%3D101429%26rk%3D4%26rkt%3D12%26sd%3D235793133625%26itm%3D267036625439%26pmt%3D1%26noa%3D0%26pg%3D2332490%26algv%3DSimPLMWebV1EmbeddedAuctionsCPCAutoManualWithCIIXAIRecallsUpdatedRanker0424NoIMA%26brand%3DFrye&_trksid=p2332490.c101429.m2460&itmprp=cksum%3A267036625439f8fdedf5072741a789137a218d244c2a%7Cenc%3AAQAJAAABMIV5CFHpx8qL94DS2Mo1uCi5RlK%252B6oGF%252Bq%252FvM6onJsyCAS4bVm4MG2DxmngmQBYs7QTou1H5%252BktC9DZbAMWEM%252B%252BdlquESLSCZunJqt41Rd0Jpo%252B961Uv4rJCVp8%252FxvBjYUwREXJW33qPfSLivHzNecR2Jm7p5LGeMZgjT1vf3edYBgwlPnLrVrVi%252BdRwqolWXXz9M3GBG01SXMA2iiWjbVlvvH4L5EOImGTVQWr%252BPu0tV3gDMvZAGSyV2V6iwXozT6HInBm%252Fps1dQm3wfKKCsplt8DBIsXWoXSXw0O1WMOplO6j5SjL2Bepsv8%252FDKscQDNXrzmQbr8mB1oyL3M6Oy2q3bsHTEacNi47sV3hJReAobIMmb%252FUyKnWFChbsLPyUmOwWLcOgwh3%252BAXJBML%252BC4w8%253D%7Campid%3APL_CLK%7Cclp%3A2332490&itmmeta=01JBC47SJ16GGXK4S2ZDT80Z8B",
            "time_usec": 1730205196691354,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.ebay.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Frye Boots Womens 9 Phillip Studded Harness Ring\u2026",
            "url": "https://www.ebay.com/itm/235793133625",
            "time_usec": 1730205181612983,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Order details | eBay",
            "url": "https://order.ebay.com/ord/show?orderId=10-12250-60397&ssPageName=STRK:MESO:VPS&_trksid=p4429486.m2548.l2673",
            "time_usec": 1730205176698268,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.ebay.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Frye Boots Womens 9 Phillip Studded Harness Ring\u2026",
            "url": "https://www.ebay.com/itm/235793133625",
            "time_usec": 1730205115837677,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Order details | eBay",
            "url": "https://order.ebay.com/ord/show?itemId=235793133625&transactionId=2204552407013&mkpid=0&emsid=e11400.m144671.l152966&mkcid=7&ch=osgood&euid=1f3a1c98aaad47359aa60fa24e324d18&bu=45329030891&exe=0&ext=0&osub=-1%7E1&crd=20241028111656&segname=11400",
            "time_usec": 1730205095818049,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://pages.ebay.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://accounts.ebay.com/acctsec/authn-register?srt=AQAJAAABAP46q9XIOPYRAKRN17PhSGeUB7JWaMNzLS5JcjznCpExD2uMFT4KQaATR8ZP-JN6FXv787EX9vfXhpX-kMgLQDbbPSfcxbgG6tTDl50oFGA6BPjbIXi2EPiflaCJK7H5eD03GPziuyYozn4AvFL43_a7M755eAvIuA_YssjOfyDt8tvhc2UPdmyxnfGfx2tc6ZNNtuyapuqtk__eKHC8hZcHvZfj5IESdHwT1VPBvaZcnACWjxdVriYwcQhlt_xn5c1MezWnvQhh0yP5vc7X9aDrWa-u_D-F8SSUCFAJUjpsd-mxrBhrq1PSqgduXJDbATd4IR5SzywuCC2_Fcw_u_Q&ru=https%3A%2F%2Forder.ebay.com%2Ford%2Fshow%3FitemId%3D235793133625%26transactionId%3D2204552407013%26mkpid%3D0%26emsid%3De11400.m144671.l152966%26mkcid%3D7%26ch%3Dosgood%26euid%3D1f3a1c98aaad47359aa60fa24e324d18%26bu%3D45329030891%26exe%3D0%26ext%3D0%26osub%3D-1%257E1%26crd%3D20241028111656%26segname%3D11400",
            "url": "https://accounts.ebay.com/acctsec/authn-register?srt=AQAJAAABAP46q9XIOPYRAKRN17PhSGeUB7JWaMNzLS5JcjznCpExD2uMFT4KQaATR8ZP-JN6FXv787EX9vfXhpX-kMgLQDbbPSfcxbgG6tTDl50oFGA6BPjbIXi2EPiflaCJK7H5eD03GPziuyYozn4AvFL43_a7M755eAvIuA_YssjOfyDt8tvhc2UPdmyxnfGfx2tc6ZNNtuyapuqtk__eKHC8hZcHvZfj5IESdHwT1VPBvaZcnACWjxdVriYwcQhlt_xn5c1MezWnvQhh0yP5vc7X9aDrWa-u_D-F8SSUCFAJUjpsd-mxrBhrq1PSqgduXJDbATd4IR5SzywuCC2_Fcw_u_Q&ru=https%3A%2F%2Forder.ebay.com%2Ford%2Fshow%3FitemId%3D235793133625%26transactionId%3D2204552407013%26mkpid%3D0%26emsid%3De11400.m144671.l152966%26mkcid%3D7%26ch%3Dosgood%26euid%3D1f3a1c98aaad47359aa60fa24e324d18%26bu%3D45329030891%26exe%3D0%26ext%3D0%26osub%3D-1%257E1%26crd%3D20241028111656%26segname%3D11400",
            "time_usec": 1730205092235265,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://signin.ebay.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign in or Register | eBay",
            "url": "https://signin.ebay.com/signin/ggl/cb?state=dl4xLjEjaV4xI0leMyNmXjAjcF4xI3JeMSN0XlVsNDFYelU2TXpFMk9UUkJRa0V4TkVSQlFUQTJSVU00UkVZeE0wRkdPRGxHT0RVelJFVmZNbDh4STBWZU1qWXc%3D%7C%7CAQAJAAAAUKXnAXFO_1KI4a1RqK2_eVTLroviDJxDQ8bPtE7iGgKCfBJ5W1xQiu28Kqngk3K4B_AtM2-QNlAb48yOhkYRXNF9_GlHIjIHYVCn8Bv4eGTx&code=4%2F0AVG7fiSvrGuDdIfJpBMEj1ZhSvaBtOxZYow4WkCarrKoQZ5JJKPvlM0PbWWd5xluCFzCRQ&scope=email+profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+openid&authuser=0&prompt=none",
            "time_usec": 1730205089957146,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://signin.ebay.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign in or Register | eBay",
            "url": "https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Forder.ebay.com%2Ford%2Fshow%3FitemId%3D235793133625%26transactionId%3D2204552407013%26mkpid%3D0%26emsid%3De11400.m144671.l152966%26mkcid%3D7%26ch%3Dosgood%26euid%3D1f3a1c98aaad47359aa60fa24e324d18%26bu%3D45329030891%26exe%3D0%26ext%3D0%26osub%3D-1%257E1%26crd%3D20241028111656%26segname%3D11400&sgfl=sm&smuid=9cc027b5cbdb4f07bc29e146cca0498c",
            "time_usec": 1730205084941780,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.masterclass.com/_next-public/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MasterClass Online Classes",
            "url": "https://www.masterclass.com/find-my-classes?categories=315&wq=t",
            "time_usec": 1730205083579960,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.masterclass.com/_next-public/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MasterClass Online Classes",
            "url": "https://www.masterclass.com/find-my-classes?categories=315&wq=t",
            "time_usec": 1730173929921845,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.masterclass.com/_next-public/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MasterClass Online Classes",
            "url": "https://www.masterclass.com/?&campaignid=20654081747&adgroupid=160260243731&adid=710854529245&utm_term=masterclass&utm_campaign=%5BMC%5D+%7C+Search+%7C+Brand+%7C+Keywords_Consolidated_EM_PM_BM+%7C+ROW_US+%7C+EN+%7C+MAX+%7C+EG&utm_source=google&utm_medium=search&utm_content=710854529245&hsa_acc=9801000675&hsa_cam=16376419640&hsa_grp=160260243731&hsa_ad=710854529245&hsa_src=g&hsa_tgt=kwd-66880027&hsa_kw=masterclass&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gbraid=0AAAAADjLLoGorLVOu9BdHu179AVc7Fpw5&gclid=Cj0KCQjw7Py4BhCbARIsAMMx-_IzDL3lcxEkZ0tcqrvWFYRWGPJgedj0DwQE2ohk4Z7Nixv16XLy8mAaAvz5EALw_wcB&gclsrc=aw.ds",
            "time_usec": 1730173920458412,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product_ios/3x/gsa_ios_60dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "mater class - Google Search",
            "url": "https://www.google.com/search?q=mater+class&rlz=1CDGOYI_enUS976US998&oq=mater+class&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQABgKGLEDGIAEMgYIAhAFGEAyDAgDEAAYChixAxiABDIMCAQQLhgKGLEDGIAEMgkIBRAAGAoYgAQyDAgGEAAYChixAxiABDIJCAcQABgKGIAEMgkICBAAGAoYgAQyCQgJEAAYChiABNIBCDIwNjFqMGo0qAITsAIB4gMEGAEgXw&hl=en-US&sourceid=chrome-mobile&ie=UTF-8",
            "time_usec": 1730173918530044,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Free Piano Masterclass by Stephen Ridley",
            "url": "https://go.masterclass-piano.com/free-masterclass-piano-giveway-a?gc_id=20148695203&h_ad_id=715805256915&wbraid=ClkKCAjw7Py4BhAqEkkA8OBQP0DjD19ZrvIQF6GaWMun3VuhAOYM467sMULs_bfNn7KeKOjE0HRFVROP8rlRe5eoCQuhzLARHjvb9LbfRJn1l3bLSTSmGgJe6Q",
            "time_usec": 1730173904303339,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://s1.s.tmol.io/static/favicon-tm.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Orders",
            "url": "https://my.ticketmaster.com/order/Z7IVgZOxvZ16kZYPPa4/tickets?eventId=01006090DA1B5E70",
            "time_usec": 1730173902685031,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app02.us.bill.com/neo/assets/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://app02.us.bill.com/neo/login",
            "url": "https://app02.us.bill.com/neo/login",
            "time_usec": 1729822050976863,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app02.us.bill.com/neo/assets/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://app02.us.bill.com/neo/login",
            "url": "https://app02.us.bill.com/Login",
            "time_usec": 1729822050669366,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app02.us.bill.com/onboarding/assets/favicons/favicon.ico?1729822046039",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Business Bill Payment | Pay Online and Get Paid",
            "url": "https://app02.us.bill.com/onboarding/flow/signup",
            "time_usec": 1729822010860685,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app02.us.bill.com/onboarding/assets/favicons/favicon.ico?1729822010994",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Business Bill Payment | Pay Online and Get Paid",
            "url": "https://app02.us.bill.com/neo/frame/redirect?urlEnum=PayablesOverview&encodedParams=",
            "time_usec": 1729822002622277,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app02.us.bill.com/neo/assets/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "BILL",
            "url": "https://app02.us.bill.com/PayablesOverview",
            "time_usec": 1729822002427617,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app02.us.bill.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Confirm 2-Step Verification | Bill.com",
            "url": "https://app02.us.bill.com/app/mfa/challenge?returnUrl=%2FPayablesOverview",
            "time_usec": 1729821978118983,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app02.us.bill.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Confirm 2-Step Verification | Bill.com",
            "url": "https://app02.us.bill.com/PayablesOverview",
            "time_usec": 1729821977964558,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app02.us.bill.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "/PayablesOverview",
            "url": "https://app02.us.bill.com/Home",
            "time_usec": 1729821977727239,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app02.us.bill.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "/Home",
            "url": "https://app02.us.bill.com/PodEntry",
            "time_usec": 1729821977567364,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://prod02-app.bdc-cdn.com/apple-touch-icon.png?ver=847071fd",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "BILL : /pod02/OrgSelect",
            "url": "https://app-signup.us.bill.com/pod02/OrgSelect?orgId=00802QGTVMPQBIJ3h9g6",
            "time_usec": 1729821969652367,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://prod02-app.bdc-cdn.com/apple-touch-icon.png?ver=847071fd",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "BILL : /pod02/OrgSelect",
            "url": "https://app-signup.us.bill.com/pod02/OrgSelect",
            "time_usec": 1729821969453847,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app-signup.us.bill.com/neo/assets/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://app-signup.us.bill.com/neo/login?invite=&existing=1&emailenc=!bgTk%2FQM2IvzYh2%2B7ccbMd%2FB4Wx%2BYxzTz0l0oxtpdTOWRCyyIqBqcG%2FBbBt1ihFJXb",
            "url": "https://app-signup.us.bill.com/neo/login?invite=&existing=1&emailenc=!bgTk%2FQM2IvzYh2%2B7ccbMd%2FB4Wx%2BYxzTz0l0oxtpdTOWRCyyIqBqcG%2FBbBt1ihFJXb",
            "time_usec": 1729821939468583,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app-signup.us.bill.com/neo/assets/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://app-signup.us.bill.com/neo/login?invite=&existing=1&emailenc=!bgTk%2FQM2IvzYh2%2B7ccbMd%2FB4Wx%2BYxzTz0l0oxtpdTOWRCyyIqBqcG%2FBbBt1ihFJXb",
            "url": "https://app-signup.us.bill.com/Login?invite=&existing=1&emailenc=!bgTk%2FQM2IvzYh2%2B7ccbMd%2FB4Wx%2BYxzTz0l0oxtpdTOWRCyyIqBqcG%2FBbBt1ihFJXb",
            "time_usec": 1729821939252352,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app-signup.us.bill.com/onboarding/assets/favicons/favicon.ico?1729821933247",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://app-signup.us.bill.com/onboarding/flow/signin-existing?sgType=Check",
            "url": "https://app-signup.us.bill.com/onboarding/flow/signin-existing?sgType=Check",
            "time_usec": 1729821935632988,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app-signup.us.bill.com/onboarding/assets/favicons/favicon.ico?1729821933247",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Business Bill Payment | Pay Online and Get Paid",
            "url": "https://app-signup.us.bill.com/onboarding/flow/signup?inviteID=90FD90072416F4DB501A3D35AC97DD441DE031B9A6531C1C2292F51A323A13BA&sg=d-54b841c6445b445ea07da43feee55614&isFundedInvite=true&dueDate=1729838700&payeeAmount=130.00&estimatedArrivalDateCheck=1730246400&estimatedArrivalDateACH=1729814400&sgType=Check",
            "time_usec": 1729821933023714,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app-signup.us.bill.com/onboarding/assets/favicons/favicon.ico?1729821933247",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Business Bill Payment | Pay Online and Get Paid",
            "url": "https://app-signup.us.bill.com/InviteSignup?invite=90FD90072416F4DB501A3D35AC97DD441DE031B9A6531C1C2292F51A323A13BA&sg=d-54b841c6445b445ea07da43feee55614&payeeAmount=130.00&dueDate=1729838700&isFundedInvite=true&estimatedArrivalDateACH=1729814400&estimatedArrivalDateCheck=1730246400&sgType=Check",
            "time_usec": 1729821932738842,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app-signup.us.bill.com/onboarding/assets/favicons/favicon.ico?1729821863161",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Business Bill Payment | Pay Online and Get Paid",
            "url": "https://app-signup.us.bill.com/onboarding/flow/org-intent",
            "time_usec": 1729821714821324,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app-signup.us.bill.com/onboarding/assets/favicons/favicon.ico?1729821618773",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://app-signup.us.bill.com/onboarding/flow/mfa/confirm",
            "url": "https://app-signup.us.bill.com/onboarding/flow/mfa/confirm",
            "time_usec": 1729821680122847,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app-signup.us.bill.com/onboarding/assets/favicons/favicon.ico?1729821618773",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://app-signup.us.bill.com/onboarding/flow/mfa/setup",
            "url": "https://app-signup.us.bill.com/onboarding/flow/mfa/setup",
            "time_usec": 1729821640049183,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app-signup.us.bill.com/onboarding/assets/favicons/favicon.ico?1729821618773",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Business Bill Payment | Pay Online and Get Paid",
            "url": "https://app-signup.us.bill.com/onboarding/flow/signup?inviteID=90FD90072416F4DB501A3D35AC97DD441DE031B9A6531C1C2292F51A323A13BA&sg=d-54b841c6445b445ea07da43feee55614&isFundedInvite=true&dueDate=1729838700&payeeAmount=130.00&estimatedArrivalDateCheck=1730246400&estimatedArrivalDateACH=1729814400&sgType=Check",
            "time_usec": 1729821612968660,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://app-signup.us.bill.com/onboarding/assets/favicons/favicon.ico?1729821618773",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Business Bill Payment | Pay Online and Get Paid",
            "url": "https://app-signup.us.bill.com/InviteSignup?invite=90FD90072416F4DB501A3D35AC97DD441DE031B9A6531C1C2292F51A323A13BA&sg=d-54b841c6445b445ea07da43feee55614&payeeAmount=130.00&dueDate=1729838700&isFundedInvite=true&estimatedArrivalDateACH=1729814400&estimatedArrivalDateCheck=1730246400&sgType=Check",
            "time_usec": 1729821609775251,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://support.apple.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign in to apps with your Apple Account using app-specific passwords - Apple Support",
            "url": "https://support.apple.com/en-us/102654",
            "time_usec": 1729821604292685,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://my.ticketmaster.com/order/Z7IVgZOxvZ16kZYPPa4/tickets?eventId=01006090DA1B5E70",
            "url": "https://my.ticketmaster.com/order/Z7IVgZOxvZ16kZYPPa4/tickets?eventId=01006090DA1B5E70",
            "time_usec": 1728345102698843,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://s1.s.tmol.io/static/favicon-tm.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Orders",
            "url": "https://my.ticketmaster.com/order/Z7IVgZOxvZ16kZYPPa4/view",
            "time_usec": 1728345097688631,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://s1.s.tmol.io/static/favicon-tm.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Transfer Accept",
            "url": "https://my.ticketmaster.com/transfer/accept?lang=en-us&transferToken=6f9136240e3dccf030fcf84381fb44622ef5e266b9b48dc01287fa7964c651aa85ac43efac030021029adae67d23c0d400b04550f1cc9e4fab2db8a8404948a2e1cf82a85b0462667934f3be2e0b44c1767737b6757b150b29ee288d6303d4f3",
            "time_usec": 1728345084032364,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://auth.ticketmaster.com/assets/favicon-32x32.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Ticketmaster Sign In",
            "url": "https://auth.ticketmaster.com/as/authorization.oauth2?client_id=8bf7204a7e97.web.ticketmaster.us&response_type=code&scope=openid%20profile%20phone%20email%20tm&redirect_uri=https://identity.ticketmaster.com/exchange&visualPresets=tm&lang=en-us&placementId=myAccount&showHeader=true&hideLeftPanel=False&integratorId=prd283.myAccount&intSiteToken=tm-us&TMUO=west_Fe7SODOCjonCFPMHZ60v7wKr0Jc3tyf0lV0Ro5lc5Pw%3D&deviceId=kQ22i5EgsjE3MjgzNDQ4MzM2Mjn%2FUj3be%2FifVg&doNotTrack=False",
            "time_usec": 1728344924242324,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Ticketmaster Sign In",
            "url": "https://auth.ticketmaster.com/as/authorization.oauth2?client_id=8bf7204a7e97.web.ticketmaster.us&response_type=code&scope=openid%20profile%20phone%20email%20tm&redirect_uri=https://identity.ticketmaster.com/exchange&visualPresets=tm&lang=en-us&placementId=myAccount&showHeader=true&hideLeftPanel=False&integratorId=prd283.myAccount&intSiteToken=tm-us&deviceId=kQ22i5EgsjE3MjgzNDQ4MzM2Mjn%2FUj3be%2FifVg",
            "time_usec": 1728344833862768,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.verizon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Bring Your Own Device (BYOD) | How To & Deals | V\u2026",
            "url": "https://www.verizon.com/bring-your-own-device/?CMP=bac_m_p_140_gdn_acq_24_01_acq_dsc-382979731_207763455&utm_medium=bac&utm_source=gdn&utm_campaign=m:acq&utm_content=acq_dsc&dclid=&wbraid=ClkKCAjw6oi4BhBfEkkAEbrBp61kMMSY4fD9btemb4Tqf5mzmyu6_sWf3y0af0nw1XOyHvafRzsZqPyW-b7U50YaT-fupJI0f67mJesTxYPALZI1O8QWGgK7Pg",
            "time_usec": 1728344832738993,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.verizon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Bring Your Own Device (BYOD) | How To & Deals | V\u2026",
            "url": "https://www.verizon.com/bring-your-own-device/?CMP=bac_m_p_140_gdn_acq_24_01_acq_dsc-382979731_207763455&utm_medium=bac&utm_source=gdn&utm_campaign=m:acq&utm_content=acq_dsc&dclid=&wbraid=ClkKCAjw6oi4BhBfEkkAEbrBp61kMMSY4fD9btemb4Tqf5mzmyu6_sWf3y0af0nw1XOyHvafRzsZqPyW-b7U50YaT-fupJI0f67mJesTxYPALZI1O8QWGgK7Pg",
            "time_usec": 1728344070690362,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://help.doordash.com/s/sfsites/c/resource/SRDdHelpSelectAssets/Favicons/apple-touch-icon.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "DoorDash Support",
            "url": "https://help.doordash.com/s/?language=en_US",
            "time_usec": 1728344068817099,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://help.doordash.com/s/sfsites/c/resource/SRDdHelpSelectAssets/Favicons/apple-touch-icon.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "DoorDash Support",
            "url": "https://help.doordash.com/s/?language=en_US",
            "time_usec": 1728090460904933,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://maps.gstatic.com/mapfiles/maps_lite/pwa/icons/maps15_bnuw3a_ios_192x192.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.google.com/maps/place/38°02'20.8\"N+78°30'02.0\"W/@38.0391154,-78.5005531,16z/data=!4m4!3m3!8m2!3d38.0391154!4d-78.5005531",
            "url": "https://www.google.com/maps/place/38%C2%B002'20.8%22N+78%C2%B030'02.0%22W/@38.0391154,-78.5005531,16z/data=!4m4!3m3!8m2!3d38.0391154!4d-78.5005531",
            "time_usec": 1728090383813761,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://maps.gstatic.com/mapfiles/maps_lite/pwa/icons/maps15_bnuw3a_ios_192x192.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.google.com/maps/place/38°02'20.8\"N+78°30'02.0\"W/@38.0391154,-78.5005531,17z/data=!4m4!3m3!8m2!3d38.0391154!4d-78.5005531",
            "url": "https://www.google.com/maps/place/38%C2%B002'20.8%22N+78%C2%B030'02.0%22W/@38.0391154,-78.5005531,17z/data=!4m4!3m3!8m2!3d38.0391154!4d-78.5005531",
            "time_usec": 1728090318510371,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "38°02'20.8\"N 78°30'02.0\"W - Google Maps",
            "url": "https://www.google.com/maps/place/38%C2%B002'20.8%22N+78%C2%B030'02.0%22W/@38.0391154,-78.5005531,16z/data=!4m4!3m3!8m2!3d38.0391154!4d-78.5005531",
            "time_usec": 1728090314591207,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge Message",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s6",
            "time_usec": 1728090313675231,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://cdn.gradescope.com/assets/logo/icons/64x64-3c29e9891a184582f67b6a2cd6c4a96bbfb20bbe7d7249d8f7feaa2ebd13832e.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "View Submission | Gradescope",
            "url": "https://www.gradescope.com/courses/884802/assignments/5070823/submissions/272931858",
            "time_usec": 1728085929863159,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s7",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s7",
            "time_usec": 1728085928913485,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge Message - Saving Session Information...",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s7",
            "time_usec": 1728085928855265,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge Message",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s6",
            "time_usec": 1728085926656895,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Duo Security",
            "url": "https://api-58663eb0.duosecurity.com/frame/v4/auth/prompt?sid=frameless-282dfc79-4dab-4591-a513-216f71370fbe",
            "time_usec": 1728085919978966,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Duo Security - Two-Factor Authentication",
            "url": "https://api-58663eb0.duosecurity.com/frame/frameless/v4/auth?sid=frameless-282dfc79-4dab-4591-a513-216f71370fbe&tx=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJkdW9fdW5hbWUiOiJ5a2MzaHAiLCJzY29wZSI6Im9wZW5pZCIsInJlc3BvbnNlX3R5cGUiOiJjb2RlIiwicmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly9zaGliaWRwLml0cy52aXJnaW5pYS5lZHUvaWRwL3Byb2ZpbGUvQXV0aG4vRHVvLzJGQS9kdW8tY2FsbGJhY2siLCJzdGF0ZSI6IjcxMGRlZGVjYjZjYjFjODU0NjY0OTBjNTY4M2E3NmE1LjY1MzE3MzM1IiwiZXhwIjoxNzI4MDg5NTE4LCJjbGllbnRfaWQiOiJESU41WkpQR0JWRzRRWTRGSVZHUSJ9.ZFgQ3JgP7GllW7hf0p8C5P3x86rq7iehW0Nujp2ZCxsN_5qY9L9aAOFTXvc0PEjBoEOFI-mUOp9Lj_a9EByiWQ&req-trace-group=93e0e2f6642ff1fe9a915fd9",
            "time_usec": 1728085919106423,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s4",
            "time_usec": 1728085902570557,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s3",
            "time_usec": 1728085884996320,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s2",
            "time_usec": 1728085879501646,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge Message - Loading Session Information",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s1",
            "time_usec": 1728085879302755,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://cdn.gradescope.com/assets/logo/icons/64x64-3c29e9891a184582f67b6a2cd6c4a96bbfb20bbe7d7249d8f7feaa2ebd13832e.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Gradescope",
            "url": "https://www.gradescope.com/saml",
            "time_usec": 1728085868863700,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://cdn.gradescope.com/assets/logo/icons/64x64-3c29e9891a184582f67b6a2cd6c4a96bbfb20bbe7d7249d8f7feaa2ebd13832e.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Log In | Gradescope",
            "url": "https://www.gradescope.com/login",
            "time_usec": 1728085865879062,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.untapped.io/app/apple-touch-icon.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign Up | Untapped",
            "url": "https://www.untapped.io/app/join/CANDIDATE",
            "time_usec": 1728085864862808,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign Up | Untapped",
            "url": "https://www.untapped.io/app/join/CANDIDATE",
            "time_usec": 1728010073138702,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Career Destination | Untapped",
            "url": "https://www.untapped.io/app/jobs/36b15740-8ee2-4fb2-90fb-755e9a0c0b40/apply?ref=email&utm_source=untapped-esp&utm_medium=email-operational&utm_campaign=Email+%231&utm_content=ctabutton&email=ykc3hp%40virginia.edu&ats_account_link_token=j8KuNX8lsjUvNRgLuSJPcnPmtNJlyjQp&student_full_name=Ryan+Steele&logo_url=https%3A%2F%2Fjumpstart-static.s3.amazonaws.com%2Fbackend%2F__sized__%2Forganizations%2Forganization%2Fz_0v7b8HS3qy4r1ceLDeEQ-thumbnail-200x200.png&organization_id=whatnot&organization_name=Whatnot&role_id=36b15740-8ee2-4fb2-90fb-755e9a0c0b40&role_type=JOB&role_title=Software+Engineer+Intern%2C+Summer+2025",
            "time_usec": 1728010045355137,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Programs-Brochure-International Studies Office",
            "url": "https://apps.educationabroad.virginia.edu/index.cfm?FuseAction=Programs.ViewProgram&Program_ID=10050",
            "time_usec": 1728010043328732,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Programs-Brochure-International Studies Office",
            "url": "https://apps.educationabroad.virginia.edu/index.cfm?FuseAction=Programs.ViewProgram&Program_ID=10050",
            "time_usec": 1727810809461148,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Education Abroad in Your Major or Minor | Educati\u2026",
            "url": "https://educationabroad.virginia.edu/education-abroad-your-major-or-minor",
            "time_usec": 1727810776425228,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge Message",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s1",
            "time_usec": 1727810774923169,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge Message",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s1",
            "time_usec": 1727810529753841,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s1",
            "time_usec": 1727810481339377,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://st1.zoom.us/zoom.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign In | Zoom",
            "url": "https://zoom.us/signin#/",
            "time_usec": 1727810444658738,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://st1.zoom.us/zoom.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Zoom meeting on web - Zoom",
            "url": "https://virginia.zoom.us/wc/97016206234/join?fromPWA=1&wpk=wcpk%7B0%7D%26%26%26%26wcpke654ebef1cd9ec028a38ae70b0da817b&_x_zm_rtaid=pdWfbmC1QZma11qN6oKxBg.1727810330808.3ad01db7bba9dea92188bc9a8f7312f6&_x_zm_rhtaid=287",
            "time_usec": 1727810442917455,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://st1.zoom.us/zoom.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Join meeting - Zoom",
            "url": "https://virginia.zoom.us/j/97016206234?pwd=mHz1XU3tiFpVj4sxaV0EQ0V5zUJ9IM.1",
            "time_usec": 1727810439911309,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge Message",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s3",
            "time_usec": 1727810432960429,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Password Help & ID Lookup - UVA ITS",
            "url": "https://virginia.service-now.com/its?id=itsweb_kb_article&sys_id=2f47ff87dbf6c744f032f1f51d961967",
            "time_usec": 1727810393819265,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s3",
            "time_usec": 1727810384743723,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s2",
            "time_usec": 1727810375390652,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge Message - Loading Session Information",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s1",
            "time_usec": 1727810375203792,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign In | Zoom",
            "url": "https://zoom.us/signin#/",
            "time_usec": 1727810340263318,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://st1.zoom.us/zoom.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Zoom meeting on web - Zoom",
            "url": "https://virginia.zoom.us/wc/97016206234/join?fromPWA=1&wpk=wcpk%7B0%7D%26%26%26%26wcpke654ebef1cd9ec028a38ae70b0da817b&_x_zm_rtaid=pdWfbmC1QZma11qN6oKxBg.1727810330808.3ad01db7bba9dea92188bc9a8f7312f6&_x_zm_rhtaid=287",
            "time_usec": 1727810337110836,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://st1.zoom.us/zoom.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Join meeting - Zoom",
            "url": "https://virginia.zoom.us/j/97016206234?pwd=mHz1XU3tiFpVj4sxaV0EQ0V5zUJ9IM.1",
            "time_usec": 1727810330859943,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "App",
            "url": "https://clientforms.mindbodyonline.com/?externalFormId=47d4b68c-bc26-4cf3-90fd-580e218af15a&utm_source=ClientForms&utm_campaign=ClientForms&utm_medium=ClientFormsUrl&_branch_referrer=H4sIAAAAAAAAA8soKSkottLXT08t0cvNS0lKqdTLqdRP1bfwM8wJK0yxTPVLsq8rSk1LLSrKzEuPTyrKLy9OLbJ1zijKz00FACuveJU9AAAA&%24web_only=true&_branch_match_id=1368343622437675893",
            "time_usec": 1727810330118163,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "App",
            "url": "https://clientforms.mindbodyonline.com/?externalFormId=47d4b68c-bc26-4cf3-90fd-580e218af15a&utm_source=ClientForms&utm_campaign=ClientForms&utm_medium=ClientFormsUrl&_branch_referrer=H4sIAAAAAAAAA8soKSkottLXT08t0cvNS0lKqdTLqdRP1bfwM8wJK0yxTPVLsq8rSk1LLSrKzEuPTyrKLy9OLbJ1zijKz00FACuveJU9AAAA&%24web_only=true&_branch_match_id=1368343622437675893",
            "time_usec": 1727476769056666,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://grader.mathworks.com/assets/favicon-c50094a0e6c4a5252144966240bdbce92c8e60d243bff587058e234363f3a019.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MATLAB Grader",
            "url": "https://grader.mathworks.com/courses/150999",
            "time_usec": 1727476767686542,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MATLAB Grader",
            "url": "https://grader.mathworks.com/courses/150999",
            "time_usec": 1726804366007603,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://grader.mathworks.com/assets/favicon-c50094a0e6c4a5252144966240bdbce92c8e60d243bff587058e234363f3a019.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MATLAB Grader",
            "url": "https://grader.mathworks.com/",
            "time_usec": 1726804362143363,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://grader.mathworks.com/assets/favicon-c50094a0e6c4a5252144966240bdbce92c8e60d243bff587058e234363f3a019.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MATLAB Grader",
            "url": "https://grader.mathworks.com/courses/150999-fall-2024-apma-3080-linear-algebra-projects-all-sections",
            "time_usec": 1726804334488358,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s4",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s4",
            "time_usec": 1726804333048569,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge Message - Saving Session Information...",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s4",
            "time_usec": 1726804332885697,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge Reminder",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s3",
            "time_usec": 1726804331390321,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Duo Security",
            "url": "https://api-58663eb0.duosecurity.com/frame/v4/auth/prompt?sid=frameless-7db4eae0-736f-4a2c-a5f5-578b6e442829",
            "time_usec": 1726804322867509,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Duo Security - Two-Factor Authentication",
            "url": "https://api-58663eb0.duosecurity.com/frame/frameless/v4/auth?sid=frameless-7db4eae0-736f-4a2c-a5f5-578b6e442829&tx=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJkdW9fdW5hbWUiOiJ5a2MzaHAiLCJzY29wZSI6Im9wZW5pZCIsInJlc3BvbnNlX3R5cGUiOiJjb2RlIiwicmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly9zaGliaWRwLml0cy52aXJnaW5pYS5lZHUvaWRwL3Byb2ZpbGUvQXV0aG4vRHVvLzJGQS9kdW8tY2FsbGJhY2siLCJzdGF0ZSI6ImIxZDkzMmFkYTQwZDFkNTAzZTJhZGY3NWJjNDQyZWI2LjY1MzI3MzMyIiwiZXhwIjoxNzI2ODA3OTIwLCJjbGllbnRfaWQiOiJESU41WkpQR0JWRzRRWTRGSVZHUSJ9.tU85CURbHUZpxpREBC831tlqY3sRRtThlA2oTa3r0-4h52MjN-9f2s5lt5Gd3typFy1fektZF-opngzMLU4mAw&req-trace-group=f0c352eac894753356e6c683",
            "time_usec": 1726804321580279,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s1",
            "time_usec": 1726804303076902,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge Message",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s2",
            "time_usec": 1726804298026143,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://shibidp.its.virginia.edu/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s2",
            "time_usec": 1726804256945907,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NetBadge Message - Loading Session Information",
            "url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s1",
            "time_usec": 1726804256707440,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.mathworks.com/etc.clientlibs/mathworks/clientlibs/customer-ui/templates/common/resources/images/favicon.20240821205631518.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MathWorks Account Sign In",
            "url": "https://www.mathworks.com/login?uri=https%3A%2F%2Fgrader.mathworks.com%2Fcourses%2F150999-fall-2024-apma-3080-linear-algebra-projects-all-sections%2Fview%2F83Tzn2lLYwLclAO7Eh4BWzcII_Si8J8p4xaINZ2w68g",
            "time_usec": 1726804246347092,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://grader.mathworks.com/assets/favicon-c50094a0e6c4a5252144966240bdbce92c8e60d243bff587058e234363f3a019.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MATLAB Grader",
            "url": "https://grader.mathworks.com/courses/150999-fall-2024-apma-3080-linear-algebra-projects-all-sections/view/83Tzn2lLYwLclAO7Eh4BWzcII_Si8J8p4xaINZ2w68g",
            "time_usec": 1726804241802309,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Greek House Chefs",
            "url": "https://beta.greekhousechefs.com/users/password",
            "time_usec": 1726666989066471,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://beta.greekhousechefs.com/icons/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Greek House Chefs",
            "url": "https://beta.greekhousechefs.com/users/password/edit?reset_password_token=bD_xSzhMd8Txbhw5iwLy",
            "time_usec": 1726666974501641,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://canaan-harris.youcanbook.me/thanks?i=itt_d7d2dcaf-6d39-46b5-96e1-d77dd4315ceb",
            "url": "https://canaan-harris.youcanbook.me/thanks?i=itt_d7d2dcaf-6d39-46b5-96e1-d77dd4315ceb",
            "time_usec": 1724205706535858,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://canaan-harris.youcanbook.me/static/img/ycbm/apple-touch-icon.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Confirm booking · Canaan Harris - Global Teaching\u2026",
            "url": "https://canaan-harris.youcanbook.me/form?i=itt_d7d2dcaf-6d39-46b5-96e1-d77dd4315ceb",
            "time_usec": 1724205589667471,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Select a time · Canaan Harris - Global Teaching P\u2026",
            "url": "https://canaan-harris.youcanbook.me/?jumpDate=2024-08-21&i=itt_d7d2dcaf-6d39-46b5-96e1-d77dd4315ceb",
            "time_usec": 1724205555558343,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://wizzair.com/dist-ssr/assets/images/apple-touch-icon.ab87a565.jpg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Cheap Flights | Book Direct for Best Deals | Wizz\u2026",
            "url": "https://wizzair.com/en-gb?emailVerification=20a9fb52-3329-474c-8e4a-c4454afd5e93",
            "time_usec": 1720800254052641,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "How to get from Bradenburg Berlin Airport to City Center - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPGGbgDDfLGdWNrFLSM",
            "time_usec": 1719921419007534,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "How to get from Bradenburg Berlin Airport to City Center - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPGGbgDDfLGdWNrFLSM?projector=1&messagePartId=0.1",
            "time_usec": 1719921379000297,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "How to get from Bradenburg Berlin Airport to City Center - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPGGbgDDfLGdWNrFLSM",
            "time_usec": 1719921330183463,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,649) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719921314516496,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "How to get from Bradenburg Berlin Airport to City Center - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPGGbgDDfLGdWNrFLSM",
            "time_usec": 1719921239127455,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,650) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719921236680955,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "ur phone number is weird - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBvvXqXBtgFbzfnDMLsnM",
            "time_usec": 1719921218073256,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,651) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719921214252527,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "worst/best night? - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBsdxwZMxggcwgxjKdNvb",
            "time_usec": 1719921209385504,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,652) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719912154968196,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hello maria - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/KtbxLvHTDKNQRZjmKCnJmzbsSmWgwPBvVV",
            "time_usec": 1719912144516582,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,649) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719912142424465,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "How to get from Bradenburg Berlin Airport to City Center - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPGGbgDDfLGdWNrFLSM",
            "time_usec": 1719910520972184,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "How to get from Bradenburg Berlin Airport to City Center - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPGGbgDDfLGdWNrFLSM?projector=1&messagePartId=0.1",
            "time_usec": 1719910500504064,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "How to get from Bradenburg Berlin Airport to City Center - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPGGbgDDfLGdWNrFLSM",
            "time_usec": 1719910434563223,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,649) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719910432299582,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "The Mandala Hotel - Google Maps",
            "url": "https://www.google.com/maps/place/The+Mandala+Hotel/@52.5091968,13.3762479,16z/data=!3m1!5s0x47a851c97f77872b:0xbae5dc0f46a654b5!4m9!3m8!1s0x47a8504a94b9e203:0xc758fe1a0a764436!5m2!4m1!1i2!8m2!3d52.5089801!4d13.3736812!16s%2Fg%2F119v8jmtf?entry=ttu",
            "time_usec": 1719910426898501,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "The Mandala Hotel - Google Maps",
            "url": "https://www.google.com/maps/place/The+Mandala+Hotel/@52.5091163,13.3734779,17.31z/data=!3m1!5s0x47a851c97f77872b:0xbae5dc0f46a654b5!4m9!3m8!1s0x47a8504a94b9e203:0xc758fe1a0a764436!5m2!4m1!1i2!8m2!3d52.5089801!4d13.3736812!16s%2Fg%2F119v8jmtf?entry=ttu",
            "time_usec": 1719910409056952,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "The Mandala Hotel - Google Maps",
            "url": "https://www.google.com/maps/place/The+Mandala+Hotel/@52.5073795,13.367285,14.34z/data=!3m1!5s0x47a851c97f77872b:0xbae5dc0f46a654b5!4m9!3m8!1s0x47a8504a94b9e203:0xc758fe1a0a764436!5m2!4m1!1i2!8m2!3d52.5089801!4d13.3736812!16s%2Fg%2F119v8jmtf?entry=ttu",
            "time_usec": 1719910397881947,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "The Mandala Hotel - Google Maps",
            "url": "https://www.google.com/maps/place/The+Mandala+Hotel/@52.5089801,13.3711063,17z/data=!3m2!4b1!5s0x47a851c97f77872b:0xbae5dc0f46a654b5!4m9!3m8!1s0x47a8504a94b9e203:0xc758fe1a0a764436!5m2!4m1!1i2!8m2!3d52.5089801!4d13.3736812!16s%2Fg%2F119v8jmtf?entry=ttu",
            "time_usec": 1719910388239822,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "The Mandala Hotel, Potsdamer Straße, Berlin, Germany - Google Maps",
            "url": "https://www.google.com/maps/@43.5355648,16.2922496,14z?entry=ttu",
            "time_usec": 1719910370522385,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Maps",
            "url": "https://www.google.com/maps",
            "time_usec": 1719910365680903,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://us.search.yahoo.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "google maps - Yahoo Search Results Yahoo Search Results",
            "url": "https://us.search.yahoo.com/yhs/search?hspart=itm&hsimp=yhs-001&type=prs_ydef_24_27&p=google%20maps&param1=1&param2=f%3D4%26b%3Dchrome%26ip%3D%26pa%3Dpdfconverterds%26type%3Dprs_ydef_24_27%26cat%3Dweb%26a%3Dprs_ydef_24_27%26xlp_pers_guid%3D6fa63486fa5b93029f1234268327e14c%26xlp_sess_guid%3D2076796b-52d5-4b3b-a5fd-2d2314961280%26uref%3D%26abid%3D%26xt_abg%3D%26xt_ver%3D10.1.4.72%26ls_ts%3D1719894020#01J1RTR50WGVWXEKKYJP0T28A5",
            "time_usec": 1719910363343028,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://us.search.yahoo.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "google maps - Yahoo Search Results Yahoo Search Results",
            "url": "https://us.search.yahoo.com/yhs/search?hspart=itm&hsimp=yhs-001&type=prs_ydef_24_27&p=google%20maps&param1=1&param2=f%3D4%26b%3Dchrome%26ip%3D%26pa%3Dpdfconverterds%26type%3Dprs_ydef_24_27%26cat%3Dweb%26a%3Dprs_ydef_24_27%26xlp_pers_guid%3D6fa63486fa5b93029f1234268327e14c%26xlp_sess_guid%3D2076796b-52d5-4b3b-a5fd-2d2314961280%26uref%3D%26abid%3D%26xt_abg%3D%26xt_ver%3D10.1.4.72%26ls_ts%3D1719894020#01J1RTR50WGVWXEKKYJP0T28A5",
            "time_usec": 1719910331287932,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Booking.com: Hotels in Berlin. Book your hotel now!",
            "url": "https://www.booking.com/searchresults.en-gb.html?aid=318615&label=New_English_EN_HR_27034596865-TuPNwxV7uxm4JdkpR_TY3gS637942140464%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-297601666035%3Adsa-64415224945%3Alp20412%3Ali%3Adec%3Adm%3Aag27034596865%3Acmp400849465&gclid=CjwKCAjwyo60BhBiEiwAHmVLJaOv-Z2gHchc-oACML1uEdqhGmAz43NaEXYzLvpCpZ0aAYBl0odhjhoC78oQAvD_BwE&highlighted_hotels=63392&redirected=1&city=-1746443&hlrd=no_dates&source=hotel&expand_sb=1&keep_landing=1&sid=143ad315046fab268076e86c4894838a#map_opened",
            "time_usec": 1719910324721561,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Booking.com: Hotels in Berlin. Book your hotel now!",
            "url": "https://www.booking.com/searchresults.en-gb.html?aid=318615&label=New_English_EN_HR_27034596865-TuPNwxV7uxm4JdkpR_TY3gS637942140464%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-297601666035%3Adsa-64415224945%3Alp20412%3Ali%3Adec%3Adm%3Aag27034596865%3Acmp400849465&gclid=CjwKCAjwyo60BhBiEiwAHmVLJaOv-Z2gHchc-oACML1uEdqhGmAz43NaEXYzLvpCpZ0aAYBl0odhjhoC78oQAvD_BwE&highlighted_hotels=63392&redirected=1&city=-1746443&hlrd=no_dates&source=hotel&expand_sb=1&keep_landing=1&sid=143ad315046fab268076e86c4894838a#map_opened",
            "time_usec": 1719910317917070,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Booking.com: Hotels in Berlin. Book your hotel now!",
            "url": "https://www.booking.com/searchresults.en-gb.html?aid=318615&label=New_English_EN_HR_27034596865-TuPNwxV7uxm4JdkpR_TY3gS637942140464%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-297601666035%3Adsa-64415224945%3Alp20412%3Ali%3Adec%3Adm%3Aag27034596865%3Acmp400849465&gclid=CjwKCAjwyo60BhBiEiwAHmVLJaOv-Z2gHchc-oACML1uEdqhGmAz43NaEXYzLvpCpZ0aAYBl0odhjhoC78oQAvD_BwE&highlighted_hotels=63392&redirected=1&city=-1746443&hlrd=no_dates&source=hotel&expand_sb=1&keep_landing=1&sid=143ad315046fab268076e86c4894838a",
            "time_usec": 1719910308743502,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hotel mandala berlin on map - Google Search",
            "url": "https://www.google.com/search?q=hotel+mandala+berlin+on++map&sca_esv=a5295d27d6bcdf79&sxsrf=ADLYWIKBF9ZIbHNHiYhfg1LQMCTAjITEFQ%3A1719910202704&ei=Or-DZpP5Ka-Hxc8PncODsAU&hotel_occupancy=2&ved=0ahUKEwiT_rTl_IeHAxWvQ_EDHZ3hAFYQ4dUDCA8&uact=5&oq=hotel+mandala+berlin+on++map&gs_lp=Egxnd3Mtd2l6LXNlcnAiHGhvdGVsIG1hbmRhbGEgYmVybGluIG9uICBtYXAyBhAAGBYYHjIIEAAYgAQYogRI6SBQiQdYoh1wAXgAkAEAmAGfAaABugqqAQMwLjm4AQPIAQD4AQGYAgmgAtEJwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigWYAwCIBgGQBgmSBwMxLjigB7QW&sclient=gws-wiz-serp",
            "time_usec": 1719910302690464,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hotel mandala berlin on map - Google Search",
            "url": "https://www.google.com/search?q=hotel+mandala+berlin+on++map&sca_esv=a5295d27d6bcdf79&sxsrf=ADLYWIKBF9ZIbHNHiYhfg1LQMCTAjITEFQ%3A1719910202704&ei=Or-DZpP5Ka-Hxc8PncODsAU&hotel_occupancy=2&ved=0ahUKEwiT_rTl_IeHAxWvQ_EDHZ3hAFYQ4dUDCA8&uact=5&oq=hotel+mandala+berlin+on++map&gs_lp=Egxnd3Mtd2l6LXNlcnAiHGhvdGVsIG1hbmRhbGEgYmVybGluIG9uICBtYXAyBhAAGBYYHjIIEAAYgAQYogRI6SBQiQdYoh1wAXgAkAEAmAGfAaABugqqAQMwLjm4AQPIAQD4AQGYAgmgAtEJwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigWYAwCIBgGQBgmSBwMxLjigB7QW&sclient=gws-wiz-serp#vhid=ESztrtRZw9PqCM&vssid=l",
            "time_usec": 1719910291928388,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hotel mandala berlin on map - Google Search",
            "url": "https://www.google.com/search?q=hotel+mandala+berlin+on++map&sca_esv=a5295d27d6bcdf79&sxsrf=ADLYWIKBF9ZIbHNHiYhfg1LQMCTAjITEFQ%3A1719910202704&ei=Or-DZpP5Ka-Hxc8PncODsAU&hotel_occupancy=2&ved=0ahUKEwiT_rTl_IeHAxWvQ_EDHZ3hAFYQ4dUDCA8&uact=5&oq=hotel+mandala+berlin+on++map&gs_lp=Egxnd3Mtd2l6LXNlcnAiHGhvdGVsIG1hbmRhbGEgYmVybGluIG9uICBtYXAyBhAAGBYYHjIIEAAYgAQYogRI6SBQiQdYoh1wAXgAkAEAmAGfAaABugqqAQMwLjm4AQPIAQD4AQGYAgmgAtEJwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigWYAwCIBgGQBgmSBwMxLjigB7QW&sclient=gws-wiz-serp",
            "time_usec": 1719910278775656,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hotel mandala berlin - Google Search",
            "url": "https://www.google.com/search?q=hotel+mandala+berlin&oq=hotel+mandala+berlin&aqs=chrome..69i64j0i22i30l9.5804j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1719910229484741,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "The Mandala Hotel",
            "url": "https://www.google.com/local/place/fid/0x47a8504a94b9e203:0xc758fe1a0a764436/photosphere?iu=https://streetviewpixels-pa.googleapis.com/v1/thumbnail?panoid%3D8FR-ovyB23NitOPLXyCwWg%26cb_client%3Dsearch.gws-prod.gps%26yaw%3D191.62308%26pitch%3D0%26thumbfov%3D100%26w%3D0%26h%3D0&ik=CAISFjhGUi1vdnlCMjNOaXRPUExYeUN3V2c%3D&sa=X&ved=2ahUKEwiT_rTl_IeHAxWvQ_EDHZ3hAFYQpx96BAgYEAo",
            "time_usec": 1719910227098857,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hotel mandala berlin - Google Search",
            "url": "https://www.google.com/search?q=hotel+mandala+berlin&oq=hotel+mandala+berlin&aqs=chrome..69i64j0i22i30l9.5804j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1719910203851937,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1719910196386931,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Airport to mandala via train - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPhqdXtPxXktmTPMLrV",
            "time_usec": 1719910195237535,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,648) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719910183105790,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hello maria - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/KtbxLvHTDKNQRZjmKCnJmzbsSmWgwPBvVV",
            "time_usec": 1719910160679299,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,649) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719910158031482,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "worst/best night? - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBsdxwZMxggcwgxjKdNvb",
            "time_usec": 1719910129318468,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,650) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719910122702575,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Gmail",
            "url": "https://mail.google.com/mail/u/0/",
            "time_usec": 1719910120237032,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "is germany in the eu - Google Search",
            "url": "https://www.google.com/search?q=is+germany+in+the+eu+&sca_esv=a5295d27d6bcdf79&biw=1078&bih=644&sxsrf=ADLYWIKmEeY_-St4NCuW6A2TI81MFE0bhQ%3A1719909082162&ei=2rqDZra3CZGHxc8PuaeGyAs&ved=0ahUKEwi2jI3P-IeHAxWRQ_EDHbmTAbkQ4dUDCA8&uact=5&oq=is+germany+in+the+eu+&gs_lp=Egxnd3Mtd2l6LXNlcnAiFWlzIGdlcm1hbnkgaW4gdGhlIGV1IDIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeSKMbUPcCWMgZcAF4AZABAJgB1AGgAfEZqgEGMC4yMC4xuAEDyAEA-AEBmAIWoAK4G6gCEcICBxAjGCcY6gLCAhQQABiABBjjBBi0AhjpBBjqAtgBAcICGhAuGIAEGNEDGOMEGLQCGMcBGOkEGOoC2AEBwgIKECMYgAQYJxiKBcICBBAjGCfCAgsQABiABBiRAhiKBcICChAAGIAEGEMYigXCAgUQABiABMICCxAuGIAEGNEDGMcBwgIREC4YgAQYkQIYxwEYigUYrwHCAgoQLhiABBhDGIoFwgILEC4YgAQYkQIYigXCAgUQLhiABMICFBAuGIAEGJcFGNwEGN4EGOAE2AECmAMQugYGCAEQARgBugYGCAIQARgUkgcGMS4yMC4xoAfcoQE&sclient=gws-wiz-serp",
            "time_usec": 1719909123446246,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "split to berlin flight 11:50am - Google Search",
            "url": "https://www.google.com/search?sca_esv=a5295d27d6bcdf79&sxsrf=ADLYWIJ_9Opbrs_DgoKk489E5dL7TmGd8w:1719909079277&q=split+to+berlin+flight+11:50am&source=lnms&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J_86uWOeqwdnV0yaSF-x2joQcoZ-0Q2Udkt2zEybT7Hdf5FBKg6QdtJ_mF8k5Wx_fIgbHvMt6hcZDR682UVZtlzdiYgOtsodGSlrzbWahCzBENuSKA&sa=X&ved=2ahUKEwjuj93N-IeHAxUDVvEDHSeHA30Q0pQJegQIChAB&biw=1078&bih=644&dpr=1",
            "time_usec": 1719909082956518,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "split to berlin flight 11:50am - Google Search",
            "url": "https://www.google.com/search?sca_esv=a5295d27d6bcdf79&sxsrf=ADLYWIL4rU6jHgDfQcdy_LlyhKjTl5hVDA:1719909069461&q=split+to+berlin+flight+11:50am&udm=2&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J_86uWOeqwdnV0yaSF-x2joQcoZ-0Q2Udkt2zEybT7Hdf5FBKg6QdtJ_mF8k5Wx_fIgbHvMt6hcZDR682UVZtlzdiYgOtsodGSlrzbWahCzBENuSKA&sa=X&ved=2ahUKEwj0jYXJ-IeHAxXVVvEDHaC6BLsQtKgLegQIBhAB&biw=1078&bih=644",
            "time_usec": 1719909080369756,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "split to berlin flight 11:50am - Google Search",
            "url": "https://www.google.com/search?q=split+to+berlin+flight+11%3A50am&oq=split+to+berlin+flight+11%3A50am&aqs=chrome..69i64j69i57.21741j0j1&sourceid=chrome&ie=UTF-8&zx=1719909071242&no_sw_cr=1",
            "time_usec": 1719909071244214,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "split to berlin flight 11:50am - Google Search",
            "url": "https://www.google.com/search?q=split+to+berlin+flight+11%3A50am&oq=split+to+berlin+flight+11%3A50am&aqs=chrome..69i64j69i57.21741j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1719909069605260,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1719909046796862,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hi I\u2019m in Berlin - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqNmpVCjZRBdfTxxBrhL",
            "time_usec": 1719908997165164,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,649) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719908771031048,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hello maria - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/KtbxLvHTDKNQRZjmKCnJmzbsSmWgwPBvVV",
            "time_usec": 1719908763918052,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,649) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719908758289511,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "How to get from Bradenburg Berlin Airport to City Center - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPGGbgDDfLGdWNrFLSM",
            "time_usec": 1719908705032415,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "How to get from Bradenburg Berlin Airport to City Center - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPGGbgDDfLGdWNrFLSM?projector=1&messagePartId=0.1",
            "time_usec": 1719908674974206,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "How to get from Bradenburg Berlin Airport to City Center - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPGGbgDDfLGdWNrFLSM",
            "time_usec": 1719908668431116,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "How to get from Bradenburg Berlin Airport to City Center - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPGGbgDDfLGdWNrFLSM?projector=1&messagePartId=0.1",
            "time_usec": 1719908667241961,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "How to get from Bradenburg Berlin Airport to City Center - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPGGbgDDfLGdWNrFLSM",
            "time_usec": 1719908664913005,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,650) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719908661689166,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sent Mail - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#sent",
            "time_usec": 1719908657193038,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,650) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719908650363349,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Airport to mandala via train - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPhqdXtPxXktmTPMLrV",
            "time_usec": 1719908590350422,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Airport to mandala via train - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPhqdXtPxXktmTPMLrV?projector=1&messagePartId=0.1",
            "time_usec": 1719908571621865,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Airport to mandala via train - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHNBqPhqdXtPxXktmTPMLrV",
            "time_usec": 1719908569283342,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,651) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719908567666679,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hello maria - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/KtbxLvHTDKNQRZjmKCnJmzbsSmWgwPBvVV",
            "time_usec": 1719908565535759,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hello maria - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/KtbxLvHTDKNQRZjmKCnJmzbsSmWgwPBvVV?compose=CllgCKCDlgwPPCxPkMpdrwhJpxGdcGtWRtNhpvHDFmHqnnQLLdvbNkjLVcKlSXnLTBRBCLMlQBV",
            "time_usec": 1719908492766418,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hello maria - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/KtbxLvHTDKNQRZjmKCnJmzbsSmWgwPBvVV",
            "time_usec": 1719908441248286,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,652) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719908439287646,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,652) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719908433904146,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Gmail",
            "url": "https://mail.google.com/mail/u/0/",
            "time_usec": 1719908430827112,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.easyjet.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "View Booking | K7NTRSK | easyJet.com",
            "url": "https://www.easyjet.com/en/manage/viewbooking?bookingReference=K7NTRSK&passengerLogin=true",
            "time_usec": 1719895100404813,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.easyjet.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "easyJet | Flights & Holidays ✈️ Book Low-Cost Airline Tickets",
            "url": "https://www.easyjet.com/en?accntmdl=2",
            "time_usec": 1719895064759173,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "View Booking | K7NTRSK | easyJet.com",
            "url": "https://www.easyjet.com/en/manage/viewbooking?bookingReference=K7NTRSK",
            "time_usec": 1719895060914371,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "easyJet booking reference: K7NTRSK - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHMFrDznKcwpvbKBHJXpqbb",
            "time_usec": 1719895052763466,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,647) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719895038119053,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "084871 is your secure sign in code - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHMFpvswdgWntptxWChrvrV",
            "time_usec": 1719895034155431,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "084871 is your secure sign in code - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHMFpvswdgWntptxWChrvrV?compose=jrjtXGkcxGHdPdRLHBPjFxWvPTQwZdSnKZghHpMDXwMlmtWZWrTQWPrXKrJxxmRglGwDGkTk",
            "time_usec": 1719894990328155,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "084871 is your secure sign in code - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHMFpvswdgWntptxWChrvrV?compose=new",
            "time_usec": 1719894975040834,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "084871 is your secure sign in code - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVxRHMFpvswdgWntptxWChrvrV",
            "time_usec": 1719894966441014,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Home - Google Drive",
            "url": "https://drive.google.com/drive/home",
            "time_usec": 1719894958373548,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Drive",
            "url": "https://drive.google.com/drive/home",
            "time_usec": 1719894956623246,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,648) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1719894956311009,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Copy of Spring Season in Fashion MK Plan XL by Slidesgo - Google Slides",
            "url": "https://docs.google.com/presentation/d/1NOtlgaTY4c6wARnkncFDtGnifsRLnVOw9HlhrH47uhU/edit#slide=id.g10cd9cec388_0_182",
            "time_usec": 1719894940840431,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Home - Google Drive",
            "url": "https://drive.google.com/drive/home",
            "time_usec": 1719894940632800,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_109",
            "time_usec": 1719894930708528,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Gmail",
            "url": "https://mail.google.com/mail/u/0/",
            "time_usec": 1719894929849882,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_109",
            "time_usec": 1719894926146668,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ra.co/static/favicon.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "RA Guide to New York City",
            "url": "https://ra.co/guide/us/newyorkcity",
            "time_usec": 1719894925117589,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Drive",
            "url": "https://drive.google.com/drive/home",
            "time_usec": 1719894923993157,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://flights.booking.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Book your flight - Booking.com",
            "url": "https://flights.booking.com/booking/confirmation/524c381301aeea854b0a36c50636dbed875ebd70983d460ea512132a36e056ba96b4eedd110640cb8c77e25fe564b1aff19482328aecd0165c41ccbda6f2effd2d8a51db2fc9bcd2eff51fd4f972?aid=2241148&label=flights-booking-unknown&ext-tr=KG6A3zNvQxiM2sPYxFyX6Q&ext-src=UK_desktop",
            "time_usec": 1719894921590518,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1719894018373388,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://mfb-fb-pdf-prod.s3.eu-central-1.amazonaws.com/3440e8nc8z8f6ba78orndeedetv4ng43rn446b211wdva2qf0k/Ticket-Dubrovnik-Split-3172778160.pdf",
            "url": "https://mfb-fb-pdf-prod.s3.eu-central-1.amazonaws.com/3440e8nc8z8f6ba78orndeedetv4ng43rn446b211wdva2qf0k/Ticket-Dubrovnik-Split-3172778160.pdf",
            "time_usec": 1719721271127584,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://shop.global.flixbus.com/rebooking",
            "url": "https://shop.global.flixbus.com/rebooking",
            "time_usec": 1719721263528288,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://d31za08snr2a6z.cloudfront.net/71fcccc3/img/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Manage My Booking | FlixBus",
            "url": "https://shop.global.flixbus.com/rebooking/login?utm_source=tripcycle&utm_medium=email&utm_campaign=..predrive&utm_content=com.flixbus",
            "time_usec": 1719721216340512,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Connect to web",
            "url": "https://www.italolive.it/en/connecttoweb",
            "time_usec": 1719558919642428,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://st1.zoom.us/zoom.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Meeting Registration - Zoom",
            "url": "https://virginia.zoom.us/rest/meeting/registrant/tJcrcu-pqzIvHdGazQvV0Kjqks2tqChs1iD1/info?tk=5QKysB1nRXkdkhr06ZooPSTxXSssOTj8BEojlbysrQyKuY6xS3tTS2Y.srHtPxAEKT9S8C4r&ac=approved&timezone_id=Europe/Rome#/edit",
            "time_usec": 1719558714979739,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Meeting Registration - Zoom",
            "url": "https://virginia.zoom.us/rest/meeting/registrant/tJcrcu-pqzIvHdGazQvV0Kjqks2tqChs1iD1/info?tk=5QKysB1nRXkdkhr06ZooPSTxXSssOTj8BEojlbysrQyKuY6xS3tTS2Y.srHtPxAEKT9S8C4r&ac=approved&timezone_id=Europe/Rome#/edit",
            "time_usec": 1719267597106615,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://st1.zoom.us/zoom.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Meeting Registration - Zoom",
            "url": "https://virginia.zoom.us/meeting/register/tJcrcu-pqzIvHdGazQvV0Kjqks2tqChs1iD1",
            "time_usec": 1719267563502040,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product_ios/3x/gsa_ios_60dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "can you make a withdrawal from any banks atm - Go\u2026",
            "url": "https://www.google.com/search?q=can+you+make+a+withdrawal+from+any+banks+atm&rlz=1CDGOYI_enUS976US998&oq=can+you+make+a+withdrawal+from+any+banks+atm&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yDQgCEAAYhgMYgAQYigUyDQgDEAAYhgMYgAQYigUyDQgEEAAYhgMYgAQYigUyDQgFEAAYhgMYgAQYigUyDQgGEAAYhgMYgAQYigUyBwgHECEYoAEyBwgIECEYoAEyBwgJECEYoAHSAQg5OTMyajBqOagCE7ACAeIDBBgBIF8&hl=en-US&sourceid=chrome-mobile&ie=UTF-8",
            "time_usec": 1719267562452460,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_114",
            "time_usec": 1718633849622916,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_97",
            "time_usec": 1718633560769484,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_97",
            "time_usec": 1718633547815051,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how much energy does pinatex require for production - Google Search",
            "url": "https://www.google.com/search?q=how+much+energy+does+pinatex+require+for+production&sca_esv=e7e7bfd0bcfc3035&sxsrf=ADLYWILxe1h5ZyfMvE2HUsZJxpqZZilW5A%3A1718632894320&ei=vkFwZoGRE_mH9u8Pzs-luAs&ved=0ahUKEwiB6Ki55uKGAxX5g_0HHc5nCbcQ4dUDCBA&uact=5&oq=how+much+energy+does+pinatex+require+for+production&gs_lp=Egxnd3Mtd2l6LXNlcnAiM2hvdyBtdWNoIGVuZXJneSBkb2VzIHBpbmF0ZXggcmVxdWlyZSBmb3IgcHJvZHVjdGlvbjIHECEYoAEYCjIHECEYoAEYCkjlhAFQ6ANYkYQBcAh4AZABAJgBrAGgAdsuqgEFMjQuMzO4AQPIAQD4AQGYAkGgAuUyqAIKwgIHECMYJxjqAsICBBAjGCfCAgsQABiABBiRAhiKBcICChAAGIAEGEMYigXCAgsQLhiABBjRAxjHAcICBRAAGIAEwgIFEC4YgATCAgoQABiABBgUGIcCwgIGEAAYFhgewgIHEAAYgAQYDcICCBAAGBYYChgewgIFECEYoAHCAgQQIRgVwgIFECEYnwWYAxDiAwUSATEgQJIHBTI0LjQxoAen0AI&sclient=gws-wiz-serp",
            "time_usec": 1718633293173386,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://dress-ecode.com/en/2024/02/16/is-pineapple-leaf-fabric-sustainable/",
            "time_usec": 1718633289508815,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how much energy does pinatex require for production - Google Search",
            "url": "https://www.google.com/search?q=how+much+energy+does+pinatex+require+for+production&sca_esv=e7e7bfd0bcfc3035&sxsrf=ADLYWILxe1h5ZyfMvE2HUsZJxpqZZilW5A%3A1718632894320&ei=vkFwZoGRE_mH9u8Pzs-luAs&ved=0ahUKEwiB6Ki55uKGAxX5g_0HHc5nCbcQ4dUDCBA&uact=5&oq=how+much+energy+does+pinatex+require+for+production&gs_lp=Egxnd3Mtd2l6LXNlcnAiM2hvdyBtdWNoIGVuZXJneSBkb2VzIHBpbmF0ZXggcmVxdWlyZSBmb3IgcHJvZHVjdGlvbjIHECEYoAEYCjIHECEYoAEYCkjlhAFQ6ANYkYQBcAh4AZABAJgBrAGgAdsuqgEFMjQuMzO4AQPIAQD4AQGYAkGgAuUyqAIKwgIHECMYJxjqAsICBBAjGCfCAgsQABiABBiRAhiKBcICChAAGIAEGEMYigXCAgsQLhiABBjRAxjHAcICBRAAGIAEwgIFEC4YgATCAgoQABiABBgUGIcCwgIGEAAYFhgewgIHEAAYgAQYDcICCBAAGBYYChgewgIFECEYoAHCAgQQIRgVwgIFECEYnwWYAxDiAwUSATEgQJIHBTI0LjQxoAen0AI&sclient=gws-wiz-serp",
            "time_usec": 1718633268874189,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_92",
            "time_usec": 1718633224301723,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "what are the requirements of a ow water use fibre - Google Search",
            "url": "https://www.google.com/search?q=what+are+the+requirements+of+a+ow+water+use+fibre&oq=what+are+the+requirements+of+a+ow+water+use+fibre&aqs=chrome..69i64j69i57.4281j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1718632934786046,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_97",
            "time_usec": 1718632927912643,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1718632904132090,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "what are tyeh requirements of a low energy material - Google Search",
            "url": "https://www.google.com/search?q=what+are+tyeh+requirements+of+a+low+energy+material&sca_esv=e7e7bfd0bcfc3035&sxsrf=ADLYWIIzk85fU6QjukidIdGCBxOO37KgOg%3A1718632788434&ei=VEFwZpqTGqX-7_UPwoydoA0&ved=0ahUKEwiajeqG5uKGAxUl_7sIHUJGB9QQ4dUDCBA&uact=5&oq=what+are+tyeh+requirements+of+a+low+energy+material&gs_lp=Egxnd3Mtd2l6LXNlcnAiM3doYXQgYXJlIHR5ZWggcmVxdWlyZW1lbnRzIG9mIGEgbG93IGVuZXJneSBtYXRlcmlhbDIHECEYoAEYCjIHECEYoAEYCkiOSVDeAljxRnACeAGQAQGYAdUBoAHWLaoBBjguNDMuMbgBA8gBAPgBAZgCNaACxS-oAg_CAgcQIxgnGOoCwgIUEAAYgAQY4wQYtAIY6QQY6gLYAQHCAgQQIxgnwgIKECMYgAQYJxiKBcICCxAAGIAEGJECGIoFwgIFEAAYgATCAgUQLhiABMICCxAuGIAEGNEDGMcBwgIQEC4YgAQY0QMYQxjHARiKBcICChAAGIAEGEMYigXCAgcQABiABBgKwgIOEC4YgAQYxwEYjgUYrwHCAgoQABiABBgUGIcCwgIHECMYsQIYJ8ICBxAAGIAEGA3CAggQABgKGA0YHsICBhAAGBYYHsICCBAAGBYYHhgPwgIIEAAYFhgKGB7CAgYQIRgVGAqYAxS6BgYIARABGAGSBwQzLjUwoAf-6QM&sclient=gws-wiz-serp",
            "time_usec": 1718632895087899,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "is pinatex a low energy product - Google Search",
            "url": "https://www.google.com/search?q=is+pinatex+a+low+energy+product&sca_esv=e7e7bfd0bcfc3035&sxsrf=ADLYWIIoFi0TB8rHIVVtlEabZNoaMID80A%3A1718630492245&ei=XDhwZqrHDviN9u8Pq72g8AU&ved=0ahUKEwiq5fW_3eKGAxX4hv0HHaseCF4Q4dUDCBA&uact=5&oq=is+pinatex+a+low+energy+product&gs_lp=Egxnd3Mtd2l6LXNlcnAiH2lzIHBpbmF0ZXggYSBsb3cgZW5lcmd5IHByb2R1Y3QyBRAhGKABMgUQIRigATIFECEYoAFIhWBQthtYzl5wBngBkAEAmAGyAaAB5B2qAQUxNS4yMbgBA8gBAPgBAZgCKqACwyCoAhHCAgcQIxgnGOoCwgIUEAAYgAQY4wQYtAIY6QQY6gLYAQHCAgsQABiABBiRAhiKBcICBRAAGIAEwgILEC4YgAQY0QMYxwHCAgUQLhiABMICChAjGIAEGCcYigXCAgQQIxgnwgIHEAAYgAQYCsICBxAuGIAEGArCAgYQABgWGB7CAggQABgWGB4YD8ICCBAAGBYYChgewgILEAAYgAQYhgMYigXCAgUQIRifBcICChAAGIAEGBQYhwLCAggQABiABBiiBMICBBAhGBXCAgcQIRigARgKmAMmugYGCAEQARgBkgcFMTUuMjegB53RAQ&sclient=gws-wiz-serp",
            "time_usec": 1718632789040943,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_92",
            "time_usec": 1718632770973961,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_109",
            "time_usec": 1718632675340960,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_102",
            "time_usec": 1718630996325551,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_102",
            "time_usec": 1718630707941011,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_92",
            "time_usec": 1718630656848203,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "what is a reach compliant - Google Search",
            "url": "https://www.google.com/search?q=what+is+a+reach+compliant&sca_esv=e7e7bfd0bcfc3035&sxsrf=ADLYWIIIZ7qbtkhNrKar31qDEuMrT3ddWQ%3A1718630396865&ei=_DdwZreVNNiL9u8P3OiesAk&ved=0ahUKEwi3g7iS3eKGAxXYhf0HHVy0B5YQ4dUDCBA&uact=5&oq=what+is+a+reach+compliant&gs_lp=Egxnd3Mtd2l6LXNlcnAiGXdoYXQgaXMgYSByZWFjaCBjb21wbGlhbnQyBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBUinKVCsAli3KHAEeAGQAQCYAeABoAHEGqoBBzE0LjExLjO4AQPIAQD4AQGYAiCgAr0dqAIUwgIHECMYJxjqAsICExAAGIAEGEMYtAIYigUY6gLYAQHCAhkQLhiABBjRAxhDGLQCGMcBGIoFGOoC2AEBwgIEECMYJ8ICChAjGIAEGCcYigXCAgoQABiABBhDGIoFwgIFEAAYgATCAgUQLhiABMICCxAuGIAEGNEDGMcBwgILEAAYgAQYkQIYigXCAhAQLhiABBjRAxhDGMcBGIoFwgIIEC4YgAQY1ALCAgsQLhiABBjHARivAcICGhAuGIAEGMcBGK8BGJcFGNwEGN4EGOAE2AECwgIOEC4YgAQYxwEYjgUYrwHCAgoQABiABBgUGIcCwgIIEAAYFhgeGA-YAyi6BgYIARABGAG6BgYIAhABGBSSBwcxNi4xMi40oAfB5wE&sclient=gws-wiz-serp",
            "time_usec": 1718630492935604,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "gots certified - Google Search",
            "url": "https://www.google.com/search?q=gots+certified&oq=gots+certified&aqs=chrome.0.0i512j0i22i30l9.6921j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1718630397533148,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://global-standard.org/",
            "time_usec": 1718630385207603,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1718630379654333,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "does pinatex productionn use harmful chemicals - Google Search",
            "url": "https://www.google.com/search?q=does+pinatex+productionn+use+harmful+chemicals+&sca_esv=e7e7bfd0bcfc3035&sxsrf=ADLYWIJDM8n3mG3VdmG2VkDXkQwyJyHXQQ%3A1718629347720&ei=4zNwZtrPK-Hr7_UPw6absAI&ved=0ahUKEwiazZWe2eKGAxXh9bsIHUPTBiYQ4dUDCBA&uact=5&oq=does+pinatex+productionn+use+harmful+chemicals+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIi9kb2VzIHBpbmF0ZXggcHJvZHVjdGlvbm4gdXNlIGhhcm1mdWwgY2hlbWljYWxzIDIHECEYoAEYCjIHECEYoAEYCki6hAFQ0wdYin9wB3gBkAEEmAHMAqABpz2qAQg3LjM1LjkuMbgBA8gBAPgBAZgCN6ACjDioAgzCAgcQIxgnGOoCwgIUEAAYgAQY4wQYtAIY6QQY6gLYAQHCAgoQIxiABBgnGIoFwgIFEAAYgATCAgsQLhiABBjRAxjHAcICBRAuGIAEwgIHEAAYgAQYCsICBhAAGBYYHsICCBAAGBYYHhgPwgIIEAAYFhgKGB7CAgsQABiABBiGAxiKBcICCxAAGIAEGKIEGIsDwgIFECEYoAHCAgUQIRifBcICBBAhGBXCAgYQIRgVGArCAgQQIRgKmAMn4gMFEgExIEC6BgYIARABGAGSBwkxMy4zNC43LjGgB-KgAg&sclient=gws-wiz-serp",
            "time_usec": 1718630179389065,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_87",
            "time_usec": 1718630156981504,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_82",
            "time_usec": 1718630138595680,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_77",
            "time_usec": 1718630054917190,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_82",
            "time_usec": 1718630032926708,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://impactful.ninja/wp-content/uploads/2020/10/cropped-Impactful-Ninja_Favicon-1-32x32.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "How Sustainable Are Piñatex Fabrics? A Life-Cycle Analysis | Impactful Ninja",
            "url": "https://impactful.ninja/how-sustainable-are-pinatex-fabrics/",
            "time_usec": 1718629999098453,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "full analysis of pinatex - Google Search",
            "url": "https://www.google.com/search?q=full+analysis+of+pinatex&sca_esv=e7e7bfd0bcfc3035&sxsrf=ADLYWILUMR-Krz47pqGUSz6YBq82FD3pvA%3A1718629540301&ei=pDRwZsH3Edm69u8Pu6y70AE&ved=0ahUKEwjB2f_52eKGAxVZnf0HHTvWDhoQ4dUDCBA&uact=5&oq=full+analysis+of+pinatex&gs_lp=Egxnd3Mtd2l6LXNlcnAiGGZ1bGwgYW5hbHlzaXMgb2YgcGluYXRleDIHECEYoAEYCkiJJVCSBFjGJHABeAGQAQOYAYoDoAGqF6oBCDcuMTMuMi4xuAEDyAEA-AEBmAIVoAKhEqgCCsICBxAjGCcY6gLCAgsQABiABBiRAhiKBcICERAuGIAEGJECGNEDGMcBGIoFwgIKEAAYgAQYQxiKBcICBRAAGIAEwgIFEC4YgATCAg4QLhiABBjHARiOBRivAcICCBAuGIAEGNQCwgIKEAAYgAQYFBiHAsICBhAAGBYYHsICCBAAGBYYHhgPwgIFECEYoAHCAgUQIRifBZgDD-IDBRIBMSBAkgcENC4xN6AHuL0B&sclient=gws-wiz-serp",
            "time_usec": 1718629993560228,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "full analysis of pinatex - Google Search",
            "url": "https://www.google.com/search?q=full+analysis+of+pinatex&sca_esv=e7e7bfd0bcfc3035&sxsrf=ADLYWILUMR-Krz47pqGUSz6YBq82FD3pvA%3A1718629540301&ei=pDRwZsH3Edm69u8Pu6y70AE&ved=0ahUKEwjB2f_52eKGAxVZnf0HHTvWDhoQ4dUDCBA&uact=5&oq=full+analysis+of+pinatex&gs_lp=Egxnd3Mtd2l6LXNlcnAiGGZ1bGwgYW5hbHlzaXMgb2YgcGluYXRleDIHECEYoAEYCkiJJVCSBFjGJHABeAGQAQOYAYoDoAGqF6oBCDcuMTMuMi4xuAEDyAEA-AEBmAIVoAKhEqgCCsICBxAjGCcY6gLCAgsQABiABBiRAhiKBcICERAuGIAEGJECGNEDGMcBGIoFwgIKEAAYgAQYQxiKBcICBRAAGIAEwgIFEC4YgATCAg4QLhiABBjHARiOBRivAcICCBAuGIAEGNQCwgIKEAAYgAQYFBiHAsICBhAAGBYYHsICCBAAGBYYHhgPwgIFECEYoAHCAgUQIRifBZgDD-IDBRIBMSBAkgcENC4xN6AHuL0B&sclient=gws-wiz-serp",
            "time_usec": 1718629979175705,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "what are most vegan leathers made of - Google Search",
            "url": "https://www.google.com/search?q=what+are+most+vegan+leathers+made+of+&sca_esv=e7e7bfd0bcfc3035&sxsrf=ADLYWIIgdmfTBtIFyfFnZclL-BJ-e8V9GQ%3A1718629419833&ei=KzRwZsqvMouG9u8P3-e5wAw&ved=0ahUKEwiK8cbA2eKGAxULg_0HHd9zDsgQ4dUDCBA&uact=5&oq=what+are+most+vegan+leathers+made+of+&gs_lp=Egxnd3Mtd2l6LXNlcnAiJXdoYXQgYXJlIG1vc3QgdmVnYW4gbGVhdGhlcnMgbWFkZSBvZiAyBxAhGKABGAoyBxAhGKABGAoyBxAhGKABGAoyBxAhGKABGAoyBxAhGKABGApIkj5QlQRYhT1wBngBkAEAmAG4AaAB2iOqAQUxMS4zMbgBA8gBAPgBAZgCL6AC-SWoAgrCAgcQIxgnGOoCwgIKECMYgAQYJxiKBcICBBAjGCfCAgsQABiABBiRAhiKBcICChAAGIAEGEMYigXCAgUQABiABMICBRAuGIAEwgILEC4YgAQY0QMYxwHCAgoQABiABBjJAxgKwgIHEAAYgAQYCsICCxAAGIAEGJIDGIoFwgIKEC4YgAQYQxiKBcICDBAuGIAEGEMYigUYCsICBxAuGIAEGArCAg0QLhiABBjRAxjHARgKwgIOEC4YgAQYxwEYjgUYrwHCAgYQABgWGB7CAggQABgWGAoYHsICCBAAGBYYHhgPwgILEAAYgAQYhgMYigXCAgUQIRigAcICBRAhGJ8FmAMO4gMFEgExIECSBwUxNC4zM6AHydMC&sclient=gws-wiz-serp",
            "time_usec": 1718629540982010,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how biodegradeable are most non-animal leathers percent - Google Search",
            "url": "https://www.google.com/search?q=how+biodegradeable+are+most+non-animal+leathers+percent&sca_esv=e7e7bfd0bcfc3035&sxsrf=ADLYWIJT_p9pBzQNBSAH7d6EByu6nfw0LQ%3A1718629399452&ei=FzRwZtyPG42B9u8Pk7iL0AU&ved=0ahUKEwic9-q22eKGAxWNgP0HHRPcAloQ4dUDCBA&uact=5&oq=how+biodegradeable+are+most+non-animal+leathers+percent&gs_lp=Egxnd3Mtd2l6LXNlcnAiN2hvdyBiaW9kZWdyYWRlYWJsZSBhcmUgbW9zdCBub24tYW5pbWFsIGxlYXRoZXJzIHBlcmNlbnQyBxAhGKABGAoyBxAhGKABGAoyBxAhGKABGApIjwtQ-gJYoApwAXgBkAEAmAGxAaAB0QeqAQMwLje4AQPIAQD4AQGYAgigApAIwgIKEAAYsAMY1gQYR8ICBBAhGBWYAwDiAwUSATEgQIgGAZAGCJIHAzEuN6AHlCw&sclient=gws-wiz-serp",
            "time_usec": 1718629420763964,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how biodegradeable are most non-animal leathers - Google Search",
            "url": "https://www.google.com/search?q=how+biodegradeable+are+most+non-animal+leathers&sca_esv=e7e7bfd0bcfc3035&sxsrf=ADLYWIKMEFwwu3hAF-Ui09nWVoTgyJaNCA%3A1718628761499&ei=mTFwZsjfHdCQ9u8Piv2-gAE&ved=0ahUKEwiIkNGG1-KGAxVQiP0HHYq-DxAQ4dUDCBA&uact=5&oq=how+biodegradeable+are+most+non-animal+leathers&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIi9ob3cgYmlvZGVncmFkZWFibGUgYXJlIG1vc3Qgbm9uLWFuaW1hbCBsZWF0aGVyczIHECEYoAEYCjIHECEYoAEYCjIHECEYoAEYCkj3UFCrCVijUHABeAGQAQKYAewBoAHvLKoBBjguMzYuMrgBA8gBAPgBAZgCLaACmiyoAgrCAgcQIxgnGOoCwgIEECMYJ8ICChAjGIAEGCcYigXCAgsQLhiABBjRAxjHAcICBRAAGIAEwgIFEC4YgATCAg4QLhiABBjHARiOBRivAcICCxAAGIAEGJECGIoFwgIGEAAYFhgewgILEAAYgAQYhgMYigXCAgsQABiABBiiBBiLA8ICCBAAGAgYDRgewgIKEAAYCBgKGA0YHsICBxAjGLACGCfCAgcQABiABBgNwgIIEAAYFhgeGA_CAgYQABgNGB7CAggQABgWGAoYHsICBRAhGJ8FwgIEECEYFZgDEJIHBjYuMzguMaAHz-IC&sclient=gws-wiz-serp",
            "time_usec": 1718629400183224,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how iodegradable is pinatex - Google Search",
            "url": "https://www.google.com/search?q=how+iodegradable+is+pinatex&sca_esv=e7e7bfd0bcfc3035&sxsrf=ADLYWIJs7fjbMsfECQ9B-pxtFTIKaCmGnA%3A1718628722839&ei=cjFwZqnbMsXd7_UPp5iHyA0&ved=0ahUKEwip3Jn01uKGAxXF7rsIHSfMAdkQ4dUDCBA&uact=5&oq=how+iodegradable+is+pinatex&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIhtob3cgaW9kZWdyYWRhYmxlIGlzIHBpbmF0ZXgyBxAhGKABGAoyBxAhGKABGAoyCBAhGBUYChgNSLouUIQGWNgtcAN4AJABAJgBtAGgAdYYqgEENy4yMLgBA8gBAPgBAZgCHaAC0BnCAgoQABiwAxjWBBhHwgIKECMYgAQYJxiKBcICCxAAGIAEGJECGIoFwgIOEC4YgAQYkQIY1AIYigXCAg4QLhiABBjHARiOBRivAcICCxAuGIAEGNEDGMcBwgIFEAAYgATCAgUQLhiABMICBBAjGCfCAgcQABiABBgKwgIGEAAYFhgewgILEAAYgAQYhgMYigXCAggQABiABBiiBMICBxAAGIAEGA3CAggQABgIGA0YHsICCxAAGIAEGKIEGIsDwgIFECEYoAHCAgYQABgNGB7CAggQABgNGB4YD8ICBRAhGJ8FwgIGECEYFRgKwgIEECEYCpgDAIgGAZAGCJIHBDcuMjKgB5fUAQ&sclient=gws-wiz-serp",
            "time_usec": 1718629349031266,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_82",
            "time_usec": 1718629309266230,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Ananas Anam - Google Search",
            "url": "https://www.google.com/search?sca_esv=e7e7bfd0bcfc3035&sxsrf=ADLYWIIw6I1cHQVQD94S7MFFigbd2vqxYw:1718628019399&q=Ananas+Anam&stick=H4sIAAAAAAAAAONgVuLVT9c3NEyrNDIvybNMWsTK7ZiXmJdYrACkcgGXVDq0HwAAAA&sa=X&ved=2ahUKEwiH1eKk1OKGAxVBhP0HHQgkBWYQmxMoAHoECDkQAg&biw=1440&bih=789&dpr=1#ip=1",
            "time_usec": 1718629172811442,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://www.bcorporation.net/en-us/find-a-b-corp/company/ananas-anam",
            "time_usec": 1718629169618738,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_77",
            "time_usec": 1718629126824682,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "biodegradability of pinatex - Google Search",
            "url": "https://www.google.com/search?q=biodegradability+of+pinatex&oq=biodegradability+of+pinatex&aqs=chrome..69i64j69i57.10193j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1718629092085240,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://www.texspacetoday.com/pinatex-eco-friendly-leather-made-from-pineapples/",
            "time_usec": 1718629089970480,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_82",
            "time_usec": 1718628798332239,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "biodegradability of pinatex - Google Search",
            "url": "https://www.google.com/search?q=biodegradability+of+pinatex&oq=biodegradability+of+pinatex&aqs=chrome..69i64j69i57.10193j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1718628788753744,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://www.ananas-anam.com/faqs/#:~:text=Is%20Pi%C3%B1atex%20biodegradable%3F,biodegradable%20under%20controlled%20industry%20conditions.",
            "time_usec": 1718628786746610,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "what is pla - Google Search",
            "url": "https://www.google.com/search?q=what+is+pla&oq=what+is+pla+&aqs=chrome..69i64j35i19i39i512i650j35i39j0i512j0i131i433i512j0i512j0i3l2j0i512j0i3.5753j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1718628762451536,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1718628755204186,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_77",
            "time_usec": 1718628733347476,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "biodegradability of pinatex - Google Search",
            "url": "https://www.google.com/search?q=biodegradability+of+pinatex&oq=biodegradability+of+pinatex&aqs=chrome..69i64j69i57.10193j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1718628723469607,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1718628711645609,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_114",
            "time_usec": 1718628651673591,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "An Analysis of Pinatex - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_82",
            "time_usec": 1718628629307750,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Ananas Anam - Google Search",
            "url": "https://www.google.com/search?sca_esv=e7e7bfd0bcfc3035&sxsrf=ADLYWIIw6I1cHQVQD94S7MFFigbd2vqxYw:1718628019399&q=Ananas+Anam&stick=H4sIAAAAAAAAAONgVuLVT9c3NEyrNDIvybNMWsTK7ZiXmJdYrACkcgGXVDq0HwAAAA&sa=X&ved=2ahUKEwiH1eKk1OKGAxVBhP0HHQgkBWYQmxMoAHoECDkQAg&biw=1440&bih=789&dpr=1",
            "time_usec": 1718628410076320,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://www.ananas-anam.com/sales-sampling/",
            "time_usec": 1718628408224108,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Untitled presentation - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_77",
            "time_usec": 1718628086953971,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Untitled presentation - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_77",
            "time_usec": 1718628038892140,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "pinatex - Google Search",
            "url": "https://www.google.com/search?q=pinatex&oq=pinatex&aqs=chrome..69i64j46i20i199i263i465i512j35i39j0i20i263i512j0i512l6.31862j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1718628021243676,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "pinatex - Google Search",
            "url": "https://www.google.com/search?q=pinatex&oq=pinatex&aqs=chrome..69i64j46i20i199i263i465i512j35i39j0i20i263i512j0i512l6.31862j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1718628019512779,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1718627986630690,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Untitled presentation - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_102",
            "time_usec": 1718627949843936,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Untitled presentation - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_97",
            "time_usec": 1718627939941330,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Untitled presentation - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_87",
            "time_usec": 1718627911844395,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Untitled presentation - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_82",
            "time_usec": 1718627894407444,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Untitled presentation - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.g2e6422d6e4f_0_77",
            "time_usec": 1718627872122906,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Untitled presentation - Google Slides",
            "url": "https://docs.google.com/presentation/d/1cv3FxrgSt50gw7I-dDzsp5_KKSAH6uok7FbnuM1Kbdg/edit#slide=id.p",
            "time_usec": 1718627797603869,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Home - Google Drive",
            "url": "https://drive.google.com/drive/home",
            "time_usec": 1718627778278597,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google",
            "url": "https://www.google.com/",
            "time_usec": 1718627772394543,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://accounts.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign in - Google Accounts",
            "url": "https://accounts.google.com/v3/signin/challenge/pwd?TL=AC3PFD6C9qFfmt_QyNZOVjROsH5QgSRiR2bUAMDf0z_ahAINmtaOQLtEO_7oYFRO&checkConnection=youtube:350&checkedDomains=youtube&cid=1&continue=https://www.google.com/&ddm=0&ec=GAZAmgQ&flowName=GlifWebSignIn&hl=en_US&ifkv=AS5LTASjHOAMKp_6x-xFO8AARma1f2PdRwU1HyDZqAnofmk7pq1X9lLzC4RYJ0bDMsuAhdNpju0x&pstMsg=1",
            "time_usec": 1718627768200599,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign in - Google Accounts",
            "url": "https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&hl=en&passive=true&ifkv=AS5LTASjHOAMKp_6x-xFO8AARma1f2PdRwU1HyDZqAnofmk7pq1X9lLzC4RYJ0bDMsuAhdNpju0x&ddm=0&flowName=GlifWebSignIn&flowEntry=ServiceLogin",
            "time_usec": 1718627765470958,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google",
            "url": "https://www.google.com/",
            "time_usec": 1718627748296795,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "http://search.anysearchmanager.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Any Search",
            "url": "http://search.anysearchmanager.com/?hsypt=iima&pub_id=3000&affid=A34DW_set_bcr_H",
            "time_usec": 1718627742924357,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product_ios/3x/gsa_ios_60dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "can you make a withdrawal from any banks atm - Go\u2026",
            "url": "https://www.google.com/search?q=can+you+make+a+withdrawal+from+any+banks+atm&rlz=1CDGOYI_enUS976US998&oq=can+you+make+a+withdrawal+from+any+banks+atm&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yDQgCEAAYhgMYgAQYigUyDQgDEAAYhgMYgAQYigUyDQgEEAAYhgMYgAQYigUyDQgFEAAYhgMYgAQYigUyDQgGEAAYhgMYgAQYigUyBwgHECEYoAEyBwgIECEYoAEyBwgJECEYoAHSAQg5OTMyajBqOagCE7ACAeIDBBgBIF8&hl=en-US&sourceid=chrome-mobile&ie=UTF-8",
            "time_usec": 1718354450843312,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://static.tacdn.com/img2/brand_refresh/application_icons/touch-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "ATM inside a bank. - Florence Forum - Tripadvisor",
            "url": "https://www.tripadvisor.com/ShowTopic-g187895-i68-k7315446-ATM_inside_a_bank-Florence_Tuscany.html",
            "time_usec": 1718354259146558,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product_ios/3x/gsa_ios_60dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "indoor cash withdrawal atm in florence - Google S\u2026",
            "url": "https://www.google.com/search?q=indoor+cash+withdrawl+atm+in+flirence&sca_esv=3fd026c1a73d8e9b&rlz=1CDGOYI_enUS976US998&hl=en-US&sxsrf=ADLYWIKlyovk5EraeXxxEfVtz2pQ23yH2A%3A1718353976377&ei=OABsZvO6E9SZi-gP75Gx8Ag&oq=indoor+cash+withdrawl+atm+in+flirence&gs_lp=EhNtb2JpbGUtZ3dzLXdpei1zZXJwIiVpbmRvb3IgY2FzaCB3aXRoZHJhd2wgYXRtIGluIGZsaXJlbmNlMgcQIRigARgKMgcQIRigARgKSIZVULEPWK9TcAR4AZABAJgBfqABlRyqAQUyMy4xNLgBA8gBAPgBAZgCKKAC7hyoAg_CAgoQABiwAxjWBBhHwgIHECMYJxjqAsICChAjGIAEGCcYigXCAgQQIxgnwgILEAAYgAQYkQIYigXCAgoQLhiABBhDGIoFwgIKEAAYgAQYQxiKBcICBRAAGIAEwgIQEC4YgAQY0QMYQxjHARiKBcICFBAuGIAEGJECGMcBGIoFGI4FGK8BwgIIEAAYgAQYkgPCAg0QABiABBhDGMkDGIoFwgIHEAAYgAQYCsICDRAuGIAEGMcBGAoYrwHCAggQABgWGAoYHsICBhAAGBYYHsICCxAAGIAEGIYDGIoFwgIFECEYoAHCAgUQIRifBcICBBAhGArCAgYQIRgVGArCAgUQIRiSA5gDCIgGAZAGCJIHBTI1LjE1oAfpgQI&sclient=mobile-gws-wiz-serp",
            "time_usec": 1718354228728708,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product_ios/3x/gsa_ios_60dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.google.com/search?q=best+atm+in+florence&rlz=1CDGOYI_enUS976US998&oq=best+atm+in+florence&gs_lcrp=EgZjaHJvbWUqCQgAEAAYExiABDIJCAAQABgTGIAEMgoIARAAGBMYFhgeMgoIAhAAGBMYFhgeMgcIAxAhGJ8FMgcIBBAhGJ8FMgcIBRAhGJ8F0gEINjM4OGowajSoAhOwAgHiAwQYASBf&hl=en-US&sourceid=chrome-mobile&ie=UTF-8#sbfbu=1&pi=best atm in florence",
            "url": "https://www.google.com/search?q=best+atm+in+florence&rlz=1CDGOYI_enUS976US998&oq=best+atm+in+florence&gs_lcrp=EgZjaHJvbWUqCQgAEAAYExiABDIJCAAQABgTGIAEMgoIARAAGBMYFhgeMgoIAhAAGBMYFhgeMgcIAxAhGJ8FMgcIBBAhGJ8FMgcIBRAhGJ8F0gEINjM4OGowajSoAhOwAgHiAwQYASBf&hl=en-US&sourceid=chrome-mobile&ie=UTF-8#sbfbu=1&pi=best%20atm%20in%20florence",
            "time_usec": 1718354217683549,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product_ios/3x/gsa_ios_60dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "best atm in florence - Google Search",
            "url": "https://www.google.com/search?q=best+atm+in+florence&rlz=1CDGOYI_enUS976US998&oq=best+atm+in+florence&gs_lcrp=EgZjaHJvbWUqCQgAEAAYExiABDIJCAAQABgTGIAEMgoIARAAGBMYFhgeMgoIAhAAGBMYFhgeMgcIAxAhGJ8FMgcIBBAhGJ8FMgcIBRAhGJ8F0gEINjM4OGowajSoAhOwAgHiAwQYASBf&hl=en-US&sourceid=chrome-mobile&ie=UTF-8",
            "time_usec": 1718353976527854,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968816441,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968815792,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968815753,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968815717,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968815682,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968815606,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968815570,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968814920,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968814886,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968814851,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968814437,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968814391,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968814355,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968814324,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968814158,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968814057,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968814025,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813946,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813876,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813809,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813754,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813680,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813647,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813608,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813485,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813405,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813313,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813276,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813241,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813198,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813093,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968813051,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968812585,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968812552,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968812515,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968812478,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968812295,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968812213,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "http://google.com/",
            "time_usec": 1718353968812122,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/forms/device_home/ios_152.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "SUMMER I 2024 WEEKEND LOCATION FORM",
            "url": "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfJAFy6pC94QTfbI3cz75SBzq12nuJc5nQWXzy-GZ5sJEm1MQ/formResponse",
            "time_usec": 1718351644925742,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/forms/device_home/ios_152.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "SUMMER I 2024 WEEKEND LOCATION FORM",
            "url": "https://docs.google.com/forms/d/e/1FAIpQLSfJAFy6pC94QTfbI3cz75SBzq12nuJc5nQWXzy-GZ5sJEm1MQ/formResponse",
            "time_usec": 1718351642899974,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "SUMMER I 2024 WEEKEND LOCATION FORM",
            "url": "https://docs.google.com/forms/d/e/1FAIpQLSfJAFy6pC94QTfbI3cz75SBzq12nuJc5nQWXzy-GZ5sJEm1MQ/viewform",
            "time_usec": 1718351623636772,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hutch Drop-Waist Maxi Skirt | Anthropologie",
            "url": "https://www.anthropologie.com/shop/hutch-drop-waist-maxi-skirt?color=084&type=STANDARD&quantity=1",
            "time_usec": 1717502653176169,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "drop waist skirt - Google Search",
            "url": "https://www.google.com/search?q=drop+waist+skirt&oq=drop+waist+skirt&aqs=chrome.0.0i19i512l8j0i19i22i30l2.7318j1j1&sourceid=chrome&ie=UTF-8#vhid=L74u1BMR2o3J9M&vssid=l",
            "time_usec": 1717502646647437,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.urbanoutfitters.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "UO Maxi gonna asimmetrica della prateria Increspata bianca | Urban Outfitters IT",
            "url": "https://www.urbanoutfitters.com/it-it/shop/uo-white-crinkle-asymmetrical-prairie-maxi-skirt2?color=010&size=XS&type=REGULAR&utm_campaign=PMAX&utm_term=IT_PMAX_ALL&utm_content=Cj0KCQjw9vqyBhCKARIsAIIcLMFvRGFCE9RgAc6A91nYZgOusfnYrIyVJ-5ABqEa9vBRud-jx4ldEo8aAt1fEALw_wcB&gad_source=1&_cclid=Google_Cj0KCQjw9vqyBhCKARIsAIIcLMFvRGFCE9RgAc6A91nYZgOusfnYrIyVJ-5ABqEa9vBRud-jx4ldEo8aAt1fEALw_wcB&gclid=Cj0KCQjw9vqyBhCKARIsAIIcLMFvRGFCE9RgAc6A91nYZgOusfnYrIyVJ-5ABqEa9vBRud-jx4ldEo8aAt1fEALw_wcB&quantity=1",
            "time_usec": 1717502620391693,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "drop waist skirt - Google Search",
            "url": "https://www.google.com/search?q=drop+waist+skirt&oq=drop+waist+skirt&aqs=chrome.0.0i19i512l8j0i19i22i30l2.7318j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1717502562563376,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1717502551869763,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "travel from florence to morocco - Google Search",
            "url": "https://www.google.com/search?q=travel+from+florence+to+morocco&sca_esv=1b6c1bc5b84c8566&sxsrf=ADLYWIKyzecfOyItbOnxOAsTp3ThCHyXjw%3A1717502518545&ei=NgJfZq_yIN6ki-gPq5aC2AY&ved=0ahUKEwiv5ZK888GGAxVe0gIHHSuLAGsQ4dUDCBA&uact=5&oq=travel+from+florence+to+morocco&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIh90cmF2ZWwgZnJvbSBmbG9yZW5jZSB0byBtb3JvY2NvMgUQIRigATIFECEYoAEyBRAhGJ8FMgUQIRifBTIFECEYnwVIgDpQmgNY5jhwA3gBkAEAmAHdAaABjRuqAQcxOC4xNC4xuAEDyAEA-AEBmAIkoALdHagCEMICBxAjGCcY6gLCAg0QLhjHARgnGOoCGK8BwgIUEAAYgAQY4wQYtAIY6QQY6gLYAQHCAgoQIxiABBgnGIoFwgIKEAAYgAQYQxiKBcICEBAuGIAEGNEDGEMYxwEYigXCAgQQIxgnwgIFEAAYgATCAgsQLhiABBjRAxjHAcICDhAuGIAEGMcBGI4FGK8BwgITEC4YgAQYQxjHARiKBRiOBRivAcICExAuGIAEGBQYhwIYxwEYjgUYrwHCAgoQLhiABBhDGIoFwgIFEC4YgATCAgcQABiABBgKwgILEC4YgAQYxwEYrwHCAgoQABiABBgUGIcCwgIIEAAYFhgeGA_CAgYQABgWGB7CAgsQABiABBiGAxiKBcICCBAAGBYYChgewgIIEAAYogQYiQXCAgsQABiABBiiBBiLA8ICBxAhGKABGAqYAxO6BgYIARABGAGSBwcxOC4xNy4xoAfFnAI&sclient=gws-wiz-serp",
            "time_usec": 1717502537106322,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "travel from budapest to prague - Google Search",
            "url": "https://www.google.com/search?q=travel+from+budapest+to+prague&oq=travel+from+budapest+to+prague&aqs=chrome..69i64j0i19i512j0i15i19i22i30j0i19i22i30j0i19i22i30i395j0i395i512i546l2j69i57.10934j1j1&sourceid=chrome&ie=UTF-8&zx=1717502511828&no_sw_cr=1",
            "time_usec": 1717502511830312,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1717502498266072,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "porto airport - Google Search",
            "url": "https://www.google.com/search?sca_esv=1b6c1bc5b84c8566&sxsrf=ADLYWIIFD6AG8_2JmAnAj_qoqtoHN6IWGA:1717502488417&q=porto+airport&uds=ADvngMgJJZ3sWYwFKSIsRiA2eMJNmSoJWGme6PcbguX30oezTA7p52KtyH2LB81b4FSnm9uWejaBVZiu5wS-JKdWjefNh6sIIrmf4IXgRqB8I2rWVeM6jiJbI06zcypoKYxmFHy4CDC_pw8T6f9GEAGZZrecmRHDtwKl50JFgh0H69dg1AtSq01fcnDRS0n2RQ7Fj25wIdMoebnKvar68bqnopM0DEpsDOsd1NYgAoobZiC1tnUQen8_YMDTXBRneVvl1uD-Dh-X&udm=2&prmd=invbz&sa=X&ved=2ahUKEwjA6OOt88GGAxVcxAIHHZ5sAA8QtKgLegQIDRAB&biw=1058&bih=701&dpr=1",
            "time_usec": 1717502486651337,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "porto airport - Google Search",
            "url": "https://www.google.com/search?gs_ssp=eJzj4tTP1TewLIg3MzBgtFIxqEgxMjFLMzMxMzRJNEpKTLEyqDA0NUw0NbdINEsxMzC2TDH04i3ILyrJV0jMLAIxACT5EmU&q=porto+airport&oq=porto&aqs=chrome.6.69i64j46i67i433i512i650j0i67i512i650j0i131i433i512j46i67i433i512i650j46i67i512i650j46i67i175i199i512i650j46i131i433i512j0i512j46i131i433i512.7736j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1717502481149946,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1717502471725080,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.notion.so/images/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Lecture notes",
            "url": "https://www.notion.so/Lecture-notes-19cbffba2cf8473a8d00cc4ad94766c3",
            "time_usec": 1717501912598888,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.notion.so/images/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Notion \u2013 The all-in-one workspace for your notes, tasks, wikis, and databases.",
            "url": "https://www.notion.so/",
            "time_usec": 1717501907809990,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1717501832697453,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://it.mytrip.com/gui/mt/image/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Mytrip",
            "url": "https://it.mytrip.com/rf/result?selectionKey=S4277-25Jul24-V%2Caffp6e%2C%3A%3Ag_0%3Ah_0%3Aa_BE%3Ab_5R%3Ac_5R%3Ad_58b6a%3Ae_-5b54%3Af_2%3Ai_1.0.0%3Aj_9E%3Az_dhba4u",
            "time_usec": 1717501685552477,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Mytrip",
            "url": "https://it.mytrip.com/rf/result?selectionKey=S4277-25Jul24-V%2Caffp6e%2C%3A%3Ag_0%3Ah_0%3Aa_BE%3Ab_5R%3Ac_5R%3Ad_58b6a%3Ae_-5b54%3Af_2%3Ai_1.0.0%3Aj_9E%3Az_dhba4u",
            "time_usec": 1717501680359865,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.skyscanner.it/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Cheap flights from Porto to New York at Skyscanner",
            "url": "https://www.skyscanner.it/transport/flights/opo/nyca/240725/config/15055-2407250650--31899-0-12712-2407250950?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=False&outboundaltsenabled=False&preferdirects=False&rtn=0",
            "time_usec": 1717501644650081,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.skyscanner.it/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Cheap flights from Porto to New York at Skyscanner",
            "url": "https://www.skyscanner.it/transport/flights/opo/nyca/240725/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=False&outboundaltsenabled=False&preferdirects=False&rtn=0",
            "time_usec": 1717501627772138,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.skyscanner.it/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Cheap flights from Porto to New York at Skyscanner",
            "url": "https://www.skyscanner.it/transport/flights/opo/nyca/240724/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=False&outboundaltsenabled=False&preferdirects=False&rtn=0",
            "time_usec": 1717501622704348,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.skyscanner.it/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Cheap flights from Porto to New York at Skyscanner",
            "url": "https://www.skyscanner.it/transport/flights/opo/nyca/240723/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=False&outboundaltsenabled=False&preferdirects=False&rtn=0",
            "time_usec": 1717501596918010,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Cheap flights from Porto to New York at Skyscanner",
            "url": "https://www.skyscanner.it/transport/flights/opo/nyca/240724/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=False&outboundaltsenabled=False&preferdirects=False&rtn=0",
            "time_usec": 1717501592931329,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.skyscanner.it/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Cheap flights from Porto to New York at Skyscanner",
            "url": "https://www.skyscanner.it/transport/flights/opo/nyca/240725/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=False&outboundaltsenabled=False&preferdirects=False&rtn=0",
            "time_usec": 1717501572547077,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.skyscanner.it/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Cheap flights from Porto to New York at Skyscanner",
            "url": "https://www.skyscanner.it/transport/flights/opo/nyca/240724/?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=0&preferdirects=False&outboundaltsenabled=False&inboundaltsenabled=False",
            "time_usec": 1717501516265971,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "ponta delgada - Google Search",
            "url": "https://www.google.com/search?sca_esv=1b6c1bc5b84c8566&sxsrf=ADLYWIKxVTa1X56AjTjtF5zr1AQzRKU6EQ:1717501489744&q=ponta+delgada&source=lnms&uds=ADvngMgJJZ3sWYwFKSIsRiA2eMJNJc616UNHKUlqnT7jB4Ucmdyp7-8P0qwuomzpDTPhctjQi5X1wxn1KCmcAvDTKpo1Ac_ObVM2ZsWxhyvmc-xiUtyNSEiiiK2N058iPwICWvPqQhj-4Yn_YrqvafW8JrmhFFPPJ6W5pqT7jUnk1IKIw6Zm5bNzu0KcGvsKDhYdIAFCCrfeeqsTlX_-6R_wZslKWTsGVw0zzF6u_6vhN3FSXgS8Tv6EQGC09liCA2z1bdFdA18q&sa=X&ved=2ahUKEwjv6snR78GGAxUrRUEAHfAUCaQQ0pQJegQIEhAB&biw=1058&bih=701&dpr=1#eim=CAEQBxoRMzguNzIxODQwMzU1Mzg5OTciEi05LjM5OTg2NjMzOTAwMTQ2MQ",
            "time_usec": 1717501501715924,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "ponta delgada - Google Search",
            "url": "https://www.google.com/search?sca_esv=1b6c1bc5b84c8566&sxsrf=ADLYWIKxVTa1X56AjTjtF5zr1AQzRKU6EQ:1717501489744&q=ponta+delgada&source=lnms&uds=ADvngMgJJZ3sWYwFKSIsRiA2eMJNJc616UNHKUlqnT7jB4Ucmdyp7-8P0qwuomzpDTPhctjQi5X1wxn1KCmcAvDTKpo1Ac_ObVM2ZsWxhyvmc-xiUtyNSEiiiK2N058iPwICWvPqQhj-4Yn_YrqvafW8JrmhFFPPJ6W5pqT7jUnk1IKIw6Zm5bNzu0KcGvsKDhYdIAFCCrfeeqsTlX_-6R_wZslKWTsGVw0zzF6u_6vhN3FSXgS8Tv6EQGC09liCA2z1bdFdA18q&sa=X&ved=2ahUKEwjv6snR78GGAxUrRUEAHfAUCaQQ0pQJegQIEhAB&biw=1058&bih=701&dpr=1#eim=CAE",
            "time_usec": 1717501489888890,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "ponta delgada - Google Search",
            "url": "https://www.google.com/search?sca_esv=1b6c1bc5b84c8566&sxsrf=ADLYWIIpr9K_upLifVpMyPZcNEcM61SrAA:1717501486733&q=ponta+delgada&uds=ADvngMgJJZ3sWYwFKSIsRiA2eMJNJc616UNHKUlqnT7jB4UcmWFw_9_o0BQ8me94hwqVT4AsjNZfDN0N2KCOlYyc-EONvJRQRxcOVmHlklSgorkLeBcVUOkKgiICNgOTcMtMXzS-Kwg7pkfsdESwOrZc1ShJ67qFyUXrDO8o5shBPeFBKfiy0qzY_R1hDpcWivkI3XDhHSlYf4sOlaUvUBxT6bK5MwGXuBfwgdSPToUsWIO6UQjNk7lDiRtTXRc3IpnzNgR_xQXJ&udm=2&prmd=invbz&sa=X&ved=2ahUKEwi99ZHQ78GGAxWcW0EAHYcFESQQtKgLegQICxAB&biw=1058&bih=701&dpr=1",
            "time_usec": 1717501483464800,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "ponta delgada - Google Search",
            "url": "https://www.google.com/search?gs_ssp=eJzj4tTP1TcwKshINjRg9OItyM8rSVRISc1JT0xJBABmqgg5&q=ponta+delgada&oq=ponta&aqs=chrome.2.69i64j46i131i433i512j46i67i433i512i650j0i512l2j46i512j0i512j46i175i199i512j46i67i512i650.8107j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1717501480346456,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1717501470246260,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.skyscanner.it/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Cheap flights from Ponta Delgada to New York at Skyscanner",
            "url": "https://www.skyscanner.it/transport/flights/pont/nyca/240724/?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=0&preferdirects=true&outboundaltsenabled=False&inboundaltsenabled=False",
            "time_usec": 1717501429957755,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.skyscanner.it/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Skyscanner | Find the cheapest flights fast: save time, save money!",
            "url": "https://www.skyscanner.it/transport/flights/pt/nyca/240724/?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=0&preferdirects=False&outboundaltsenabled=False&inboundaltsenabled=False",
            "time_usec": 1717501420129527,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.skyscanner.it/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Skyscanner | Find the cheapest flights fast: save time, save money!",
            "url": "https://www.skyscanner.it/transport/flights/pt/us/240724/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&inboundaltsenabled=False&infants=0&originentityid=29475349&outboundaltsenabled=False&preferdirects=False&ref=home&rtn=0",
            "time_usec": 1717501403738262,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.skyscanner.it/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Cheap Flights to United States | Skyscanner",
            "url": "https://www.skyscanner.it/voli-per/us/voli-economici-per-stati-uniti.html?utm_source=google&utm_medium=cpc&utm_campaign=IT-Flights-Search-EN-Destination-International-North+America&utm_term=flights+to+United+States&associateID=SEM_FLI_19465_00000&campaign_id=20441767106&adgroupid=152991718555&keyword_id=kwd-23486101&gad_source=1&gclid=Cj0KCQjw9vqyBhCKARIsAIIcLMHGGCqHsgXK7-SjmKj3VWfoBdgy7QIF3H0RZ5Q90ulA0fKCiV8HYFkaAkF3EALw_wcB&gclsrc=aw.ds",
            "time_usec": 1717501368430541,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "cheapest flight from western europe to the united states july 25 - Google Search",
            "url": "https://www.google.com/search?q=cheapest+flight+from+western+europe+to+the+united+states+july+25&oq=cheapest+flight+from+western+europe+to+the+united+states+july+25+&aqs=chrome..69i64j69i57.18181j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1717501365639258,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://www.cheapflights.com/flights-to-europe/usa/aid=151062112072&tid=kwd-266189973&locp=1008311&loci=9004509&mt=p&n=g&d=c&cid=663305156047&pos=?gad_source=1&gclid=Cj0KCQjw9vqyBhCKARIsAIIcLMGonpqor6xRjmqUPrMN465oO3NmA6bROllKd_Xxen5IYxXX7xfzhp8aAiN_EALw_wcB",
            "time_usec": 1717501363737594,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1717501335615411,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.buzzfeed.com/static-assets/_next/static/images/favicon-496b7cee633e6a7dca162654e1bb39c9.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Can I Guess Your Zodiac Element? Music Quiz",
            "url": "https://www.buzzfeed.com/lady_emerald/songs-decade-zodiac-can-we-guess-quiz",
            "time_usec": 1717501174174475,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.buzzfeed.com/static-assets/bf-quiz-feed-ui/_next/static/images/favicon-496b7cee633e6a7dca162654e1bb39c9.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "BuzzFeed Quizzes",
            "url": "https://www.buzzfeed.com/quizzes",
            "time_usec": 1717501126568415,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "buzzfeed quizes - Google Search",
            "url": "https://www.google.com/search?q=buzzfeed+quizes&oq=buzzfeed+quizes&aqs=chrome..69i64j0i10i512j0i10i22i30l8.8130j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1717501071376521,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1717501061411952,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "botega veneta - Google Search",
            "url": "https://www.google.com/search?q=botega+veneta&oq=botega+veneta&aqs=chrome..69i64j46i10i199i433i465i512j0i10i433i512j46i10i175i199i512i654j0i10i512l4j0i3i10.6073j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1717072833008576,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1717072823755118,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weather in florence italy today - Google Search",
            "url": "https://www.google.com/search?q=weather+in+florence+italy+today&sca_esv=4fabb05b4b801908&biw=1058&bih=701&sxsrf=ADLYWIL6oVGGXFWhDGT0WdOL5UeKiwScHg%3A1717072050538&ei=snBYZra5IK6Gxc8P-t2KiAY&ved=0ahUKEwi22oDtr7WGAxUuQ_EDHfquAmEQ4dUDCBA&uact=5&oq=weather+in+florence+italy+today&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIh93ZWF0aGVyIGluIGZsb3JlbmNlIGl0YWx5IHRvZGF5MgoQABiABBhGGIACMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTIIEAAYgAQYogQyCBAAGIAEGKIEMggQABiABBiiBDIIEAAYgAQYogQyFhAAGIAEGEYYgAIYlwUYjAUY3QTYAQJI9DdQ0QFYhzZwCXgBkAEBmAG3AqABsiGqAQkxNi4yMi4wLjG4AQPIAQD4AQGYAi-gAuMiqAIUwgIHECMYJxjqAsICExAAGIAEGEMYtAIYigUY6gLYAQHCAgUQABiABMICCxAuGIAEGNEDGMcBwgIEECMYJ8ICChAjGIAEGCcYigXCAgoQABiABBhDGIoFwgIQEC4YgAQYQxjHARiKBRivAcICDRAjGIAEGCcYigUYnQLCAg0QABiABBhDGMkDGIoFwgIIEAAYgAQYkgPCAgsQABiABBiSAxiKBcICEhAjGIAEGCcYigUYnQIYRhiAAsICHBAAGIAEGIoFGJ0CGEYYgAIYlwUYjAUY3QTYAQLCAhAQLhiABBjRAxhDGMcBGIoFwgIHEAAYgAQYCsICCRAAGIAEGAoYDcICBxAAGIAEGA3CAggQABgKGA0YHsICCBAAGA0YHhgPwgIKEAAYCBgNGB4YD8ICCxAAGIAEGKIEGIsDwgIGEAAYFhgemAMTugYGCAEQARgBugYGCAIQARgTkgcFMTguMjmgB5O8Ag&sclient=gws-wiz-serp",
            "time_usec": 1717072640429875,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://prm.com/it/p/salomon-scarpe-xt-6-colore-marrone-l47445100-39204?ref=Channable&gad_source=1&gclid=CjwKCAjwx-CyBhAqEiwAeOcTdUagqgDRfY-j_CljI6BckeV41X5vpTWpNC4VbCFmROENBg1UJ0mtBhoCfW0QAvD_BwE",
            "time_usec": 1717072205005179,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "meyerds briggs test free - Google Search",
            "url": "https://www.google.com/search?q=meyerds+briggs+test+free&sca_esv=cd3ec118dfb68f5c&sxsrf=ADLYWIIW3X_YwULzdpIP6jwuAaSpKm5Gyg%3A1717070106698&ei=GmlYZraNKpiM9u8PxYyDyAM&ved=0ahUKEwi2go7OqLWGAxUYhv0HHUXGADkQ4dUDCBA&uact=5&oq=meyerds+briggs+test+free&gs_lp=Egxnd3Mtd2l6LXNlcnAiGG1leWVyZHMgYnJpZ2dzIHRlc3QgZnJlZTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIIEAAYBRgNGB4yCBAAGAUYDRgeSI4IUIkDWMMHcAF4AJABAJgBcaABiwSqAQMyLjO4AQPIAQD4AQGYAgWgAt4DwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigWYAwDiAwUSATEgQIgGAZAGCpIHAzEuNKAHzis&sclient=gws-wiz-serp",
            "time_usec": 1717072132992383,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MEXICO 66 SLIP-ON | Onitsuka Tiger IT",
            "url": "https://www.onitsukatiger.com/it/it-it/mexico-66-slip-on/p/1183b782-001.html?channable=01662a6964003131383331f3&gad_source=1&gclid=CjwKCAjwx-CyBhAqEiwAeOcTdbUWdZibOjk1aLdUu9E1juizCm4XVf7QEyg_FLvj4_XRCJgexcF-xhoCnAAQAvD_BwE&gclsrc=aw.ds#1183B782.001",
            "time_usec": 1717072129904638,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "salomon shoes - Google Search",
            "url": "https://www.google.com/search?q=salomon+shoes+&sca_esv=4fabb05b4b801908&biw=1058&bih=701&sxsrf=ADLYWILM0AL-XgQ_N9_9IfW7-o9L7-NZKw%3A1717071904406&ei=IHBYZtutGPmpxc8PxauAsAo&ved=0ahUKEwjbvamnr7WGAxX5VPEDHcUVAKYQ4dUDCBA&uact=5&oq=salomon+shoes+&gs_lp=Egxnd3Mtd2l6LXNlcnAiDnNhbG9tb24gc2hvZXMgMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEjGJFCaCVjLI3ACeAGQAQCYAaYBoAHWDaoBBDQuMTG4AQPIAQD4AQGYAhGgAowPqAIRwgIHECMYJxjqAsICExAAGIAEGEMYtAIYigUY6gLYAQHCAhQQABiABBjjBBi0AhjpBBjqAtgBAcICChAjGIAEGCcYigXCAgQQIxgnwgILEC4YgAQYkQIYigXCAgsQABiABBiRAhiKBcICEBAuGIAEGNEDGEMYxwEYigXCAgoQABiABBhDGIoFwgILEC4YgAQY0QMYxwHCAgoQLhiABBhDGIoFwgIKEC4YgAQYFBiHAsICBRAuGIAEwgIIEC4YgAQY1ALCAhkQLhiABBhDGIoFGJcFGNwEGN4EGN8E2AECwgINEAAYgAQYQxjJAxiKBcICCxAAGIAEGJIDGIoFwgIOEC4YgAQYxwEYjgUYrwHCAgoQABiABBgUGIcCmAMUugYGCAEQARgBugYGCAIQARgUkgcENi4xMaAHkZkB&sclient=gws-wiz-serp",
            "time_usec": 1717072052902516,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "lip gloss phone case - Google Search",
            "url": "https://www.google.com/search?q=lip+gloss+phone+case&sca_esv=4fabb05b4b801908&biw=1058&bih=701&sxsrf=ADLYWII14vpzDl80qo9_WXoZ-pKVyEtz-A%3A1717070669386&ei=TWtYZo6WF7CL9u8P0P-pmA8&ved=0ahUKEwjO8LXaqrWGAxWwhf0HHdB_CvMQ4dUDCBA&uact=5&oq=lip+gloss+phone+case&gs_lp=Egxnd3Mtd2l6LXNlcnAiFGxpcCBnbG9zcyBwaG9uZSBjYXNlMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBUiQLlDDC1isLXABeAGQAQCYAZ8BoAHpEKoBBDkuMTG4AQPIAQD4AQGYAhWgAqkSqAIPwgIHECMYJxjqAsICHBAuGIAEGNEDGEMYtAIYxwEYyAMYigUY6gLYAQHCAhYQLhiABBhDGLQCGMgDGIoFGOoC2AEBwgIKECMYgAQYJxiKBcICCxAuGIAEGJECGIoFwgIKEC4YgAQYQxiKBcICDhAuGIAEGMcBGI4FGK8BwgIKEAAYgAQYQxiKBcICCxAAGIAEGJECGIoFwgIFEC4YgATCAhoQLhiABBiRAhiKBRiXBRjcBBjeBBjgBNgBApgDFLoGBggBEAEYCLoGBggCEAEYFJIHBDYuMTWgB4eHAQ&sclient=gws-wiz-serp",
            "time_usec": 1717071906588333,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "tiger sneakers - Google Search",
            "url": "https://www.google.com/search?q=tiger+sneakers&sca_esv=cd3ec118dfb68f5c&sxsrf=ADLYWIJqEof9OtWSc19FMGXlhOSt2HvD1Q%3A1717070124037&ei=LGlYZqnvAcbY7_UPifC74AM&ved=0ahUKEwiptbDWqLWGAxVG7LsIHQn4DjwQ4dUDCBA&uact=5&oq=tiger+sneakers&gs_lp=Egxnd3Mtd2l6LXNlcnAiDnRpZ2VyIHNuZWFrZXJzMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCSJsTUPYEWLgScAF4AZABAJgBAKABAKoBALgBA8gBAPgBAZgCAaACDqgCCpgDDuIDBRIBMSBAkgcBMaAHAA&sclient=gws-wiz-serp",
            "time_usec": 1717071812151994,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Collezione Completa Calzature e Sneakers da Donna | Onitsuka Tiger",
            "url": "https://www.onitsukatiger.com/it/it-it/donna/scarpe/tutte-le-scarpe/?gad_source=1&gclid=CjwKCAjwx-CyBhAqEiwAeOcTdTHwhsnpRZEQ8z3nS-BzIHgz_yxkIqMiemD6QXF_IJEiWjdckbPWZxoCdH0QAvD_BwE&gclsrc=aw.ds",
            "time_usec": 1717071810004485,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MEXICO 66 | Onitsuka Tiger IT",
            "url": "https://www.onitsukatiger.com/it/it-it/mexico-66/p/1183b566-021.html?channable=01662a69640031363630313962&gad_source=1&gclsrc=aw.ds#1183B566.021",
            "time_usec": 1717071798092520,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MEXICO 66 | Onitsuka Tiger IT",
            "url": "https://www.onitsukatiger.com/it/it-it/mexico-66/p/1183b566-021.html?channable=01662a69640031363630313962&gad_source=1&gclsrc=aw.ds#1183B566.021",
            "time_usec": 1717071788596190,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MEXICO 66 | Onitsuka Tiger IT",
            "url": "https://www.onitsukatiger.com/it/it-it/mexico-66/p/1183b566-021.html?channable=01662a69640031363630313962&gad_source=1&gclsrc=aw.ds#1183B566.021",
            "time_usec": 1717071764907820,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "tiger sneakers - Google Search",
            "url": "https://www.google.com/search?q=tiger+sneakers&sca_esv=cd3ec118dfb68f5c&sxsrf=ADLYWIJqEof9OtWSc19FMGXlhOSt2HvD1Q%3A1717070124037&ei=LGlYZqnvAcbY7_UPifC74AM&ved=0ahUKEwiptbDWqLWGAxVG7LsIHQn4DjwQ4dUDCBA&uact=5&oq=tiger+sneakers&gs_lp=Egxnd3Mtd2l6LXNlcnAiDnRpZ2VyIHNuZWFrZXJzMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCMgcQIxgnGOoCSJsTUPYEWLgScAF4AZABAJgBAKABAKoBALgBA8gBAPgBAZgCAaACDqgCCpgDDuIDBRIBMSBAkgcBMaAHAA&sclient=gws-wiz-serp",
            "time_usec": 1717071742107768,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Booking.com: Hotels in Elba. Book your hotel now!",
            "url": "https://www.booking.com/searchresults.html?ss=Elba%2C+Italy&ssne=Palmanova&ssne_untouched=Palmanova&label=gog235jc-1DCBkoggI46AdIM1gDaHGIAQGYATG4AQfIAQzYAQPoAQH4AQOIAgGoAgO4AoXX4bIGwAIB0gIkZWI1ODhmZWMtM2JiNS00Y2FiLWIxYTItNWY0OTgwOGU4NjI22AIE4AIB&sid=143ad315046fab268076e86c4894838a&aid=356980&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=1433&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=f902550d65630080&ac_meta=GhA3ZTI3NTUxMjNkYjAwMzRhIAAoATICZW46BGVsYmFAAEoAUAA%3D&checkin=2024-06-01&checkout=2024-06-03&group_adults=4&no_rooms=1&group_children=0#map_opened",
            "time_usec": 1717070776058665,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Booking.com: Hotels in Elba. Book your hotel now!",
            "url": "https://www.booking.com/searchresults.html?ss=Elba%2C+Italy&ssne=Palmanova&ssne_untouched=Palmanova&label=gog235jc-1DCBkoggI46AdIM1gDaHGIAQGYATG4AQfIAQzYAQPoAQH4AQOIAgGoAgO4AoXX4bIGwAIB0gIkZWI1ODhmZWMtM2JiNS00Y2FiLWIxYTItNWY0OTgwOGU4NjI22AIE4AIB&sid=143ad315046fab268076e86c4894838a&aid=356980&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=1433&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=f902550d65630080&ac_meta=GhA3ZTI3NTUxMjNkYjAwMzRhIAAoATICZW46BGVsYmFAAEoAUAA%3D&checkin=2024-06-01&checkout=2024-06-03&group_adults=4&no_rooms=1&group_children=0",
            "time_usec": 1717070770316897,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Booking.com: Hotels in Palmanova. Book your hotel now!",
            "url": "https://www.booking.com/searchresults.html?aid=356980&label=gog235jc-1DCBkoggI46AdIM1gDaHGIAQGYATG4AQfIAQzYAQPoAQH4AQOIAgGoAgO4AoXX4bIGwAIB0gIkZWI1ODhmZWMtM2JiNS00Y2FiLWIxYTItNWY0OTgwOGU4NjI22AIE4AIB&sid=143ad315046fab268076e86c4894838a&sb=1&src=error404&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Ferror404.html%3Faid%3D356980%26label%3Dgog235jc-1DCBkoggI46AdIM1gDaHGIAQGYATG4AQfIAQzYAQPoAQH4AQOIAgGoAgO4AoXX4bIGwAIB0gIkZWI1ODhmZWMtM2JiNS00Y2FiLWIxYTItNWY0OTgwOGU4NjI22AIE4AIB%26sid%3D143ad315046fab268076e86c4894838a%26&ss=Elba+Sunset+Mallorca+Thalasso+Spa%2C+Palmanova%2C+Balearic+Islands%2C+Spain&is_ski_area=0&checkin_year=2024&checkin_month=6&checkin_monthday=1&checkout_year=2024&checkout_month=6&checkout_monthday=3&group_adults=4&group_children=0&b_h4u_keep_filters=&from_sf=1&ss_raw=elba+island&ac_position=0&ac_langcode=en&ac_click_type=b&ac_meta=GhA1MTJhNTUwMmVlMzUwMzYyIAAoATICZW46C2VsYmEgaXNsYW5kQABKAFAA&dest_id=4040481&dest_type=hotel&place_id_lat=39.51024&place_id_lon=2.544622&search_pageview_id=512a5502ee350362&search_selected=true",
            "time_usec": 1717070746555128,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Booking.com Online Hotel Reservations",
            "url": "https://www.booking.com/city/it/cavo.html-cwXMtrVjixWl_6IOj4YiWgS491871584044:pl:ta:p1:p2:ac:ap:neg:fi:tiaud-297601666035:kwd-339121505754:lp1008311:li:dec:dm;ws=?gclid=CjwKCAjwx-CyBhAqEiwAeOcTdcGbA41LGyj0G6V_vBXsUAI0TOFiS88ZVENXUJ42A_PbmWQBRiD6TRoCducQAvD_BwE",
            "time_usec": 1717070725634966,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hostels in elba island cavo - Google Search",
            "url": "https://www.google.com/search?q=hostels+in+elba+island+cavo&sca_esv=cd3ec118dfb68f5c&sxsrf=ADLYWIJDpWOo7SOBl_5ed368pjJFtNZUeg%3A1717070648356&ei=OGtYZuCOFbWN9u8Piam6eA&ved=0ahUKEwjgirLQqrWGAxW1hv0HHYmUDg8Q4dUDCBA&uact=5&oq=hostels+in+elba+island+cavo&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIhtob3N0ZWxzIGluIGVsYmEgaXNsYW5kIGNhdm8yBRAhGKABMgUQIRigAUj7ClDbA1jVCHABeACQAQCYAaUBoAHkBKoBAzAuNbgBA8gBAPgBAZgCBqACkwXCAg4QABiABBiwAxiGAxiKBcICERAAGIAEGLADGIYDGIoFGIsDwgIFECEYnwXCAgcQIRigARgKmAMAiAYBkAYCkgcDMS41oAfYFA&sclient=gws-wiz-serp",
            "time_usec": 1717070722635615,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "map of elba - Google Search",
            "url": "https://www.google.com/search?sca_esv=4fabb05b4b801908&sxsrf=ADLYWIKB0_ami1HnTm-8QdIOFsE4eRU4bA:1717070665776&q=map+of+elba&source=lnms&uds=ADvngMgeeERJXFVkoA-kHoELer72KqjqgNHf-g6tjrmRJslsbhCmgMcHULvhFln5R3K7h6G0IlhDKFTv3a7NJFydu08jLWwNxqrNmQhDsfb7iLHfr1dTiPIbu1akutKQpIvsuiUBKgt4__uwkYTqOvt73KMiTmcDERjF6yQp0Mc2z4doHErcR8iHzdWdPJEIKgT6pemFIrHv1WSabGfrV0U1t9WfNhuUhyr2LHB_OZWv5-4Xy9O5-VJgcBYJPmi1Ic7iUWm1xM9bJWN6F_ThYlLp1miOdTFSxg&sa=X&ved=2ahUKEwi6utnYqrWGAxVUgf0HHdMuCQcQ0pQJegQIDBAB&biw=1058&bih=701&dpr=1#smwie=1",
            "time_usec": 1717070675196590,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "map of elba - Google Search",
            "url": "https://www.google.com/search?sca_esv=4fabb05b4b801908&sxsrf=ADLYWIKB0_ami1HnTm-8QdIOFsE4eRU4bA:1717070665776&q=map+of+elba&source=lnms&uds=ADvngMgeeERJXFVkoA-kHoELer72KqjqgNHf-g6tjrmRJslsbhCmgMcHULvhFln5R3K7h6G0IlhDKFTv3a7NJFydu08jLWwNxqrNmQhDsfb7iLHfr1dTiPIbu1akutKQpIvsuiUBKgt4__uwkYTqOvt73KMiTmcDERjF6yQp0Mc2z4doHErcR8iHzdWdPJEIKgT6pemFIrHv1WSabGfrV0U1t9WfNhuUhyr2LHB_OZWv5-4Xy9O5-VJgcBYJPmi1Ic7iUWm1xM9bJWN6F_ThYlLp1miOdTFSxg&sa=X&ved=2ahUKEwi6utnYqrWGAxVUgf0HHdMuCQcQ0pQJegQIDBAB&biw=1058&bih=701&dpr=1",
            "time_usec": 1717070670009866,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "map of elba - Google Search",
            "url": "https://www.google.com/search?sca_esv=4fabb05b4b801908&sxsrf=ADLYWIJFI_bEdSXW4Q0Dy-fq13GkqcFnMA:1717070660472&q=map+of+elba&uds=ADvngMgeeERJXFVkoA-kHoELer722-gqjeu7RjZbL877RJUt2poo0I9xSsTY9QwI3wZYNMOpN0dl8_50oy0U0hkCrJsUqeq239nztTnc4gS0M8FLqiPp1a8ZJe8JGt6E6phqrFmd5M_GAIgmFQd2-oGRGwtAlen6c7csWsA02MUj9p-2A0FHKCYdFBEKaPZOQyzW0yXVYZhfe8bUkFY2MX1g2RpODtElk0yfQkTfaEaoJa0yklJzHikgivEMicOqTMPcbBbwO8zay0w5k3lMcmfiusAvkvbY0g&udm=2&prmd=ivnbz&sa=X&ved=2ahUKEwip75TWqrWGAxXuhv0HHQ4JA-wQtKgLegQIERAB&biw=1058&bih=701&dpr=1",
            "time_usec": 1717070667117548,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "map of elba - Google Search",
            "url": "https://www.google.com/search?q=map+of+elba&oq=map+of+elba+&aqs=chrome..69i64j0i19i512l7j0i19i22i30l2.8837j0j1&sourceid=chrome&ie=UTF-8#vhid=vKRV5G9BQoDFgM&vssid=l",
            "time_usec": 1717070663106680,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "map of elba - Google Search",
            "url": "https://www.google.com/search?q=map+of+elba&oq=map+of+elba+&aqs=chrome..69i64j0i19i512l7j0i19i22i30l2.8837j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1717070661319213,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1717070650948645,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hostels in elba island - Google Search",
            "url": "https://www.google.com/search?q=hostels+in+elba+island&oq=hostels+in+elba+island+&aqs=chrome..69i64j69i57.9663j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1717070649601825,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1717070638233680,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "meyerds briggs test free - Google Search",
            "url": "https://www.google.com/search?q=meyerds+briggs+test+free&sca_esv=cd3ec118dfb68f5c&sxsrf=ADLYWIIW3X_YwULzdpIP6jwuAaSpKm5Gyg%3A1717070106698&ei=GmlYZraNKpiM9u8PxYyDyAM&ved=0ahUKEwi2go7OqLWGAxUYhv0HHUXGADkQ4dUDCBA&uact=5&oq=meyerds+briggs+test+free&gs_lp=Egxnd3Mtd2l6LXNlcnAiGG1leWVyZHMgYnJpZ2dzIHRlc3QgZnJlZTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIIEAAYBRgNGB4yCBAAGAUYDRgeSI4IUIkDWMMHcAF4AJABAJgBcaABiwSqAQMyLjO4AQPIAQD4AQGYAgWgAt4DwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigWYAwDiAwUSATEgQIgGAZAGCpIHAzEuNKAHzis&sclient=gws-wiz-serp",
            "time_usec": 1717070124665258,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "meyerds briggs test - Google Search",
            "url": "https://www.google.com/search?q=meyerds+briggs+test&sca_esv=cd3ec118dfb68f5c&sxsrf=ADLYWIKsy3pkruLEgWMNqVFFdUDK3fwIZQ%3A1717069766219&ei=xmdYZseHDdb_i-gPkJKcsAI&ved=0ahUKEwjHguGrp7WGAxXW_wIHHRAJByYQ4dUDCBA&uact=5&oq=meyerds+briggs+test&gs_lp=Egxnd3Mtd2l6LXNlcnAiE21leWVyZHMgYnJpZ2dzIHRlc3QyBxAjGLACGCcyBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA1I7TJQoANY7TBwBngBkAEBmAG5AaAB6xaqAQQxLjIzuAEDyAEA-AEBmAIdoALIF6gCFMICBxAjGCcY6gLCAhMQABiABBhDGLQCGIoFGOoC2AEBwgIUEAAYgAQY4wQYtAIY6QQY6gLYAQHCAgoQIxiABBgnGIoFwgIEECMYJ8ICChAAGIAEGEMYigXCAgUQABiABMICCxAuGIAEGNEDGMcBwgIFEC4YgATCAgsQLhiABBjHARivAcICBxAAGIAEGArCAgcQIxixAhgnwgINEC4YgAQY0QMYxwEYCsICDhAuGIAEGMcBGI4FGK8BwgIMEAAYgAQYQxiKBRgKwgIKEAAYgAQYyQMYCsICCxAAGIAEGJIDGIoFwgIKEAAYgAQYyQMYDZgDF7oGBggBEAEYAZIHBDYuMjOgB4bpAQ&sclient=gws-wiz-serp",
            "time_usec": 1717070117290851,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://www.16personalities.com/free-personality-test",
            "time_usec": 1717070115182150,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "infp - Google Search",
            "url": "https://www.google.com/search?q=infp&oq=infp&aqs=chrome..69i64j0i67i512i650l6j0i20i263i512j0i67i512i650j0i512.3179j0j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1717069767082087,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.themyersbriggs.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MBTI | The Myers-Briggs Company",
            "url": "https://www.themyersbriggs.com/en-US/Products-and-Services/Myers-Briggs",
            "time_usec": 1717069754192528,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "meyers briggs test - Google Search",
            "url": "https://www.google.com/search?q=meyers+briggs+test&oq=meyers+briggs+test&aqs=chrome..69i64j0i10i433i512j0i10i512l4j0i22i30j0i10i22i30l3.25237j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1717069744464655,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1717069743203693,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://psality.com/wp-content/uploads/2023/05/cropped-Logotype_Favicon-32x32.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Homepage - PSALITY",
            "url": "https://psality.com/?gad_source=1&gclid=CjwKCAjwx-CyBhAqEiwAeOcTddZooT4-aOeV4f13ekkxL33P9-h4QLG3n1ioKwAN-tVZeCO3UO1eHxoCAtAQAvD_BwE",
            "time_usec": 1717069742940877,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.notion.so/images/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Lecture notes",
            "url": "https://www.notion.so/Lecture-notes-19cbffba2cf8473a8d00cc4ad94766c3",
            "time_usec": 1717069652456008,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.notion.so/images/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Notion \u2013 The all-in-one workspace for your notes, tasks, wikis, and databases.",
            "url": "https://www.notion.so/",
            "time_usec": 1717069641806166,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1717069638392549,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://psality.com/wp-content/uploads/2023/05/cropped-Logotype_Favicon-32x32.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Big 5 Test - PSALITY",
            "url": "https://psality.com/test-en/",
            "time_usec": 1717069033974424,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://psality.com/wp-content/uploads/2023/05/cropped-Logotype_Favicon-32x32.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Homepage - PSALITY",
            "url": "https://psality.com/?gad_source=1&gclid=CjwKCAjwx-CyBhAqEiwAeOcTddZooT4-aOeV4f13ekkxL33P9-h4QLG3n1ioKwAN-tVZeCO3UO1eHxoCAtAQAvD_BwE",
            "time_usec": 1717069031775894,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "meyers briggs test - Google Search",
            "url": "https://www.google.com/search?q=meyers+briggs+test&oq=meyers+briggs+test&aqs=chrome..69i64j0i10i433i512j0i10i512l4j0i22i30j0i10i22i30l3.25237j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1717069023958588,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://www.16personalities.com/free-personality-test",
            "time_usec": 1717068981073376,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "meyers briggs test - Google Search",
            "url": "https://www.google.com/search?q=meyers+briggs+test&oq=meyers+briggs+test&aqs=chrome..69i64j0i10i433i512j0i10i512l4j0i22i30j0i10i22i30l3.25237j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1717068975364733,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1717068928864479,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe apps available for download",
            "url": "https://helpx.adobe.com/download-install/kb/download-availability.html?clickref=1100lyxovjAn&mv=affiliate&mv2=pz&as_camptype=&as_channel=affiliate&as_source=partnerize&as_campaign=prodesigntools",
            "time_usec": 1716979428529100,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://prodesigntools.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe CC 2015 Direct Download Links: Creative Cloud 2015 Release | ProDesignTools",
            "url": "https://prodesigntools.com/adobe-cc-2015-direct-download-links.html",
            "time_usec": 1716979419142072,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe apps available for download",
            "url": "https://helpx.adobe.com/download-install/kb/download-availability.html?clickref=1011lyBqMLYR&mv=affiliate&mv2=pz&as_camptype=&as_channel=affiliate&as_source=partnerize&as_campaign=prodesigntools",
            "time_usec": 1716979387467451,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://prodesigntools.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe CC 2015 Direct Download Links: Creative Cloud 2015 Release | ProDesignTools",
            "url": "https://prodesigntools.com/adobe-cc-2015-direct-download-links.html",
            "time_usec": 1716979349632335,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://prodesigntools.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "All Adobe CC 2015 Updates: The Direct Download Links for Mac OS | ProDesignTools",
            "url": "https://prodesigntools.com/adobe-cc-2015-updates-links-mac.html",
            "time_usec": 1716979335622892,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://prodesigntools.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Get Adobe Stock for Free + Download 1,000,000 High-Quality Assets | ProDesignTools",
            "url": "https://prodesigntools.com/free-adobe-stock-images.html",
            "time_usec": 1716979328307994,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://prodesigntools.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "All Adobe CC 2015 Updates: The Direct Download Links for Mac OS | ProDesignTools",
            "url": "https://prodesigntools.com/adobe-cc-2015-updates-links-mac.html",
            "time_usec": 1716979316122359,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://prodesigntools.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Search Results for 'photoshop 2015' at ProDesignTools",
            "url": "https://prodesigntools.com/?s=photoshop+2015#gsc.tab=0&gsc.q=photoshop%202015&gsc.page=1",
            "time_usec": 1716979299267644,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://prodesigntools.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "ProDesignTools: Helping Adobe® Users Since 2009",
            "url": "https://prodesigntools.com/",
            "time_usec": 1716979288243438,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "prodesign tools - Google Search",
            "url": "https://www.google.com/search?q=prodesign+tools&oq=prodesign+tools+&aqs=chrome..69i64j0i10i512j0i10i22i30j0i10i15i22i30j0i22i30l4j0i15i22i30j0i22i30.6474j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716979284002871,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716979276672931,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how to get an older version of photoshop from the creative cloud app - Google Search",
            "url": "https://www.google.com/search?q=how+to+get+an+older+version+of+photoshop+from+the+creative+cloud+app&oq=how+to+get+an+older+version+of+photoshop+from+the+creative+cloud+app+&aqs=chrome..69i64j69i57.15507j1j4&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:484a0d04,vid:UpsTroy64JM,st:24",
            "time_usec": 1716979190266292,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/creativecloud/img/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Official Adobe Photoshop - Leading AI photo & design software",
            "url": "https://www.adobe.com/products/photoshop.html#access_token=eyJhbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LWF0LTEuY2VyIiwia2lkIjoiaW1zX25hMS1rZXktYXQtMSIsIml0dCI6ImF0In0.eyJpZCI6IjE3MTY5NzkwOTY5NTNfNGU1YTgzNWUtNWYxYS00NWMxLTk0NGYtOWYwMTg3Yzc2ZDBjX3ZhNmMyIiwidHlwZSI6ImFjY2Vzc190b2tlbiIsImNsaWVudF9pZCI6IkNyZWF0aXZlQ2xvdWREb3dubG9hZFdvcmtmbG93V2ViMSIsInVzZXJfaWQiOiJBQzVENTY0ODVFQjcyMUNDMEE0OTVFQjFAQWRvYmVJRCIsImFzIjoiaW1zLW5hMSIsImFhX2lkIjoiQUM1RDU2NDg1RUI3MjFDQzBBNDk1RUIxQEFkb2JlSUQiLCJjdHAiOjAsImZnIjoiWVBTVlVaUVlWUFA1TUhVS0ZNUVZZSEFBQ0E9PT09PT0iLCJzaWQiOiIxNzE2OTc3OTMwMTYyXzk1ZDc5MmJlLTliMzYtNGNmYi05NDAzLTM2YTAxMDU4OWM0Y192YTZjMiIsIm1vaSI6ImE3MjRhMzliIiwiZXhwaXJlc19pbiI6Ijg2NDAwMDAwIiwiY3JlYXRlZF9hdCI6IjE3MTY5NzkwOTY5NTMiLCJzY29wZSI6Im9wZW5pZCxjcmVhdGl2ZV9jbG91ZCxyZWFkX29yZ2FuaXphdGlvbnMsYWRkaXRpb25hbF9pbmZvLnNjcmVlbl9uYW1lLGFkZGl0aW9uYWxfaW5mby5zZWNvbmRhcnlfZW1haWwifQ.ZzFATIQPG2-m3Iyi2doZFue4tq7fuSwloitXcuZ6_xG3A7g5Ztv3cRzngdqMPeqV169fM6JeNXkGVM3Ci3GSZ2brheQmjd03y3xh3UccKGhPfDwUi28qAJJxY20wNVbpAQHYDgxfpJgw17aiBk6T1fibfCT6FKoSZrTS1SwYsAl3sOFDGU5xZ6qGq5wXUxolX3lPo4sXIjxqxpzUrY7tu668g-2_biDxX9uKop26YyuGcA8F-UcbKsEX-E3FIHMMdOBDgN5hEsWZil0Ai9q5v-wzolw22034sN_rNWb4ZuxvvfU9pB6HGJze15BNU-raCHZqgsCGWkdYBCjoE5_eHw&token_type=bearer&expires_in=86399996",
            "time_usec": 1716979096732900,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how to get an older version of photoshop from the creative cloud app - Google Search",
            "url": "https://www.google.com/search?q=how+to+get+an+older+version+of+photoshop+from+the+creative+cloud+app&oq=how+to+get+an+older+version+of+photoshop+from+the+creative+cloud+app+&aqs=chrome..69i64j69i57.15507j1j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716979085216569,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://creativecloud.adobe.com/cc_favicon_48.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Creative Cloud | Adobe Creative Cloud",
            "url": "https://creativecloud.adobe.com/campaign/creative-cloud?workflow=route-to-path&route-path=/apps/beta-apps&id=psaprilbetarelease&source=acom",
            "time_usec": 1716979008921832,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/creativecloud/img/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Official Adobe Photoshop - Leading AI photo & design software",
            "url": "https://www.adobe.com/products/photoshop.html",
            "time_usec": 1716978978843618,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cdn.apponic.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Download Adobe Photoshop CC for Mac",
            "url": "https://adobe-photoshop-cc.apponic.com/mac/download/",
            "time_usec": 1716978975338219,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cdn.apponic.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Download Adobe Photoshop CC for Mac",
            "url": "https://adobe-photoshop-cc.apponic.com/mac/download/",
            "time_usec": 1716978955515244,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.nchsoftware.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Download Animation Software Free. Start Animating Videos Today on Windows or Mac.",
            "url": "https://www.nchsoftware.com/animation/index.html?kw=adobe%20flash%20animation&m=&d=c&c=662033156631&ag=21023439735&gclid=EAIaIQobChMIp-e68dSyhgMVdp5QBh3YmAGkEAEYASAAEgI1jvD_BwE",
            "time_usec": 1716978922934789,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cdn.apponic.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Download Adobe Photoshop CC for Mac",
            "url": "https://adobe-photoshop-cc.apponic.com/mac/download/",
            "time_usec": 1716978911448699,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cdn.apponic.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe Photoshop CC for Mac Download",
            "url": "https://adobe-photoshop-cc.apponic.com/mac/",
            "time_usec": 1716978883668004,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "photoshop CC 2015.x download for mac - Google Search",
            "url": "https://www.google.com/search?q=photoshop+CC+2015.x+download+for+mac&sca_esv=68ec23b20c823977&sxsrf=ADLYWILMb_ThxvTjxm5ssVr7qNjUJ90MXw%3A1716978840247&ei=mARXZqjODpSL9u8P0ZOwmAw&ved=0ahUKEwio-u_O1LKGAxWUhf0HHdEJDMMQ4dUDCBA&uact=5&oq=photoshop+CC+2015.x+download+for+mac&gs_lp=Egxnd3Mtd2l6LXNlcnAiJHBob3Rvc2hvcCBDQyAyMDE1LnggZG93bmxvYWQgZm9yIG1hY0i8LFDRDljOK3AIeAGQAQCYAeIBoAGFCqoBBTQuNS4xuAEDyAEA-AEBmAIGoAL3AsICChAAGLADGNYEGEfCAgUQIRigAcICBBAhGBWYAwCIBgGQBgiSBwU0LjEuMaAHogw&sclient=gws-wiz-serp",
            "time_usec": 1716978854381593,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "photoshop CC 2015.x download - Google Search",
            "url": "https://www.google.com/search?q=photoshop+CC+2015.x+download+&sca_esv=68ec23b20c823977&sxsrf=ADLYWIIXsv0H4WPVLFhRmiUBosIxlTXzzA%3A1716977667505&ei=AwBXZpO5Hp397_UPo6KDSA&ved=0ahUKEwjTxtWf0LKGAxWd_rsIHSPRAAkQ4dUDCBA&uact=5&oq=photoshop+CC+2015.x+download+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIh1waG90b3Nob3AgQ0MgMjAxNS54IGRvd25sb2FkIEiXW1CyB1jxWnAMeAGQAQCYAaABoAHmGKoBBTIyLjExuAEDyAEA-AEBmAIkoAKnFagCCsICChAAGLADGNYEGEfCAgQQIxgnwgIKECMYgAQYJxiKBcICCxAAGIAEGJECGIoFwgIIEC4YgAQY1ALCAgUQABiABMICCxAuGIAEGNEDGMcBwgIKEC4YgAQYQxiKBcICBRAuGIAEwgIZEC4YgAQYQxiKBRiXBRjcBBjeBBjgBNgBAcICBxAAGIAEGArCAgcQLhiABBgKwgIHECMYJxjqAsICGRAuGIAEGEMYigUYlwUY3AQY3gQY3wTYAQHCAhoQLhiABBjRAxjHARiXBRjcBBjeBBjgBNgBAcICChAAGIAEGEMYigXCAgoQABiABBgUGIcCwgIIEAAYgAQYiwPCAgYQABgWGB7CAgkQABgWGIsDGB6YAwqIBgGQBgi6BgYIARABGBSSBwUyNC4xMqAHubkB&sclient=gws-wiz-serp",
            "time_usec": 1716978840204791,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how do i download photoshop 2015 - Google Search",
            "url": "https://www.google.com/search?q=how+do+i+download+photoshop+2015&oq=how+do+i+download+photoshop+2015&aqs=chrome..69i64j69i57.11192j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716978825384855,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.youtube.com/s/desktop/11f8caf2/img/favicon_32x32.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "How to install photoshop cc2015 - YouTube",
            "url": "https://www.youtube.com/watch?v=J8WKP7csMfM",
            "time_usec": 1716978806675648,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://photoshop.adobe.com/favicon-32x32.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe Photoshop",
            "url": "https://photoshop.adobe.com/?promoid=4F569DWB&mv=product&mv2=accc#access_token=eyJhbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LWF0LTEuY2VyIiwia2lkIjoiaW1zX25hMS1rZXktYXQtMSIsIml0dCI6ImF0In0.eyJpZCI6IjE3MTY5Nzg2NzA1MTNfMTNmYjM1NzQtYjgwNC00ZDc5LWFkY2EtMThjMDg3M2U3NmY0X3ZhNmMyIiwidHlwZSI6ImFjY2Vzc190b2tlbiIsImNsaWVudF9pZCI6IlBTV2ViQXBwMSIsInVzZXJfaWQiOiJBQzVENTY0ODVFQjcyMUNDMEE0OTVFQjFAQWRvYmVJRCIsInN0YXRlIjoiIiwiYXMiOiJpbXMtbmExIiwiYWFfaWQiOiJBQzVENTY0ODVFQjcyMUNDMEE0OTVFQjFAQWRvYmVJRCIsImN0cCI6MCwiZmciOiJZUFNWR1pRWVZQUDVNSFVLRk1RVllIQUFDQSIsInNpZCI6IjE3MTY5Nzc5MzAxNjJfOTVkNzkyYmUtOWIzNi00Y2ZiLTk0MDMtMzZhMDEwNTg5YzRjX3ZhNmMyIiwibW9pIjoiNjA0MGI3YjMiLCJwYmEiOiJNZWRTZWNOb0VWLExvd1NlYyIsImV4cGlyZXNfaW4iOiI4NjQwMDAwMCIsImNyZWF0ZWRfYXQiOiIxNzE2OTc4NjcwNTEzIiwic2NvcGUiOiJhYi5tYW5hZ2UsQWRvYmVJRCxvcGVuaWQsY3JlYXRpdmVfc2RrLHRrX3BsYXRmb3JtLHRrX3BsYXRmb3JtX3N5bmMsYWZfYnlvZix1ZHNfcmVhZCx1ZHNfd3JpdGUifQ.Qldci5wrXJymDeXk35JdBP2-1SHfkwiDF7dpoCIzVtByMCc1OkfX6QRyeVyD5wZKxHs5Z6cw42kGVL490L7CUYi3tF_gLFo0BsHZ-7Hh3vd1Tqh8xg_xgQMhx1ZOTRnNNHb2m7pvmbxpdNO-RJpnIkw1-qrK-Su--s_ftNG6a03qmQ6UTQPHBZXdwCJKEQ6_py2I_UjN5uazMwDg83g3zzsus9rLrMzSbBprEcLQiRt7sy22PTgV54YMzCgeKX-pw9AFhlmxaeitqUQ0RCIlAA3QdutVu5QzY3lR4RO81ets2Cb4W7RN27ohHXg-eRGZioVUEKsUufhRbjY5nRMfIg&token_type=bearer&expires_in=86399997",
            "time_usec": 1716978675097252,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://auth.services.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe ID",
            "url": "https://auth.services.adobe.com/en_US/deeplink.html#/deeplink",
            "time_usec": 1716978668122855,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://auth.services.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe ID",
            "url": "https://auth.services.adobe.com/en_US/deeplink.html#/jump/complete",
            "time_usec": 1716978667918529,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://auth.services.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe ID",
            "url": "https://auth.services.adobe.com/en_US/deeplink.html?delegated_request_id=73a90f80-0f5a-45df-8893-c6547ce36fdc&client_id=CreativeCloudInstallerWeb_v1_0&deeplink=delegation#/delegation/success",
            "time_usec": 1716978519893173,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://auth.services.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe ID",
            "url": "https://auth.services.adobe.com/en_US/deeplink.html?delegated_request_id=73a90f80-0f5a-45df-8893-c6547ce36fdc&client_id=CreativeCloudInstallerWeb_v1_0&deeplink=delegation#/delegation",
            "time_usec": 1716978519700431,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://auth.services.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe ID",
            "url": "https://auth.services.adobe.com/en_US/deeplink.html?delegated_request_id=73a90f80-0f5a-45df-8893-c6547ce36fdc&client_id=CreativeCloudInstallerWeb_v1_0&deeplink=delegation#/deeplink",
            "time_usec": 1716978519527776,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://auth.services.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe ID",
            "url": "https://auth.services.adobe.com/en_US/deeplink.html?deeplink=ssofirst&callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2FCreativeCloudInstallerWeb_v1_0%2FAdobeID%2Fcode%3Fredirect_uri%3Dhttps%253A%252F%252Fauth.services.adobe.com%252Fen_US%252Fdeeplink.html%253Fdelegated_request_id%253D73a90f80-0f5a-45df-8893-c6547ce36fdc%2526client_id%253DCreativeCloudInstallerWeb_v1_0%2526deeplink%253Ddelegation%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=CreativeCloudInstallerWeb_v1_0&scope=allow_ac_dt_exchange%2Copenid%2CAdobeID%2Ccreative_cloud%2Ccreative_sdk%2Cread_organizations%2Csao.cce_private%2Cadditional_info.account_type&relay=34af0867-5f19-41dd-8712-c91ebf17cdfa&locale=en_US&flow_type=code&idp_flow_type=login&s_p=google%2Cfacebook%2Capple%2Cmicrosoft&response_type=code&code_challenge_method=plain&redirect_uri=https%3A%2F%2Fauth.services.adobe.com%2Fen_US%2Fdeeplink.html%3Fdelegated_request_id%3D73a90f80-0f5a-45df-8893-c6547ce36fdc%26client_id%3DCreativeCloudInstallerWeb_v1_0%26deeplink%3Ddelegation&use_ms_for_expiry=true#/deeplink",
            "time_usec": 1716978516955952,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://creativecloud.adobe.com/cc_favicon_48.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Install Creative Cloud | Adobe Creative Cloud",
            "url": "https://creativecloud.adobe.com/apps/all/desktop?action=install&source=allAppsAppPicker&productId=creative-cloud&isStarter=true",
            "time_usec": 1716978472762558,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://creativecloud.adobe.com/cc_favicon_48.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Creative Cloud All Apps | Adobe Creative Cloud",
            "url": "https://creativecloud.adobe.com/apps/starter/all-apps?context.guid=ab663836-8c16-4b6a-9140-39dbc896f1df&mv=other&promoid=QGMZPG6T",
            "time_usec": 1716978456160303,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://productrouter.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Product Router",
            "url": "https://productrouter.adobe.com/?orderId=E56D6C5328AE217169780184998756&workflow=edu&context=iframe&cloud=CREATIVE&familyName=CC_ALL_APPS&x-product=CCHome&x-product-location=Apps&guid=e431d3b5-6685-4775-9f7b-355b84e0a6bd&context_guid=ab663836-8c16-4b6a-9140-39dbc896f1df&promoid=QGMZPG6T&mv=other&mv2=ahome",
            "time_usec": 1716978454673987,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "All Apps | Adobe Home",
            "url": "https://www.adobe.com/apps/all/all-platforms",
            "time_usec": 1716978446729159,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "All Apps | Adobe Home",
            "url": "https://www.adobe.com/apps/all/all-platforms",
            "time_usec": 1716978399909628,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "All Apps | Adobe Home",
            "url": "https://www.adobe.com/apps/all/all-platforms",
            "time_usec": 1716978034414551,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "All Apps | Adobe Home",
            "url": "https://www.adobe.com/apps/all/all-platforms",
            "time_usec": 1716978024781028,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "All Apps | Adobe Home",
            "url": "https://www.adobe.com/apps/all/all-platforms",
            "time_usec": 1716978016756424,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "All Apps | Adobe Home",
            "url": "https://www.adobe.com/apps/all/all-platforms",
            "time_usec": 1716977941482301,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://auth.services.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe ID",
            "url": "https://auth.services.adobe.com/en_US/deeplink.html#/progressive-profile/terms-of-use/",
            "time_usec": 1716977921116905,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://auth.services.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe ID",
            "url": "https://auth.services.adobe.com/en_US/index.html?callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2FCCHomeWeb1%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%253A%252F%252Fcreativecloud.adobe.com%252Fapps%253Fsa_src%253DAVA_JC_Bot-Eng-DISU.HowToDownload.DownloadCC-SSWF10-CCI-Msg%2523old_hash%253Dsa_src%253Dweb-messaging%2526from_ims%253Dtrue%2526client_id%253DCCHomeWeb1%2526api%253Dauthorize%2526scope%253DAdobeID%252Copenid%252Cgnav%252Cread_organizations%252Ccreative_sdk%252Cadditional_info.optionalAgreements%252Cadditional_info.screen_name%252Cadditional_info.roles%252Ctk_platform%252Cpiip_read%252Ctk_platform_sync%252Caf_byof%252Cpps.read%252Cfirefly_api%26state%3D%257B%2522jslibver%2522%253A%2522v2-v0.31.0-2-g1e8a8a8%2522%252C%2522nonce%2522%253A%25221889405343673458%2522%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=CCHomeWeb1&scope=AdobeID%2Copenid%2Cgnav%2Cread_organizations%2Ccreative_sdk%2Cadditional_info.optionalAgreements%2Cadditional_info.screen_name%2Cadditional_info.roles%2Ctk_platform%2Cpiip_read%2Ctk_platform_sync%2Caf_byof%2Cpps.read%2Cfirefly_api&state=%7B%22jslibver%22%3A%22v2-v0.31.0-2-g1e8a8a8%22%2C%22nonce%22%3A%221889405343673458%22%7D&relay=34af0867-5f19-41dd-8712-c91ebf17cdfa&locale=en_US&flow_type=token&idp_flow_type=login&s_p=google%2Cfacebook%2Capple%2Cmicrosoft&response_type=token&code_challenge_method=plain&redirect_uri=https%3A%2F%2Fcreativecloud.adobe.com%2Fapps%3Fsa_src%3DAVA_JC_Bot-Eng-DISU.HowToDownload.DownloadCC-SSWF10-CCI-Msg%23old_hash%3Dsa_src%3Dweb-messaging%26from_ims%3Dtrue%26client_id%3DCCHomeWeb1%26api%3Dauthorize%26scope%3DAdobeID%2Copenid%2Cgnav%2Cread_organizations%2Ccreative_sdk%2Cadditional_info.optionalAgreements%2Cadditional_info.screen_name%2Cadditional_info.roles%2Ctk_platform%2Cpiip_read%2Ctk_platform_sync%2Caf_byof%2Cpps.read%2Cfirefly_api&use_ms_for_expiry=true#/",
            "time_usec": 1716977909850349,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://creativecloud.adobe.com/cc_favicon_48.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe Creative Cloud | Sign in",
            "url": "https://creativecloud.adobe.com/apps?sa_src=AVA_JC_Bot-Eng-DISU.HowToDownload.DownloadCC-SSWF10-CCI-Msg#sa_src=web-messaging",
            "time_usec": 1716977901856528,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/content/dam/cc/Adobe_favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe Photoshop for students | Adobe",
            "url": "https://www.adobe.com/creativecloud/buy/students/photoshop.html",
            "time_usec": 1716977839640138,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/content/dam/cc/Adobe_favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe Creative Cloud for students and teachers | Adobe Creative Cloud",
            "url": "https://www.adobe.com/creativecloud/buy/students.html",
            "time_usec": 1716977790039709,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/creativecloud/img/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Official Adobe Photoshop - Leading AI photo & design software",
            "url": "https://www.adobe.com/products/photoshop.html?gclid=Cj0KCQjwpNuyBhCuARIsANJqL9OCs2BRxpgs8vDHLwKEzvB5mOjP8Ee5x0iUmp4Yf0QG3gtoM8zz7XAaAogSEALw_wcB&sdid=1SQHCYZL&mv=search&mv2=paidsearch&ef_id=Cj0KCQjwpNuyBhCuARIsANJqL9OCs2BRxpgs8vDHLwKEzvB5mOjP8Ee5x0iUmp4Yf0QG3gtoM8zz7XAaAogSEALw_wcB:G:s&s_kwcid=AL!3085!3!667539960892!e!!g!!adobe%20creative%20cloud%20application!151098760!109927013492&gad_source=1",
            "time_usec": 1716977787487187,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/creativecloud/img/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Official Adobe Photoshop - Leading AI photo & design software",
            "url": "https://www.adobe.com/products/photoshop.html?gclid=Cj0KCQjwpNuyBhCuARIsANJqL9OCs2BRxpgs8vDHLwKEzvB5mOjP8Ee5x0iUmp4Yf0QG3gtoM8zz7XAaAogSEALw_wcB&sdid=1SQHCYZL&mv=search&mv2=paidsearch&ef_id=Cj0KCQjwpNuyBhCuARIsANJqL9OCs2BRxpgs8vDHLwKEzvB5mOjP8Ee5x0iUmp4Yf0QG3gtoM8zz7XAaAogSEALw_wcB:G:s&s_kwcid=AL!3085!3!667539960892!e!!g!!adobe%20creative%20cloud%20application!151098760!109927013492&gad_source=1",
            "time_usec": 1716977706604670,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "creative cloud desktop app - Google Search",
            "url": "https://www.google.com/search?q=creative+cloud+desktop+app&oq=creative+cloud+desktop+app&aqs=chrome..69i64j0i20i263i512j0i22i30l8.7664j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716977697805512,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716977689113114,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how do i download photoshop 2015 - Google Search",
            "url": "https://www.google.com/search?q=how+do+i+download+photoshop+2015&oq=how+do+i+download+photoshop+2015&aqs=chrome..69i64j69i57.11192j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716977667725926,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716977654419874,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Older versions of Photoshop system requirements",
            "url": "https://helpx.adobe.com/photoshop/system-requirements-old-versions.html",
            "time_usec": 1716977611480962,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Photoshop system requirements",
            "url": "https://helpx.adobe.com/photoshop/system-requirements/earlier-versions.html",
            "time_usec": 1716977570504458,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Photoshop for Max OS X 10.11 (El Capitan) - Adobe Community - 11094517",
            "url": "https://community.adobe.com/t5/photoshop-ecosystem-discussions/photoshop-for-max-os-x-10-11-el-capitan/m-p/11094517",
            "time_usec": 1716977550461849,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "photoshop for el capitan download - Google Search",
            "url": "https://www.google.com/search?q=photoshop+for+el+capitan+download&sca_esv=68ec23b20c823977&sxsrf=ADLYWIJ3vxc1kfqEqLRGarCf-4zkEqoOqA%3A1716977291017&ei=i_5WZrxTremL6A-0koi4BQ&oq=photoshop+for+el+captain&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIhhwaG90b3Nob3AgZm9yIGVsIGNhcHRhaW4qAggBMgcQABiABBgNMgYQABgWGB4yCBAAGAgYDRgeMgsQABiABBiiBBiLA0j9Q1CtBFiLNXAEeACQAQCYAbgBoAGOFKoBBDIyLjW4AQHIAQD4AQGYAh-gArkWqAIKwgIHECMYJxjqAsICChAjGIAEGCcYigXCAgQQIxgnwgILEAAYgAQYkQIYigXCAgoQABiABBhDGIoFwgIFEAAYgATCAgUQLhiABMICChAuGIAEGEMYigXCAg4QLhiABBjHARiOBRivAcICCxAuGIAEGMcBGK8BwgIHEAAYgAQYCsICHRAuGIAEGMcBGI4FGK8BGJcFGNwEGN4EGOAE2AEBwgILEC4YgAQY0QMYxwHCAgsQABiABBiGAxiKBcICCBAAGIAEGKIEwgILEAAYogQYiQUYiwPCAgYQABgNGB6YAw-6BgYIARABGBSSBwUxOC4xM6AH870B&sclient=gws-wiz-serp",
            "time_usec": 1716977530797234,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "can you download photoshop on a macbook version 10.11 - Google Search",
            "url": "https://www.google.com/search?q=can+you+download+photoshop+on+a+macbook+version+10.11&oq=can+you+download+photoshop+on+a+macbook+version+10.11&aqs=chrome..69i64j69i57.45030j1j1&sourceid=chrome&ie=UTF-8#ip=1",
            "time_usec": 1716977452966147,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://apple.stackexchange.com/questions/345873/el-capitan-and-old-photoshop-to-bootable-partition",
            "time_usec": 1716977448475654,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "can you download photoshop on a macbook version 10.11 - Google Search",
            "url": "https://www.google.com/search?q=can+you+download+photoshop+on+a+macbook+version+10.11&oq=can+you+download+photoshop+on+a+macbook+version+10.11&aqs=chrome..69i64j69i57.45030j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716977290964427,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716977244213568,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Re: How to install old Photoshop version on a old ... - Adobe Community - 12555848",
            "url": "https://community.adobe.com/t5/photoshop-ecosystem-discussions/how-to-install-old-photoshop-version-on-a-old-macbook/m-p/12557536",
            "time_usec": 1716977216090956,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "adobe photoshop download for an old mac - Google Search",
            "url": "https://www.google.com/search?q=adobe+photoshop+download+for+an+old+mac&sca_esv=68ec23b20c823977&sxsrf=ADLYWIJqyg7e0I8SOCzllCwn4swlZBwfBg%3A1716977091668&ei=w_1WZv6QKODji-gPsZSqwAo&ved=0ahUKEwi-_oqNzrKGAxXg8QIHHTGKCqgQ4dUDCBA&uact=5&oq=adobe+photoshop+download+for+an+old+mac&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIidhZG9iZSBwaG90b3Nob3AgZG93bmxvYWQgZm9yIGFuIG9sZCBtYWMyBRAhGKABMgUQIRigATIFECEYnwUyBRAhGJ8FMgUQIRifBTIFECEYnwUyBRAhGJ8FMgUQIRifBTIFECEYnwVIqPYBUMcJWJ_1AXAFeASQAQGYAdMDoAGHKaoBCzM4LjEzLjEuMC4xuAEDyAEA-AEBmAI6oALHKMICBBAAGEfCAgoQIxiABBgnGIoFwgIEECMYJ8ICChAAGIAEGEMYigXCAhAQLhiABBjRAxhDGMcBGIoFwgILEC4YgAQY0QMYxwHCAgoQABiABBgUGIcCwgIFEAAYgATCAgsQLhiABBjHARivAcICHxAuGIAEGNEDGEMYxwEYigUYlwUY3AQY3gQY4ATYAQHCAgcQABiABBgKwgINEC4YgAQY0QMYxwEYCsICBxAjGLECGCfCAgsQABiABBiRAhiKBcICCxAAGIAEGIYDGIoFwgILEAAYgAQYogQYiwPCAggQABiABBiiBMICDhAAGIAEGIYDGIoFGIsDwgIGEAAYFhgewgIHECEYoAEYCpgDAOIDBRIBMSBAiAYBkAYIugYGCAEQARgUkgcHMzcuMjAuMaAHv7kD&sclient=gws-wiz-serp",
            "time_usec": 1716977132478994,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "lightroom login - Google Search",
            "url": "https://www.google.com/search?q=lightroom+ogin&oq=lightroom+ogin&aqs=chrome..69i64j0i13i512j0i13i30l7j0i5i13i30.7181j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716977091749590,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716977083263280,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://auth.services.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe ID",
            "url": "https://auth.services.adobe.com/en_US/index.html#/error",
            "time_usec": 1716977080289400,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://auth.services.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe ID",
            "url": "https://auth.services.adobe.com/en_US/index.html#/error",
            "time_usec": 1716977072622909,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "https://federatedid-na1.services.adobe.com/federated/fromOIDC?state=AS49AakHANgSwklzvnGm4a90n7tDuDNvqbL0mxdS21U-8auN1BLHsJ-63JXhRgiEi1YkH0UAlVg_&code=4%2F0AdLIrYeymE3eQqu2JyERStary2uRZsueCVlNwpv1bwIAxXEPQsqe1MM-q1YqSQp1SFUIEQ&scope=email+profile+openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&authuser=0&prompt=none",
            "time_usec": 1716977053171398,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://auth.services.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe ID",
            "url": "https://auth.services.adobe.com/en_US/deeplink.html?deeplink=ssofirst&callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2Funified_checkout_client_v3%2FAdobeID%2Fcode%3Fredirect_uri%3Dhttps%253A%252F%252Fcommerce.adobe.com%252Fstore%252Fpayment%253Fucc%253D1%26state%3D%257B%2522ac%2522%253A%2522commerce.adobe.com%2522%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=unified_checkout_client_v3&scope=AdobeID%2Caccount_cluster.read%2Cadditional_info.authenticatingAccount%2Cadditional_info.roles%2Cadditional_info.vat_id%2Cbis.read.pan%2Cbis.read.pi%2Copenid%2Cupdate_profile.countryCode%2Cupdate_profile.optionalAgreements&state=%7B%22ac%22%3A%22commerce.adobe.com%22%7D&relay=34af0867-5f19-41dd-8712-c91ebf17cdfa&locale=en_US&flow_type=code&dc=true&puser=ryanfrancissteele%40gmail.com&pcountry=US&eu=true&dctx_id=v%3A2%2Ch%2Cdcp-r%2Cbg-c%3A%23F5F5F5FF%2Ccace2630-1da2-11ef-8b5d-e918f0c4be6a&idp_flow_type=login&s_p=google%2Cfacebook%2Capple%2Cmicrosoft&response_type=code&code_challenge_method=plain&redirect_uri=https%3A%2F%2Fcommerce.adobe.com%2Fstore%2Fpayment%3Fucc%3D1&use_ms_for_expiry=true#/social-only",
            "time_usec": 1716977051976503,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://auth.services.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe ID",
            "url": "https://auth.services.adobe.com/en_US/deeplink.html?deeplink=ssofirst&callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2Funified_checkout_client_v3%2FAdobeID%2Fcode%3Fredirect_uri%3Dhttps%253A%252F%252Fcommerce.adobe.com%252Fstore%252Fpayment%253Fucc%253D1%26state%3D%257B%2522ac%2522%253A%2522commerce.adobe.com%2522%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=unified_checkout_client_v3&scope=AdobeID%2Caccount_cluster.read%2Cadditional_info.authenticatingAccount%2Cadditional_info.roles%2Cadditional_info.vat_id%2Cbis.read.pan%2Cbis.read.pi%2Copenid%2Cupdate_profile.countryCode%2Cupdate_profile.optionalAgreements&state=%7B%22ac%22%3A%22commerce.adobe.com%22%7D&relay=34af0867-5f19-41dd-8712-c91ebf17cdfa&locale=en_US&flow_type=code&dc=true&puser=ryanfrancissteele%40gmail.com&pcountry=US&eu=true&dctx_id=v%3A2%2Ch%2Cdcp-r%2Cbg-c%3A%23F5F5F5FF%2Ccace2630-1da2-11ef-8b5d-e918f0c4be6a&idp_flow_type=login&s_p=google%2Cfacebook%2Capple%2Cmicrosoft&response_type=code&code_challenge_method=plain&redirect_uri=https%3A%2F%2Fcommerce.adobe.com%2Fstore%2Fpayment%3Fucc%3D1&use_ms_for_expiry=true#/deeplink",
            "time_usec": 1716977051233258,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://commerce.adobe.com/store/favicon_adobe.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe Checkout",
            "url": "https://commerce.adobe.com/store/email?items%5B0%5D%5Bid%5D=B85C86D4214EF804F8951D7E0A0E1945&items%5B0%5D%5Bq%5D=1&co=US&lang=en&cli=mini_plans&ss=recommendation&swc=4552&rrItems%5B0%5D%5Bid%5D=E27CB5D79014ACAB6953B091CEA72228",
            "time_usec": 1716977036563063,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://commerce.adobe.com/store/favicon_adobe.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe Checkout",
            "url": "https://commerce.adobe.com/store/recommendation?items%5B0%5D%5Bid%5D=E27CB5D79014ACAB6953B091CEA72228&co=US&lang=en&cli=mini_plans&rrItems%5B0%5D%5Bid%5D=E27CB5D79014ACAB6953B091CEA72228",
            "time_usec": 1716977015018210,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/creativecloud/img/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Transform photos and make gorgeous graphics | Adobe Photoshop",
            "url": "https://www.adobe.com/products/photoshop/landpa.html?gclid=Cj0KCQjwpNuyBhCuARIsANJqL9PYrAtziAbcGK95dzdz14e6s2GbABglKHCk3yuvrSIztesFggVn6sIaAsImEALw_wcB&sdid=NC5FRF5H&mv=search&mv2=paidsearch&ef_id=Cj0KCQjwpNuyBhCuARIsANJqL9PYrAtziAbcGK95dzdz14e6s2GbABglKHCk3yuvrSIztesFggVn6sIaAsImEALw_wcB:G:s&s_kwcid=AL!3085!3!697384330723!e!!g!!photoshop!1712238394!67643541820&mv=search&gad_source=1#modal-photoshop",
            "time_usec": 1716977006069599,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://commerce.adobe.com/store/favicon_adobe.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe Checkout",
            "url": "https://commerce.adobe.com/store/recommendation?items%5B0%5D%5Bid%5D=E27CB5D79014ACAB6953B091CEA72228&co=US&lang=en&cli=mini_plans&rrItems%5B0%5D%5Bid%5D=E27CB5D79014ACAB6953B091CEA72228",
            "time_usec": 1716976967035532,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/creativecloud/img/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Transform photos and make gorgeous graphics | Adobe Photoshop",
            "url": "https://www.adobe.com/products/photoshop/landpa.html?gclid=Cj0KCQjwpNuyBhCuARIsANJqL9PYrAtziAbcGK95dzdz14e6s2GbABglKHCk3yuvrSIztesFggVn6sIaAsImEALw_wcB&sdid=NC5FRF5H&mv=search&mv2=paidsearch&ef_id=Cj0KCQjwpNuyBhCuARIsANJqL9PYrAtziAbcGK95dzdz14e6s2GbABglKHCk3yuvrSIztesFggVn6sIaAsImEALw_wcB:G:s&s_kwcid=AL!3085!3!697384330723!e!!g!!photoshop!1712238394!67643541820&mv=search&gad_source=1#modal-photoshop",
            "time_usec": 1716976953888063,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/creativecloud/img/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Transform photos and make gorgeous graphics | Adobe Photoshop",
            "url": "https://www.adobe.com/products/photoshop/landpa.html?gclid=Cj0KCQjwpNuyBhCuARIsANJqL9PYrAtziAbcGK95dzdz14e6s2GbABglKHCk3yuvrSIztesFggVn6sIaAsImEALw_wcB&sdid=NC5FRF5H&mv=search&mv2=paidsearch&ef_id=Cj0KCQjwpNuyBhCuARIsANJqL9PYrAtziAbcGK95dzdz14e6s2GbABglKHCk3yuvrSIztesFggVn6sIaAsImEALw_wcB:G:s&s_kwcid=AL!3085!3!697384330723!e!!g!!photoshop!1712238394!67643541820&mv=search&gad_source=1",
            "time_usec": 1716976944570112,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "photoshop - Google Search",
            "url": "https://www.google.com/search?q=photoshop&sca_esv=792c36b2414f597c&sxsrf=ADLYWIKWldWgCRbXc6quExVFyKjvNqGutA%3A1716906757123&ei=BetVZsiIB7GK9u8PpdKZ4AE&ved=0ahUKEwiIn_uKyLCGAxUxhf0HHSVpBhwQ4dUDCBA&uact=5&oq=photoshop&gs_lp=Egxnd3Mtd2l6LXNlcnAiCXBob3Rvc2hvcDILEAAYgAQYkQIYigUyChAAGIAEGEMYigUyCxAAGIAEGJECGIoFMgsQABiABBiRAhiKBTILEAAYgAQYkQIYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigUyChAAGIAEGEMYigVIviNQzANY-yFwBHgBkAEEmAGKBaABvh6qAQsxLjQuNy4xLjEuMbgBA8gBAPgBAZgCD6ACvxOoAhLCAgcQIxgnGOoCwgITEAAYgAQYQxi0AhiKBRjqAtgBAcICFBAAGIAEGOMEGLQCGOkEGOoC2AEBwgIREC4YgAQYkQIY0QMYxwEYigXCAgUQABiABMICCxAuGIAEGNEDGMcBwgIIEC4YgAQY1ALCAiAQLhiABBiRAhjRAxjHARiKBRiXBRjcBBjeBBjgBNgBAsICDxAuGIAEGEMYRhj5ARiKBcICChAuGIAEGEMYigXCAgUQLhiABMICKRAAGIAEGEMYRhj5ARiKBRiXBRiMBRjdBBhGGPkBGPQDGPUDGPYD2AEDwgIKEAAYgAQYyQMYCsICBxAAGIAEGArCAgsQABiABBiSAxiKBcICBBAjGCfCAgoQIxiABBgnGIoFmAMyugYGCAEQARgBugYGCAIQARgUugYGCAMQARgTkgcHNS4zLjQuM6AHrXE&sclient=gws-wiz-serp",
            "time_usec": 1716976936208005,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "what is the difference between lightroom and photoshop - Google Search",
            "url": "https://www.google.com/search?q=what+is+the+difference+between+lightroom+and+photoshop&oq=what+is+the+difference+between+lightroom+and+photoshop&aqs=chrome..69i64j0i19i512j0i19i22i30j0i19i22i30i395l5j0i395i512i546j69i57.13204j1j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716906757951968,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://accounts.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign in - Google Accounts",
            "url": "https://accounts.google.com/signin/oauth/id?authuser=0&part=AJi8hANv7F8uJfdHCaq8ObapUoYPNHFAHTb6KackTECFRRmJvsd3HnCU4OAJEmAOTHi5nhFim7YXDngvkbWGYMGui8_Qt57C8XNE_nbGoDP56hB86L9uBkscG3S5PrU6jIUYa6vjemEjF8WwvEVsoBnprjKkqkeuAYSC9zsh1qIr4sPD0ffqStA0LtiPrVNWV5Z2a7HgIOkMZBcomsHbIivvs_vuF6F5b8FRqPkzt7EMkboMgvea6KbW7jtjTgs-OFxwPtfj1J1T5sRVQymyZqUKYVfWsU757WrH4UcEIwzBn1uvy7yoZVU0DqJVuppT2LU5klV5VpR00E29H6JHF0zzrV81xE9MeMilUeMENmhwwtebjOUwBo9MyDc0Rd5Lobwrsi9ywqJSn1-BuJNqss7Oj7C047M30uBRSTBZTjvBTPcrkeKzv9TvIEnWR9cJy8_RD4aPVOwxeNKfNAoSTWTxFZhHlGyqf7v-n8yqrUhxjexuhzI2kp3Oelf5_Ln-9nW5TfPtSjKWShM54isfDYKfgP7GnVTvZd7bdw6FcHXWwN6KzWmvnGMXwa_uMat1qesISunGXPIbmOki0f78Nf5nyAA0YjoEihtYuzM2hDOPxL3FjqSFWEag6X0rCA468G_0w9Zq-C2mgQZi1Cmwb20505j63Yw_YBqrxI33AFAmpCKn8BZ-iQMTOiZVy8-vpyldZHzTkcLpjfoNgxXkaT0dU59htApJC0nsDrmA88tqostZCv9jQS76E2Dnwel9ZweyTHxXVX8wYrgVSod9QFhbjH7epdc_LYpveYEXA2G7KQjuu7DYIJXb5-B-YvssvmnCUx10PYsFvrduVlt-7XToMjj6OlzcgWNhNoLJM94gqbmEVmQQcQiJbe0dx2si149vA7b9kx7Pv8ifIY8ROkdDR7is_MpckoxGjZGoA6KfKtC8-KSEzkT_66zlh6juv7JuE9eAZ06W0fdgqN9v4h2tfnayF7_XY3YGs228m5az11fgQ4E4hOQkUXjpBfiuFFafSzsg8xV2&flowName=GeneralOAuthFlow&as=S-989005611%3A1716906722586551&client_id=1014431251553-kq98rctnjtv76ag4ulrfkem43b74poni.apps.googleusercontent.com&rapt=AEjHL4Ohs0uRtOUVQQJ_vHhxDCx1Y4T323IUGcNzeel9oH-4BLp_CQCsU9vdDgjCxjlY5Rci__RHetqDwgL1wBRnRJyGq0LHag#",
            "time_usec": 1716906725732665,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign in - Google Accounts",
            "url": "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?client_id=1014431251553-kq98rctnjtv76ag4ulrfkem43b74poni.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Ffederatedid-na1.services.adobe.com%2Ffederated%2FfromOIDC&state=AbqWImixiqT6yfdc06cKl69UWbc53V0KDAmrqCz-heo9Irnr7ULMU7pApFkD9N5D4bd_InAk8tBh&scope=email%20openid%20profile&response_type=code&service=lso&o2v=2&ddm=0&flowName=GeneralOAuthFlow",
            "time_usec": 1716906723704280,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://auth.services.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe ID",
            "url": "https://auth.services.adobe.com/en_US/deeplink.html?deeplink=ssofirst&callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2Funified_checkout_client_v3%2FAdobeID%2Fcode%3Fredirect_uri%3Dhttps%253A%252F%252Fcommerce.adobe.com%252Fstore%252Fpayment%253Fucc%253D1%26state%3D%257B%2522ac%2522%253A%2522commerce.adobe.com%2522%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=unified_checkout_client_v3&scope=AdobeID%2Caccount_cluster.read%2Cadditional_info.authenticatingAccount%2Cadditional_info.roles%2Cadditional_info.vat_id%2Cbis.read.pan%2Cbis.read.pi%2Copenid%2Cupdate_profile.countryCode%2Cupdate_profile.optionalAgreements&state=%7B%22ac%22%3A%22commerce.adobe.com%22%7D&relay=34af0867-5f19-41dd-8712-c91ebf17cdfa&locale=en_US&flow_type=code&dc=true&puser=ryanfrancissteele%40gmail.com&pcountry=US&eu=true&dctx_id=v%3A2%2Ch%2Cdcp-r%2Cbg-c%3A%23F5F5F5FF%2C0aaf8d10-1cff-11ef-82cf-f5496040a204&idp_flow_type=login&s_p=google%2Cfacebook%2Capple%2Cmicrosoft&response_type=code&code_challenge_method=plain&redirect_uri=https%3A%2F%2Fcommerce.adobe.com%2Fstore%2Fpayment%3Fucc%3D1&use_ms_for_expiry=true#/social-only",
            "time_usec": 1716906721827396,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://auth.services.adobe.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe ID",
            "url": "https://auth.services.adobe.com/en_US/deeplink.html?deeplink=ssofirst&callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2Funified_checkout_client_v3%2FAdobeID%2Fcode%3Fredirect_uri%3Dhttps%253A%252F%252Fcommerce.adobe.com%252Fstore%252Fpayment%253Fucc%253D1%26state%3D%257B%2522ac%2522%253A%2522commerce.adobe.com%2522%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=unified_checkout_client_v3&scope=AdobeID%2Caccount_cluster.read%2Cadditional_info.authenticatingAccount%2Cadditional_info.roles%2Cadditional_info.vat_id%2Cbis.read.pan%2Cbis.read.pi%2Copenid%2Cupdate_profile.countryCode%2Cupdate_profile.optionalAgreements&state=%7B%22ac%22%3A%22commerce.adobe.com%22%7D&relay=34af0867-5f19-41dd-8712-c91ebf17cdfa&locale=en_US&flow_type=code&dc=true&puser=ryanfrancissteele%40gmail.com&pcountry=US&eu=true&dctx_id=v%3A2%2Ch%2Cdcp-r%2Cbg-c%3A%23F5F5F5FF%2C0aaf8d10-1cff-11ef-82cf-f5496040a204&idp_flow_type=login&s_p=google%2Cfacebook%2Capple%2Cmicrosoft&response_type=code&code_challenge_method=plain&redirect_uri=https%3A%2F%2Fcommerce.adobe.com%2Fstore%2Fpayment%3Fucc%3D1&use_ms_for_expiry=true#/deeplink",
            "time_usec": 1716906721099402,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://commerce.adobe.com/store/favicon_adobe.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Adobe Checkout",
            "url": "https://commerce.adobe.com/store/email?items[0][id]=C6DBF840A991DF84B7B3F871ABAD2415&co=US&lang=en&cli=mini_plans",
            "time_usec": 1716906661257070,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/creativecloud/img/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Photoshop free trial & free download | Official Adobe Photoshop",
            "url": "https://www.adobe.com/products/photoshop/free-trial-download.html?gclid=CjwKCAjwgdayBhBQEiwAXhMxtnNM3hwifUHym-Rrj-UoDyLg_DXVKdd1wkYIpWK2kmU58AwVkpsysBoCfeYQAvD_BwE&sdid=N3PCRNMK&mv=search&mv2=paidsearch&ef_id=CjwKCAjwgdayBhBQEiwAXhMxtnNM3hwifUHym-Rrj-UoDyLg_DXVKdd1wkYIpWK2kmU58AwVkpsysBoCfeYQAvD_BwE:G:s&s_kwcid=AL!3085!3!673842474193!p!!g!!download%20photoshop%20cc!10751508196!107075284518&mv=search&gad_source=1#modal-twp-photoshop",
            "time_usec": 1716906635697227,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/creativecloud/img/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Photoshop free trial & free download | Official Adobe Photoshop",
            "url": "https://www.adobe.com/products/photoshop/free-trial-download.html?gclid=CjwKCAjwgdayBhBQEiwAXhMxtnNM3hwifUHym-Rrj-UoDyLg_DXVKdd1wkYIpWK2kmU58AwVkpsysBoCfeYQAvD_BwE&sdid=N3PCRNMK&mv=search&mv2=paidsearch&ef_id=CjwKCAjwgdayBhBQEiwAXhMxtnNM3hwifUHym-Rrj-UoDyLg_DXVKdd1wkYIpWK2kmU58AwVkpsysBoCfeYQAvD_BwE:G:s&s_kwcid=AL!3085!3!673842474193!p!!g!!download%20photoshop%20cc!10751508196!107075284518&mv=search&gad_source=1#",
            "time_usec": 1716906631158445,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/creativecloud/img/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Photoshop free trial & free download | Official Adobe Photoshop",
            "url": "https://www.adobe.com/products/photoshop/free-trial-download.html?gclid=CjwKCAjwgdayBhBQEiwAXhMxtnNM3hwifUHym-Rrj-UoDyLg_DXVKdd1wkYIpWK2kmU58AwVkpsysBoCfeYQAvD_BwE&sdid=N3PCRNMK&mv=search&mv2=paidsearch&ef_id=CjwKCAjwgdayBhBQEiwAXhMxtnNM3hwifUHym-Rrj-UoDyLg_DXVKdd1wkYIpWK2kmU58AwVkpsysBoCfeYQAvD_BwE:G:s&s_kwcid=AL!3085!3!673842474193!p!!g!!download%20photoshop%20cc!10751508196!107075284518&mv=search&gad_source=1",
            "time_usec": 1716906628072917,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "adobe photoshop download cheapest - Google Search",
            "url": "https://www.google.com/search?q=adobe+photoshop+download+cheapest&sca_esv=8a43c4591a19e45c&sxsrf=ADLYWIKjwuPdWwkxBPicbRSyphw95f1AoA%3A1716906536678&ei=KOpVZuT7KOGB9u8P1uSPwAE&ved=0ahUKEwjkr-yhx7CGAxXhgP0HHVbyAxgQ4dUDCBA&uact=5&oq=adobe+photoshop+download+cheapest&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIiFhZG9iZSBwaG90b3Nob3AgZG93bmxvYWQgY2hlYXBlc3QyBRAhGKABMgUQIRigATIFECEYnwUyBRAhGJ8FMgUQIRifBTIFECEYnwUyBRAhGJ8FMgUQIRifBUj1GFCWA1juFnABeAGQAQCYAb0BoAGgCaoBAzAuObgBA8gBAPgBAZgCCqAC9QnCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICChAAGIAEGEMYigXCAgUQABiABMICChAAGIAEGBQYhwLCAgYQABgWGB7CAgsQABiABBiGAxiKBcICCxAAGIAEGKIEGIsDwgIEECEYFcICBxAhGKABGAqYAwCIBgGQBgqSBwMxLjmgB8A3&sclient=gws-wiz-serp",
            "time_usec": 1716906566736284,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "adobe photoshop download - Google Search",
            "url": "https://www.google.com/search?q=adobe+photoshop+download&oq=adobe+photoshop+download+&aqs=chrome..69i64j0i20i263i512l2j0i512l2j0i22i30l2j69i60.7836j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716906537367632,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "adobe photoshop download - Google Search",
            "url": "https://www.google.com/search?q=adobe+photoshop+download&oq=adobe+photoshop+download+&aqs=chrome..69i64j0i20i263i512l2j0i512l2j0i22i30l2j69i60.7836j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716906536785777,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716906527903936,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/creativecloud/img/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Photo editing and organizing software | Adobe Photoshop Lightroom",
            "url": "https://www.adobe.com/products/photoshop-lightroom/campaign/pricing.html?gclid=CjwKCAjwgdayBhBQEiwAXhMxtjqfGlNx_FkPRJdyXM-mY5XuOJn6fraukdOHUIstbOwbs-lN8AJ1GhoCbfEQAvD_BwE&sdid=BDDS3CR2&mv=search&mv2=paidsearch&ef_id=CjwKCAjwgdayBhBQEiwAXhMxtjqfGlNx_FkPRJdyXM-mY5XuOJn6fraukdOHUIstbOwbs-lN8AJ1GhoCbfEQAvD_BwE:G:s&s_kwcid=AL!3085!3!677050899261!e!!g!!lightroom%20mac!1712238382!67643558540&mv=search&gad_source=1",
            "time_usec": 1716906526303186,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/creativecloud/img/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Photo editing and organizing software | Adobe Photoshop Lightroom",
            "url": "https://www.adobe.com/products/photoshop-lightroom/campaign/pricing.html?gclid=CjwKCAjwgdayBhBQEiwAXhMxtjqfGlNx_FkPRJdyXM-mY5XuOJn6fraukdOHUIstbOwbs-lN8AJ1GhoCbfEQAvD_BwE&sdid=BDDS3CR2&mv=search&mv2=paidsearch&ef_id=CjwKCAjwgdayBhBQEiwAXhMxtjqfGlNx_FkPRJdyXM-mY5XuOJn6fraukdOHUIstbOwbs-lN8AJ1GhoCbfEQAvD_BwE:G:s&s_kwcid=AL!3085!3!677050899261!e!!g!!lightroom%20mac!1712238382!67643558540&mv=search&gad_source=1#model-lightroom",
            "time_usec": 1716906504819089,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.adobe.com/creativecloud/img/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Photo editing and organizing software | Adobe Photoshop Lightroom",
            "url": "https://www.adobe.com/products/photoshop-lightroom/campaign/pricing.html?gclid=CjwKCAjwgdayBhBQEiwAXhMxtjqfGlNx_FkPRJdyXM-mY5XuOJn6fraukdOHUIstbOwbs-lN8AJ1GhoCbfEQAvD_BwE&sdid=BDDS3CR2&mv=search&mv2=paidsearch&ef_id=CjwKCAjwgdayBhBQEiwAXhMxtjqfGlNx_FkPRJdyXM-mY5XuOJn6fraukdOHUIstbOwbs-lN8AJ1GhoCbfEQAvD_BwE:G:s&s_kwcid=AL!3085!3!677050899261!e!!g!!lightroom%20mac!1712238382!67643558540&mv=search&gad_source=1",
            "time_usec": 1716906428082883,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "adobe photoshop lightroom download for mac - Google Search",
            "url": "https://www.google.com/search?q=adobe+photoshop+lightroom+download+for+mac+&sca_esv=8a43c4591a19e45c&sxsrf=ADLYWIKZsYUZG3oXx5Wc7MXAIsxm_YLU1A%3A1716906388641&ei=lOlVZvjgJpGI7NYPkPmMiAg&ved=0ahUKEwj4-qDbxrCGAxURBNsEHZA8A4EQ4dUDCBA&uact=5&oq=adobe+photoshop+lightroom+download+for+mac+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIithZG9iZSBwaG90b3Nob3AgbGlnaHRyb29tIGRvd25sb2FkIGZvciBtYWMgMgYQABgWGB4yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYogQYiwNI4BtQ2AJY2RpwAXgBkAEAmAGkAaABvQ-qAQM5Ljm4AQPIAQD4AQGYAhOgAs0QwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigXCAgUQABiABMICChAAGIAEGBQYhwKYAwCIBgGQBgqSBwQzLjE2oAfKbQ&sclient=gws-wiz-serp",
            "time_usec": 1716906414541251,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "adobe photoshop lightroom - Google Search",
            "url": "https://www.google.com/search?q=adobe+photoshop+lightroom&sca_esv=8a43c4591a19e45c&sxsrf=ADLYWIIMR669qDam-iYFHzh70Ljd9OsG6g%3A1716906380856&ei=jOlVZpfsM_qGxc8P6rTMmQs&ved=0ahUKEwiX4sXXxrCGAxV6Q_EDHWoaM7MQ4dUDCBA&uact=5&oq=adobe+photoshop+lightroom&gs_lp=Egxnd3Mtd2l6LXNlcnAiGWFkb2JlIHBob3Rvc2hvcCBsaWdodHJvb20yBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESIkeUL4FWP8ccAF4AZABAZgB5gGgAcIIqgEFNi4zLjG4AQPIAQD4AQGYAgqgArQHwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigXCAgsQABiABBiRAhiKBZgDAIgGAZAGCpIHAzUuNaAHxjw&sclient=gws-wiz-serp",
            "time_usec": 1716906388798851,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "adobe photoshop - Google Search",
            "url": "https://www.google.com/search?q=adobe+photoshop&oq=adobe+photoshop&aqs=chrome.0.69i59j0i131i433i512j0i433i512j0i131i433i512l2j0i512l5.9690j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716906382149057,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716906368425227,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://it.diesel.com/on/demandware.static/Sites-DieselIT-Site/-/default/dw24ce1337/imgs/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Jeans Uomo in Denim: classici, per tutti i giorni | Diesel®",
            "url": "https://it.diesel.com/it/uomo/denimcore/",
            "time_usec": 1716905683226297,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Jeans Uomo in Denim: classici, per tutti i giorni | Diesel®",
            "url": "https://it.diesel.com/it/uomo/denimcore/",
            "time_usec": 1716905679814718,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://it.diesel.com/on/demandware.static/Sites-DieselIT-Site/-/default/dw24ce1337/imgs/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Denim Trends: I Jeans Bestseller e i Fit di tendenza | Diesel®",
            "url": "https://it.diesel.com/it/denim-guide/",
            "time_usec": 1716905657047285,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://it.diesel.com/on/demandware.static/Sites-DieselIT-Site/-/default/dw24ce1337/imgs/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Jeans dritti donna | Nero/grigio scuro | Diesel 1996 D-Sire",
            "url": "https://it.diesel.com/it/straight-jeans-1996-d-sire-09i47-nero/8058992403202.html?utm_source=google&utm_medium=cpc&utm_campaign=conversion-LOWER_PURC_EMEA_IT-IT_ALW_ADW_BRAN-GENERAL_SHP_INTARGET--_cross_&utm_content=--&ds_cid=71700000102454210&gad_source=1&gclid=CjwKCAjwgdayBhBQEiwAXhMxthFtsd1IhVpYQq1YDQemchWFZYRjxLEBClk58xp8b8XXHjGCb2Xh0BoCPEEQAvD_BwE&gclsrc=aw.ds",
            "time_usec": 1716905645319294,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "agolde jeans - Google Search",
            "url": "https://www.google.com/search?sca_esv=8a43c4591a19e45c&sxsrf=ADLYWILUzeZ6OAOq30wz9MJyTe1UWaUOjA:1716905586312&q=agolde+jeans&source=lnms&uds=ADvngMgqPfd500FffDLSjDoas1rZDzdjprcwtEVkMr3h8rM5NST_7UnNTKvRCA6TFJARwCFsz2ZeuPc_cOMV7zL1ondP8jfIaiqGOqDHrvo9J2Vb_gJ3e2ZM8JesgfzEn8ukOFxHwydwoCEnwesPVir-4tHkl6g9EowHgL3I6e3h3c72PX6olNK0EeKYcJQGUX9iN2NfC5zYH5OqR082vmevJxEFAkqMLIwOzJkoRbEL82SfaHZ0O-iZFmsRlAR5bqZmoMHc-IrAOKJ_RBCCrSWbY_7Yh9tMMA&sa=X&ved=2ahUKEwivzNbcw7CGAxVhh_0HHSrcBSEQ0pQJegQIEBAB&biw=1440&bih=789&dpr=1",
            "time_usec": 1716905620765378,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "agolde jeans - Google Search",
            "url": "https://www.google.com/search?q=agolde+jeans&sca_esv=8a43c4591a19e45c&udm=2&biw=1440&bih=789&sxsrf=ADLYWIKVMA-smuxu4S7yzKxF_71n4PhNPQ%3A1716905529993&ei=OeZVZrWOPP6A9u8Pk-KemA0&ved=0ahUKEwj1junBw7CGAxV-gP0HHROxB9MQ4dUDCBA&uact=5&oq=agolde+jeans&gs_lp=Egxnd3Mtd2l6LXNlcnAiDGFnb2xkZSBqZWFuczIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARIrRFQ6ARYzQ9wAXgAkAEAmAFloAG_CKoBBDExLjG4AQPIAQD4AQGYAg2gAqcJqAIKwgIHECMYJxjqAsICBBAjGCfCAgoQABiABBhDGIoFmAMOkgcDOS40oAeHPg&sclient=gws-wiz-serp",
            "time_usec": 1716905587665909,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "mud jeans - Google Search",
            "url": "https://www.google.com/search?sca_esv=8a43c4591a19e45c&sxsrf=ADLYWIKNWfzYdyOhx1yrNfYNLZMe70ZHzA:1716905469169&q=mud+jeans&uds=ADvngMgNUs2jQs_tnEFE7jpafjfejguuCyQhkCyEcXGQ0hMXrvyUH1TRgeuH64MOQB78pP-uCvegekWOtxixOdxaqbjWKQ-PWwizeY4clPnEr06hiIk8cXR7wQeNaIz_NY1ZR3ofp87gtH4DSfsWX-I0lgqm2tTrV-cyceonIBwLQUhyzFtJFY9RIw6UIykCYqAl6J3Ocy5yikZAub_RBNYBV9bPSfwEbfUP7YKA8u7bR-_Muu6ioIJOu598qru3wmm2FkMIOz9611uJIsA9QjZ5_psu2TWFV_Yvv-RSoVyPa4ln6fxVJDq_yCoOUFuYODbIj3P5-1gn&udm=2&prmd=ivnbz&sa=X&ved=2ahUKEwjl2uikw7CGAxXL_7sIHR7nAtkQtKgLegQIFxAB&biw=1440&bih=789&dpr=1#vhid=ZaArVSP0KXhFeM&vssid=mosaic",
            "time_usec": 1716905582260347,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "mud jeans - Google Search",
            "url": "https://www.google.com/search?sca_esv=8a43c4591a19e45c&sxsrf=ADLYWIKNWfzYdyOhx1yrNfYNLZMe70ZHzA:1716905469169&q=mud+jeans&uds=ADvngMgNUs2jQs_tnEFE7jpafjfejguuCyQhkCyEcXGQ0hMXrvyUH1TRgeuH64MOQB78pP-uCvegekWOtxixOdxaqbjWKQ-PWwizeY4clPnEr06hiIk8cXR7wQeNaIz_NY1ZR3ofp87gtH4DSfsWX-I0lgqm2tTrV-cyceonIBwLQUhyzFtJFY9RIw6UIykCYqAl6J3Ocy5yikZAub_RBNYBV9bPSfwEbfUP7YKA8u7bR-_Muu6ioIJOu598qru3wmm2FkMIOz9611uJIsA9QjZ5_psu2TWFV_Yvv-RSoVyPa4ln6fxVJDq_yCoOUFuYODbIj3P5-1gn&udm=2&prmd=ivnbz&sa=X&ved=2ahUKEwjl2uikw7CGAxXL_7sIHR7nAtkQtKgLegQIFxAB&biw=1440&bih=789&dpr=1",
            "time_usec": 1716905531275227,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "mud jeans - Google Search",
            "url": "https://www.google.com/search?q=mud+jeans&oq=mud+jeans&aqs=chrome..69i64j46i199i465i512j0i22i30l8.3116j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716905524085737,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "mud jeans - Google Search",
            "url": "https://www.google.com/search?q=mud+jeans&oq=mud+jeans&aqs=chrome..69i64j46i199i465i512j0i22i30l8.3116j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716905471379362,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716905465314695,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g2e0550065d7_0_72",
            "time_usec": 1716904568671853,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_87",
            "time_usec": 1716904389647193,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g2e072932187_0_9",
            "time_usec": 1716904360539425,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_111",
            "time_usec": 1716904295122208,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_80",
            "time_usec": 1716904258374780,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g2e0550065d7_0_72",
            "time_usec": 1716904228585964,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_47",
            "time_usec": 1716904131641087,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g2e0550065d7_0_56",
            "time_usec": 1716904025137041,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g2e0550065d7_0_42",
            "time_usec": 1716904009843279,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_63",
            "time_usec": 1716903901246702,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.ge77270587f_0_1636",
            "time_usec": 1716903824965318,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.ge77270587f_0_11",
            "time_usec": 1716903728919621,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Calendar - 4 days, starting Tuesday, May 28, 2024",
            "url": "https://calendar.google.com/calendar/u/0/r?pli=1",
            "time_usec": 1716901363102135,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://calendar.google.com/googlecalendar/images/favicons_2020q4/calendar_28.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Calendar - 4 days, starting Tuesday, May 28, 2024",
            "url": "https://calendar.google.com/calendar/u/0/r?pli=1",
            "time_usec": 1716901359830649,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "calendario - Google Search",
            "url": "https://www.google.com/search?q=calendario&oq=calendar&aqs=chrome.0.0i131i433i457i512j69i64j0i433i512j0i67i512i650j0i433i512j0i512j0i433i512j0i131i433i512i650j0i512j0i131i433i512i650.12257j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716901353697810,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716901339401194,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.alltrails.com/app-icon-32.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "10 Best Lake Trails in Ortisei | AllTrails",
            "url": "https://www.alltrails.com/italy/south-tyrol/ortisei/lake",
            "time_usec": 1716901096128783,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "bolzano - Google Search",
            "url": "https://www.google.com/search?q=bolzano&oq=bolzano&aqs=chrome..69i64j46i131i433i512j46i67i512i650j0i67i512i650l2j46i512j46i131i433i512j0i67i512i650j0i433i512j0i3.4633j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716900749486717,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716900741094211,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how to get from ortisei to lakes - Google Search",
            "url": "https://www.google.com/search?sca_esv=d65c73666fce9bae&sxsrf=ADLYWIJexJb5qtPEKAjX6F3LyWQ3zbC4_Q:1716900703163&q=how+to+get+from+ortisei+to+lakes&source=lnms&uds=ADvngMgQ0JvoRVMOByH_6PqaqtKIwa7lOayGNwr6wJ9OQ_giewHMCQgJ-2NQxPnlaUnXYR4aKpigw9So0tTBYknB_Ka1oglXFbkgADUYSMSFS9dW8itza2HbYyHmpfVJQuQI6UN9VvP6Mgvehuj3thuSVJtQe9CBFR4i7tT1q2y4y8Jo6uAlmOl-LIgDX2sF6BO0aujEivS2M-_88FGRPCklPFtrRrqphnddG0eHuBVYc8KNi-DVWY12ilArrF-Nacde2u29fWvsoc0NGZ9xH9U4odTUsei65elKuWjjsZsi7kCg8M3T6XQo_GI978PZc3UT9kJuVFEM&sa=X&ved=2ahUKEwia45rEsbCGAxWMgP0HHc8jAb8Q0pQJegQIERAB&biw=1289&bih=701&dpr=1",
            "time_usec": 1716900706653864,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how to get from ortisei to lakes - Google Search",
            "url": "https://www.google.com/search?q=how+to+get+from+ortisei+to+lakes&sca_esv=d65c73666fce9bae&udm=2&biw=1289&bih=701&sxsrf=ADLYWIJ6Re52mWgW9rIh4dNYZIKngDgvkA%3A1716900651361&ei=K9NVZqHQFbWD9u8PmbaI8AE&ved=0ahUKEwjhkcGrsbCGAxW1gf0HHRkbAh4Q4dUDCBA&uact=5&oq=how+to+get+from+ortisei+to+lakes&gs_lp=Egxnd3Mtd2l6LXNlcnAiIGhvdyB0byBnZXQgZnJvbSBvcnRpc2VpIHRvIGxha2VzSM80UOkEWJ8ucAF4AJABAJgBlgGgAcMWqgEEMjguNLgBA8gBAPgBAZgCHKACxxSoAgrCAgcQIxgnGOoCwgIEECMYJ8ICBRAAGIAEwgIKEAAYgAQYQxiKBcICBhAAGAgYHsICBxAAGIAEGBiYAw2SBwQyMS43oAfKlQE&sclient=gws-wiz-serp",
            "time_usec": 1716900704155444,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "lakes near ortisei - Google Search",
            "url": "https://www.google.com/search?sca_esv=d65c73666fce9bae&sxsrf=ADLYWIIP-9VyewlGEt64anUP9S_Wz64-zA:1716900495209&q=lakes+near+ortisei&uds=ADvngMgM3sJHGRUUapkgumPBd1g4rDVC-cBmRg8lBWcSvgmlhn8YofZOlTNYrbbpujgLxYWtNQ7krzsTv3np1uxahqKF7VYs0TJEkrTO2me0gLfW8LzY5SoORh34SQhfBvb-LUB03iaJQTqIg-v73FSdbIgPVXPDs8zqLx5Ac3ldEAf8YFRs1ZIt9H7rOnxgFV1rWoXnBU_yK1dc_9rAjKpWxwjbyNINBW_UPHYn1rlmblSOKMKj6sp5H_emWEf2FyhgI81L1EIwqnhk2PVEsyAe3qdittZsL3QsvKhvfpb2aq4F5GPPqhgAlJA7SJLpi0pD_DjKtWb4&udm=2&prmd=ivnbz&sa=X&ved=2ahUKEwjAh4bhsLCGAxXggP0HHcZqBigQtKgLegQIEBAB&biw=1289&bih=701&dpr=1",
            "time_usec": 1716900685091956,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "lakes near ortisei - Google Search",
            "url": "https://www.google.com/search?sca_esv=d65c73666fce9bae&sxsrf=ADLYWIIP-9VyewlGEt64anUP9S_Wz64-zA:1716900495209&q=lakes+near+ortisei&uds=ADvngMgM3sJHGRUUapkgumPBd1g4rDVC-cBmRg8lBWcSvgmlhn8YofZOlTNYrbbpujgLxYWtNQ7krzsTv3np1uxahqKF7VYs0TJEkrTO2me0gLfW8LzY5SoORh34SQhfBvb-LUB03iaJQTqIg-v73FSdbIgPVXPDs8zqLx5Ac3ldEAf8YFRs1ZIt9H7rOnxgFV1rWoXnBU_yK1dc_9rAjKpWxwjbyNINBW_UPHYn1rlmblSOKMKj6sp5H_emWEf2FyhgI81L1EIwqnhk2PVEsyAe3qdittZsL3QsvKhvfpb2aq4F5GPPqhgAlJA7SJLpi0pD_DjKtWb4&udm=2&prmd=ivnbz&sa=X&ved=2ahUKEwjAh4bhsLCGAxXggP0HHcZqBigQtKgLegQIEBAB&biw=1289&bih=701&dpr=1#vhid=O39cHbk2Zei6vM&vssid=mosaic",
            "time_usec": 1716900665213592,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "lakes near ortisei - Google Search",
            "url": "https://www.google.com/search?sca_esv=d65c73666fce9bae&sxsrf=ADLYWIIP-9VyewlGEt64anUP9S_Wz64-zA:1716900495209&q=lakes+near+ortisei&uds=ADvngMgM3sJHGRUUapkgumPBd1g4rDVC-cBmRg8lBWcSvgmlhn8YofZOlTNYrbbpujgLxYWtNQ7krzsTv3np1uxahqKF7VYs0TJEkrTO2me0gLfW8LzY5SoORh34SQhfBvb-LUB03iaJQTqIg-v73FSdbIgPVXPDs8zqLx5Ac3ldEAf8YFRs1ZIt9H7rOnxgFV1rWoXnBU_yK1dc_9rAjKpWxwjbyNINBW_UPHYn1rlmblSOKMKj6sp5H_emWEf2FyhgI81L1EIwqnhk2PVEsyAe3qdittZsL3QsvKhvfpb2aq4F5GPPqhgAlJA7SJLpi0pD_DjKtWb4&udm=2&prmd=ivnbz&sa=X&ved=2ahUKEwjAh4bhsLCGAxXggP0HHcZqBigQtKgLegQIEBAB&biw=1289&bih=701&dpr=1",
            "time_usec": 1716900652295568,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "lakes near ortisei - Google Search",
            "url": "https://www.google.com/search?q=lakes+near+ortisei&sca_esv=d65c73666fce9bae&sxsrf=ADLYWIKaAk8ftIctS6TZxXEve2pohPS0mg%3A1716900417518&ei=QdJVZqSkH_vm7_UPx5aAyA4&ved=0ahUKEwjkyIC8sLCGAxV787sIHUcLAOkQ4dUDCBA&uact=5&oq=lakes+near+ortisei&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIhJsYWtlcyBuZWFyIG9ydGlzZWkyBRAAGIAEMgYQABgWGB4yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiiBBiLA0jZIVCuBFiHIHABeAGQAQCYAbcBoAHPEKoBBDIuMTa4AQPIAQD4AQGYAhOgApgSqAIPwgIHECMYJxjqAsICFBAAGIAEGOMEGLQCGOkEGOoC2AEBwgIKECMYgAQYJxiKBcICCxAuGIAEGJECGIoFwgILEAAYgAQYkQIYigXCAg4QLhiABBjHARiOBRivAcICBRAuGIAEwgILEC4YgAQY0QMYxwHCAgsQLhiABBjHARivAcICChAAGIAEGEMYigXCAgoQLhiABBhDGIoFwgINEAAYgAQYQxjJAxiKBcICGhAuGIAEGJECGIoFGJcFGNwEGN4EGOAE2AECwgIREC4YgAQYxwEYmAUYmQUYrwHCAgoQABiABBgUGIcCmAMVugYGCAEQARgBugYGCAIQARgUkgcEMS4xOKAHw6EB&sclient=gws-wiz-serp",
            "time_usec": 1716900495946039,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "best hiking from ortisei - Google Search",
            "url": "https://www.google.com/search?q=best+hiking+from+ortisei&sca_esv=d65c73666fce9bae&sxsrf=ADLYWILeKB8WMLiVfX76uyhuIptzA_4c8A%3A1716900287179&ei=v9FVZu63CpiM9u8P5L6xkAo&ved=0ahUKEwiuk-39r7CGAxUYhv0HHWRfDKIQ4dUDCBA&uact=5&oq=best+hiking+from+ortisei&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIhhiZXN0IGhpa2luZyBmcm9tIG9ydGlzZWkyBhAAGBYYHjILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMggQABiABBiiBDILEAAYgAQYogQYiwNI1lVQ8ghY6FNwDHgAkAEAmAGqAaABwByqAQQ3LjI2uAEDyAEA-AEBmAItoALVH6gCCsICBxAjGCcY6gLCAgQQIxgnwgILEAAYgAQYkQIYigXCAgsQLhiABBiRAhiKBcICDRAuGIAEGEMY1AIYigXCAgUQABiABMICBRAuGIAEwgILEC4YgAQY0QMYxwHCAgoQABiABBhDGIoFwgIKEC4YgAQYQxiKBcICEBAuGIAEGNEDGEMYxwEYigXCAhMQLhiABBjRAxhDGMcBGMkDGIoFwgILEAAYgAQYkgMYigXCAgoQIxiABBgnGIoFwgIKEAAYgAQYFBiHAsICBxAAGIAEGArCAgcQIRigARgKwgIGECEYFRgKwgIHEAAYgAQYDcICBhAAGA0YHsICCBAAGAgYDRgewgIIEAAYFhgeGA-YAxHiAwUSATEgQJIHBTE0LjMxoAes8AE&sclient=gws-wiz-serp",
            "time_usec": 1716900418193223,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how to get from florence to san cassiano - Google Search",
            "url": "https://www.google.com/search?q=how+to+get+from+flornce+to+san+cassiano&oq=how+to+get+from+flornce+to+san+cassiano&aqs=chrome..69i64j69i57.16320j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716900288132913,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716900270226111,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how to get from florence to ortisei - Google Search",
            "url": "https://www.google.com/search?q=how+to+get+from+florence+to+ortisei&oq=how+to+get+from+florence+to+ortisei&aqs=chrome..69i64j33i160l2j33i671l7.14450j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716899917859913,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716899900794817,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Residence Lastei, Ortisei \u2013 Updated 2024 Prices",
            "url": "https://www.booking.com/hotel/it/residence-lastei-ortisei.html?aid=318615&label=New_English_EN_IT_26745744865-%2AVSAocZBG_Sbbv4LeMu5FgS640938663104%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-297601666955%3Adsa-135840688825%3Alp1008311%3Ali%3Adec%3Adm%3Aag26745744865%3Acmp393949585&sid=143ad315046fab268076e86c4894838a&all_sr_blocks=63314603_325866634_4_0_0;checkin=2024-06-07;checkout=2024-06-10;dest_id=-123483;dest_type=city;dist=0;group_adults=4;group_children=0;hapos=1;highlighted_blocks=63314603_325866634_4_0_0;hpos=1;map=1;matching_block_id=63314603_325866634_4_0_0;no_rooms=1;req_adults=4;req_children=0;room1=A%2CA%2CA%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=63314603_325866634_4_0_0__60240;srepoch=1716899867;srpvid=cfd358c30aec0315;type=total;ucfs=1&#map_opened-hotel_sidebar_static_map",
            "time_usec": 1716899886374141,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Residence Lastei, Ortisei \u2013 Updated 2024 Prices",
            "url": "https://www.booking.com/hotel/it/residence-lastei-ortisei.html?aid=318615&label=New_English_EN_IT_26745744865-%2AVSAocZBG_Sbbv4LeMu5FgS640938663104%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-297601666955%3Adsa-135840688825%3Alp1008311%3Ali%3Adec%3Adm%3Aag26745744865%3Acmp393949585&sid=143ad315046fab268076e86c4894838a&all_sr_blocks=63314603_325866634_4_0_0;checkin=2024-06-07;checkout=2024-06-10;dest_id=-123483;dest_type=city;dist=0;group_adults=4;group_children=0;hapos=1;highlighted_blocks=63314603_325866634_4_0_0;hpos=1;map=1;matching_block_id=63314603_325866634_4_0_0;no_rooms=1;req_adults=4;req_children=0;room1=A%2CA%2CA%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=63314603_325866634_4_0_0__60240;srepoch=1716899867;srpvid=cfd358c30aec0315;type=total;ucfs=1&#map_closed",
            "time_usec": 1716899874361966,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Residence Lastei, Ortisei \u2013 Updated 2024 Prices",
            "url": "https://www.booking.com/hotel/it/residence-lastei-ortisei.html?aid=318615&label=New_English_EN_IT_26745744865-%2AVSAocZBG_Sbbv4LeMu5FgS640938663104%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-297601666955%3Adsa-135840688825%3Alp1008311%3Ali%3Adec%3Adm%3Aag26745744865%3Acmp393949585&sid=143ad315046fab268076e86c4894838a&all_sr_blocks=63314603_325866634_4_0_0;checkin=2024-06-07;checkout=2024-06-10;dest_id=-123483;dest_type=city;dist=0;group_adults=4;group_children=0;hapos=1;highlighted_blocks=63314603_325866634_4_0_0;hpos=1;map=1;matching_block_id=63314603_325866634_4_0_0;no_rooms=1;req_adults=4;req_children=0;room1=A%2CA%2CA%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=63314603_325866634_4_0_0__60240;srepoch=1716899867;srpvid=cfd358c30aec0315;type=total;ucfs=1&#map_opened-auto_open",
            "time_usec": 1716899872384746,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Residence Lastei, Ortisei \u2013 Updated 2024 Prices",
            "url": "https://www.booking.com/searchresults.html?aid=318615&label=New_English_EN_IT_26745744865-%2AVSAocZBG_Sbbv4LeMu5FgS640938663104%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-297601666955%3Adsa-135840688825%3Alp1008311%3Ali%3Adec%3Adm%3Aag26745744865%3Acmp393949585&sid=143ad315046fab268076e86c4894838a&checkin=2024-06-07&checkout=2024-06-10&dest_id=-123483&dest_type=city&srpvid=cfd358c30aec0315&track_hp_back_button=1#hotel_633146-back",
            "time_usec": 1716899871458665,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Booking.com: Hotels in Ortisei. Book your hotel now!",
            "url": "https://www.booking.com/searchresults.html?aid=318615&label=New_English_EN_IT_26745744865-%2AVSAocZBG_Sbbv4LeMu5FgS640938663104%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-297601666955%3Adsa-135840688825%3Alp1008311%3Ali%3Adec%3Adm%3Aag26745744865%3Acmp393949585&no_rooms=1&srpvid=6eaa58b2d08101e9&highlighted_hotels=633146&checkin=2024-06-07&redirected=1&city=-123483&hlrd=with_av&group_adults=4&source=hotel&group_children=0&checkout=2024-06-10&keep_landing=1&sid=143ad315046fab268076e86c4894838a#hotelTmpl",
            "time_usec": 1716899848252001,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Booking.com: Hotels in Ortisei. Book your hotel now!",
            "url": "https://www.booking.com/searchresults.html?ss=Ortisei&ssne=Ortisei&ssne_untouched=Ortisei&theme_id=7&efdco=1&label=New_English_EN_IT_26745744865-*VSAocZBG_Sbbv4LeMu5FgS640938663104%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-297601666955%3Adsa-135840688825%3Alp1008311%3Ali%3Adec%3Adm%3Aag26745744865%3Acmp393949585&aid=318615&lang=en-us&sb=1&src_elem=sb&src=city&dest_id=-123483&dest_type=city&checkin=2024-06-07&checkout=2024-06-10&group_adults=4&no_rooms=1&group_children=0&sb_travel_purpose=leisure&sb_lp=1",
            "time_usec": 1716899813725684,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "The 10 best cheap hotels in Ortisei, Italy | Booking.com",
            "url": "https://www.booking.com/budget/city/it/ortisei.html?aid=318615;label=New_English_EN_IT_26745744865-*VSAocZBG_Sbbv4LeMu5FgS640938663104:pl:ta:p1:p2:ac:ap:neg:fi:tiaud-297601666955:dsa-135840688825:lp1008311:li:dec:dm:ag26745744865:cmp393949585;ws=&gclid=CjwKCAjwgdayBhBQEiwAXhMxtp4v4OzcolVq6k6e9P82Yi3jnkBwWf4EJzT4RNTBsQQ_3RQO1jdWOBoC69wQAvD_BwE",
            "time_usec": 1716899775939391,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "ortisei hostels for backpackers - Google Search",
            "url": "https://www.google.com/search?q=ortisei+hostels+for+backpackers&oq=ortisei+hostels+for+backpackers&aqs=chrome..69i64j69i57.8679j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716899768498986,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716899758277794,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "best day hikes in the italian alps - Google Search",
            "url": "https://www.google.com/search?q=best+day+hikes+in+the+italian+alps+&sca_esv=d65c73666fce9bae&biw=1289&bih=701&sxsrf=ADLYWIJ1CL94yCuZ1h2NAKDoR6OHl2QX1A%3A1716899325800&ei=_c1VZp66MKyA9u8P7qey2Ac&ved=0ahUKEwjerLezrLCGAxUsgP0HHe6TDHsQ4dUDCBA&uact=5&oq=best+day+hikes+in+the+italian+alps+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIiNiZXN0IGRheSBoaWtlcyBpbiB0aGUgaXRhbGlhbiBhbHBzIDIGEAAYFhgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGKIEGIsDSP87UIILWL07cAV4AZABAJgBvwGgAa0fqgEFMTIuMjS4AQPIAQD4AQGYAimgAuoiwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigXCAg4QABiwAxjkAhjWBNgBAcICExAuGIAEGLADGEMYyAMYigXYAQLCAgQQIxgnwgIKECMYgAQYJxiKBcICCxAuGIAEGJECGIoFwgIFEAAYgATCAgsQLhiABBjRAxjHAcICBRAuGIAEwgIQEC4YgAQYQxjHARiKBRivAcICCxAAGIAEGJECGIoFwgILEAAYgAQYkgMYigXCAggQABiABBjJA8ICChAAGIAEGBQYhwLCAg4QABiABBiGAxiKBRiLA5gDAIgGAZAGE7oGBggBEAEYCboGBggCEAEYCJIHBTEwLjMxoAfthQI&sclient=gws-wiz-serp",
            "time_usec": 1716899589515773,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "italian alps - Google Search",
            "url": "https://www.google.com/search?sca_esv=d65c73666fce9bae&sxsrf=ADLYWIKQl7q2YMMD9XZ5VDpoQzzzQRA2gA:1716899317605&q=italian+alps&source=lnms&uds=ADvngMiYRgkE3CWJnTkzafKEyekl16LSnnHZ1rxX_2okigdZKy9SwljXSV0DOm-3MWeTBIwysI8wzeFrrwbHYzA1fBCleIK-eZDzIxXD2kWrI8D-pj4gHEvyYHiLZmhsYGeB8Uc2lL08n4GrZJFTh43hq8X6FKdmj9SDSnKZkICb5iITzOEba0JPjfU1PfzuxmpdPyooxxbXyrnwbWkjze30xEUkTbZ9BABiE3gpa1OOgTX24ZCWAyuLcu97LfrrgMvJq3FInwqXMe7-m4fNIjiT3UjkulVcPw&sa=X&ved=2ahUKEwiK5MKvrLCGAxWsg_0HHdmqCXMQ0pQJegQIERAB&biw=1289&bih=701&dpr=1",
            "time_usec": 1716899580694092,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "italian alps - Google Search",
            "url": "https://www.google.com/search?sca_esv=d65c73666fce9bae&sxsrf=ADLYWIKQl7q2YMMD9XZ5VDpoQzzzQRA2gA:1716899317605&q=italian+alps&source=lnms&uds=ADvngMiYRgkE3CWJnTkzafKEyekl16LSnnHZ1rxX_2okigdZKy9SwljXSV0DOm-3MWeTBIwysI8wzeFrrwbHYzA1fBCleIK-eZDzIxXD2kWrI8D-pj4gHEvyYHiLZmhsYGeB8Uc2lL08n4GrZJFTh43hq8X6FKdmj9SDSnKZkICb5iITzOEba0JPjfU1PfzuxmpdPyooxxbXyrnwbWkjze30xEUkTbZ9BABiE3gpa1OOgTX24ZCWAyuLcu97LfrrgMvJq3FInwqXMe7-m4fNIjiT3UjkulVcPw&sa=X&ved=2ahUKEwiK5MKvrLCGAxWsg_0HHdmqCXMQ0pQJegQIERAB&biw=1289&bih=701&dpr=1",
            "time_usec": 1716899577556390,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "THE 10 BEST Italian Alps Mountains to Visit (Updated 2024)",
            "url": "https://www.tripadvisor.com/Attractions-g2324485-Activities-c57-t66-Italian_Alps.html",
            "time_usec": 1716899574821816,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "THE 10 BEST Italian Alps Mountains to Visit (Updated 2024)",
            "url": "https://www.tripadvisor.com/Attractions-g2324485-Activities-c57-t66-Italian_Alps.html",
            "time_usec": 1716899565623630,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "THE 10 BEST Italian Alps Mountains to Visit (Updated 2024)",
            "url": "https://www.tripadvisor.com/Attractions-g2324485-Activities-c57-t66-Italian_Alps.html",
            "time_usec": 1716899548607092,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "italian alps - Google Search",
            "url": "https://www.google.com/search?sca_esv=d65c73666fce9bae&sxsrf=ADLYWIKQl7q2YMMD9XZ5VDpoQzzzQRA2gA:1716899317605&q=italian+alps&source=lnms&uds=ADvngMiYRgkE3CWJnTkzafKEyekl16LSnnHZ1rxX_2okigdZKy9SwljXSV0DOm-3MWeTBIwysI8wzeFrrwbHYzA1fBCleIK-eZDzIxXD2kWrI8D-pj4gHEvyYHiLZmhsYGeB8Uc2lL08n4GrZJFTh43hq8X6FKdmj9SDSnKZkICb5iITzOEba0JPjfU1PfzuxmpdPyooxxbXyrnwbWkjze30xEUkTbZ9BABiE3gpa1OOgTX24ZCWAyuLcu97LfrrgMvJq3FInwqXMe7-m4fNIjiT3UjkulVcPw&sa=X&ved=2ahUKEwiK5MKvrLCGAxWsg_0HHdmqCXMQ0pQJegQIERAB&biw=1289&bih=701&dpr=1",
            "time_usec": 1716899347294348,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://anywhereweroam.com/italian-alps/",
            "time_usec": 1716899342474406,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "italian alps - Google Search",
            "url": "https://www.google.com/search?sca_esv=d65c73666fce9bae&sxsrf=ADLYWIKQl7q2YMMD9XZ5VDpoQzzzQRA2gA:1716899317605&q=italian+alps&source=lnms&uds=ADvngMiYRgkE3CWJnTkzafKEyekl16LSnnHZ1rxX_2okigdZKy9SwljXSV0DOm-3MWeTBIwysI8wzeFrrwbHYzA1fBCleIK-eZDzIxXD2kWrI8D-pj4gHEvyYHiLZmhsYGeB8Uc2lL08n4GrZJFTh43hq8X6FKdmj9SDSnKZkICb5iITzOEba0JPjfU1PfzuxmpdPyooxxbXyrnwbWkjze30xEUkTbZ9BABiE3gpa1OOgTX24ZCWAyuLcu97LfrrgMvJq3FInwqXMe7-m4fNIjiT3UjkulVcPw&sa=X&ved=2ahUKEwiK5MKvrLCGAxWsg_0HHdmqCXMQ0pQJegQIERAB&biw=1289&bih=701&dpr=1",
            "time_usec": 1716899329766593,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "italian alps - Google Search",
            "url": "https://www.google.com/search?sca_esv=d65c73666fce9bae&sxsrf=ADLYWIKQl7q2YMMD9XZ5VDpoQzzzQRA2gA:1716899317605&q=italian+alps&source=lnms&uds=ADvngMiYRgkE3CWJnTkzafKEyekl16LSnnHZ1rxX_2okigdZKy9SwljXSV0DOm-3MWeTBIwysI8wzeFrrwbHYzA1fBCleIK-eZDzIxXD2kWrI8D-pj4gHEvyYHiLZmhsYGeB8Uc2lL08n4GrZJFTh43hq8X6FKdmj9SDSnKZkICb5iITzOEba0JPjfU1PfzuxmpdPyooxxbXyrnwbWkjze30xEUkTbZ9BABiE3gpa1OOgTX24ZCWAyuLcu97LfrrgMvJq3FInwqXMe7-m4fNIjiT3UjkulVcPw&sa=X&ved=2ahUKEwiK5MKvrLCGAxWsg_0HHdmqCXMQ0pQJegQIERAB&biw=1289&bih=701&dpr=1",
            "time_usec": 1716899326788837,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "italian alps - Google Search",
            "url": "https://www.google.com/search?q=italian+alps&sca_esv=d65c73666fce9bae&udm=2&biw=1289&bih=701&sxsrf=ADLYWIKqT983vZMrRHB4EUXUJl_yN00Rgg%3A1716899244028&ei=rM1VZsGeAcqM9u8Pquy5-Ag&ved=0ahUKEwjBpLiMrLCGAxVKhv0HHSp2Do8Q4dUDCBA&uact=5&oq=italian+alps&gs_lp=Egxnd3Mtd2l6LXNlcnAiDGl0YWxpYW4gYWxwczIFEAAYgAQyBRAAGIAEMgoQABiABBhDGIoFMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEjtI1DsEljDInABeACQAQCYAWagAZ8IqgEEMTEuMbgBA8gBAPgBAZgCDaAChAmoAgrCAgcQIxgnGOoCwgIEECMYJ5gDEJIHAzkuNKAHoT0&sclient=gws-wiz-serp",
            "time_usec": 1716899318628077,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "northern italy towns - Google Search",
            "url": "https://www.google.com/search?q=northern+italy+towns+&sca_esv=d65c73666fce9bae&udm=2&biw=1289&bih=701&sxsrf=ADLYWIIo8qC9JySqa_Ca8ke11eJtKxaI9w%3A1716899096056&ei=GM1VZrDxAuj87_UPgJaaiAs&ved=0ahUKEwiw3fDFq7CGAxVo_rsIHQCLBrEQ4dUDCBA&uact=5&oq=northern+italy+towns+&gs_lp=Egxnd3Mtd2l6LXNlcnAiFW5vcnRoZXJuIGl0YWx5IHRvd25zIDIFEAAYgAQyBhAAGAUYHjIGEAAYBRgeMgYQABgIGB4yBhAAGAgYHjIHEAAYgAQYGEjDUlC1CVjfUHAPeACQAQCYAYgCoAHGHqoBBzIxLjEwLjO4AQPIAQD4AQGYAi6gAvcfqAIKwgIHECMYJxjqAsICBBAjGCfCAgoQABiABBhDGIoFwgIJEAAYgAQYGBgKmAMMkgcHMjkuMTQuM6AH7qEB&sclient=gws-wiz-serp#vhid=bLRCQYpB801W-M&vssid=mosaic",
            "time_usec": 1716899300961316,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "northern italy towns - Google Search",
            "url": "https://www.google.com/search?q=northern+italy+towns+&sca_esv=d65c73666fce9bae&udm=2&biw=1289&bih=701&sxsrf=ADLYWIIo8qC9JySqa_Ca8ke11eJtKxaI9w%3A1716899096056&ei=GM1VZrDxAuj87_UPgJaaiAs&ved=0ahUKEwiw3fDFq7CGAxVo_rsIHQCLBrEQ4dUDCBA&uact=5&oq=northern+italy+towns+&gs_lp=Egxnd3Mtd2l6LXNlcnAiFW5vcnRoZXJuIGl0YWx5IHRvd25zIDIFEAAYgAQyBhAAGAUYHjIGEAAYBRgeMgYQABgIGB4yBhAAGAgYHjIHEAAYgAQYGEjDUlC1CVjfUHAPeACQAQCYAYgCoAHGHqoBBzIxLjEwLjO4AQPIAQD4AQGYAi6gAvcfqAIKwgIHECMYJxjqAsICBBAjGCfCAgoQABiABBhDGIoFwgIJEAAYgAQYGBgKmAMMkgcHMjkuMTQuM6AH7qEB&sclient=gws-wiz-serp#imgrc=lu2YLlzq2RKKOM&imgdii=yfzYBh0B1dLYKM",
            "time_usec": 1716899262489416,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "northern italy towns - Google Search",
            "url": "https://www.google.com/search?q=northern+italy+towns+&sca_esv=d65c73666fce9bae&udm=2&biw=1289&bih=701&sxsrf=ADLYWIIo8qC9JySqa_Ca8ke11eJtKxaI9w%3A1716899096056&ei=GM1VZrDxAuj87_UPgJaaiAs&ved=0ahUKEwiw3fDFq7CGAxVo_rsIHQCLBrEQ4dUDCBA&uact=5&oq=northern+italy+towns+&gs_lp=Egxnd3Mtd2l6LXNlcnAiFW5vcnRoZXJuIGl0YWx5IHRvd25zIDIFEAAYgAQyBhAAGAUYHjIGEAAYBRgeMgYQABgIGB4yBhAAGAgYHjIHEAAYgAQYGEjDUlC1CVjfUHAPeACQAQCYAYgCoAHGHqoBBzIxLjEwLjO4AQPIAQD4AQGYAi6gAvcfqAIKwgIHECMYJxjqAsICBBAjGCfCAgoQABiABBhDGIoFwgIJEAAYgAQYGBgKmAMMkgcHMjkuMTQuM6AH7qEB&sclient=gws-wiz-serp#imgrc=huZYxL-Jj-XvTM&imgdii=lu2YLlzq2RKKOM",
            "time_usec": 1716899262479392,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "northern italy towns - Google Search",
            "url": "https://www.google.com/search?q=northern+italy+towns+&sca_esv=d65c73666fce9bae&udm=2&biw=1289&bih=701&sxsrf=ADLYWIIo8qC9JySqa_Ca8ke11eJtKxaI9w%3A1716899096056&ei=GM1VZrDxAuj87_UPgJaaiAs&ved=0ahUKEwiw3fDFq7CGAxVo_rsIHQCLBrEQ4dUDCBA&uact=5&oq=northern+italy+towns+&gs_lp=Egxnd3Mtd2l6LXNlcnAiFW5vcnRoZXJuIGl0YWx5IHRvd25zIDIFEAAYgAQyBhAAGAUYHjIGEAAYBRgeMgYQABgIGB4yBhAAGAgYHjIHEAAYgAQYGEjDUlC1CVjfUHAPeACQAQCYAYgCoAHGHqoBBzIxLjEwLjO4AQPIAQD4AQGYAi6gAvcfqAIKwgIHECMYJxjqAsICBBAjGCfCAgoQABiABBhDGIoFwgIJEAAYgAQYGBgKmAMMkgcHMjkuMTQuM6AH7qEB&sclient=gws-wiz-serp#vhid=huZYxL-Jj-XvTM&vssid=mosaic",
            "time_usec": 1716899257927729,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "northern italy towns - Google Search",
            "url": "https://www.google.com/search?q=northern+italy+towns+&sca_esv=d65c73666fce9bae&udm=2&biw=1289&bih=701&sxsrf=ADLYWIIo8qC9JySqa_Ca8ke11eJtKxaI9w%3A1716899096056&ei=GM1VZrDxAuj87_UPgJaaiAs&ved=0ahUKEwiw3fDFq7CGAxVo_rsIHQCLBrEQ4dUDCBA&uact=5&oq=northern+italy+towns+&gs_lp=Egxnd3Mtd2l6LXNlcnAiFW5vcnRoZXJuIGl0YWx5IHRvd25zIDIFEAAYgAQyBhAAGAUYHjIGEAAYBRgeMgYQABgIGB4yBhAAGAgYHjIHEAAYgAQYGEjDUlC1CVjfUHAPeACQAQCYAYgCoAHGHqoBBzIxLjEwLjO4AQPIAQD4AQGYAi6gAvcfqAIKwgIHECMYJxjqAsICBBAjGCfCAgoQABiABBhDGIoFwgIJEAAYgAQYGBgKmAMMkgcHMjkuMTQuM6AH7qEB&sclient=gws-wiz-serp",
            "time_usec": 1716899245661635,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "gucci north face - Google Search",
            "url": "https://www.google.com/search?sca_esv=d65c73666fce9bae&sxsrf=ADLYWIJg6MD8w-Rg_v-pUa3X9fQ2Fn8skw:1716899072417&q=gucci+north+face&uds=ADvngMhXvLAy9adNrmazH6IkPBchM2IVXZLozfPSoGqtRgwCnr91x51qbpLLTfXj3RZlVlHRQLcxIIAGfrX9MndRAM0-qtABEl3R0shaOGH4yQv-FxbuUC8quwuq5HmMGbCbNwInt9mDK1l8yHb-5Vm7yoTfsnD3iJrEYCd-EZOUq8QGymtLlyKAlc99arUKbUUcbANqi0A9E7DSEHZm74z8k85xvPNoEwDJnd0_X9G_Og_SYqaVVx-AzUfMbPqTPnl-JfoKsS8IR_yCA6tNM5TJ9Qq8w08SmKfeXN6nji9O4l4hSb1KkL7w7EtM2RP6tcWFqEQjr6i7&udm=2&prmd=ivnbz&sa=X&ved=2ahUKEwi_-M26q7CGAxXq77sIHZZuBSMQtKgLegQIEhAB&biw=1289&bih=701&dpr=1",
            "time_usec": 1716899108072081,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "gucci north face - Google Search",
            "url": "https://www.google.com/search?sca_esv=d65c73666fce9bae&sxsrf=ADLYWIJg6MD8w-Rg_v-pUa3X9fQ2Fn8skw:1716899072417&q=gucci+north+face&uds=ADvngMhXvLAy9adNrmazH6IkPBchM2IVXZLozfPSoGqtRgwCnr91x51qbpLLTfXj3RZlVlHRQLcxIIAGfrX9MndRAM0-qtABEl3R0shaOGH4yQv-FxbuUC8quwuq5HmMGbCbNwInt9mDK1l8yHb-5Vm7yoTfsnD3iJrEYCd-EZOUq8QGymtLlyKAlc99arUKbUUcbANqi0A9E7DSEHZm74z8k85xvPNoEwDJnd0_X9G_Og_SYqaVVx-AzUfMbPqTPnl-JfoKsS8IR_yCA6tNM5TJ9Qq8w08SmKfeXN6nji9O4l4hSb1KkL7w7EtM2RP6tcWFqEQjr6i7&udm=2&prmd=ivnbz&sa=X&ved=2ahUKEwi_-M26q7CGAxXq77sIHZZuBSMQtKgLegQIEhAB&biw=1289&bih=701&dpr=1#vhid=SUu7EIA-s4bA4M&vssid=mosaic",
            "time_usec": 1716899100195930,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "gucci north face - Google Search",
            "url": "https://www.google.com/search?sca_esv=d65c73666fce9bae&sxsrf=ADLYWIJg6MD8w-Rg_v-pUa3X9fQ2Fn8skw:1716899072417&q=gucci+north+face&uds=ADvngMhXvLAy9adNrmazH6IkPBchM2IVXZLozfPSoGqtRgwCnr91x51qbpLLTfXj3RZlVlHRQLcxIIAGfrX9MndRAM0-qtABEl3R0shaOGH4yQv-FxbuUC8quwuq5HmMGbCbNwInt9mDK1l8yHb-5Vm7yoTfsnD3iJrEYCd-EZOUq8QGymtLlyKAlc99arUKbUUcbANqi0A9E7DSEHZm74z8k85xvPNoEwDJnd0_X9G_Og_SYqaVVx-AzUfMbPqTPnl-JfoKsS8IR_yCA6tNM5TJ9Qq8w08SmKfeXN6nji9O4l4hSb1KkL7w7EtM2RP6tcWFqEQjr6i7&udm=2&prmd=ivnbz&sa=X&ved=2ahUKEwi_-M26q7CGAxXq77sIHZZuBSMQtKgLegQIEhAB&biw=1289&bih=701&dpr=1",
            "time_usec": 1716899097336708,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "gucci north face - Google Search",
            "url": "https://www.google.com/search?q=gucci+north+fce+&sca_esv=d65c73666fce9bae&sxsrf=ADLYWIIsBPyw-_SA0VXLAE_eL_TbEJzXmQ%3A1716897730374&ei=wsdVZuapFoaG9u8P4cmDiA0&ved=0ahUKEwjmkta6prCGAxUGg_0HHeHkANEQ4dUDCBA&uact=5&oq=gucci+north+fce+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIhBndWNjaSBub3J0aCBmY2UgMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNMgcQABiABBgNSPckUIQHWLkjcAF4AZABAJgBpAGgAZoOqgEENi4xMLgBA8gBAPgBAZgCEaACzQ-oAhTCAgcQIxgnGOoCwgITEAAYgAQYQxi0AhiKBRjqAtgBAcICChAAGIAEGEMYigXCAhAQLhiABBjRAxhDGMcBGIoFwgIFEAAYgATCAgQQIxgnwgIOEC4YgAQYxwEYjgUYrwHCAgsQLhiABBjRAxjHAcICBRAuGIAEwgIUEC4YgAQYkQIY0QMYxwEYyQMYigXCAgsQABiABBiRAhiKBcICCBAAGIAEGJIDwgILEAAYgAQYkgMYigXCAiMQLhiABBiRAhjRAxjHARjJAxiKBRiXBRjcBBjeBBjgBNgBAsICCBAAGIAEGMkDwgILEC4YgAQYxwEYrwHCAggQABgWGAoYHsICCxAAGIAEGIYDGIoFwgILEAAYgAQYogQYiwOYAxS6BgYIARABGAG6BgYIAhABGBSSBwQzLjE0oAeOjgE&sclient=gws-wiz-serp",
            "time_usec": 1716899074047482,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "adobe photoshop - Google Search",
            "url": "https://www.google.com/search?q=adobe+photoshop&sca_esv=d65c73666fce9bae&sxsrf=ADLYWIIPh0hIq2vbSiwDLtdg97ELYq5BPg%3A1716897723482&source=hp&ei=u8dVZqOpGbSG9u8P_6S2sAo&iflsig=AL9hbdgAAAAAZlXVy4v166Rvg_4FCPEl7AGdusT4SSVV&ved=0ahUKEwjj8q23prCGAxU0g_0HHX-SDaYQ4dUDCBU&uact=5&oq=adobe+photoshop&gs_lp=Egdnd3Mtd2l6Ig9hZG9iZSBwaG90b3Nob3AyChAAGIAEGEMYigUyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARIwBVQAFjgE3AAeACQAQCYAY4CoAHOGKoBBTAuNi45uAEDyAEA-AEBmAIPoAK-GcICBBAjGCfCAgoQIxiABBgnGIoFwgIREC4YgAQYkQIY0QMYxwEYigXCAgsQLhiABBjRAxjHAcICBRAuGIAEwgIQEC4YgAQY0QMYQxjHARiKBcICCxAAGIAEGJECGIoFwgIKEC4YgAQYQxiKBZgDAJIHBTAuNi45oAfVZw&sclient=gws-wiz",
            "time_usec": 1716897732486037,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google",
            "url": "https://www.google.com/",
            "time_usec": 1716897723963079,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google",
            "url": "https://www.google.com/",
            "time_usec": 1716897723614960,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716897718075022,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "does h and m own weekday - Google Search",
            "url": "https://www.google.com/search?q=does+h+and+m+own+weekday&sca_esv=d65c73666fce9bae&sxsrf=ADLYWIK2XEqoH1n30EFcG1resxgcLjJ_UQ%3A1716897428116&ei=lMZVZuDBBvL_7_UP346E6AM&ved=0ahUKEwjg28WqpbCGAxXy_7sIHV8HAT0Q4dUDCBA&uact=5&oq=does+h+and+m+own+weekday&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIhhkb2VzIGggYW5kIG0gb3duIHdlZWtkYXkyBhAAGBYYHjILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBUjTa1CcQ1j8anABeACQAQCYAeABoAHyFKoBBjMuMTkuMbgBA8gBAPgBAZgCGKACwBaoAhHCAgcQIxgnGOoCwgITEAAYgAQYQxi0AhiKBRjqAtgBAcICHBAuGIAEGNEDGEMYtAIYxwEYyAMYigUY6gLYAQLCAgoQIxiABBgnGIoFwgIEECMYJ8ICCxAAGIAEGJECGIoFwgIFEAAYgATCAg4QLhiABBjHARiOBRivAcICCBAuGIAEGNQCwgILEC4YgAQY0QMYxwHCAgUQLhiABMICCBAAGIAEGKIEwgILEAAYgAQYogQYiwOYAxW6BgYIARABGAG6BgYIAhABGAiSBwYyLjIxLjGgB-eqAQ&sclient=gws-wiz-serp",
            "time_usec": 1716897608609157,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "mud jeans - Google Search",
            "url": "https://www.google.com/search?q=mud+jeans&oq=mud+jeans&aqs=chrome..69i64j46i199i465i512j0i22i30l8.4884j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716897472127811,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://mudjeans.com/",
            "time_usec": 1716897468610072,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "mud jeans - Google Search",
            "url": "https://www.google.com/search?q=mud+jeans&oq=mud+jeans&aqs=chrome..69i64j46i199i465i512j0i22i30l8.4884j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716897429948547,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716897421178305,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.nytimes.com/games-assets/v2/assets/connections/NYT-Connections-Icon.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Connections - The New York Times - The New York Times",
            "url": "https://www.nytimes.com/games/connections",
            "time_usec": 1716896878572191,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "connections - Google Search",
            "url": "https://www.google.com/search?q=connections&sca_esv=8870e14de2d74e2a&sxsrf=ADLYWIK_BcuaJYXPws66VLTzWJjGUI51fQ%3A1716813432214&ei=eH5UZqvbDKjbi-gP9My9YA&ved=0ahUKEwir95a27K2GAxWo7QIHHXRmDwwQ4dUDCBA&uact=5&oq=connections&gs_lp=Egxnd3Mtd2l6LXNlcnAiC2Nvbm5lY3Rpb25zMgoQIxiABBgnGIoFMgoQLhiABBhDGIoFMgUQABiABDIIEC4YgAQY1AIyBRAAGIAEMgUQLhiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyGRAuGIAEGEMYigUYlwUY3AQY3gQY4ATYAQNI2S1QvB9Y_ixwAXgAkAEAmAGbAaAB0wmqAQMxLjm4AQPIAQD4AQGYAgugAuwKqAIRwgIHECMYJxjqAsICExAAGIAEGEMYtAIYigUY6gLYAQHCAhwQLhiABBjRAxhDGLQCGMcBGMgDGIoFGOoC2AECwgILEAAYgAQYkQIYigXCAgoQABiABBhDGIoFwgILEC4YgAQY0QMYxwHCAhAQLhiABBjRAxhDGMcBGIoFmAMh4gMFEgExIEC6BgYIARABGAG6BgYIAhABGAi6BgYIAxABGBSSBwQxLjEwoAemhQE&sclient=gws-wiz-serp",
            "time_usec": 1716896864840222,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "signe drapy maxi skirt - Dark Blue | Weekday EU",
            "url": "https://www.weekday.com/en-eu/p/women/skirts/maxi/signe-drapy-maxi-skirt-dark-blue-1155504007/",
            "time_usec": 1716896703528483,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "signe drapy maxi skirt - Dark Beige | Weekday EU",
            "url": "https://www.weekday.com/en-eu/p/women/skirts/maxi/signe-drapy-maxi-skirt-dark-beige-1155504006/",
            "time_usec": 1716896699277406,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "signe drapy maxi skirt - Black | Weekday EU",
            "url": "https://www.weekday.com/en-eu/p/women/skirts/maxi/signe-drapy-maxi-skirt-black-001/",
            "time_usec": 1716896693986556,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Women's Clothing | Shop Womenswear & Fashion Online",
            "url": "https://www.weekday.com/en-eu/c/women/",
            "time_usec": 1716896679788241,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.notion.so/images/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Lecture notes",
            "url": "https://www.notion.so/Lecture-notes-19cbffba2cf8473a8d00cc4ad94766c3",
            "time_usec": 1716896485984460,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.notion.so/images/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Notion - Log in",
            "url": "https://www.notion.so/",
            "time_usec": 1716896484966241,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.notion.so/images/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Notion - Log in",
            "url": "https://www.notion.so/oauth2callback?state=eyJjYWxsYmFja1R5cGUiOiJwb3B1cCIsImVuY3J5cHRlZFRva2VuIjoidjAyOmxvZ2luX3dpdGhfZ29vZ2xlOnM5eVN3NEM1UF9wRGNMV3lGVmJSNkF1Ull0ZnBhOUZGcVNaNzBjU2dLRkpCN3lrTHdEWmV4aFVRNzcwNy1qMGRxZ0lVejl6djlwNE9GOTVCLXRJblVkUmtuYllPVGFteW9ETlctQks5QzBfV3NROE1jRXVvYW5jU2FZNGRTQnBFLUdWNiJ9&code=4%2F0AdLIrYfB4B0okZt6WbtXb2URdaolyhY2YWNTAQSU0BdDS0RcGTYfDldMtYS5Gh9oa_kqNQ&scope=email+profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+openid&authuser=0&prompt=none",
            "time_usec": 1716896483554780,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "https://www.notion.so/googlepopupcallback?state=eyJjYWxsYmFja1R5cGUiOiJwb3B1cCIsImVuY3J5cHRlZFRva2VuIjoidjAyOmxvZ2luX3dpdGhfZ29vZ2xlOnM5eVN3NEM1UF9wRGNMV3lGVmJSNkF1Ull0ZnBhOUZGcVNaNzBjU2dLRkpCN3lrTHdEWmV4aFVRNzcwNy1qMGRxZ0lVejl6djlwNE9GOTVCLXRJblVkUmtuYllPVGFteW9ETlctQks5QzBfV3NROE1jRXVvYW5jU2FZNGRTQnBFLUdWNiJ9&code=4%2F0AdLIrYfB4B0okZt6WbtXb2URdaolyhY2YWNTAQSU0BdDS0RcGTYfDldMtYS5Gh9oa_kqNQ&scope=email+profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+openid&authuser=0&prompt=none",
            "time_usec": 1716896483518206,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign in - Google Accounts",
            "url": "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?access_type=offline&scope=profile%20email%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile&state=eyJjYWxsYmFja1R5cGUiOiJwb3B1cCIsImVuY3J5cHRlZFRva2VuIjoidjAyOmxvZ2luX3dpdGhfZ29vZ2xlOnM5eVN3NEM1UF9wRGNMV3lGVmJSNkF1Ull0ZnBhOUZGcVNaNzBjU2dLRkpCN3lrTHdEWmV4aFVRNzcwNy1qMGRxZ0lVejl6djlwNE9GOTVCLXRJblVkUmtuYllPVGFteW9ETlctQks5QzBfV3NROE1jRXVvYW5jU2FZNGRTQnBFLUdWNiJ9&prompt=select_account&response_type=code&client_id=905154081809-858sm3f0qnalqd9d44d9gecjtrdji9tf.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fwww.notion.so%2Fgooglepopupcallback&service=lso&o2v=2&ddm=0&flowName=GeneralOAuthFlow",
            "time_usec": 1716896481454597,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.notion.so/images/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Notion - Log in",
            "url": "https://www.notion.so/login",
            "time_usec": 1716896477787084,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.notion.so/front-static/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Your connected workspace for wiki, docs & projects | Notion",
            "url": "https://www.notion.so/product?utm_source=affl&utm_medium=katychmela3457&pscd=affiliate.notion.so&ps_partner_key=a2F0eWNobWVsYTM0NTc&ps_xid=CkXBwdkahCMaVG&gsxid=CkXBwdkahCMaVG&gspk=a2F0eWNobWVsYTM0NTc&gad_source=1&gclid=CjwKCAjwgdayBhBQEiwAXhMxtr07K8-t_0zAeuexG7wOq9sevnZAvs15DF8JsmbwvrlKR6oWgbHnAxoClGEQAvD_BwE",
            "time_usec": 1716896459030495,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "notion - Google Search",
            "url": "https://www.google.com/search?q=notion&oq=notion&aqs=chrome..69i64j0i433i512l3j0i131i433i512j0i433i512l2j5.7465j0j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716896449963002,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_45",
            "time_usec": 1716896418771433,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.ge77270587f_0_1636",
            "time_usec": 1716896417002504,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_80",
            "time_usec": 1716896399460157,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_71",
            "time_usec": 1716896369743737,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_71",
            "time_usec": 1716896352286267,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.ge77270587f_0_1636",
            "time_usec": 1716896339218045,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "rail mid loose straight jeans - Trove Blue | Weekday EU",
            "url": "https://www.weekday.com/en-eu/p/women/jeans/rail/rail-mid-loose-straight-jeans-trove-blue-0885676036/",
            "time_usec": 1716813612389960,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "rail mid loose straight jeans - Clay Grey | Weekday EU",
            "url": "https://www.weekday.com/en-eu/p/women/jeans/loose-fit/rail-mid-loose-straight-jeans-clay-grey-039/",
            "time_usec": 1716813606899551,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "rail mid loose straight jeans - Jackpot Blue | Weekday EU",
            "url": "https://www.weekday.com/en-eu/p/women/jeans/rail/rail-mid-loose-straight-jeans-jackpot-blue-035/",
            "time_usec": 1716813578105304,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "rail mid loose straight jeans - Tide Blue | Weekday EU",
            "url": "https://www.weekday.com/en-eu/p/women/jeans/rail/rail-mid-loose-straight-jeans-tide-blue-0885676045/",
            "time_usec": 1716813570130919,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "ample low loose jeans - Ice Blue | Weekday EU",
            "url": "https://www.weekday.com/en-eu/p/women/jeans/ample/ample-low-loose-jeans-ice-blue-1090322022/",
            "time_usec": 1716813559945092,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "ample low loose jeans - Treasure Blue | Weekday EU",
            "url": "https://www.weekday.com/en-eu/p/women/jeans/ample/ample-low-loose-jeans-treasure-blue-007/",
            "time_usec": 1716813553512381,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "ample low loose jeans - Sapphire blue | Weekday EU",
            "url": "https://www.weekday.com/en-eu/p/women/jeans/loose-fit/ample-low-loose-jeans-sapphire-blue-1090322020/",
            "time_usec": 1716813502511111,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Women's Jeans - Shop Women's Jeans Online",
            "url": "https://www.weekday.com/en-eu/c/women/jeans/",
            "time_usec": 1716813485861477,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "what is the value for customersof the brand weekday - Google Search",
            "url": "https://www.google.com/search?q=what+is+the+value+for+customersof+the+brand+weekday&oq=what+is+the+value+for+customersof+the+brand+weekday+&aqs=chrome..69i64j0i512i546l3j0i395i512i546l2j69i57.15381j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716813432869178,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716813415701616,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_71",
            "time_usec": 1716813095236051,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Supply chain",
            "url": "https://www.weekday.com/en-eu/responsibility/supply-chain/",
            "time_usec": 1716812930057756,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g2e072932187_0_53",
            "time_usec": 1716812918469619,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_47",
            "time_usec": 1716812910322630,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g2e072932187_0_53",
            "time_usec": 1716812891750414,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_80",
            "time_usec": 1716812882355099,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g2e072932187_0_9",
            "time_usec": 1716812810856954,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_80",
            "time_usec": 1716812684920784,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_80",
            "time_usec": 1716812648234775,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_47",
            "time_usec": 1716812603510038,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_111",
            "time_usec": 1716812588224074,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g2e072932187_0_9",
            "time_usec": 1716812358476865,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_111",
            "time_usec": 1716812313450364,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_80",
            "time_usec": 1716812294128947,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g2e072932187_0_9",
            "time_usec": 1716812003260913,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g2e072932187_0_9",
            "time_usec": 1716811863717648,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_111",
            "time_usec": 1716811851091415,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "where to get tattoos in florence - Google Search",
            "url": "https://www.google.com/search?q=where+to+get+tattoos+in+flronece&oq=where+to+get+tattoos+in+flronece&aqs=chrome..69i64j69i57.8439j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716811670953865,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716811661269548,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_80",
            "time_usec": 1716811595773243,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inclusion and diversity",
            "url": "https://www.weekday.com/en-eu/responsibility/inclusion-and-diversity/",
            "time_usec": 1716811593168221,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_47",
            "time_usec": 1716811081345996,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_80",
            "time_usec": 1716811074415565,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_80",
            "time_usec": 1716811012043961,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Responsibility",
            "url": "https://www.weekday.com/en-eu/responsibility/",
            "time_usec": 1716810987883635,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_80",
            "time_usec": 1716810980232229,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.ge77270587f_0_11",
            "time_usec": 1716810972960727,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g2e0550065d7_0_3",
            "time_usec": 1716810961598019,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_111",
            "time_usec": 1716810882910307,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_63",
            "time_usec": 1716810874123632,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_111",
            "time_usec": 1716810775367722,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_80",
            "time_usec": 1716810739710895,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hand foot and mouth disease - Google Search",
            "url": "https://www.google.com/search?q=hand+foot+and+mouth+disease&oq=hand+foot+and+mouth+disease&aqs=chrome..69i64j0i512l4j0i22i30l5.10206j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716810325896540,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716810314440867,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_111",
            "time_usec": 1716810102003744,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_80",
            "time_usec": 1716810044805508,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_47",
            "time_usec": 1716810026161047,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.ge77270587f_0_11",
            "time_usec": 1716809995064367,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Supply chain",
            "url": "https://www.weekday.com/en-eu/responsibility/supply-chain/",
            "time_usec": 1716809726488697,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Responsibility",
            "url": "https://www.weekday.com/en-eu/responsibility/",
            "time_usec": 1716809723562714,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_111",
            "time_usec": 1716809632374220,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sustainability Performance",
            "url": "https://www.weekday.com/en-eu/responsibility/sustainability-performance/",
            "time_usec": 1716809511346151,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Responsibility",
            "url": "https://www.weekday.com/en-eu/responsibility/",
            "time_usec": 1716809504814303,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_80",
            "time_usec": 1716809232006063,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g11b51f659ec_0_47",
            "time_usec": 1716809192100091,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_65",
            "time_usec": 1716809178489770,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_65",
            "time_usec": 1716809026768094,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.ge77270587f_0_11",
            "time_usec": 1716808924002475,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "what is the vaolue of a brand in fashion - Google Search",
            "url": "https://www.google.com/search?q=what+is+the+vaolue+of+a+brand+in+fashion&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIKAzLAsZdIMFU9EqGl0Rortsv141A%3A1716807529832&ei=aWdUZvm1Mq6Cxc8PyeCz8A4&ved=0ahUKEwi5jtq31q2GAxUuQfEDHUnwDO4Q4dUDCBA&uact=5&oq=what+is+the+vaolue+of+a+brand+in+fashion&gs_lp=Egxnd3Mtd2l6LXNlcnAiKHdoYXQgaXMgdGhlIHZhb2x1ZSBvZiBhIGJyYW5kIGluIGZhc2hpb25IuqEBUMoCWNSgAXAdeACQAQKYAfABoAGcLKoBBjU3LjYuMrgBA8gBAPgBAZgCQ6ACjx2oAgrCAgcQIxgnGOoCwgIKEAAYgAQYQxiKBcICBRAAGIAEwgIGEAAYBRgewgIEEAAYHsICBxAAGIAEGBjCAgkQABiABBgYGArCAgQQIxgnwgIGEAAYCBgemAMOkgcFNTcuMTCgB52iAg&sclient=gws-wiz-serp#vhid=xibiKdfMsqhAaM&vssid=mosaic",
            "time_usec": 1716808543622775,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "what is the vaolue of a brand in fashion - Google Search",
            "url": "https://www.google.com/search?q=what+is+the+vaolue+of+a+brand+in+fashion&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIKAzLAsZdIMFU9EqGl0Rortsv141A%3A1716807529832&ei=aWdUZvm1Mq6Cxc8PyeCz8A4&ved=0ahUKEwi5jtq31q2GAxUuQfEDHUnwDO4Q4dUDCBA&uact=5&oq=what+is+the+vaolue+of+a+brand+in+fashion&gs_lp=Egxnd3Mtd2l6LXNlcnAiKHdoYXQgaXMgdGhlIHZhb2x1ZSBvZiBhIGJyYW5kIGluIGZhc2hpb25IuqEBUMoCWNSgAXAdeACQAQKYAfABoAGcLKoBBjU3LjYuMrgBA8gBAPgBAZgCQ6ACjx2oAgrCAgcQIxgnGOoCwgIKEAAYgAQYQxiKBcICBRAAGIAEwgIGEAAYBRgewgIEEAAYHsICBxAAGIAEGBjCAgkQABiABBgYGArCAgQQIxgnwgIGEAAYCBgemAMOkgcFNTcuMTCgB52iAg&sclient=gws-wiz-serp#vhid=W6OMRkCt7dB7mM&vssid=mosaic",
            "time_usec": 1716808509623689,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "what is the vaolue of a brand in fashion - Google Search",
            "url": "https://www.google.com/search?q=what+is+the+vaolue+of+a+brand+in+fashion&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIKAzLAsZdIMFU9EqGl0Rortsv141A%3A1716807529832&ei=aWdUZvm1Mq6Cxc8PyeCz8A4&ved=0ahUKEwi5jtq31q2GAxUuQfEDHUnwDO4Q4dUDCBA&uact=5&oq=what+is+the+vaolue+of+a+brand+in+fashion&gs_lp=Egxnd3Mtd2l6LXNlcnAiKHdoYXQgaXMgdGhlIHZhb2x1ZSBvZiBhIGJyYW5kIGluIGZhc2hpb25IuqEBUMoCWNSgAXAdeACQAQKYAfABoAGcLKoBBjU3LjYuMrgBA8gBAPgBAZgCQ6ACjx2oAgrCAgcQIxgnGOoCwgIKEAAYgAQYQxiKBcICBRAAGIAEwgIGEAAYBRgewgIEEAAYHsICBxAAGIAEGBjCAgkQABiABBgYGArCAgQQIxgnwgIGEAAYCBgemAMOkgcFNTcuMTCgB52iAg&sclient=gws-wiz-serp#vhid=enGaWVo-3yNkNM&vssid=mosaic",
            "time_usec": 1716808496574270,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "what is the vaolue of a brand in fashion - Google Search",
            "url": "https://www.google.com/search?q=what+is+the+vaolue+of+a+brand+in+fashion&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIKAzLAsZdIMFU9EqGl0Rortsv141A%3A1716807529832&ei=aWdUZvm1Mq6Cxc8PyeCz8A4&ved=0ahUKEwi5jtq31q2GAxUuQfEDHUnwDO4Q4dUDCBA&uact=5&oq=what+is+the+vaolue+of+a+brand+in+fashion&gs_lp=Egxnd3Mtd2l6LXNlcnAiKHdoYXQgaXMgdGhlIHZhb2x1ZSBvZiBhIGJyYW5kIGluIGZhc2hpb25IuqEBUMoCWNSgAXAdeACQAQKYAfABoAGcLKoBBjU3LjYuMrgBA8gBAPgBAZgCQ6ACjx2oAgrCAgcQIxgnGOoCwgIKEAAYgAQYQxiKBcICBRAAGIAEwgIGEAAYBRgewgIEEAAYHsICBxAAGIAEGBjCAgkQABiABBgYGArCAgQQIxgnwgIGEAAYCBgemAMOkgcFNTcuMTCgB52iAg&sclient=gws-wiz-serp",
            "time_usec": 1716808494717276,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_71",
            "time_usec": 1716808321434962,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.ge77270587f_0_1636",
            "time_usec": 1716808278658949,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand denim styles ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+denim+styles++%27&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIK4beXcY_fCPiz9jb_vD7eIo1Jegw%3A1716807519138&ei=X2dUZqeHCIyXxc8PrdqB8Ac&ved=0ahUKEwjnss2y1q2GAxWMS_EDHS1tAH4Q4dUDCBA&uact=5&oq=weekday+brand+denim+styles++%27&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXdlZWtkYXkgYnJhbmQgZGVuaW0gc3R5bGVzICAnSIsZUIYNWM4YcAR4AJABAJgBVaABhgeqAQIxMrgBA8gBAPgBAZgCAKACAJgDAIgGAZIHAKAHnAQ&sclient=gws-wiz-serp#imgrc=BcElc_UVfn-q2M&imgdii=8JzqEPddx98rDM",
            "time_usec": 1716807982308656,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand denim styles ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+denim+styles++%27&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIK4beXcY_fCPiz9jb_vD7eIo1Jegw%3A1716807519138&ei=X2dUZqeHCIyXxc8PrdqB8Ac&ved=0ahUKEwjnss2y1q2GAxWMS_EDHS1tAH4Q4dUDCBA&uact=5&oq=weekday+brand+denim+styles++%27&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXdlZWtkYXkgYnJhbmQgZGVuaW0gc3R5bGVzICAnSIsZUIYNWM4YcAR4AJABAJgBVaABhgeqAQIxMrgBA8gBAPgBAZgCAKACAJgDAIgGAZIHAKAHnAQ&sclient=gws-wiz-serp#imgrc=sjenELQDv2gfTM&imgdii=BcElc_UVfn-q2M",
            "time_usec": 1716807982299211,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand denim styles ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+denim+styles++%27&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIK4beXcY_fCPiz9jb_vD7eIo1Jegw%3A1716807519138&ei=X2dUZqeHCIyXxc8PrdqB8Ac&ved=0ahUKEwjnss2y1q2GAxWMS_EDHS1tAH4Q4dUDCBA&uact=5&oq=weekday+brand+denim+styles++%27&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXdlZWtkYXkgYnJhbmQgZGVuaW0gc3R5bGVzICAnSIsZUIYNWM4YcAR4AJABAJgBVaABhgeqAQIxMrgBA8gBAPgBAZgCAKACAJgDAIgGAZIHAKAHnAQ&sclient=gws-wiz-serp#imgrc=sjenELQDv2gfTM&imgdii=BcElc_UVfn-q2M",
            "time_usec": 1716807698345408,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand denim styles ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+denim+styles++%27&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIK4beXcY_fCPiz9jb_vD7eIo1Jegw%3A1716807519138&ei=X2dUZqeHCIyXxc8PrdqB8Ac&ved=0ahUKEwjnss2y1q2GAxWMS_EDHS1tAH4Q4dUDCBA&uact=5&oq=weekday+brand+denim+styles++%27&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXdlZWtkYXkgYnJhbmQgZGVuaW0gc3R5bGVzICAnSIsZUIYNWM4YcAR4AJABAJgBVaABhgeqAQIxMrgBA8gBAPgBAZgCAKACAJgDAIgGAZIHAKAHnAQ&sclient=gws-wiz-serp#imgrc=BcElc_UVfn-q2M&imgdii=sjenELQDv2gfTM",
            "time_usec": 1716807698327913,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand denim styles ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+denim+styles++%27&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIK4beXcY_fCPiz9jb_vD7eIo1Jegw%3A1716807519138&ei=X2dUZqeHCIyXxc8PrdqB8Ac&ved=0ahUKEwjnss2y1q2GAxWMS_EDHS1tAH4Q4dUDCBA&uact=5&oq=weekday+brand+denim+styles++%27&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXdlZWtkYXkgYnJhbmQgZGVuaW0gc3R5bGVzICAnSIsZUIYNWM4YcAR4AJABAJgBVaABhgeqAQIxMrgBA8gBAPgBAZgCAKACAJgDAIgGAZIHAKAHnAQ&sclient=gws-wiz-serp#imgrc=aV-LtPnaLCM2EM&imgdii=BcElc_UVfn-q2M",
            "time_usec": 1716807696547353,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand denim styles ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+denim+styles++%27&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIK4beXcY_fCPiz9jb_vD7eIo1Jegw%3A1716807519138&ei=X2dUZqeHCIyXxc8PrdqB8Ac&ved=0ahUKEwjnss2y1q2GAxWMS_EDHS1tAH4Q4dUDCBA&uact=5&oq=weekday+brand+denim+styles++%27&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXdlZWtkYXkgYnJhbmQgZGVuaW0gc3R5bGVzICAnSIsZUIYNWM4YcAR4AJABAJgBVaABhgeqAQIxMrgBA8gBAPgBAZgCAKACAJgDAIgGAZIHAKAHnAQ&sclient=gws-wiz-serp#vhid=aV-LtPnaLCM2EM&vssid=mosaic",
            "time_usec": 1716807693768699,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand denim styles ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+denim+styles++%27&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIK4beXcY_fCPiz9jb_vD7eIo1Jegw%3A1716807519138&ei=X2dUZqeHCIyXxc8PrdqB8Ac&ved=0ahUKEwjnss2y1q2GAxWMS_EDHS1tAH4Q4dUDCBA&uact=5&oq=weekday+brand+denim+styles++%27&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXdlZWtkYXkgYnJhbmQgZGVuaW0gc3R5bGVzICAnSIsZUIYNWM4YcAR4AJABAJgBVaABhgeqAQIxMrgBA8gBAPgBAZgCAKACAJgDAIgGAZIHAKAHnAQ&sclient=gws-wiz-serp#vhid=aV-LtPnaLCM2EM&vssid=mosaic",
            "time_usec": 1716807680648568,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand denim styles ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+denim+styles++%27&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIK4beXcY_fCPiz9jb_vD7eIo1Jegw%3A1716807519138&ei=X2dUZqeHCIyXxc8PrdqB8Ac&ved=0ahUKEwjnss2y1q2GAxWMS_EDHS1tAH4Q4dUDCBA&uact=5&oq=weekday+brand+denim+styles++%27&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXdlZWtkYXkgYnJhbmQgZGVuaW0gc3R5bGVzICAnSIsZUIYNWM4YcAR4AJABAJgBVaABhgeqAQIxMrgBA8gBAPgBAZgCAKACAJgDAIgGAZIHAKAHnAQ&sclient=gws-wiz-serp#vhid=ZTtE0ZMs6rRZcM&vssid=mosaic",
            "time_usec": 1716807636760481,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "https://hypebae.com/2021/3/weekday-denim-jeans-hemp-plant-based-sustainable-jackets-skirts-pants-price-where-to-buy",
            "time_usec": 1716807614717423,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand denim styles ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+denim+styles++%27&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIK4beXcY_fCPiz9jb_vD7eIo1Jegw%3A1716807519138&ei=X2dUZqeHCIyXxc8PrdqB8Ac&ved=0ahUKEwjnss2y1q2GAxWMS_EDHS1tAH4Q4dUDCBA&uact=5&oq=weekday+brand+denim+styles++%27&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXdlZWtkYXkgYnJhbmQgZGVuaW0gc3R5bGVzICAnSIsZUIYNWM4YcAR4AJABAJgBVaABhgeqAQIxMrgBA8gBAPgBAZgCAKACAJgDAIgGAZIHAKAHnAQ&sclient=gws-wiz-serp#vhid=uK3PObiFsxh9CM&vssid=mosaic",
            "time_usec": 1716807607643612,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand denim styles ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+denim+styles++%27&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIK4beXcY_fCPiz9jb_vD7eIo1Jegw%3A1716807519138&ei=X2dUZqeHCIyXxc8PrdqB8Ac&ved=0ahUKEwjnss2y1q2GAxWMS_EDHS1tAH4Q4dUDCBA&uact=5&oq=weekday+brand+denim+styles++%27&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXdlZWtkYXkgYnJhbmQgZGVuaW0gc3R5bGVzICAnSIsZUIYNWM4YcAR4AJABAJgBVaABhgeqAQIxMrgBA8gBAPgBAZgCAKACAJgDAIgGAZIHAKAHnAQ&sclient=gws-wiz-serp#vhid=aKNXg3P7w1yOhM&vssid=mosaic",
            "time_usec": 1716807596716909,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand denim styles ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+denim+styles++%27&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIK4beXcY_fCPiz9jb_vD7eIo1Jegw%3A1716807519138&ei=X2dUZqeHCIyXxc8PrdqB8Ac&ved=0ahUKEwjnss2y1q2GAxWMS_EDHS1tAH4Q4dUDCBA&uact=5&oq=weekday+brand+denim+styles++%27&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXdlZWtkYXkgYnJhbmQgZGVuaW0gc3R5bGVzICAnSIsZUIYNWM4YcAR4AJABAJgBVaABhgeqAQIxMrgBA8gBAPgBAZgCAKACAJgDAIgGAZIHAKAHnAQ&sclient=gws-wiz-serp#vhid=3Dlq2KS8sRSiSM&vssid=mosaic",
            "time_usec": 1716807575947171,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Women's fit guide",
            "url": "https://www.weekday.com/en-eu/weekday-jeans/womens-fit-guide/",
            "time_usec": 1716807546280045,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand denim styles ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+denim+styles++%27&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIK4beXcY_fCPiz9jb_vD7eIo1Jegw%3A1716807519138&ei=X2dUZqeHCIyXxc8PrdqB8Ac&ved=0ahUKEwjnss2y1q2GAxWMS_EDHS1tAH4Q4dUDCBA&uact=5&oq=weekday+brand+denim+styles++%27&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXdlZWtkYXkgYnJhbmQgZGVuaW0gc3R5bGVzICAnSIsZUIYNWM4YcAR4AJABAJgBVaABhgeqAQIxMrgBA8gBAPgBAZgCAKACAJgDAIgGAZIHAKAHnAQ&sclient=gws-wiz-serp#vhid=hJyj0B9kuxaCPM&vssid=mosaic",
            "time_usec": 1716807543922907,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand denim styles ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+denim+styles++%27&sca_esv=8870e14de2d74e2a&udm=2&biw=1289&bih=701&sxsrf=ADLYWIK4beXcY_fCPiz9jb_vD7eIo1Jegw%3A1716807519138&ei=X2dUZqeHCIyXxc8PrdqB8Ac&ved=0ahUKEwjnss2y1q2GAxWMS_EDHS1tAH4Q4dUDCBA&uact=5&oq=weekday+brand+denim+styles++%27&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXdlZWtkYXkgYnJhbmQgZGVuaW0gc3R5bGVzICAnSIsZUIYNWM4YcAR4AJABAJgBVaABhgeqAQIxMrgBA8gBAPgBAZgCAKACAJgDAIgGAZIHAKAHnAQ&sclient=gws-wiz-serp",
            "time_usec": 1716807530925397,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand history ' - Google Search",
            "url": "https://www.google.com/search?sca_esv=8870e14de2d74e2a&sxsrf=ADLYWIK7l9SnyqSkKFOwK4puVKry6hpv6w:1716807512176&q=weekday+brand+history+%27&uds=ADvngMgiPmsFSnX7QtZmBAeJzn8v2I5ppknZDfOGS9A5FubwRuI-tbmtqbdWhafWaCyw-_FBwC6y4c3f_QD03KzI1Sg4GZ7gAlq4knez_I1Nu3-ekJSHgGUSQUjUmwthQgg-CPzGOzojaj_B8FexBBwKNpHnokg5QbDEnDktSa31OdqHa14SLS4T61ucvaXwq3GbmqT-AfAbdU5YvXh0qqsi7xHcEhJ3nzWzdoobOGR5ht2LVTkhaNQlYdS-pOhMW8kO_zvRKFMD8AgDscfrajwoGe5aoDXujg&udm=2&prmd=ivnbz&sa=X&ved=2ahUKEwjIwKSv1q2GAxV2SvEDHQxHBngQtKgLegQIDBAB&biw=1289&bih=701&dpr=1",
            "time_usec": 1716807520279692,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand history ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+history+%27&oq=weekday+brand&aqs=chrome.0.69i59j69i64j0i22i30l8.4187j0j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716807512803434,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://moodle.isiflorence.org/",
            "time_usec": 1716807458733663,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "http://moodle.isiflorence.org/theme/image.php/boost/theme/1693921684/favicon",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Dashboard",
            "url": "http://moodle.isiflorence.org/my/",
            "time_usec": 1716807425680534,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "http://moodle.isiflorence.org/theme/image.php/boost/theme/1693921684/favicon",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Moodle ISI Florence: Log in to the site",
            "url": "http://moodle.isiflorence.org/login/index.php",
            "time_usec": 1716807407115450,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.ge77270587f_0_1636",
            "time_usec": 1716807330045856,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_45",
            "time_usec": 1716807319275143,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.g1254f724beb_0_71",
            "time_usec": 1716807222684281,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.ge77270587f_0_11",
            "time_usec": 1716807151166339,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.ge77270587f_0_11",
            "time_usec": 1716807080985730,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Responsibility",
            "url": "https://www.weekday.com/en-eu/responsibility/",
            "time_usec": 1716807045863075,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.ge77270587f_0_1636",
            "time_usec": 1716807039125805,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.ge77270587f_0_11",
            "time_usec": 1716806957204248,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.weekday.com/static_assets/image/favicons/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "About us",
            "url": "https://www.weekday.com/en-eu/about-us/",
            "time_usec": 1716806885302954,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "About us",
            "url": "https://www.weekday.com/en-eu/about-us/",
            "time_usec": 1716806878864410,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand history ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+history+%27&sca_esv=8870e14de2d74e2a&sxsrf=ADLYWILhYDEjBhD-cVUxk53sohU1JDsbSQ%3A1716805704851&ei=SGBUZvHFM7yyi-gPh96IuAU&ved=0ahUKEwjxib7Rz62GAxU82QIHHQcvAlcQ4dUDCBA&uact=5&oq=weekday+brand+history+%27&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIhd3ZWVrZGF5IGJyYW5kIGhpc3RvcnkgJzIGEAAYFhgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIEMggQABiABBiiBEi2HFDeA1iTHHABeAGQAQCYAcQCoAHIF6oBCDguMTAuMy4xuAEDyAEA-AEBmAIXoAKNGagCEcICBxAjGCcY6gLCAhQQABiABBjjBBi0AhjpBBjqAtgBAcICCxAAGIAEGJECGIoFwgIKEAAYgAQYQxiKBcICCxAuGIAEGNEDGMcBwgIKECMYgAQYJxiKBcICCxAuGIAEGJECGIoFwgIEECMYJ8ICChAAGIAEGBQYhwLCAgUQABiABMICDRAAGIAEGEMYyQMYigXCAgsQABiABBiiBBiLA5gDFroGBggBEAEYAZIHCDcuMTIuMy4xoAfYew&sclient=gws-wiz-serp",
            "time_usec": 1716806870115973,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "http://moodle.isiflorence.org/theme/image.php/boost/theme/1693921684/favicon",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "moodle.isiflorence.org/login/index.php",
            "url": "http://moodle.isiflorence.org/login/index.php",
            "time_usec": 1716806840197775,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "http://moodle.isiflorence.org/theme/image.php/boost/theme/1693921684/favicon",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Dashboard",
            "url": "http://moodle.isiflorence.org/my/",
            "time_usec": 1716806826359323,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "http://moodle.isiflorence.org/theme/image.php/boost/theme/1693921684/favicon",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Forgotten password",
            "url": "http://moodle.isiflorence.org/login/forgot_password.php",
            "time_usec": 1716806794337171,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Moodle ISI Florence",
            "url": "http://moodle.isiflorence.org/index.php?",
            "time_usec": 1716806784045241,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "http://moodle.isiflorence.org/theme/image.php/boost/theme/1693921684/favicon",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Forgotten password",
            "url": "http://moodle.isiflorence.org/login/forgot_password.php",
            "time_usec": 1716806681040156,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "http://moodle.isiflorence.org/theme/image.php/boost/theme/1693921684/favicon",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Forgotten password",
            "url": "http://moodle.isiflorence.org/login/forgot_password.php",
            "time_usec": 1716806671178485,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "http://moodle.isiflorence.org/theme/image.php/boost/theme/1693921684/favicon",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Forgotten password",
            "url": "http://moodle.isiflorence.org/login/forgot_password.php",
            "time_usec": 1716806652801429,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "http://moodle.isiflorence.org/theme/image.php/boost/theme/1693921684/favicon",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Moodle ISI Florence: Log in to the site",
            "url": "http://moodle.isiflorence.org/login/index.php",
            "time_usec": 1716806646592243,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.theindustry.fashion/wp-content/uploads/2021/09/cropped-LOGO-32x32.jpg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Weekday - TheIndustry.fashion",
            "url": "https://www.theindustry.fashion/the_directory/weekday/#:~:text=Description%3A,emphasises%20sustainable%20practices%20and%20inclusivity.",
            "time_usec": 1716806629588657,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "weekday brand history ' - Google Search",
            "url": "https://www.google.com/search?q=weekday+brand+history+%27&sca_esv=8870e14de2d74e2a&sxsrf=ADLYWILhYDEjBhD-cVUxk53sohU1JDsbSQ%3A1716805704851&ei=SGBUZvHFM7yyi-gPh96IuAU&ved=0ahUKEwjxib7Rz62GAxU82QIHHQcvAlcQ4dUDCBA&uact=5&oq=weekday+brand+history+%27&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIhd3ZWVrZGF5IGJyYW5kIGhpc3RvcnkgJzIGEAAYFhgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIEMggQABiABBiiBEi2HFDeA1iTHHABeAGQAQCYAcQCoAHIF6oBCDguMTAuMy4xuAEDyAEA-AEBmAIXoAKNGagCEcICBxAjGCcY6gLCAhQQABiABBjjBBi0AhjpBBjqAtgBAcICCxAAGIAEGJECGIoFwgIKEAAYgAQYQxiKBcICCxAuGIAEGNEDGMcBwgIKECMYgAQYJxiKBcICCxAuGIAEGJECGIoFwgIEECMYJ8ICChAAGIAEGBQYhwLCAgUQABiABMICDRAAGIAEGEMYyQMYigXCAgsQABiABBiiBBiLA5gDFroGBggBEAEYAZIHCDcuMTIuMy4xoAfYew&sclient=gws-wiz-serp",
            "time_usec": 1716806581984538,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "http://moodle.isiflorence.org/theme/image.php/boost/theme/1693921684/favicon",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Moodle ISI Florence: Log in to the site",
            "url": "http://moodle.isiflorence.org/login/index.php",
            "time_usec": 1716806574210718,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.ge77270587f_0_11",
            "time_usec": 1716806571082785,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/presentations/images/favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit#slide=id.p",
            "time_usec": 1716806561413349,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation #1 - Google Slides",
            "url": "https://docs.google.com/presentation/d/1LpCQWb0sZiiI3KgUrO1H5-fJJ0M5u-YQ0Ea-k-RFRF0/edit",
            "time_usec": 1716806553173399,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Presentation shared with you: \"Copy of Fashion Portraits Newsletter XL by Slidesgo\" - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzQVwnVJsxBDHbLPCZjnJdJGvqjx",
            "time_usec": 1716806545856696,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,433) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1716806543210378,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/search",
            "url": "https://www.condor.com/oci/en-EU/search",
            "time_usec": 1716806496019554,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://cb6q-04.na1.hs-sales-engage.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://cb6q-04.na1.hs-sales-engage.com/Ctc/W0+23284/cB6q-04/JkM2-6qcW6N1vHY6lZ3kNW9l6N6M2k7VL6W19kY2s1qRr50W90-42-6sJvJ0W1l02pp8Z18p2W8B8rz111gwkpW91_9bN4mq8PRW4mxLSv2bFMJHW8VTpFG70g934W5g960V3tblnfW35hmpr5gxq9tW4rw2w77-lRDLW19j6_j6GGYhFW5b_H_L6-qKdTW6mxcvN1gGZsQW11k1w01004qpW7tLDW01CWWcmW7Hq_PT1MwPB2W55_nh93y58GPW6CsHJx5hZdTQW2_LSgF5fyvQSW7D3srT1Sz-qnVShW2X3dBZYYf5h3JRR04",
            "url": "https://cb6q-04.na1.hs-sales-engage.com/Ctc/W0+23284/cB6q-04/JkM2-6qcW6N1vHY6lZ3kNW9l6N6M2k7VL6W19kY2s1qRr50W90-42-6sJvJ0W1l02pp8Z18p2W8B8rz111gwkpW91_9bN4mq8PRW4mxLSv2bFMJHW8VTpFG70g934W5g960V3tblnfW35hmpr5gxq9tW4rw2w77-lRDLW19j6_j6GGYhFW5b_H_L6-qKdTW6mxcvN1gGZsQW11k1w01004qpW7tLDW01CWWcmW7Hq_PT1MwPB2W55_nh93y58GPW6CsHJx5hZdTQW2_LSgF5fyvQSW7D3srT1Sz-qnVShW2X3dBZYYf5h3JRR04",
            "time_usec": 1716806488853803,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Condor Online Check-in",
            "url": "https://www.condor.com/oci/en-EU/confirmation",
            "time_usec": 1716806487427341,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "[IMPORTANT] Incomplete Pre-Departure Moodle Course for ISI Florence - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#search/moodle/FMfcgzGxStxTBqGlqGpmTzZGcbsGsnnH",
            "time_usec": 1716806387961557,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Search results - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#search/moodle",
            "time_usec": 1716806383325204,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "where to stay in the dolomites for backpackers - Google Search",
            "url": "https://www.google.com/search?q=where+to+stay+in+the+dolomites+for+backpackers&sca_esv=8870e14de2d74e2a&sxsrf=ADLYWIJKD8JS6yBbUAJ1XT3UeVv-6oUkmA%3A1716805760971&ei=gGBUZofyOsjii-gPrMizgAU&ved=0ahUKEwiHsp_sz62GAxVI8QIHHSzkDFAQ4dUDCBA&uact=5&oq=where+to+stay+in+the+dolomites+for+backpackers&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIi53aGVyZSB0byBzdGF5IGluIHRoZSBkb2xvbWl0ZXMgZm9yIGJhY2twYWNrZXJzMgUQIRigATIFECEYkgMyBRAhGJIDMgUQIRiSAzIFECEYkgMyBRAhGJIDMgUQIRiSAzIFECEYnwVIuRRQ9gJYyBNwAHgCkAEBmAH3AaAB3w2qAQYxMC41LjG4AQPIAQD4AQGYAhCgAsQMwgIEEAAYR8ICBRAAGIAEwgIKEAAYgAQYFBiHAsICCxAAGIAEGIYDGIoFwgIIEAAYgAQYogTCAgsQABiABBiiBBiLA8ICBhAAGBYYHsICBxAhGKABGAqYAwDiAwUSATEgQIgGAZAGCJIHAzguOKAH0VE&sclient=gws-wiz-serp",
            "time_usec": 1716805875404999,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://weareglobaltravellers.com/2022/11/dolomites-backpacking-guide/",
            "time_usec": 1716805869163816,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "where to stay in the dolomites for backpackers - Google Search",
            "url": "https://www.google.com/search?q=where+to+stay+in+the+dolomites+for+backpackers&sca_esv=8870e14de2d74e2a&sxsrf=ADLYWIJKD8JS6yBbUAJ1XT3UeVv-6oUkmA%3A1716805760971&ei=gGBUZofyOsjii-gPrMizgAU&ved=0ahUKEwiHsp_sz62GAxVI8QIHHSzkDFAQ4dUDCBA&uact=5&oq=where+to+stay+in+the+dolomites+for+backpackers&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIi53aGVyZSB0byBzdGF5IGluIHRoZSBkb2xvbWl0ZXMgZm9yIGJhY2twYWNrZXJzMgUQIRigATIFECEYkgMyBRAhGJIDMgUQIRiSAzIFECEYkgMyBRAhGJIDMgUQIRiSAzIFECEYnwVIuRRQ9gJYyBNwAHgCkAEBmAH3AaAB3w2qAQYxMC41LjG4AQPIAQD4AQGYAhCgAsQMwgIEEAAYR8ICBRAAGIAEwgIKEAAYgAQYFBiHAsICCxAAGIAEGIYDGIoFwgIIEAAYgAQYogTCAgsQABiABBiiBBiLA8ICBhAAGBYYHsICBxAhGKABGAqYAwDiAwUSATEgQIgGAZAGCJIHAzguOKAH0VE&sclient=gws-wiz-serp",
            "time_usec": 1716805830944864,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://freewildsouls.com/destination/backpacking-dolomites",
            "time_usec": 1716805828745925,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "where to stay in the dolomites for backpackers - Google Search",
            "url": "https://www.google.com/search?q=where+to+stay+in+the+dolomites+for+backpackers&sca_esv=8870e14de2d74e2a&sxsrf=ADLYWIJKD8JS6yBbUAJ1XT3UeVv-6oUkmA%3A1716805760971&ei=gGBUZofyOsjii-gPrMizgAU&ved=0ahUKEwiHsp_sz62GAxVI8QIHHSzkDFAQ4dUDCBA&uact=5&oq=where+to+stay+in+the+dolomites+for+backpackers&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIi53aGVyZSB0byBzdGF5IGluIHRoZSBkb2xvbWl0ZXMgZm9yIGJhY2twYWNrZXJzMgUQIRigATIFECEYkgMyBRAhGJIDMgUQIRiSAzIFECEYkgMyBRAhGJIDMgUQIRiSAzIFECEYnwVIuRRQ9gJYyBNwAHgCkAEBmAH3AaAB3w2qAQYxMC41LjG4AQPIAQD4AQGYAhCgAsQMwgIEEAAYR8ICBRAAGIAEwgIKEAAYgAQYFBiHAsICCxAAGIAEGIYDGIoFwgIIEAAYgAQYogTCAgsQABiABBiiBBiLA8ICBhAAGBYYHsICBxAhGKABGAqYAwDiAwUSATEgQIgGAZAGCJIHAzguOKAH0VE&sclient=gws-wiz-serp",
            "time_usec": 1716805778088322,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "where to stay in the dolomites - Google Search",
            "url": "https://www.google.com/search?q=where+to+stay+in+the+dolomits&sca_esv=8870e14de2d74e2a&sxsrf=ADLYWIL-B3PPyoWmTrX5LmgK98jhvrucuA%3A1716805734795&ei=ZmBUZrH7L9yoi-gP2p218AM&ved=0ahUKEwixxuHfz62GAxVc1AIHHdpODT4Q4dUDCBA&uact=5&oq=where+to+stay+in+the+dolomits&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIh13aGVyZSB0byBzdGF5IGluIHRoZSBkb2xvbWl0czIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIHEAAYgAQYDTIGEAAYFhgeMgYQABgWGB5IiXVQ4RJYjHRwBXgBkAEAmAHdA6ABoiWqAQsxMy4xMS4zLjEuMrgBA8gBAPgBAZgCI6ACsSeoAhLCAgcQIxgnGOoCwgIUEAAYgAQY4wQYtAIY6QQY6gLYAQHCAhYQLhiABBhDGLQCGMgDGIoFGOoC2AECwgIXEC4YgAQY4wQYtAIYyAMY6QQY6gLYAQLCAgoQIxiABBgnGIoFwgILEAAYgAQYkQIYigXCAgoQABiABBhDGIoFwgILEC4YgAQY0QMYxwHCAgUQABiABMICBBAjGCfCAgoQABiABBgUGIcCwgILEAAYgAQYhgMYigXCAgsQABiABBiiBBiLA8ICCBAAGIAEGKIEwgIFECEYoAGYAxW6BgYIARABGAG6BgYIAhABGAiSBwsxNy4xMC40LjIuMqAHn94B&sclient=gws-wiz-serp",
            "time_usec": 1716805761778201,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "northern italy mountains - Google Search",
            "url": "https://www.google.com/search?q=northern+italy+mountains&oq=northern+italy+mountains+&aqs=chrome..69i64j0i19i512l4j0i19i395i512j0i395i512i546l3j69i57.12262j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716805735627512,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716805721867818,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "train from florence to interlaken - Google Search",
            "url": "https://www.google.com/search?q=train+from+florence+to+interlaken&sca_esv=8870e14de2d74e2a&sxsrf=ADLYWIJCUvZfQC-6_mB8SncRHQr71-eOgg%3A1716805441664&ei=QV9UZvWVKPDdxc8PoZSe-A8&ved=0ahUKEwi1uv7Tzq2GAxXwbvEDHSGKB_8Q4dUDCBA&uact=5&oq=train+from+florence+to+interlaken&gs_lp=Egxnd3Mtd2l6LXNlcnAiIXRyYWluIGZyb20gZmxvcmVuY2UgdG8gaW50ZXJsYWtlbjIFEAAYgAQyBRAAGIAEMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGIAEGKIEMggQABiABBiiBEi1QlChCli5QXACeAGQAQSYAbMFoAGcTaoBDDguMTEuMi4yLjcuNrgBA8gBAPgBAZgCIaACxTyoAgvCAgcQIxgnGOoCwgITEAAYgAQYQxi0AhiKBRjqAtgBAcICChAjGIAEGCcYigXCAgsQABiABBiRAhiKBcICChAAGIAEGEMYigXCAgsQLhiABBjRAxjHAcICBBAjGCfCAg4QLhiABBjHARiOBRivAcICFBAuGIAEGJECGMcBGIoFGI4FGK8BwgINEAAYgAQYQxjJAxiKBcICCxAAGIAEGJIDGIoFwgITEC4YgAQYQxjHARiKBRiOBRivAcICExAuGIAEGNEDGEMYxwEYyQMYigXCAgoQLhiABBhDGIoFwgIGEAAYFhgemAMQugYGCAEQARgBkgcMOC4xMy4xLjIuNy4yoAfToQI&sclient=gws-wiz-serp",
            "time_usec": 1716805717355192,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://www.omio.com/trains/florence/interlaken?gad_source=1&gclid=Cj0KCQjw3tCyBhDBARIsAEY0XNnA-xigmabK2Rk208nGuWGpGPXbAe44a0o_dNH8soiQZOOMxxrVsKUaAr35EALw_wcB",
            "time_usec": 1716805715029943,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "train from florence to interlaken - Google Search",
            "url": "https://www.google.com/search?q=train+from+florence+to+interlaken&sca_esv=8870e14de2d74e2a&sxsrf=ADLYWIJCUvZfQC-6_mB8SncRHQr71-eOgg%3A1716805441664&ei=QV9UZvWVKPDdxc8PoZSe-A8&ved=0ahUKEwi1uv7Tzq2GAxXwbvEDHSGKB_8Q4dUDCBA&uact=5&oq=train+from+florence+to+interlaken&gs_lp=Egxnd3Mtd2l6LXNlcnAiIXRyYWluIGZyb20gZmxvcmVuY2UgdG8gaW50ZXJsYWtlbjIFEAAYgAQyBRAAGIAEMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGIAEGKIEMggQABiABBiiBEi1QlChCli5QXACeAGQAQSYAbMFoAGcTaoBDDguMTEuMi4yLjcuNrgBA8gBAPgBAZgCIaACxTyoAgvCAgcQIxgnGOoCwgITEAAYgAQYQxi0AhiKBRjqAtgBAcICChAjGIAEGCcYigXCAgsQABiABBiRAhiKBcICChAAGIAEGEMYigXCAgsQLhiABBjRAxjHAcICBBAjGCfCAg4QLhiABBjHARiOBRivAcICFBAuGIAEGJECGMcBGIoFGI4FGK8BwgINEAAYgAQYQxjJAxiKBcICCxAAGIAEGJIDGIoFwgITEC4YgAQYQxjHARiKBRiOBRivAcICExAuGIAEGNEDGEMYxwEYyQMYigXCAgoQLhiABBhDGIoFwgIGEAAYFhgemAMQugYGCAEQARgBkgcMOC4xMy4xLjIuNy4yoAfToQI&sclient=gws-wiz-serp",
            "time_usec": 1716805706204639,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "NoReply New sign in to your Moodle ISI Florence account - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#search/moodle/FMfcgzGxTFbdqDvBFVjjblZldmncVNvc",
            "time_usec": 1716805441671949,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "isi florence - Google Search",
            "url": "https://www.google.com/search?q=isi+florence&sca_esv=8870e14de2d74e2a&sxsrf=ADLYWIJaGjxIyP5HIkn7nGjbpczpvwpUnw%3A1716805438028&source=hp&ei=PV9UZsbsPIeWxc8PwZKaoAY&iflsig=AL9hbdgAAAAAZlRtThVVNGPr6KWpi-m6rJ_axyjYQSNV&ved=0ahUKEwiG_57Szq2GAxUHS_EDHUGJBmQQ4dUDCBU&uact=5&oq=isi+florence&gs_lp=Egdnd3Mtd2l6Igxpc2kgZmxvcmVuY2UyChAjGIAEGCcYigUyBBAjGCcyChAjGIAEGCcYigUyExAuGIAEGEMYxwEYigUYjgUYrwEyChAAGIAEGEMYigUyChAAGIAEGEMYigUyBRAAGIAEMg4QLhiABBjHARiOBRivATIFEAAYgAQyChAAGIAEGEMYigVIrRBQAFjbD3AAeACQAQCYAYYBoAHbCaoBAzMuOLgBA8gBAPgBAZgCC6AC5grCAgsQABiABBiRAhiKBcICDhAAGIAEGJECGMkDGIoFmAMAkgcEMS4xMKAHoJkB&sclient=gws-wiz",
            "time_usec": 1716805439780724,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google",
            "url": "https://www.google.com/",
            "time_usec": 1716805433482270,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google",
            "url": "https://www.google.com/",
            "time_usec": 1716805433082084,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://isiflorence.org/isiflorence-app/",
            "time_usec": 1716805429392951,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "moodle isi florence - Google Search",
            "url": "https://www.google.com/search?q=moodle+isi+florence&oq=moodle+isi+florence&aqs=chrome..69i64j0i22i30j0i512i546j0i395i512i546j0i395i546i649j69i57l2.6183j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716805423341719,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://isiflorence.org/application-dashboard/",
            "time_usec": 1716805416754679,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "moodle isi florence - Google Search",
            "url": "https://www.google.com/search?q=moodle+isi+florence&oq=moodle+isi+florence&aqs=chrome..69i64j0i22i30j0i512i546j0i395i512i546j0i395i546i649j69i57l2.6183j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716805414037184,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "moodle isi florence - Google Search",
            "url": "https://www.google.com/search?q=moodle+isi+florence&oq=moodle+isi+florence&aqs=chrome..69i64j0i22i30j0i512i546j0i395i512i546j0i395i546i649j69i57l2.6183j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1716805388068788,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716805379424620,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Search results - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#search/moodle",
            "time_usec": 1716805367005484,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,432) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1716805357983978,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Gmail",
            "url": "https://mail.google.com/mail/u/0/",
            "time_usec": 1716805350937440,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Error 404 (Not Found)!!1",
            "url": "http://gmail.co/",
            "time_usec": 1716805342801087,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716805338123473,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google",
            "url": "https://www.google.com/",
            "time_usec": 1716805336361062,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google",
            "url": "https://www.google.com/",
            "time_usec": 1716805335086313,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1716805323712875,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/documents/images/kix-favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Untitled document - Google Docs",
            "url": "https://docs.google.com/document/d/1Ltgs9ktgBFPwfeQ2hMn0z1-Ey82OzOYFxBkekMcmxPA/edit",
            "time_usec": 1715848770061615,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Untitled document - Google Docs",
            "url": "https://docs.google.com/document/create?usp=drive_web&ouid=107899628227935306394&folder=15kP3GadKm-ZqasMXQJXYpUCSVYm1MPno",
            "time_usec": 1715848765529900,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "summer 2024 - Google Drive",
            "url": "https://drive.google.com/drive/folders/15kP3GadKm-ZqasMXQJXYpUCSVYm1MPno",
            "time_usec": 1715848760042849,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Travel - Google Drive",
            "url": "https://drive.google.com/drive/folders/1Q8OZlnqFsux-k-Jz-x2O_d4H2WL3NZjU",
            "time_usec": 1715848758361740,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "My Drive - Google Drive",
            "url": "https://drive.google.com/drive/my-drive",
            "time_usec": 1715848755079522,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Home - Google Drive",
            "url": "https://drive.google.com/drive/home",
            "time_usec": 1715848468721577,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Recent - Google Drive",
            "url": "https://drive.google.com/drive/recent",
            "time_usec": 1715848441943919,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Shared with me - Google Drive",
            "url": "https://drive.google.com/drive/shared-with-me",
            "time_usec": 1715848435358068,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://www.offbeatbudapest.com/top10/best-ruin-bars-budapest/",
            "time_usec": 1715848098649593,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "ruin bars budapest - Google Search",
            "url": "https://www.google.com/search?gs_ssp=eJzj4tVP1zc0TCrPSzI0NjE0YLRSNagwMTcxTEk2N7SwsLQ0N0s2tDKoMDQ1TjVNS0szMzI1Sks0MPASKirNzFNISiwqVkgqTUksSC0uAQDg3xVi&q=ruin+bars+budapest&oq=ruin+bar&aqs=chrome.1.69i64j46i67i175i199i433i512i650j0i67i512i650j46i175i199i512l3j0i512l3.12187j0j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715848078336779,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "14 Best Budapest Nightlife Spots, Picked By A Local",
            "url": "https://www.timeout.com/budapest/things-to-do/best-nightlife-in-budapest",
            "time_usec": 1715848037496768,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "14 Best Budapest Nightlife Spots, Picked By A Local",
            "url": "https://www.timeout.com/budapest/things-to-do/best-nightlife-in-budapest",
            "time_usec": 1715848037486723,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "14 Best Budapest Nightlife Spots, Picked By A Local",
            "url": "https://www.timeout.com/budapest/things-to-do/best-nightlife-in-budapest",
            "time_usec": 1715848027475132,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "14 Best Budapest Nightlife Spots, Picked By A Local",
            "url": "https://www.timeout.com/budapest/things-to-do/best-nightlife-in-budapest",
            "time_usec": 1715848016849342,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "best nigh life in budapest - Google Search",
            "url": "https://www.google.com/search?q=best+nigh+life+in+budapest&sca_esv=94fa641d5e31d942&sxsrf=ADLYWIJeA1dLpR_xvw0gJ-VS6KIEG7jdiA%3A1715847962834&ei=GsNFZpO8Mrii0PEP9LawsAg&ved=0ahUKEwiTscDi35GGAxU4ETQIHXQbDIYQ4dUDCBE&uact=5&oq=best+nigh+life+in+budapest&gs_lp=Egxnd3Mtd2l6LXNlcnAiGmJlc3QgbmlnaCBsaWZlIGluIGJ1ZGFwZXN0MgcQABiABBgNMgcQABiABBgNMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigVI-yxQuwNY5ipwAXgAkAEAmAHdAqAB-TqqAQcyLTE1LjEwuAEDyAEA-AEBmAIaoALZPagCEsICBxAjGCcY6gLCAhQQABiABBjjBBi0AhjpBBjqAtgBAcICBBAjGCfCAgoQABiABBhDGIoFwgILEAAYgAQYkQIYigXCAgsQLhiABBiRAhiKBcICChAuGIAEGEMYigXCAhYQLhiABBhDGMcBGJgFGJkFGIoFGK8BwgIREC4YgAQYsQMY0QMYgwEYxwHCAggQABiABBixA8ICCxAAGIAEGJIDGIoFwgIFEAAYgATCAggQABiABBjJA8ICCxAAGIAEGLEDGIMBwgIHEAAYgAQYCsICChAAGIAEGLEDGArCAgcQLhiABBgKwgIJEAAYgAQYChgNwgIMEAAYgAQYyQMYChgNwgIKEAAYgAQYkgMYDcICChAAGIAEGMkDGA2YAxa6BgYIARABGAGSBwgxLjAuNC4yMaAHqu8B&sclient=gws-wiz-serp",
            "time_usec": 1715848013301393,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "music in budapest in july - Google Search",
            "url": "https://www.google.com/search?q=music+in+budapest+in+july+&sca_esv=94fa641d5e31d942&sxsrf=ADLYWIKRwO9ZB1TfgOI45gzNnBoU6xiVNA%3A1715847104597&ei=wL9FZtWDJL-L0PEPgN284Aw&ved=0ahUKEwjV46HJ3JGGAxW_BTQIHYAuD8wQ4dUDCBE&uact=5&oq=music+in+budapest+in+july+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIhptdXNpYyBpbiBidWRhcGVzdCBpbiBqdWx5IDIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYogQYiwMyCxAAGIAEGKIEGIsDMgsQABiABBiiBBiLAzILEAAYgAQYogQYiwNItD5QhwZYrT1wAXgAkAEAmAHcAqABiDmqAQcyLTEwLjE0uAEDyAEA-AEBmAIZoALHO6gCFMICBxAjGCcY6gLCAhYQABgDGLQCGOUCGOoCGIwDGI8B2AEBwgIWEC4YAxi0AhjlAhjqAhiMAxiPAdgBAcICChAjGIAEGCcYigXCAgQQIxgnwgIUEC4YgAQYkQIYxwEYmAUYigUYrwHCAgsQABiABBixAxiDAcICDhAuGIAEGLEDGIMBGIoFwgILEC4YgAQYsQMYgwHCAgsQLhiABBiRAhiKBcICERAuGIAEGJECGMcBGIoFGK8BwgIKEAAYgAQYQxiKBcICDRAAGIAEGLEDGEMYigXCAgsQABiABBiRAhiKBcICExAuGIAEGLEDGEMYgwEY1AIYigXCAhAQLhiABBhDGMcBGIoFGK8BwgILEAAYgAQYkgMYigXCAggQABiABBixA8ICBRAAGIAEwgIIEAAYgAQYyQPCAg0QABiABBixAxhGGP8BwgIZEAAYgAQYsQMYRhj_ARiXBRiMBRjdBNgBAsICBBAAGAPCAgoQABiABBgUGIcCwgIIEAAYFhgKGB7CAggQABiABBiiBJgDEOIDBRIBMSBAugYGCAEQARgLugYGCAIQARgTkgcIMS4wLjQuMjCgB4_GAQ&sclient=gws-wiz-serp",
            "time_usec": 1715847999361404,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.corinthia.com/static/img/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "The Best Summer Events In Budapest | Destination Guides | Corinthia Budapest | Corinthia",
            "url": "https://www.corinthia.com/en-gb/budapest/discover-budapest/the-best-summer-events-in-budapest/#:~:text=Usually%20held%20during%20July%20and,swing%20and%20authentic%20gypsy%20melodies.",
            "time_usec": 1715847975844689,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "music in budapest in july - Google Search",
            "url": "https://www.google.com/search?q=music+in+budapest+in+july+&sca_esv=94fa641d5e31d942&sxsrf=ADLYWIKRwO9ZB1TfgOI45gzNnBoU6xiVNA%3A1715847104597&ei=wL9FZtWDJL-L0PEPgN284Aw&ved=0ahUKEwjV46HJ3JGGAxW_BTQIHYAuD8wQ4dUDCBE&uact=5&oq=music+in+budapest+in+july+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIhptdXNpYyBpbiBidWRhcGVzdCBpbiBqdWx5IDIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYogQYiwMyCxAAGIAEGKIEGIsDMgsQABiABBiiBBiLAzILEAAYgAQYogQYiwNItD5QhwZYrT1wAXgAkAEAmAHcAqABiDmqAQcyLTEwLjE0uAEDyAEA-AEBmAIZoALHO6gCFMICBxAjGCcY6gLCAhYQABgDGLQCGOUCGOoCGIwDGI8B2AEBwgIWEC4YAxi0AhjlAhjqAhiMAxiPAdgBAcICChAjGIAEGCcYigXCAgQQIxgnwgIUEC4YgAQYkQIYxwEYmAUYigUYrwHCAgsQABiABBixAxiDAcICDhAuGIAEGLEDGIMBGIoFwgILEC4YgAQYsQMYgwHCAgsQLhiABBiRAhiKBcICERAuGIAEGJECGMcBGIoFGK8BwgIKEAAYgAQYQxiKBcICDRAAGIAEGLEDGEMYigXCAgsQABiABBiRAhiKBcICExAuGIAEGLEDGEMYgwEY1AIYigXCAhAQLhiABBhDGMcBGIoFGK8BwgILEAAYgAQYkgMYigXCAggQABiABBixA8ICBRAAGIAEwgIIEAAYgAQYyQPCAg0QABiABBixAxhGGP8BwgIZEAAYgAQYsQMYRhj_ARiXBRiMBRjdBNgBAsICBBAAGAPCAgoQABiABBgUGIcCwgIIEAAYFhgKGB7CAggQABiABBiiBJgDEOIDBRIBMSBAugYGCAEQARgLugYGCAIQARgTkgcIMS4wLjQuMjCgB4_GAQ&sclient=gws-wiz-serp",
            "time_usec": 1715847963421232,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "art scene in budpest - Google Search",
            "url": "https://www.google.com/search?q=art+scene+in+budpest&oq=art+scene+in+budpest+&aqs=chrome..69i64j0i22i30j0i512i546j0i395i512i546l3j69i57.7586j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715847948409158,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://havefun.travel/things-to-do/arts-and-culture/budapest-contemporary-art-scene/",
            "time_usec": 1715847946564940,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "art scene in budpest - Google Search",
            "url": "https://www.google.com/search?q=art+scene+in+budpest&oq=art+scene+in+budpest+&aqs=chrome..69i64j0i22i30j0i512i546j0i395i512i546l3j69i57.7586j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715847349524691,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://budapestflow.com/a-guide-to-budapests-alternative-art-scene/",
            "time_usec": 1715847347290711,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "YOUR ARRIVAL IN FLORENCE: MORE INFORMATION & LOST LUGGAGE - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#search/isi/FMfcgzGxTNsckMfRhHKDktXsXfLHphpn",
            "time_usec": 1715847131727947,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Search results - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#search/isi",
            "time_usec": 1715847125123059,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "art scene in budpest - Google Search",
            "url": "https://www.google.com/search?q=art+scene+in+budpest&oq=art+scene+in+budpest+&aqs=chrome..69i64j0i22i30j0i512i546j0i395i512i546l3j69i57.7586j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715847105199580,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715847095109556,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "maverick urban lodge budapest - Google Search",
            "url": "https://www.google.com/search?q=maverick+urban+lodge+budapest&sca_esv=c22fddfe247c1d12&sxsrf=ADLYWIJYkwf_ln0a9R8eDu7nCoHYkZGLnw%3A1715845446286&ei=RrlFZsGPEKmO0PEP37uO4Aw&oq=maver&gs_lp=Egxnd3Mtd2l6LXNlcnAiBW1hdmVyKgIIATIEECMYJzIKECMYgAQYJxiKBTIQEAAYgAQYsQMYQxiDARiKBTILEC4YgAQYsQMYgwEyChAAGIAEGEMYigUyFBAuGIAEGJECGMcBGJgFGIoFGK8BMhQQLhiABBiRAhjHARiYBRiKBRivATILEAAYgAQYsQMYgwEyEBAAGIAEGLEDGEMYgwEYigUyCxAAGIAEGLEDGIMBSKI1UKYJWJUbcAN4AJABAJgBwwKgAesQqgEFMi0xLja4AQHIAQD4AQGYAgqgAp8SqAIUwgIHECMYJxjqAsICFhAAGAMYtAIY5QIY6gIYjAMYjwHYAQHCAhYQLhgDGLQCGOUCGOoCGIwDGI8B2AEBwgIREAAYgAQYkQIYsQMYgwEYigXCAgsQABiABBiRAhiKBcICDhAAGIAEGLEDGIMBGIoFwgIOEC4YgAQYsQMY0QMYxwHCAgoQLhiABBhDGIoFwgIREC4YgAQYsQMY0QMYgwEYxwHCAggQABiABBixA8ICDhAuGIAEGLEDGMcBGK8BwgIFEAAYgATCAgcQLhiABBgKmAMa4gMFEgExIEC6BgYIARABGAuSBwczLjAuMS42oAevbg&sclient=gws-wiz-serp",
            "time_usec": 1715847092980579,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "maverick urban lodge budapest - Google Search",
            "url": "https://www.google.com/search?q=maverick+urban+lodge+budapest&sca_esv=c22fddfe247c1d12&sxsrf=ADLYWIJYkwf_ln0a9R8eDu7nCoHYkZGLnw%3A1715845446286&ei=RrlFZsGPEKmO0PEP37uO4Aw&oq=maver&gs_lp=Egxnd3Mtd2l6LXNlcnAiBW1hdmVyKgIIATIEECMYJzIKECMYgAQYJxiKBTIQEAAYgAQYsQMYQxiDARiKBTILEC4YgAQYsQMYgwEyChAAGIAEGEMYigUyFBAuGIAEGJECGMcBGJgFGIoFGK8BMhQQLhiABBiRAhjHARiYBRiKBRivATILEAAYgAQYsQMYgwEyEBAAGIAEGLEDGEMYgwEYigUyCxAAGIAEGLEDGIMBSKI1UKYJWJUbcAN4AJABAJgBwwKgAesQqgEFMi0xLja4AQHIAQD4AQGYAgqgAp8SqAIUwgIHECMYJxjqAsICFhAAGAMYtAIY5QIY6gIYjAMYjwHYAQHCAhYQLhgDGLQCGOUCGOoCGIwDGI8B2AEBwgIREAAYgAQYkQIYsQMYgwEYigXCAgsQABiABBiRAhiKBcICDhAAGIAEGLEDGIMBGIoFwgIOEC4YgAQYsQMY0QMYxwHCAgoQLhiABBhDGIoFwgIREC4YgAQYsQMY0QMYgwEYxwHCAggQABiABBixA8ICDhAuGIAEGLEDGMcBGK8BwgIFEAAYgATCAgcQLhiABBgKmAMa4gMFEgExIEC6BgYIARABGAuSBwczLjAuMS42oAevbg&sclient=gws-wiz-serp#lrd=0x4741dd58ac68d971:0x2eab4f2ec9ddec8a,1,,,,",
            "time_usec": 1715847018776812,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "maverick urban lodge budapest - Google Search",
            "url": "https://www.google.com/search?q=maverick+urban+lodge+budapest&sca_esv=c22fddfe247c1d12&sxsrf=ADLYWIJYkwf_ln0a9R8eDu7nCoHYkZGLnw%3A1715845446286&ei=RrlFZsGPEKmO0PEP37uO4Aw&oq=maver&gs_lp=Egxnd3Mtd2l6LXNlcnAiBW1hdmVyKgIIATIEECMYJzIKECMYgAQYJxiKBTIQEAAYgAQYsQMYQxiDARiKBTILEC4YgAQYsQMYgwEyChAAGIAEGEMYigUyFBAuGIAEGJECGMcBGJgFGIoFGK8BMhQQLhiABBiRAhjHARiYBRiKBRivATILEAAYgAQYsQMYgwEyEBAAGIAEGLEDGEMYgwEYigUyCxAAGIAEGLEDGIMBSKI1UKYJWJUbcAN4AJABAJgBwwKgAesQqgEFMi0xLja4AQHIAQD4AQGYAgqgAp8SqAIUwgIHECMYJxjqAsICFhAAGAMYtAIY5QIY6gIYjAMYjwHYAQHCAhYQLhgDGLQCGOUCGOoCGIwDGI8B2AEBwgIREAAYgAQYkQIYsQMYgwEYigXCAgsQABiABBiRAhiKBcICDhAAGIAEGLEDGIMBGIoFwgIOEC4YgAQYsQMY0QMYxwHCAgoQLhiABBhDGIoFwgIREC4YgAQYsQMY0QMYgwEYxwHCAggQABiABBixA8ICDhAuGIAEGLEDGMcBGK8BwgIFEAAYgATCAgcQLhiABBgKmAMa4gMFEgExIEC6BgYIARABGAuSBwczLjAuMS42oAevbg&sclient=gws-wiz-serp",
            "time_usec": 1715847015191988,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "maverick urban lodge budapest - Google Search",
            "url": "https://www.google.com/search?q=maverick+urban+lodge+budapest&sca_esv=c22fddfe247c1d12&sxsrf=ADLYWIJYkwf_ln0a9R8eDu7nCoHYkZGLnw%3A1715845446286&ei=RrlFZsGPEKmO0PEP37uO4Aw&oq=maver&gs_lp=Egxnd3Mtd2l6LXNlcnAiBW1hdmVyKgIIATIEECMYJzIKECMYgAQYJxiKBTIQEAAYgAQYsQMYQxiDARiKBTILEC4YgAQYsQMYgwEyChAAGIAEGEMYigUyFBAuGIAEGJECGMcBGJgFGIoFGK8BMhQQLhiABBiRAhjHARiYBRiKBRivATILEAAYgAQYsQMYgwEyEBAAGIAEGLEDGEMYgwEYigUyCxAAGIAEGLEDGIMBSKI1UKYJWJUbcAN4AJABAJgBwwKgAesQqgEFMi0xLja4AQHIAQD4AQGYAgqgAp8SqAIUwgIHECMYJxjqAsICFhAAGAMYtAIY5QIY6gIYjAMYjwHYAQHCAhYQLhgDGLQCGOUCGOoCGIwDGI8B2AEBwgIREAAYgAQYkQIYsQMYgwEYigXCAgsQABiABBiRAhiKBcICDhAAGIAEGLEDGIMBGIoFwgIOEC4YgAQYsQMY0QMYxwHCAgoQLhiABBhDGIoFwgIREC4YgAQYsQMY0QMYgwEYxwHCAggQABiABBixA8ICDhAuGIAEGLEDGMcBGK8BwgIFEAAYgATCAgcQLhiABBgKmAMa4gMFEgExIEC6BgYIARABGAuSBwczLjAuMS42oAevbg&sclient=gws-wiz-serp",
            "time_usec": 1715845653113278,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how far between gradio party hostel and vintageand giselle vintage doubles - Google Search",
            "url": "https://www.google.com/search?q=how+far+between+gradio+party+hostel+and+vintageand+giselle+vintage+doubles&oq=how+far+between+gradio+party+hostel+and+vintageand+giselle+vintage+doubles&aqs=chrome..69i64j69i57.7389j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715845447793956,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hotel Stachus - Google Maps",
            "url": "https://www.google.com/maps/place/Hotel+Stachus/@48.1433161,11.51467,12z/data=!4m9!3m8!1s0x479e75f76f1fc155:0x83ae38306881a206!5m2!4m1!1i2!8m2!3d48.1391754!4d11.5633128!16s%2Fg%2F11hv448yv?entry=ttu",
            "time_usec": 1715845354021078,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715845331784923,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Grandio Jungle Bar - Google Maps",
            "url": "https://www.google.com/maps/place/Grandio+Jungle+Bar/@47.4890011,19.0571631,16.03z/data=!4m11!3m10!1s0x4741dc67f98453ad:0xf7f589162154c7e0!5m4!1s2024-07-08!2i3!4m1!1i1!8m2!3d47.4969444!4d19.0652778!16s%2Fg%2F1tjt0q8t?entry=ttu",
            "time_usec": 1715845317259748,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html",
            "time_usec": 1715845209322431,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html",
            "time_usec": 1715845200981374,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html",
            "time_usec": 1715845190935341,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html",
            "time_usec": 1715845179931104,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html",
            "time_usec": 1715845144177948,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html",
            "time_usec": 1715845142445787,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html",
            "time_usec": 1715845129492033,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html",
            "time_usec": 1715845100888297,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html",
            "time_usec": 1715845089721706,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html",
            "time_usec": 1715845082154285,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html",
            "time_usec": 1715845032780056,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html",
            "time_usec": 1715845026728006,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html",
            "time_usec": 1715845015129064,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html#/media/2218961/?albumid=101&type=0&category=101",
            "time_usec": 1715845000800760,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html#/media/2218961/?albumid=101&type=0&category=101",
            "time_usec": 1715844990086241,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "GRANDIO PARTY HOSTEL - Reviews (Budapest, Hungary)",
            "url": "https://www.tripadvisor.com/Hotel_Review-g274887-d2218961-Reviews-Grandio_Party_Hostel-Budapest_Central_Hungary.html",
            "time_usec": 1715844988193747,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "grandio party hostel budapest - Google Search",
            "url": "https://www.google.com/search?q=grandio+party+hostel+budapest&oq=grandio+party+hostel+&aqs=chrome.0.69i59j46i175i199i512i664i668i670j69i64j0i22i30l3j69i60l2.10222j1j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715844967431790,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Wombat's City Hostel Budapest",
            "url": "https://www.expedia.com/Budapest-Hotels-Wombats-The-City-Hostel-Budapest.h20070854.Hotel-Information?chkin=2024-07-08&chkout=2024-07-11&x_pwa=1&rfrr=HSR&pwa_ts=1715844802694&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=715&destination=Budapest%2C%20Hungary&destType=MARKET&neighborhoodId=699504603700457472&latLong=47.49316%2C19.0556&lodging=HOSTEL&sort=RECOMMENDED&top_dp=27&top_cur=USD&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798325764.b1116152237393.g1aud-2068928983903%3Akwd-310532979073.e1c.m1Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB.r108a35aa7efc4598500e649c693cbd1d77549a93288e7d12a546ce58a05676187.c1.j19004425.k1.d1663164254443.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&userIntent=&selectedRoomType=216660615&selectedRatePlan=264247546&searchId=a994d3d8-fecf-4f27-82a1-a51536d00f2c&propertyName=Wombat%27s%20City%20Hostel%20Budapest",
            "time_usec": 1715844883385305,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Wombat's City Hostel Budapest",
            "url": "https://www.expedia.com/Budapest-Hotels-Wombats-The-City-Hostel-Budapest.h20070854.Hotel-Information?chkin=2024-07-08&chkout=2024-07-11&x_pwa=1&rfrr=HSR&pwa_ts=1715844802694&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=715&destination=Budapest%2C%20Hungary&destType=MARKET&neighborhoodId=699504603700457472&latLong=47.49316%2C19.0556&lodging=HOSTEL&sort=RECOMMENDED&top_dp=27&top_cur=USD&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798325764.b1116152237393.g1aud-2068928983903%3Akwd-310532979073.e1c.m1Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB.r108a35aa7efc4598500e649c693cbd1d77549a93288e7d12a546ce58a05676187.c1.j19004425.k1.d1663164254443.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&userIntent=&selectedRoomType=216660615&selectedRatePlan=264247546&searchId=a994d3d8-fecf-4f27-82a1-a51536d00f2c&propertyName=Wombat%27s%20City%20Hostel%20Budapest&pwaThumbnailDialog=thumbnail-gallery",
            "time_usec": 1715844880968340,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Wombat's City Hostel Budapest",
            "url": "https://www.expedia.com/Budapest-Hotels-Wombats-The-City-Hostel-Budapest.h20070854.Hotel-Information?chkin=2024-07-08&chkout=2024-07-11&x_pwa=1&rfrr=HSR&pwa_ts=1715844802694&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=715&destination=Budapest%2C%20Hungary&destType=MARKET&neighborhoodId=699504603700457472&latLong=47.49316%2C19.0556&lodging=HOSTEL&sort=RECOMMENDED&top_dp=27&top_cur=USD&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798325764.b1116152237393.g1aud-2068928983903%3Akwd-310532979073.e1c.m1Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB.r108a35aa7efc4598500e649c693cbd1d77549a93288e7d12a546ce58a05676187.c1.j19004425.k1.d1663164254443.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&userIntent=&selectedRoomType=216660615&selectedRatePlan=264247546&searchId=a994d3d8-fecf-4f27-82a1-a51536d00f2c&propertyName=Wombat%27s%20City%20Hostel%20Budapest&pwaThumbnailDialog=thumbnail-gallery&pwaDialogNested=media-gallery",
            "time_usec": 1715844864560449,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Wombat's City Hostel Budapest",
            "url": "https://www.expedia.com/Budapest-Hotels-Wombats-The-City-Hostel-Budapest.h20070854.Hotel-Information?chkin=2024-07-08&chkout=2024-07-11&x_pwa=1&rfrr=HSR&pwa_ts=1715844802694&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=715&destination=Budapest%2C%20Hungary&destType=MARKET&neighborhoodId=699504603700457472&latLong=47.49316%2C19.0556&lodging=HOSTEL&sort=RECOMMENDED&top_dp=27&top_cur=USD&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798325764.b1116152237393.g1aud-2068928983903%3Akwd-310532979073.e1c.m1Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB.r108a35aa7efc4598500e649c693cbd1d77549a93288e7d12a546ce58a05676187.c1.j19004425.k1.d1663164254443.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&userIntent=&selectedRoomType=216660615&selectedRatePlan=264247546&searchId=a994d3d8-fecf-4f27-82a1-a51536d00f2c&propertyName=Wombat%27s%20City%20Hostel%20Budapest&pwaThumbnailDialog=thumbnail-gallery",
            "time_usec": 1715844849923236,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Wombat's City Hostel Budapest",
            "url": "https://www.expedia.com/Budapest-Hotels-Wombats-The-City-Hostel-Budapest.h20070854.Hotel-Information?chkin=2024-07-08&chkout=2024-07-11&x_pwa=1&rfrr=HSR&pwa_ts=1715844802694&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=715&destination=Budapest%2C%20Hungary&destType=MARKET&neighborhoodId=699504603700457472&latLong=47.49316%2C19.0556&lodging=HOSTEL&sort=RECOMMENDED&top_dp=27&top_cur=USD&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798325764.b1116152237393.g1aud-2068928983903%3Akwd-310532979073.e1c.m1Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB.r108a35aa7efc4598500e649c693cbd1d77549a93288e7d12a546ce58a05676187.c1.j19004425.k1.d1663164254443.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&userIntent=&selectedRoomType=216660615&selectedRatePlan=264247546&searchId=a994d3d8-fecf-4f27-82a1-a51536d00f2c&propertyName=Wombat%27s%20City%20Hostel%20Budapest",
            "time_usec": 1715844847717719,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Budapest, Hungary Hotel Search Results",
            "url": "https://www.expedia.com/Hotel-Search?regionId=715&locale=en_US&siteid=1&lodging=HOSTEL&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798325764.b1116152237393.g1aud-2068928983903%3Akwd-310532979073.e1c.m1Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB.r108a35aa7efc4598500e649c693cbd1d77549a93288e7d12a546ce58a05676187.c1.j19004425.k1.d1663164254443.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&gad_source=1&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB&destination=Budapest%2C%20Hungary&theme=&userIntent=&useRewards=true&sort=RECOMMENDED&latLong=&adults=1&children=&pwaDialog=&mapBounds=&allowPreAppliedFilters=False&startDate=2024-07-08&endDate=2024-07-11",
            "time_usec": 1715844801923797,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Budapest, Hungary Hotel Search Results",
            "url": "https://www.expedia.com/Hotel-Search?regionId=715&locale=en_US&siteid=1&lodging=HOSTEL&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798325764.b1116152237393.g1aud-2068928983903%3Akwd-310532979073.e1c.m1Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB.r108a35aa7efc4598500e649c693cbd1d77549a93288e7d12a546ce58a05676187.c1.j19004425.k1.d1663164254443.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&gad_source=1&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB&destination=Budapest%2C%20Hungary&theme=&userIntent=&useRewards=true&sort=RECOMMENDED&latLong=&adults=1&children=&pwaDialog=&mapBounds=&allowPreAppliedFilters=False&flexibility=2_DAY_LOWER&flexibility=3_DAY_UPPER&searchRange=2024-07-01_2024-07-31",
            "time_usec": 1715844776087092,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Budapest, Hungary Hotel Search Results",
            "url": "https://www.expedia.com/Hotel-Search?regionId=715&locale=en_US&siteid=1&lodging=HOSTEL&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798325764.b1116152237393.g1aud-2068928983903%3Akwd-310532979073.e1c.m1Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB.r108a35aa7efc4598500e649c693cbd1d77549a93288e7d12a546ce58a05676187.c1.j19004425.k1.d1663164254443.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&gad_source=1&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB&destination=Budapest%2C+Hungary&theme=&userIntent=&useRewards=true&sort=RECOMMENDED&latLong=&adults=1&children=&pwaDialog=&mapBounds=&allowPreAppliedFilters=False&flexibility=2_DAY_LOWER&flexibility=3_DAY_UPPER&searchRange=2024-07-01_2024-07-31",
            "time_usec": 1715844773652701,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Budapest, Hungary Hotel Search Results",
            "url": "https://www.expedia.com/Hotel-Search?regionId=715&locale=en_US&siteid=1&lodging=HOSTEL&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798325764.b1116152237393.g1aud-2068928983903%3Akwd-310532979073.e1c.m1Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB.r108a35aa7efc4598500e649c693cbd1d77549a93288e7d12a546ce58a05676187.c1.j19004425.k1.d1663164254443.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&gad_source=1&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB&destination=Budapest%2C%20Hungary&theme=&userIntent=&useRewards=true&sort=RECOMMENDED&latLong=&adults=1&children=&pwaDialog=&mapBounds=&allowPreAppliedFilters=False&flexibility=1_DAY&searchRange=2024-05-01_2024-05-31&searchRange=2024-06-01_2024-06-30",
            "time_usec": 1715844768599607,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Budapest, Hungary Hotel Search Results",
            "url": "https://www.expedia.com/Hotel-Search?regionId=715&locale=en_US&siteid=1&lodging=HOSTEL&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798325764.b1116152237393.g1aud-2068928983903%3Akwd-310532979073.e1c.m1Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB.r108a35aa7efc4598500e649c693cbd1d77549a93288e7d12a546ce58a05676187.c1.j19004425.k1.d1663164254443.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&gad_source=1&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB&startDate=2024-05-30&endDate=2024-05-31&destination=Budapest%2C%20Hungary&theme=&userIntent=&useRewards=true&sort=RECOMMENDED",
            "time_usec": 1715844759483368,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "grandio party hostel budapest - Google Search",
            "url": "https://www.google.com/search?q=grandio+party+hostel+budapest&oq=grandio+party+hostel+&aqs=chrome.0.0i20i263i355i512j46i20i175i199i263i512i664i668i670j69i64j0i512j0i22i30j69i60l3.10269j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715844750601482,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "grandio party hostel budapest - Google Search",
            "url": "https://www.google.com/search?q=grandio+party+hostel+budapest&oq=grandio+party+hostel+&aqs=chrome.0.0i20i263i355i512j46i20i175i199i263i512i664i668i670j69i64j0i512j0i22i30j69i60l3.10269j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715844737280563,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "",
            "url": "https://www.expedia.com/Hotel-Search?regionId=715&locale=en_US&siteid=1&lodging=HOSTEL&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798325764.b1116152237393.g1aud-2068928983903:kwd-310532979073.e1c.m1Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB.r108a35aa7efc4598500e649c693cbd1d77549a93288e7d12a546ce58a05676187.c1.j19004425.k1.d1663164254443.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&gad_source=1&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8qfQnl8G_8Z_L6Tt02iWZ5TTi8ijoQDdZNTGJlEmx72BCaXzHPyY98aAorpEALw_wcB",
            "time_usec": 1715844735408054,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "grandio party hostel budapest - Google Search",
            "url": "https://www.google.com/search?q=grandio+party+hostel+budapest&oq=grandio+party+hostel+&aqs=chrome.0.0i20i263i355i512j46i20i175i199i263i512i664i668i670j69i64j0i512j0i22i30j69i60l3.10269j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715844724946909,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715844712413580,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Grandio Jungle Bar - Google Maps",
            "url": "https://www.google.com/maps/place/Grandio+Jungle+Bar/@47.4969276,19.0655321,17z/data=!4m11!3m10!1s0x4741dc67f98453ad:0xf7f589162154c7e0!5m4!1s2024-07-08!2i3!4m1!1i1!8m2!3d47.4969444!4d19.0652778!16s%2Fg%2F1tjt0q8t?entry=ttu",
            "time_usec": 1715844678026898,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Grandio Jungle Bar - Google Maps",
            "url": "https://www.google.com/maps/place/Grandio+Jungle+Bar/@47.4969276,19.0655321,3a,75y,90t/data=!3m9!1e2!3m6!1sAF1QipN7eOzbVzg42zEWSq7Xowk4ObdQjONTmKDe1O-K!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipN7eOzbVzg42zEWSq7Xowk4ObdQjONTmKDe1O-K%3Dw203-h270-k-no!7i3024!8i4032!5s0x4741dc67ff3ccb31:0xffaf30b4d808095b!4m12!3m11!1s0x4741dc67f98453ad:0xf7f589162154c7e0!5m4!1s2024-07-08!2i3!4m1!1i1!8m2!3d47.4969444!4d19.0652778!10e5!16s%2Fg%2F1tjt0q8t?entry=ttu",
            "time_usec": 1715844552041430,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Grandio Jungle Bar - Google Maps",
            "url": "https://www.google.com/maps/place/Grandio+Jungle+Bar/@47.4969276,19.0655321,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipN7eOzbVzg42zEWSq7Xowk4ObdQjONTmKDe1O-K!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipN7eOzbVzg42zEWSq7Xowk4ObdQjONTmKDe1O-K%3Dw203-h270-k-no!7i3024!8i4032!4m12!3m11!1s0x4741dc67f98453ad:0xf7f589162154c7e0!5m4!1s2024-07-08!2i3!4m1!1i2!8m2!3d47.4969444!4d19.0652778!10e5!16s%2Fg%2F1tjt0q8t?entry=ttu",
            "time_usec": 1715844512358898,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Grandio Jungle Bar - Google Maps",
            "url": "https://www.google.com/maps/place/Grandio+Jungle+Bar/@47.4969727,19.0653149,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipO4cJigsrvaJVF0NTy4QO1QN_1KcFwxEKGTEfwi!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipO4cJigsrvaJVF0NTy4QO1QN_1KcFwxEKGTEfwi%3Dw203-h152-k-no!7i2560!8i1920!4m12!3m11!1s0x4741dc67f98453ad:0xf7f589162154c7e0!5m4!1s2024-07-08!2i3!4m1!1i2!8m2!3d47.4969444!4d19.0652778!10e5!16s%2Fg%2F1tjt0q8t?entry=ttu",
            "time_usec": 1715844502682556,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Grandio Jungle Bar - Google Maps",
            "url": "https://www.google.com/maps/place/Grandio+Jungle+Bar/@47.4969444,19.0652778,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipPFmguVr_qHbxinXC7qT8VTqiSBi789rd7iTmUm!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipPFmguVr_qHbxinXC7qT8VTqiSBi789rd7iTmUm%3Dw203-h152-k-no!7i4160!8i3120!4m12!3m11!1s0x4741dc67f98453ad:0xf7f589162154c7e0!5m4!1s2024-07-08!2i3!4m1!1i2!8m2!3d47.4969444!4d19.0652778!10e5!16s%2Fg%2F1tjt0q8t?entry=ttu",
            "time_usec": 1715844492137854,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Maps",
            "url": "https://www.google.com/maps/place/Grandio+Jungle+Bar/@47.4969276,19.0655321,3a,115.4y,90t/data=!3m8!1e2!3m6!1shttps:%2F%2Fdynamic-media-cdn.tripadvisor.com%2Fmedia%2Fphoto-o%2F01%2Ff3%2F75%2F9b%2Fgrandio-party-hostel.jpg!2e7!3e27!6shttps:%2F%2Flh3.googleusercontent.com%2Fgps-proxy%2FALd4DhHJ_4iwmn3al9wJcdDNxlg0fVpQelxrVoP510wPcj9QQRPeTHFSmbSHgu4TrHpekTfYwsMW0DC6niKX0EY52NxHCiQblFuSob-DpDhNl691Jy-HOQeYwkYlWMcPS4FX4J8kql93_k9WJwyftbIG-z-6GJR1YRFRePkV1PNiWuWAVZD9vk-XZbGD%3Dw153-h86-k-no!7i520!8i292!4m12!3m11!1s0x4741dc67f98453ad:0xf7f589162154c7e0!5m4!1s2024-07-08!2i3!4m1!1i2!8m2!3d47.4969444!4d19.0652778!10e5!16s%2Fg%2F1tjt0q8t?entry=ttu",
            "time_usec": 1715844483073546,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Grandio Jungle Bar - Google Maps",
            "url": "https://www.google.com/maps/place/Grandio+Jungle+Bar/@47.496948,19.0626975,17z/data=!3m2!4b1!5s0x4741dc67ff3ccb31:0xffaf30b4d808095b!4m11!3m10!1s0x4741dc67f98453ad:0xf7f589162154c7e0!5m4!1s2024-07-08!2i3!4m1!1i2!8m2!3d47.4969444!4d19.0652778!16s%2Fg%2F1tjt0q8t?entry=ttu",
            "time_usec": 1715844472412837,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Maps",
            "url": "https://www.google.com/maps/@47.4985143,19.0505148,14.15z?entry=ttu",
            "time_usec": 1715844449778013,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Carpe Noctem Hostel - Google Maps",
            "url": "https://www.google.com/maps/place/Carpe+Noctem+Hostel/@47.4985143,19.0505148,14.15z/data=!4m11!3m10!1s0x4741dc72b8d1110f:0xffa919161d04c85f!5m4!1s2024-07-08!2i3!4m1!1i2!8m2!3d47.5087428!4d19.0596343!16s%2Fg%2F1tdwj8pc?entry=ttu",
            "time_usec": 1715844355498074,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Carpe Noctem Hostel - Google Maps",
            "url": "https://www.google.com/maps/place/Carpe+Noctem+Hostel/@47.5050601,19.0481893,14.15z/data=!4m11!3m10!1s0x4741dc72b8d1110f:0xffa919161d04c85f!5m4!1s2024-07-08!2i3!4m1!1i2!8m2!3d47.5087428!4d19.0596343!16s%2Fg%2F1tdwj8pc?entry=ttu",
            "time_usec": 1715844351649276,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Carpe Noctem Hostel - Google Maps",
            "url": "https://www.google.com/maps/place/Carpe+Noctem+Hostel/@47.5087464,19.057054,17z/data=!3m1!4b1!4m11!3m10!1s0x4741dc72b8d1110f:0xffa919161d04c85f!5m4!1s2024-07-08!2i3!4m1!1i2!8m2!3d47.5087428!4d19.0596343!16s%2Fg%2F1tdwj8pc?entry=ttu",
            "time_usec": 1715844345140040,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Maps",
            "url": "https://www.google.com/maps/@47.4924338,19.0458103,15.36z?entry=ttu",
            "time_usec": 1715844337635326,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.thebrokebackpacker.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Where to Stay in Budapest (Guide to the Best Places in 2024)",
            "url": "https://www.thebrokebackpacker.com/where-to-stay-in-budapest-hungary/",
            "time_usec": 1715844328730260,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.thebrokebackpacker.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "5 EPIC Party Hostels in Budapest [TOP PICKS 2024]",
            "url": "https://www.thebrokebackpacker.com/party-hostels-in-budapest/",
            "time_usec": 1715844266563206,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "most fun budapest hostels for social - Google Search",
            "url": "https://www.google.com/search?q=most+fun+budapest+hostels+for+social&sca_esv=c22fddfe247c1d12&sxsrf=ADLYWIIBhIiK8JaiNIidxtk1k9v4IwDQMA%3A1715843745844&ei=obJFZteTM9DK0PEPl56E-A8&ved=0ahUKEwiX6NeH0JGGAxVQJTQIHRcPAf8Q4dUDCBE&uact=5&oq=most+fun+budapest+hostels+for+social&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgBIiRtb3N0IGZ1biBidWRhcGVzdCBob3N0ZWxzIGZvciBzb2NpYWwyCBAAGIAEGKIEMggQABiABBiiBDIIEAAYgAQYogQyCxAAGIAEGKIEGIsDSKAOUNkFWMYKcAB4A5ABAJgBrwKgAdoPqgEFMi02LjG4AQPIAQD4AQGYAgOgAscCwgIEEAAYR5gDAOIDBRIBMSBAiAYBkAYIkgcFMi4zLTGgB8cY&sclient=gws-wiz-serp",
            "time_usec": 1715844263208217,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://partyhostels.org/Budapest?utm_source=google&utm_medium=cpc&gad_source=1&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8r5gOhr4b0CBdmv1ukQeCg3mpb6ehRgoHxgG_H3Jd3zqINLwc_Zp5waAt06EALw_wcB",
            "time_usec": 1715844261153322,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Maverick Urban Lodge - Hostel",
            "url": "https://www.expedia.com/Budapest-Hotels-Maverick-Student-Lodge.h44237956.Hotel-Information?chkin=2024-07-08&chkout=2024-07-11&x_pwa=1&rfrr=HSR&pwa_ts=1715844000791&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=715&destination=Budapest%2C+Hungary&destType=MARKET&neighborhoodId=553248635976382361&selected=44237956&latLong=47.49316%2C19.0556&sort=RECOMMENDED&top_dp=34&top_cur=USD&userIntent=&selectedRoomType=218833005&selectedRatePlan=278280862&searchId=98bb73aa-f903-4894-ae34-b3518649754b&propertyName=Maverick+Urban+Lodge+-+Hostel",
            "time_usec": 1715844189101245,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Giselle Vintage Doubles - Google Maps",
            "url": "https://www.google.com/maps/place/Giselle+Vintage+Doubles/@47.4924338,19.0458103,15.36z/data=!4m11!3m10!1s0x4741dc44055eb4e9:0xadbedacd289e9ed1!5m4!1s2024-07-08!2i3!4m1!1i2!8m2!3d47.4927869!4d19.0554446!16s%2Fg%2F11jz61ptdf?entry=ttu",
            "time_usec": 1715844169635980,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Giselle Vintage Doubles - Google Maps",
            "url": "https://www.google.com/maps/place/Giselle+Vintage+Doubles/@47.491018,19.0422696,15z/data=!4m11!3m10!1s0x4741dc44055eb4e9:0xadbedacd289e9ed1!5m4!1s2024-07-08!2i3!4m1!1i2!8m2!3d47.4927869!4d19.0554446!16s%2Fg%2F11jz61ptdf?entry=ttu",
            "time_usec": 1715844133491734,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Maps",
            "url": "https://www.google.com/maps/place/Giselle+Vintage+Doubles/@47.4927869,19.0554446,15z/data=!4m2!3m1!1s0x0:0xadbedacd289e9ed1?sa=X&ved=1t:2428&ictx=111",
            "time_usec": 1715844127486443,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "gaselle vintage doubles - Google Search",
            "url": "https://www.google.com/search?q=gaselle+vintage+doubles&oq=gaselle+vintage+doubles&aqs=chrome..69i64j0i13i512l6j0i13i30l3.14687j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715844119061499,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Maverick Urban Lodge - Hostel",
            "url": "https://www.expedia.com/Budapest-Hotels-Maverick-Student-Lodge.h44237956.Hotel-Information?chkin=2024-07-08&chkout=2024-07-11&x_pwa=1&rfrr=HSR&pwa_ts=1715844000791&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=715&destination=Budapest%2C%20Hungary&destType=MARKET&neighborhoodId=553248635976382361&selected=44237956&latLong=47.49316%2C19.0556&sort=RECOMMENDED&top_dp=34&top_cur=USD&userIntent=&selectedRoomType=218833005&selectedRatePlan=278280862&searchId=98bb73aa-f903-4894-ae34-b3518649754b&propertyName=Maverick%20Urban%20Lodge%20-%20Hostel&pwaOverlay=property-summary-map",
            "time_usec": 1715844076606766,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Maverick Urban Lodge - Hostel",
            "url": "https://www.expedia.com/Budapest-Hotels-Maverick-Student-Lodge.h44237956.Hotel-Information?chkin=2024-07-08&chkout=2024-07-11&x_pwa=1&rfrr=HSR&pwa_ts=1715844000791&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=715&destination=Budapest%2C+Hungary&destType=MARKET&neighborhoodId=553248635976382361&selected=44237956&latLong=47.49316%2C19.0556&sort=RECOMMENDED&top_dp=34&top_cur=USD&userIntent=&selectedRoomType=218833005&selectedRatePlan=278280862&searchId=98bb73aa-f903-4894-ae34-b3518649754b&propertyName=Maverick+Urban+Lodge+-+Hostel",
            "time_usec": 1715844068328623,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Maverick Urban Lodge - Hostel",
            "url": "https://www.expedia.com/Budapest-Hotels-Maverick-Student-Lodge.h44237956.Hotel-Information?chkin=2024-07-08&chkout=2024-07-11&x_pwa=1&rfrr=HSR&pwa_ts=1715844000791&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=715&destination=Budapest%2C%20Hungary&destType=MARKET&neighborhoodId=553248635976382361&selected=44237956&latLong=47.49316%2C19.0556&sort=RECOMMENDED&top_dp=34&top_cur=USD&userIntent=&selectedRoomType=218833005&selectedRatePlan=278280862&searchId=98bb73aa-f903-4894-ae34-b3518649754b&propertyName=Maverick%20Urban%20Lodge%20-%20Hostel&pwaThumbnailDialog=thumbnail-gallery",
            "time_usec": 1715844036338981,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Maverick Urban Lodge - Hostel",
            "url": "https://www.expedia.com/Budapest-Hotels-Maverick-Student-Lodge.h44237956.Hotel-Information?chkin=2024-07-08&chkout=2024-07-11&x_pwa=1&rfrr=HSR&pwa_ts=1715844000791&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=715&destination=Budapest%2C+Hungary&destType=MARKET&neighborhoodId=553248635976382361&selected=44237956&latLong=47.49316%2C19.0556&sort=RECOMMENDED&top_dp=34&top_cur=USD&userIntent=&selectedRoomType=218833005&selectedRatePlan=278280862&searchId=98bb73aa-f903-4894-ae34-b3518649754b&propertyName=Maverick+Urban+Lodge+-+Hostel",
            "time_usec": 1715844030714294,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Budapest, Hungary Hotel Search Results",
            "url": "https://www.expedia.com/Hotel-Search?destination=Budapest%2C%20Hungary&selected=44237956&d1=2024-07-08&startDate=2024-07-08&d2=2024-07-11&endDate=2024-07-11&adults=1&rooms=1&regionId=715&theme=&userIntent=&semdtl=&useRewards=true&sort=RECOMMENDED",
            "time_usec": 1715844004945381,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Maverick Urban Lodge - Hostel Reviews, Deals & Photos 2024 - Expedia",
            "url": "https://www.expedia.com/Budapest-Hotels-Maverick-Student-Lodge.h44237956.Hotel-Information?semcid=US.UB.GOOGLE.PT-DSA-c-EN.HOTEL&semdtl=a112063396151.b1116254839517.g1aud-2067245471241:dsa-980773961492.e1c.m1Cj0KCQjw3ZayBhDRARIsAPWzx8oF8OI1zucY30MjtPvty-7JIW2HN5QlgR3TeF0vmcxvT14TWZNHYWwaAn48EALw_wcB.r1.c1.j19004425.k1.d1673050934522.h1.i195083552297.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&gad_source=1&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8oF8OI1zucY30MjtPvty-7JIW2HN5QlgR3TeF0vmcxvT14TWZNHYWwaAn48EALw_wcB",
            "time_usec": 1715843981743217,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Maverick Urban Lodge - Hostel Reviews, Deals & Photos 2024 - Expedia",
            "url": "https://www.expedia.com/Budapest-Hotels-Maverick-Student-Lodge.h44237956.Hotel-Information?pwaDialog=uitk-date-selector-dialog-1714680325004-3&semcid=US.UB.GOOGLE.PT-DSA-c-EN.HOTEL&semdtl=a112063396151.b1116254839517.g1aud-2067245471241:dsa-980773961492.e1c.m1Cj0KCQjw3ZayBhDRARIsAPWzx8oF8OI1zucY30MjtPvty-7JIW2HN5QlgR3TeF0vmcxvT14TWZNHYWwaAn48EALw_wcB.r1.c1.j19004425.k1.d1673050934522.h1.i195083552297.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&gad_source=1&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8oF8OI1zucY30MjtPvty-7JIW2HN5QlgR3TeF0vmcxvT14TWZNHYWwaAn48EALw_wcB",
            "time_usec": 1715843977985564,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "maverick urban lodge budapest july 8-11 - Google Search",
            "url": "https://www.google.com/search?q=maverick+urban+lodge+budapest+july+8-11&sca_esv=c22fddfe247c1d12&sxsrf=ADLYWIKuyRFAQoTDUUQmkFqOWDMAK8ofXw%3A1715843835690&ei=-7JFZpLlKdW80PEPuNitwAo&hotel_occupancy=1&ved=0ahUKEwjSzsOy0JGGAxVVHjQIHThsC6gQ4dUDCBE&uact=5&oq=maverick+urban+lodge+budapest+july+8-11&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIidtYXZlcmljayB1cmJhbiBsb2RnZSBidWRhcGVzdCBqdWx5IDgtMTEyBRAhGKABMgUQIRigATIFECEYoAEyBRAhGKABMgUQIRigAUiiLVCrA1jKLHABeAGQAQCYAcYCoAHWEqoBBTItNC40uAEDyAEA-AEBmAIJoAKSE8ICChAAGLADGNYEGEfCAhAQABiABBiwAxhDGMkDGIoFwgIOEAAYgAQYsAMYkgMYigXCAgYQABgWGB7CAgsQABiABBiiBBiLA5gDAIgGAZAGCpIHBzEuMC4zLjWgB4Im&sclient=gws-wiz-serp",
            "time_usec": 1715843969803340,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.hostelworld.com/st/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hostelworld",
            "url": "https://www.hostelworld.com/st/404",
            "time_usec": 1715843951793254,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.hostelworld.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hostelworld",
            "url": "https://www.hostelworld.com/pwa/wds/hosteldetails.php/Carpe-Noctem/Budapest/24308?from=2024-07-08&to=2024-07-11&guests=1",
            "time_usec": 1715843950108241,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.hostelworld.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Maverick Urban Lodge, Budapest - Online Hostel Bookings, Ratings and Reviews",
            "url": "https://www.hostelworld.com/pwa/wds/hosteldetails.php/Maverick-Urban-Lodge/Budapest/303065?from=2024-07-08&to=2024-07-11&HostelNumber=303065&guests=1&Type=1&aff2=US_x_desktop&utm_medium=metasearch&utm_source=googlehotelfinder&utm_content=hpa_08_07_2024_3_localuniversal_303065_US_desktop_selected_11894995329_8024049375_1&utm_campaign=US&lead_time=53&campaign_id=11894995329&hpa_click_type=hotel&hpa_date_search_type=selected&hpa_site_property=localuniversal&hpa_occupancy=1&hpa_d_tax=4.54&hpa_d_total=117.95&hpa_rateplan_id=808554%7C1&hpa_u_country=US&hpa_u_currency=USD&hpa_u_lang=en&hpa_u_list_id=8024049375&number_of_guests=1&hpa_room_id=951461&hpa_pos=en&source=googlehotelads_x_desktop_x_11894995329&gad_source=1&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8oxE1TmH0KQJLcULFwI2QaMDBA_mU8yAOkNS7ZQ3jwlyL1mq313l-saAtz1EALw_wcB",
            "time_usec": 1715843873833909,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "maverick urban lodge budapest - Google Search",
            "url": "https://www.google.com/search?q=maverick+urban+lodge+budapest&hotel_occupancy=1#ahotel_dates=2024-07-08,3",
            "time_usec": 1715843861174666,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "maverick urban lodge budapest - Google Search",
            "url": "https://www.google.com/search?q=maverick+urban+lodge+budapest&hotel_occupancy=1#ahotel_dates=2024-07-05,3",
            "time_usec": 1715843846163831,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "most fun budapest hotels for social - Google Search",
            "url": "https://www.google.com/search?q=most+fun+bidapest+hotels+for+social&oq=most+fun+bidapest+hotels+for+social&aqs=chrome..69i64j69i57.11921j1j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715843804610036,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.hostelworld.com/st/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hostels In Budapest from \u20ac1 - Top Rated Hostels 2024",
            "url": "https://www.hostelworld.com/st/hostels/europe/hungary/budapest/?source=ppc_gooads_nonbrand_dsk_search_ds_en_us&network=g&campaign_id=20707737008&adgroup_id=155368645336&criteria_id=kwd-456063291&creative_id=680352557932&location_physical_id=9004425&location_interest_id&adposition&uniqueclickID=16061432790723724014&sub_keyword=best%20hostel%20budapest&sub_ad=b&sub_publisher=ADW&gclsrc=aw.ds&gad_source=1&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8onpEo7jlAH-qYNZ04W9V3Z4IDRlNuCNqxoiemaSOb631rfe-dfpyIaAuFYEALw_wcB",
            "time_usec": 1715843765237900,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "most fun budapest hostels for social - Google Search",
            "url": "https://www.google.com/search?q=most+fun+budapest+hostels+for+social&sca_esv=c22fddfe247c1d12&sxsrf=ADLYWIIBhIiK8JaiNIidxtk1k9v4IwDQMA%3A1715843745844&ei=obJFZteTM9DK0PEPl56E-A8&ved=0ahUKEwiX6NeH0JGGAxVQJTQIHRcPAf8Q4dUDCBE&uact=5&oq=most+fun+budapest+hostels+for+social&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgBIiRtb3N0IGZ1biBidWRhcGVzdCBob3N0ZWxzIGZvciBzb2NpYWwyCBAAGIAEGKIEMggQABiABBiiBDIIEAAYgAQYogQyCxAAGIAEGKIEGIsDSKAOUNkFWMYKcAB4A5ABAJgBrwKgAdoPqgEFMi02LjG4AQPIAQD4AQGYAgOgAscCwgIEEAAYR5gDAOIDBRIBMSBAiAYBkAYIkgcFMi4zLTGgB8cY&sclient=gws-wiz-serp",
            "time_usec": 1715843754955770,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "most fun budapest hotels for social - Google Search",
            "url": "https://www.google.com/search?q=most+fun+bidapest+hotels+for+social&oq=most+fun+bidapest+hotels+for+social&aqs=chrome..69i64j69i57.11921j1j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715843748037417,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715843727883718,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Booking.com: Hotels in Prague. Book your hotel now!",
            "url": "https://www.booking.com/searchresults.en-us.html?ss=Prague&ssne=Prague&ssne_untouched=Prague&highlighted_hotels=2527359&hp_sbox=1&label=metagha-link-MRUS-hotel-2527359_dev-desktop_los-3_bw-50_dow-Friday_defdate-0_room-0_gstadt-1_rateid-0_aud-7177173165_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240705_ppt-_lp-2840_r-7831999324863003215&sid=143ad315046fab268076e86c4894838a&aid=356929&lang=en-us&sb=1&src_elem=sb&src=hotel&dest_id=-553173&dest_type=city&checkin=2024-07-05&checkout=2024-07-08&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure",
            "time_usec": 1715843506788018,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MeetMe23, Prague \u2013 Updated 2024 Prices",
            "url": "https://www.booking.com/hotel/cz/meetme23.html?aid=356929&label=metagha-link-MRUS-hotel-2527359_dev-desktop_los-3_bw-50_dow-Friday_defdate-0_room-0_gstadt-1_rateid-0_aud-7177173165_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240705_ppt-_lp-2840_r-7831999324863003215&sid=143ad315046fab268076e86c4894838a&all_sr_blocks=252735908_103825146_0_2_0;checkin=2024-07-05;checkout=2024-07-08;dest_id=-553173;dest_type=city;dist=0;group_adults=1;group_children=0;hapos=1;highlighted_blocks=252735908_103825146_0_2_0;hpos=1;matching_block_id=252735908_103825146_0_2_0;no_rooms=1;req_adults=1;req_children=0;room1=A;sb_price_type=total;sr_order=popularity;sr_pri_blocks=252735908_103825146_0_2_0__15400;srepoch=1715843424;srpvid=c7cf3267295c01b3;type=total;ucfs=1&#hotelTmpl",
            "time_usec": 1715843429369811,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MeetMe23, Prague \u2013 Updated 2024 Prices",
            "url": "https://www.booking.com/searchresults.html?aid=356929&label=metagha-link-MRUS-hotel-2527359_dev-desktop_los-3_bw-50_dow-Friday_defdate-0_room-0_gstadt-1_rateid-0_aud-7177173165_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240705_ppt-_lp-2840_r-7831999324863003215&utm_medium=mapresults&hca=m&no_rooms=1&show_room=252735908_103825146_0_2_0&lang=en&utm_content=dev-desktop_los-3_bw-50_dow-Friday_defdate-0_room-0_gstadt-1_rateid-0_aud-7177173165_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240705_ppt-&utm_campaign=US&utm_term=hotel-2527359&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8rcAZehSiweaGQ7TLgX1Nqe96JPcuEDC9ojIO0ASsts7Kszs2m4-V4aAvPBEALw_wcB&ext_price_total=174.06&utm_source=metagha&ts=1715828781&highlighted_hotels=2527359&show_room=252735908_103825146_0_2_0&checkin=2024-07-05&redirected=1&city=-553173&hlrd=with_dates&group_adults=1&source=hotel&group_children=0&checkout=2024-07-08&sr_show_room=252735908_103825146_0_2_0&keep_landing=1&sid=143ad315046fab268076e86c4894838a&track_hp_back_button=1#hotel_2527359-back",
            "time_usec": 1715843429348194,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Booking.com: Hotels in Prague. Book your hotel now!",
            "url": "https://www.booking.com/searchresults.html?aid=356929&label=metagha-link-MRUS-hotel-2527359_dev-desktop_los-3_bw-50_dow-Friday_defdate-0_room-0_gstadt-1_rateid-0_aud-7177173165_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240705_ppt-_lp-2840_r-7831999324863003215&utm_medium=mapresults&hca=m&no_rooms=1&show_room=252735908_103825146_1_2_0&lang=en&utm_content=dev-desktop_los-3_bw-50_dow-Friday_defdate-0_room-0_gstadt-1_rateid-0_aud-7177173165_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240705_ppt-&utm_campaign=US&utm_term=hotel-2527359&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8rcAZehSiweaGQ7TLgX1Nqe96JPcuEDC9ojIO0ASsts7Kszs2m4-V4aAvPBEALw_wcB&ext_price_total=174.06&utm_source=metagha&ts=1715828781&highlighted_hotels=2527359&show_room=252735908_103825146_0_2_0&checkin=2024-07-05&redirected=1&city=-553173&hlrd=with_dates&group_adults=1&source=hotel&group_children=0&checkout=2024-07-08&sr_show_room=252735908_103825146_0_2_0&keep_landing=1&sid=143ad315046fab268076e86c4894838a",
            "time_usec": 1715843407291205,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MeetMe23 - Google Maps",
            "url": "https://www.google.com/maps/place/MeetMe23/@50.082256,14.4299077,17z/data=!4m23!1m10!2m9!1sHotels!5m6!5m4!1s2024-07-05!2i3!4m1!1i1!9i89!6e3!3m11!1s0x470b9493b27daaf1:0x2083dd541fa86afb!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.082256!4d14.4322936!15sCgZIb3RlbHOSAQVob3RlbOABAA!16s%2Fg%2F11f04phqzk?entry=ttu",
            "time_usec": 1715843399802700,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MeetMe23 - Google Maps",
            "url": "https://www.google.com/maps/place/MeetMe23/@50.0766531,14.4254489,17.92z/data=!4m23!1m10!2m9!1sHotels!5m6!5m4!1s2024-07-05!2i3!4m1!1i1!9i89!6e3!3m11!1s0x470b9493b27daaf1:0x2083dd541fa86afb!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.082256!4d14.4322936!15sCgZIb3RlbHOSAQVob3RlbOABAA!16s%2Fg%2F11f04phqzk?entry=ttu",
            "time_usec": 1715843385958386,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "MeetMe23 - Google Maps",
            "url": "https://www.google.com/maps/search/Hotels/@50.0766531,14.4254489,17.92z/data=!4m9!2m8!5m6!5m4!1s2024-07-05!2i3!4m1!1i1!9i89!6e3?entry=ttu",
            "time_usec": 1715843373406960,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hotels - Google Maps",
            "url": "https://www.google.com/maps/search/Hotels/@50.076681,14.426059,19z/data=!4m9!2m8!5m6!5m4!1s2024-07-05!2i3!4m1!1i1!9i89!6e3?entry=ttu",
            "time_usec": 1715843371432804,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hotels - Google Maps",
            "url": "https://www.google.com/maps/place/Hostel+Bell/@50.076681,14.426059,19z/data=!4m22!1m10!2m9!1sHotels!5m6!5m4!1s2024-07-05!2i3!4m1!1i1!9i89!6e3!3m10!1s0x470b948ce92e1bcf:0xb672f2df31b7757e!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0766806!4d14.4270018!16s%2Fg%2F1tfb0q6w?entry=ttu",
            "time_usec": 1715843369203615,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hostel Bell - Google Maps",
            "url": "https://www.google.com/maps/place/Hostel+Bell/@50.076681,14.426059,19z/data=!4m18!1m6!2m5!1sHotels!5m3!5m2!1s2024-07-05!2i3!3m10!1s0x470b948ce92e1bcf:0xb672f2df31b7757e!5m4!1s2024-07-05!2i3!4m1!1i2!8m2!3d50.0766806!4d14.4270018!16s%2Fg%2F1tfb0q6w?entry=ttu",
            "time_usec": 1715843349689612,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hostel Bell - Google Maps",
            "url": "https://www.google.com/maps/place/Prague-1+Hostel/@50.0779129,14.4289701,19.26z/data=!4m24!1m12!3m11!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!2sLuma+Terra+Prague!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!16s%2Fg%2F11t80gzsnv!3m10!1s0x470b948da99418d1:0x1e82a472cdeb8d76!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0777038!4d14.4290584!16s%2Fg%2F1vzqqzlb?entry=ttu",
            "time_usec": 1715843314620954,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hotel Royal Plaza - Google Maps",
            "url": "https://www.google.com/maps/place/Hotel+Royal+Plaza/@50.0779095,14.4322371,16.47z/data=!4m24!1m12!3m11!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!2sLuma+Terra+Prague!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!16s%2Fg%2F11t80gzsnv!3m10!1s0x470b950035e5259f:0x114d65c795c7fe!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0780961!4d14.4320737!16s%2Fg%2F11y3km6mvj?entry=ttu",
            "time_usec": 1715843304219050,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hotel Royal Plaza - Google Maps",
            "url": "https://www.google.com/maps/place/Hotel+Royal+Plaza/@50.077094,14.4323694,17.51z/data=!4m24!1m12!3m11!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!2sLuma+Terra+Prague!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!16s%2Fg%2F11t80gzsnv!3m10!1s0x470b950035e5259f:0x114d65c795c7fe!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0780961!4d14.4320737!16s%2Fg%2F11y3km6mvj?entry=ttu",
            "time_usec": 1715843295209471,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Maps",
            "url": "https://www.google.com/maps/place/Arkada+Hotel+Prague/@50.077094,14.4323694,17.51z/data=!4m24!1m12!3m11!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!2sLuma+Terra+Prague!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!16s%2Fg%2F11t80gzsnv!3m10!1s0x470b948e677ff399:0x16c4654bf2f81ed0!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0771561!4d14.4341212!16s%2Fg%2F1tf46w4t?entry=ttu",
            "time_usec": 1715843275365526,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hotel Brixen - Google Maps",
            "url": "https://www.google.com/maps/place/Hotel+Brixen/@50.0749927,14.4299457,17.51z/data=!4m24!1m12!3m11!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!2sLuma+Terra+Prague!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!16s%2Fg%2F11t80gzsnv!3m10!1s0x470b948bf22d58b9:0x6470440e289062d!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0741245!4d14.4294417!16s%2Fg%2F1tgn_j21?entry=ttu",
            "time_usec": 1715843263149774,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Alfons Boutique Hotel - Google Maps",
            "url": "https://www.google.com/maps/place/Alfons+Boutique+Hotel/@50.076052,14.4302732,16z/data=!4m24!1m12!3m11!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!2sLuma+Terra+Prague!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!16s%2Fg%2F11t80gzsnv!3m10!1s0x470b95008d99ac67:0xac919f58bf56f6d3!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0740867!4d14.4300504!16s%2Fg%2F11gmx7b_qz?entry=ttu",
            "time_usec": 1715843252260820,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Alfons Boutique Hotel - Google Maps",
            "url": "https://www.google.com/maps/place/Alfons+Boutique+Hotel/@50.0766917,14.4300754,16.15z/data=!4m24!1m12!3m11!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!2sLuma+Terra+Prague!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!16s%2Fg%2F11t80gzsnv!3m10!1s0x470b95008d99ac67:0xac919f58bf56f6d3!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0740867!4d14.4300504!16s%2Fg%2F11gmx7b_qz?entry=ttu",
            "time_usec": 1715843251743197,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Luma Terra Prague Hostel, Prague \u2013 Updated 2024 Prices",
            "url": "https://www.booking.com/hotel/cz/luma-terra-prague-hostel.html?aid=356929&label=metagha-link-MRUS-hotel-8564965_dev-desktop_los-3_bw-50_dow-Friday_defdate-0_room-0_gstadt-1_rateid-0_aud-7177173165_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240705_ppt-_lp-2840_r-11295749760981878907&sid=143ad315046fab268076e86c4894838a&all_sr_blocks=856496501_360294575_0_2_0;checkin=2024-07-05;checkout=2024-07-08;dest_id=-553173;dest_type=city;dist=0;group_adults=1;group_children=0;hapos=1;highlighted_blocks=856496501_360294575_0_2_0;hpos=1;matching_block_id=856496501_360294575_0_2_0;no_rooms=1;req_adults=1;req_children=0;room1=A;sb_price_type=total;sr_order=popularity;sr_pri_blocks=856496501_360294575_0_2_0__19348;srepoch=1715843021;srpvid=0d893184e82400e7;type=total;ucfs=1&#hotelTmpl",
            "time_usec": 1715843070350251,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Luma Terra Prague Hostel, Prague \u2013 Updated 2024 Prices",
            "url": "https://www.booking.com/hotel/cz/luma-terra-prague-hostel.html?aid=356929&label=metagha-link-MRUS-hotel-8564965_dev-desktop_los-3_bw-50_dow-Friday_defdate-0_room-0_gstadt-1_rateid-0_aud-7177173165_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240705_ppt-_lp-2840_r-11295749760981878907&sid=143ad315046fab268076e86c4894838a&all_sr_blocks=856496501_360294575_0_2_0;checkin=2024-07-05;checkout=2024-07-08;dest_id=-553173;dest_type=city;dist=0;group_adults=1;group_children=0;hapos=1;highlighted_blocks=856496501_360294575_0_2_0;hpos=1;matching_block_id=856496501_360294575_0_2_0;no_rooms=1;req_adults=1;req_children=0;room1=A;sb_price_type=total;sr_order=popularity;sr_pri_blocks=856496501_360294575_0_2_0__19348;srepoch=1715843021;srpvid=0d893184e82400e7;type=total;ucfs=1&#hotelTmpl",
            "time_usec": 1715843028959622,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Luma Terra Prague Hostel, Prague \u2013 Updated 2024 Prices",
            "url": "https://www.booking.com/searchresults.html?aid=356929&label=metagha-link-MRUS-hotel-8564965_dev-desktop_los-3_bw-50_dow-Friday_defdate-0_room-0_gstadt-1_rateid-0_aud-7177173165_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240705_ppt-_lp-2840_r-11295749760981878907&sid=143ad315046fab268076e86c4894838a&checkin=2024-07-05&checkout=2024-07-08&dest_id=-553173&dest_type=city&srpvid=0d893184e82400e7&track_hp_back_button=1#hotel_8564965-back",
            "time_usec": 1715843028947903,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://cf.bstatic.com/static/img/favicon/9ca83ba2a5a3293ff07452cb24949a5843af4592.svg",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Booking.com: Hotels in Prague. Book your hotel now!",
            "url": "https://www.booking.com/searchresults.html?aid=356929&label=metagha-link-MRUS-hotel-8564965_dev-desktop_los-3_bw-50_dow-Friday_defdate-0_room-0_gstadt-1_rateid-0_aud-7177173165_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240705_ppt-_lp-2840_r-11295749760981878907&utm_medium=mapresults&hca=m&no_rooms=1&show_room=856496501_360294575_1_2_0&lang=en&utm_content=dev-desktop_los-3_bw-50_dow-Friday_defdate-0_room-0_gstadt-1_rateid-0_aud-7177173165_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240705_ppt-&utm_campaign=US&utm_term=hotel-8564965&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8qQKpehqj5EvU0UcdjkbgZnanYVUAp_4TV6HLhV5uxnJ6pbJAnrSFAaAvZVEALw_wcB&ext_price_total=217.17&utm_source=metagha&ts=1715792436&highlighted_hotels=8564965&show_room=856496501_360294575_0_2_0&checkin=2024-07-05&redirected=1&city=-553173&hlrd=with_dates&group_adults=1&source=hotel&group_children=0&checkout=2024-07-08&sr_show_room=856496501_360294575_0_2_0&keep_landing=1&sid=143ad315046fab268076e86c4894838a",
            "time_usec": 1715842954151579,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Luma Terra Prague - Google Maps",
            "url": "https://www.google.com/maps/place/Luma+Terra+Prague/@50.076052,14.4302732,16.93z/data=!4m11!3m10!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!16s%2Fg%2F11t80gzsnv?entry=ttu",
            "time_usec": 1715842934912972,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Luma Terra Prague - Google Maps",
            "url": "https://www.google.com/maps/place/Luma+Terra+Prague/@50.0755014,14.4268101,16z/data=!4m11!3m10!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!16s%2Fg%2F11t80gzsnv?entry=ttu",
            "time_usec": 1715842925632446,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Luma Terra Prague - Google Maps",
            "url": "https://www.google.com/maps/place/Luma+Terra+Prague/@50.0762588,14.4304579,16z/data=!4m11!3m10!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!16s%2Fg%2F11t80gzsnv?entry=ttu",
            "time_usec": 1715842922835600,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Luma Terra Prague - Google Maps",
            "url": "https://www.google.com/maps/place/Luma+Terra+Prague/@50.0762588,14.4304579,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipOxKc9_kmS6RUjuJ7UtqL62JMIWy-tZsAt5Fsn7!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOxKc9_kmS6RUjuJ7UtqL62JMIWy-tZsAt5Fsn7%3Dw203-h152-k-no!7i4032!8i3024!4m12!3m11!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!10e5!16s%2Fg%2F11t80gzsnv?entry=ttu",
            "time_usec": 1715842916942208,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Luma Terra Prague - Google Maps",
            "url": "https://www.google.com/maps/place/Luma+Terra+Prague/@50.0766032,14.4317492,3a,75y,90t/data=!3m8!1e2!3m6!1shttps:%2F%2Fcdn.worldota.net%2Ft%2F1024x768%2Fcontent%2F31%2Fc8%2F31c8bc05e99fc4c51c5b538f34be2df8de8500d5.jpeg!2e7!3e27!6shttps:%2F%2Flh3.googleusercontent.com%2Fgps-proxy%2FALd4DhFugny7U2fY4bmz1iueGxUR6YNNXnErCHknP676CedEDKEddmabUByayP7xar39IHVi9loA01xDBmepgcXqBHJzTSJeG491nDSRmUa7NbkHt7O5V8sqElsxLbQcB8odUK0dUZHqhAhILQJiJbhrkW7fraKTYHi-bUMXmNdgTvD7Gfabaw5IgPGq8Q%3Dw203-h130-k-no!7i1024!8i768!4m12!3m11!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!10e5!16s%2Fg%2F11t80gzsnv?entry=ttu",
            "time_usec": 1715842905416913,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Maps",
            "url": "https://www.google.com/maps/place/Luma+Terra+Prague/@50.0766032,14.4317492,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipPkkkdzsPLiPLi78Bv7tM6S3xOyeCK0WavmG140!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipPkkkdzsPLiPLi78Bv7tM6S3xOyeCK0WavmG140%3Dw222-h100-k-no!7i4032!8i1816!4m12!3m11!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!10e5!16s%2Fg%2F11t80gzsnv?entry=ttu",
            "time_usec": 1715842904578535,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Maps",
            "url": "https://www.google.com/maps/place/Luma+Terra+Prague/@50.0766032,14.4317492,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipONRfZB6ZibQmTj89IVfQVXK2Dh0_R2a4zFcATg!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipONRfZB6ZibQmTj89IVfQVXK2Dh0_R2a4zFcATg%3Dw203-h270-k-no!7i3024!8i4032!4m12!3m11!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!10e5!16s%2Fg%2F11t80gzsnv?entry=ttu",
            "time_usec": 1715842893626992,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Luma Terra Prague - Google Maps",
            "url": "https://www.google.com/maps/place/Luma+Terra+Prague/@50.0766032,14.4317492,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipOCOZU4CEJL2xhC1Zpl4QzU8BwOnqL9Os4M1BnU!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOCOZU4CEJL2xhC1Zpl4QzU8BwOnqL9Os4M1BnU%3Dw203-h135-k-no!7i2048!8i1366!4m12!3m11!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!10e5!16s%2Fg%2F11t80gzsnv?entry=ttu",
            "time_usec": 1715842880993921,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Luma Terra Prague - Google Maps",
            "url": "https://www.google.com/maps/place/Luma+Terra+Prague/@50.0766032,14.4317492,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipPYoXvuw7eKdU_HkUocw6aY2rGKNvtLcmdUx8w_!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipPYoXvuw7eKdU_HkUocw6aY2rGKNvtLcmdUx8w_%3Dw203-h270-k-no!7i3024!8i4032!4m12!3m11!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!10e5!16s%2Fg%2F11t80gzsnv?entry=ttu",
            "time_usec": 1715842868627582,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Maps",
            "url": "https://www.google.com/maps/place/Luma+Terra+Prague/@50.0766032,14.4317492,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipP7jRUk343fXDVu-6rfhVmoDw92k3mtajSWgAWJ!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipP7jRUk343fXDVu-6rfhVmoDw92k3mtajSWgAWJ%3Dw86-h128-k-no!7i1366!8i2048!4m12!3m11!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!10e5!16s%2Fg%2F11t80gzsnv?entry=ttu",
            "time_usec": 1715842861010975,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Luma Terra Prague - Google Maps",
            "url": "https://www.google.com/maps/place/Luma+Terra+Prague/@50.0754752,14.4297737,16.93z/data=!4m11!3m10!1s0x470b957c1fd475a9:0x2974b1241d5d5d52!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0762588!4d14.4304579!16s%2Fg%2F11t80gzsnv?entry=ttu",
            "time_usec": 1715842853970883,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Prague Saints - Google Maps",
            "url": "https://www.google.com/maps/place/Prague+Saints/@50.0783018,14.4405827,16.93z/data=!4m11!3m10!1s0x470b95adc0317855:0x2db5c06242283415!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0782871!4d14.4431812!16s%2Fg%2F11rw66v9c?entry=ttu",
            "time_usec": 1715842834245587,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Prague Roof Apartments - Google Maps",
            "url": "https://www.google.com/maps/place/Prague+Roof+Apartments/@50.0777971,14.4360097,16.93z/data=!4m11!3m10!1s0x470b9540f7eaef61:0xaf8be34cc09e04b7!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.077506!4d14.4402752!16s%2Fg%2F11j5_z9npx?entry=ttu",
            "time_usec": 1715842826238145,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Prague Roof Apartments - Google Maps",
            "url": "https://www.google.com/maps/place//@50.0777971,14.4360097,16.93z/data=!4m10!3m9!1s0x470b9540f7eaef61:0xaf8be34cc09e04b7!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0774477!4d14.4402623?entry=ttu",
            "time_usec": 1715842825262422,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Libero Residence - Google Maps",
            "url": "https://www.google.com/maps/place/Libero+Residence/@50.077487,14.434785,16.93z/data=!4m11!3m10!1s0x470b952f69f5e977:0x4dbb6b20fb67278a!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0766776!4d14.4384463!16s%2Fg%2F11t32197m9?entry=ttu",
            "time_usec": 1715842823093848,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Libero Residence - Google Maps",
            "url": "https://www.google.com/maps/place/Libero+Residence/@50.07749,14.4346588,16.9z/data=!4m11!3m10!1s0x470b952f69f5e977:0x4dbb6b20fb67278a!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0766776!4d14.4384463!16s%2Fg%2F11t32197m9?entry=ttu",
            "time_usec": 1715842815540170,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "CORU House by Prague Days - Google Maps",
            "url": "https://www.google.com/maps/place/CORU+House+by+Prague+Days/@50.0779708,14.4333379,16.3z/data=!4m11!3m10!1s0x470b95dfb3e2ca47:0x4abb32621a4a5e1e!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0754216!4d14.4393578!16s%2Fg%2F11vf3xklt5?entry=ttu",
            "time_usec": 1715842807604203,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Aparthotel Rimska 14 - Google Maps",
            "url": "https://www.google.com/maps/place/Aparthotel+Rimska+14/@50.0775868,14.433774,17z/data=!4m11!3m10!1s0x470b95ccb4200fb9:0x1030530fbf6be8ac!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0775868!4d14.433774!16s%2Fg%2F11rxrm880d?entry=ttu",
            "time_usec": 1715842800958902,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Aparthotel Rimska 14 - Google Maps",
            "url": "https://www.google.com/maps/place/Aparthotel+Rimska+14/@50.0775868,14.433774,17z/data=!4m11!3m10!1s0x470b95ccb4200fb9:0x1030530fbf6be8ac!5m4!1s2024-06-30!2i5!4m1!1i2!8m2!3d50.0775868!4d14.433774!16s%2Fg%2F11rxrm880d?entry=ttu",
            "time_usec": 1715842790080848,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Aparthotel Rimska 14 - Google Maps",
            "url": "https://www.google.com/maps/place/Onefam+M%C3%ADru+Hostel+Prague/@50.0764432,14.4337577,17.45z/data=!4m24!1m12!3m11!1s0x470b95ccb4200fb9:0x1030530fbf6be8ac!2sAparthotel+Rimska+14!5m4!1s2024-07-02!2i3!4m1!1i2!8m2!3d50.0775868!4d14.433774!16s%2Fg%2F11rxrm880d!3m10!1s0x470b948f76548c65:0x49c6caefaed9e4d1!5m4!1s2024-07-05!2i3!4m1!1i1!8m2!3d50.0760456!4d14.4378953!16s%2Fg%2F11f50ppnlt?entry=ttu",
            "time_usec": 1715842759899111,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Onefam Míru Hostel Prague - Google Maps",
            "url": "https://www.google.com/maps/place/Onefam+M%C3%ADru+Hostel+Prague/@50.0764432,14.4337577,17.45z/data=!4m23!1m12!3m11!1s0x470b95ccb4200fb9:0x1030530fbf6be8ac!2sAparthotel+Rimska+14!5m4!1s2024-07-02!2i3!4m1!1i2!8m2!3d50.0775868!4d14.433774!16s%2Fg%2F11rxrm880d!3m9!1s0x470b948f76548c65:0x49c6caefaed9e4d1!5m3!1s2024-07-05!4m1!1i1!8m2!3d50.0760456!4d14.4378953!16s%2Fg%2F11f50ppnlt?entry=ttu",
            "time_usec": 1715842750939197,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Onefam Míru Hostel Prague - Google Maps",
            "url": "https://www.google.com/maps/place/Onefam+M%C3%ADru+Hostel+Prague/@50.0764432,14.4337577,17.45z/data=!4m24!1m12!3m11!1s0x470b95ccb4200fb9:0x1030530fbf6be8ac!2sAparthotel+Rimska+14!5m4!1s2024-07-02!2i3!4m1!1i2!8m2!3d50.0775868!4d14.433774!16s%2Fg%2F11rxrm880d!3m10!1s0x470b948f76548c65:0x49c6caefaed9e4d1!5m4!1s2024-07-02!2i3!4m1!1i2!8m2!3d50.0760456!4d14.4378953!16s%2Fg%2F11f50ppnlt?entry=ttu",
            "time_usec": 1715842730599814,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Onefam Míru Hostel Prague - Google Maps",
            "url": "https://www.google.com/maps/place/Onefam+M%C3%ADru+Hostel+Prague/@50.0764432,14.4337577,17.45z/data=!4m24!1m12!3m11!1s0x470b95ccb4200fb9:0x1030530fbf6be8ac!2sAparthotel+Rimska+14!5m4!1s2024-07-02!2i3!4m1!1i2!8m2!3d50.0775868!4d14.433774!16s%2Fg%2F11rxrm880d!3m10!1s0x470b948f76548c65:0x49c6caefaed9e4d1!5m4!1s2024-07-02!2i3!4m1!1i2!8m2!3d50.0760456!4d14.4378953!16s%2Fg%2F11f50ppnlt?entry=ttu",
            "time_usec": 1715842730064261,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Aparthotel Rimska 14 - Google Maps",
            "url": "https://www.google.com/maps/place/Aparthotel+Rimska+14/@50.0754936,14.4349777,17.45z/data=!4m11!3m10!1s0x470b95ccb4200fb9:0x1030530fbf6be8ac!5m4!1s2024-07-02!2i3!4m1!1i2!8m2!3d50.0775868!4d14.433774!16s%2Fg%2F11rxrm880d?entry=ttu",
            "time_usec": 1715842716166531,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Aparthotel Rimska 14 - Google Maps",
            "url": "https://www.google.com/maps/place/Aparthotel+Rimska+14/@50.077589,14.431682,16.4z/data=!4m11!3m10!1s0x470b95ccb4200fb9:0x1030530fbf6be8ac!5m4!1s2024-07-02!2i3!4m1!1i2!8m2!3d50.0775868!4d14.433774!16s%2Fg%2F11rxrm880d?entry=ttu",
            "time_usec": 1715842706635040,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Aparthotel Rimska 14 - Google Maps",
            "url": "https://www.google.com/maps/place/Aparthotel+Rimska+14/@50.0780171,14.4331571,17z/data=!4m11!3m10!1s0x470b95ccb4200fb9:0x1030530fbf6be8ac!5m4!1s2024-07-02!2i3!4m1!1i2!8m2!3d50.0775868!4d14.433774!16s%2Fg%2F11rxrm880d?entry=ttu",
            "time_usec": 1715842690142649,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Maps",
            "url": "https://www.google.com/maps/place/Aparthotel+Rimska+14/@50.0775868,14.433774,15z/data=!4m2!3m1!1s0x0:0x1030530fbf6be8ac?sa=X&ved=1t:2428&ictx=111",
            "time_usec": 1715842680805871,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "aparthotel rimsa prague - Google Search",
            "url": "https://www.google.com/search?q=aparthotel+rimsa+prague&sca_esv=c22fddfe247c1d12&sxsrf=ADLYWILhk3bHKbkgw3MQ9Qvz_sWE5ZY1aA%3A1715842360897&ei=OK1FZtG4Nq2_0PEPldKG8AU&ved=0ahUKEwjRtKXzypGGAxWtHzQIHRWpAV4Q4dUDCBE&uact=5&oq=aparthotel+rimsa+prague&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIhdhcGFydGhvdGVsIHJpbXNhIHByYWd1ZTIFECEYoAEyBRAhGKABMgUQIRigATIFECEYoAEyBRAhGKABSKJbUOQDWN9VcAR4AZABAJgBjAOgAZg-qgEHMi0xMi4xNLgBA8gBAPgBAZgCHqAC-0CoAhDCAgcQIxgnGOoCwgIaEC4YgAQY0QMY4wQYtAIYxwEY6QQY6gLYAQHCAhQQABiABBjjBBi0AhjpBBjqAtgBAcICBBAjGCfCAgoQIxiABBgnGIoFwgIREC4YgAQYkQIYxwEYigUYrwHCAhEQLhiABBixAxjRAxiDARjHAcICCxAAGIAEGLEDGIMBwgIOEC4YgAQYsQMYgwEYigXCAg4QABiABBixAxiDARiKBcICCxAAGIAEGJECGIoFwgIKEC4YgAQYQxiKBcICFBAuGIAEGLEDGNEDGIMBGMcBGIoFwgIXEC4YgAQYkQIYsQMY0QMYgwEYxwEYigXCAhEQABiABBiRAhixAxiDARiKBcICChAAGIAEGEMYigXCAggQLhiABBixA8ICJhAuGIAEGJECGLEDGNEDGIMBGMcBGIoFGJcFGNwEGN4EGOAE2AECwgIZEC4YgAQYsQMY0QMYQxiDARjUAhjHARiKBcICExAuGIAEGLEDGEMYgwEY1AIYigXCAhEQLhiABBixAxiDARjHARivAcICCBAAGIAEGLEDwgIFEAAYgATCAigQLhiABBixAxjRAxhDGIMBGNQCGMcBGIoFGJcFGNwEGN4EGOAE2AECwgINEAAYgAQYsQMYQxiKBcICFhAuGIAEGLEDGNEDGEMYgwEYxwEYigXCAgsQABiABBiSAxiKBcICERAAGIAEGLEDGJIDGIMBGIoFwgIUEC4YgAQYsQMY0QMYgwEYxwEYyQPCAg4QABiABBixAxiDARjJA8ICFBAuGIAEGMcBGJgFGJkFGJ4FGK8BwgILEC4YgAQY0QMYxwHCAhEQLhiABBjHARiYBRiZBRivAcICChAAGIAEGBQYhwLCAg4QLhiABBjHARiYBRivAcICCxAuGIAEGMcBGK8BwgIHEAAYgAQYCsICHRAuGIAEGMcBGJgFGK8BGJcFGNwEGN4EGOAE2AECwgIGEAAYFhgewgIIEAAYFhgeGA_CAggQABgWGAoYHsICCBAAGIAEGKIEwgILEAAYgAQYogQYiwPCAgQQIRgVwgIIECEYoAEYiwOYAxa6BgYIARABGAG6BgYIAhABGBSSBwo0LjAuOS4xNi4xoAeNsgI&sclient=gws-wiz-serp",
            "time_usec": 1715842672089405,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "footlocker florence italy - Google Search",
            "url": "https://www.google.com/search?q=footlocker+florence+italy&oq=footlocker+florence+italy+&aqs=chrome..69i64j0i67i512i650j46i10i175i199i512l2j46i175i199i512j0i10i22i30j0i22i30l2j46i10i22i30i175i199.9227j0j1&sourceid=chrome&ie=UTF-8#rlimm=11786000633158805671",
            "time_usec": 1715842476583973,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "footlocker florence italy - Google Search",
            "url": "https://www.google.com/search?q=footlocker+florence+italy&oq=footlocker+florence+italy+&aqs=chrome..69i64j0i67i512i650j46i10i175i199i512l2j46i175i199i512j0i10i22i30j0i22i30l2j46i10i22i30i175i199.9227j0j1&sourceid=chrome&ie=UTF-8#rlimm=11786000633158805671&lpg=cid:CgIgAQ%3D%3D,ik:CAoSLEFGMVFpcE5NZlZ6bVpJd1NfUFBRR0pCYy1pQmx5MDR1MHg3YzlmQ1U4ZU5u",
            "time_usec": 1715842451679428,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "footlocker florence italy - Google Search",
            "url": "https://www.google.com/search?q=footlocker+florence+italy&oq=footlocker+florence+italy+&aqs=chrome..69i64j0i67i512i650j46i10i175i199i512l2j46i175i199i512j0i10i22i30j0i22i30l2j46i10i22i30i175i199.9227j0j1&sourceid=chrome&ie=UTF-8#rlimm=11786000633158805671",
            "time_usec": 1715842451280015,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "footlocker florence italy - Google Search",
            "url": "https://www.google.com/search?q=footlocker+florence+italy&oq=footlocker+florence+italy+&aqs=chrome..69i64j0i67i512i650j46i10i175i199i512l2j46i175i199i512j0i10i22i30j0i22i30l2j46i10i22i30i175i199.9227j0j1&sourceid=chrome&ie=UTF-8#rlimm=11786000633158805671",
            "time_usec": 1715842448875507,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "footlocker florence italy - Google Search",
            "url": "https://www.google.com/search?q=footlocker+florence+italy&oq=footlocker+florence+italy+&aqs=chrome..69i64j0i67i512i650j46i10i175i199i512l2j46i175i199i512j0i10i22i30j0i22i30l2j46i10i22i30i175i199.9227j0j1&sourceid=chrome&ie=UTF-8#rlimm=8309197215175022829",
            "time_usec": 1715842447407165,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "footlocker florence italy - Google Search",
            "url": "https://www.google.com/search?q=footlocker+florence+italy&oq=footlocker+florence+italy+&aqs=chrome..69i64j0i67i512i650j46i10i175i199i512l2j46i175i199i512j0i10i22i30j0i22i30l2j46i10i22i30i175i199.9227j0j1&sourceid=chrome&ie=UTF-8#rlimm=8309197215175022829&lpg=cid:CgIgAQ%3D%3D,ik:CAoSLEFGMVFpcE1wRVhHRTYzU1lFLTJHLVhPeGlLYW9SVlV5cTNqSW1HYXlITlg5",
            "time_usec": 1715842392975463,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "footlocker florence italy - Google Search",
            "url": "https://www.google.com/search?q=footlocker+florence+italy&oq=footlocker+florence+italy+&aqs=chrome..69i64j0i67i512i650j46i10i175i199i512l2j46i175i199i512j0i10i22i30j0i22i30l2j46i10i22i30i175i199.9227j0j1&sourceid=chrome&ie=UTF-8#rlimm=8309197215175022829",
            "time_usec": 1715842391203125,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "footlocker florence italy - Google Search",
            "url": "https://www.google.com/search?q=footlocker+florence+italy&oq=footlocker+florence+italy+&aqs=chrome..69i64j0i67i512i650j46i10i175i199i512l2j46i175i199i512j0i10i22i30j0i22i30l2j46i10i22i30i175i199.9227j0j1&sourceid=chrome&ie=UTF-8#rlimm=8309197215175022829",
            "time_usec": 1715842388231900,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "footlocker florence italy - Google Search",
            "url": "https://www.google.com/search?q=footlocker+florence+italy&oq=footlocker+florence+italy+&aqs=chrome..69i64j0i67i512i650j46i10i175i199i512l2j46i175i199i512j0i10i22i30j0i22i30l2j46i10i22i30i175i199.9227j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715842379641100,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715842367098626,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "isi florence italy location - Google Search",
            "url": "https://www.google.com/search?q=isi+florence+italy+location&sca_esv=c22fddfe247c1d12&sxsrf=ADLYWIJSoIF6p1gi9pb0nBp6bOWboQ8GqQ%3A1715842351536&ei=L61FZrGrIKXw0PEPjYeZmAk&oq=isi+florence&gs_lp=Egxnd3Mtd2l6LXNlcnAiDGlzaSBmbG9yZW5jZSoCCAEyChAjGIAEGCcYigUyBBAjGCcyChAjGIAEGCcYigUyEBAuGIAEGEMYxwEYigUYrwEyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyHxAuGIAEGEMYxwEYigUYrwEYlwUY3AQY3gQY4ATYAQJIhiVQxwZYsBdwAXgBkAEAmAGEA6ABlB2qAQUyLTUuN7gBAcgBAPgBAZgCDaAC3B6oAhTCAgcQIxgnGOoCwgIWEAAYAxi0AhjlAhjqAhiMAxiPAdgBAcICFhAuGAMYtAIY5QIY6gIYjAMYjwHYAQHCAgoQLhiABBhDGIoFwgIREC4YgAQYkQIYxwEYigUYrwHCAgsQABiABBiRAhiKBcICChAAGIAEGEMYigXCAgsQABiABBixAxiDAcICDhAuGIAEGLEDGIMBGIoFwgIIEC4YgAQYsQPCAggQABiABBixA8ICDRAAGIAEGLEDGEMYigXCAhAQABiABBixAxhDGIMBGIoFwgILEC4YgAQYsQMYgwHCAgoQABiABBgUGIcCmAMb4gMFEgExIEC6BgYIARABGAu6BgYIAhABGBSSBwgxLjMtMTEuMaAHxKMB&sclient=gws-wiz-serp",
            "time_usec": 1715842361880169,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "isi florence italy location - Google Search",
            "url": "https://www.google.com/search?q=isi+florence+italy+location&sca_esv=c22fddfe247c1d12&sxsrf=ADLYWIJSoIF6p1gi9pb0nBp6bOWboQ8GqQ%3A1715842351536&ei=L61FZrGrIKXw0PEPjYeZmAk&oq=isi+florence&gs_lp=Egxnd3Mtd2l6LXNlcnAiDGlzaSBmbG9yZW5jZSoCCAEyChAjGIAEGCcYigUyBBAjGCcyChAjGIAEGCcYigUyEBAuGIAEGEMYxwEYigUYrwEyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyHxAuGIAEGEMYxwEYigUYrwEYlwUY3AQY3gQY4ATYAQJIhiVQxwZYsBdwAXgBkAEAmAGEA6ABlB2qAQUyLTUuN7gBAcgBAPgBAZgCDaAC3B6oAhTCAgcQIxgnGOoCwgIWEAAYAxi0AhjlAhjqAhiMAxiPAdgBAcICFhAuGAMYtAIY5QIY6gIYjAMYjwHYAQHCAgoQLhiABBhDGIoFwgIREC4YgAQYkQIYxwEYigUYrwHCAgsQABiABBiRAhiKBcICChAAGIAEGEMYigXCAgsQABiABBixAxiDAcICDhAuGIAEGLEDGIMBGIoFwgIIEC4YgAQYsQPCAggQABiABBixA8ICDRAAGIAEGLEDGEMYigXCAhAQABiABBixAxhDGIMBGIoFwgILEC4YgAQYsQMYgwHCAgoQABiABBgUGIcCmAMb4gMFEgExIEC6BgYIARABGAu6BgYIAhABGBSSBwgxLjMtMTEuMaAHxKMB&sclient=gws-wiz-serp",
            "time_usec": 1715842361099402,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "nbest vintage stores in florence italy - Google Search",
            "url": "https://www.google.com/search?q=nbest+vintage+stores+in+florence+italy&oq=nbest+vintage+stores+in+florence+italy+&aqs=chrome..69i64j0i22i30l3j0i390i512i650l4j0i512i546j0i395i512i546.10775j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715842350803783,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "florence museums - Google Search",
            "url": "https://www.google.com/search?q=florence+museums+&sca_esv=862d19b374e0a29b&biw=1287&bih=701&sxsrf=ADLYWIJS3lTJw6ZFlbmCeBSWZG0lZva0xw%3A1715842204910&ei=nKxFZrOSN7-o0PEPts-N2AY&ved=0ahUKEwiz0PSoypGGAxU_FDQIHbZnA2sQ4dUDCBE&uact=5&oq=florence+museums+&gs_lp=Egxnd3Mtd2l6LXNlcnAiEWZsb3JlbmNlIG11c2V1bXMgMgsQABiABBiRAhiKBTIFEAAYgAQyCxAAGIAEGJECGIoFMgsQLhiABBjHARivATIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEi-X1DFH1ipW3AMeACQAQOYAd0CoAGaRKoBBjItMS4yNrgBA8gBAPgBAZgCJKAC6j-oAg_CAgcQIxgnGOoCwgIcEC4YgAQYQxi0AhjHARjIAxiKBRjqAhivAdgBAcICChAjGIAEGCcYigXCAgoQLhiABBhDGIoFwgIQEC4YgAQYQxjHARiKBRivAcICChAAGIAEGEMYigXCAhEQLhiABBixAxjRAxiDARjHAcICDRAuGIAEGEMY1AIYigXCAhMQLhiABBhDGNQCGMcBGIoFGK8BwgIEECMYJ8ICEBAuGIAEGLEDGEMYgwEYigXCAhAQABiABBixAxhDGIMBGIoFwgIIEC4YgAQYsQPCAgoQABiABBgUGIcCwgILEC4YgAQYsQMYgwHCAgcQABiABBgNwgINEC4YgAQYxwEYDRivAcICDRAuGIAEGLEDGIMBGA3CAgcQLhiABBgNwgIGEAAYFhgewgIGEAAYDRgewgIIEAAYBRgNGB7CAggQABgIGA0YHsICDhAuGIAEGLEDGMcBGK8BwgIFEC4YgATCAggQABiABBixA8ICCxAAGIAEGLEDGIMBwgIQEC4YgAQYFBiHAhjHARivAcICGhAuGIAEGMcBGK8BGJcFGNwEGN4EGOAE2AECwgIQEC4YgAQYRhjHARj7ARivAcICHBAAGIAEGEYYxwEY-wEYrwEYlwUYjAUY3QTYAQPCAhAQABiABBixAxiDARgUGIcCmAMYugYGCAEQARgIugYGCAIQARgUugYGCAMQARgTkgcHMTIuMy0yNKAHquwD&sclient=gws-wiz-serp",
            "time_usec": 1715842336886113,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://www.florence-museum.com/",
            "time_usec": 1715842334243674,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "florence museums - Google Search",
            "url": "https://www.google.com/search?q=florence+museums+&sca_esv=862d19b374e0a29b&biw=1287&bih=701&sxsrf=ADLYWIJS3lTJw6ZFlbmCeBSWZG0lZva0xw%3A1715842204910&ei=nKxFZrOSN7-o0PEPts-N2AY&ved=0ahUKEwiz0PSoypGGAxU_FDQIHbZnA2sQ4dUDCBE&uact=5&oq=florence+museums+&gs_lp=Egxnd3Mtd2l6LXNlcnAiEWZsb3JlbmNlIG11c2V1bXMgMgsQABiABBiRAhiKBTIFEAAYgAQyCxAAGIAEGJECGIoFMgsQLhiABBjHARivATIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEi-X1DFH1ipW3AMeACQAQOYAd0CoAGaRKoBBjItMS4yNrgBA8gBAPgBAZgCJKAC6j-oAg_CAgcQIxgnGOoCwgIcEC4YgAQYQxi0AhjHARjIAxiKBRjqAhivAdgBAcICChAjGIAEGCcYigXCAgoQLhiABBhDGIoFwgIQEC4YgAQYQxjHARiKBRivAcICChAAGIAEGEMYigXCAhEQLhiABBixAxjRAxiDARjHAcICDRAuGIAEGEMY1AIYigXCAhMQLhiABBhDGNQCGMcBGIoFGK8BwgIEECMYJ8ICEBAuGIAEGLEDGEMYgwEYigXCAhAQABiABBixAxhDGIMBGIoFwgIIEC4YgAQYsQPCAgoQABiABBgUGIcCwgILEC4YgAQYsQMYgwHCAgcQABiABBgNwgINEC4YgAQYxwEYDRivAcICDRAuGIAEGLEDGIMBGA3CAgcQLhiABBgNwgIGEAAYFhgewgIGEAAYDRgewgIIEAAYBRgNGB7CAggQABgIGA0YHsICDhAuGIAEGLEDGMcBGK8BwgIFEC4YgATCAggQABiABBixA8ICCxAAGIAEGLEDGIMBwgIQEC4YgAQYFBiHAhjHARivAcICGhAuGIAEGMcBGK8BGJcFGNwEGN4EGOAE2AECwgIQEC4YgAQYRhjHARj7ARivAcICHBAAGIAEGEYYxwEY-wEYrwEYlwUYjAUY3QTYAQPCAhAQABiABBixAxiDARgUGIcCmAMYugYGCAEQARgIugYGCAIQARgUugYGCAMQARgTkgcHMTIuMy0yNKAHquwD&sclient=gws-wiz-serp",
            "time_usec": 1715842262294131,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Uffizi Gallery - Google Search",
            "url": "https://www.google.com/search?sa=X&sca_esv=862d19b374e0a29b&sxsrf=ADLYWIKrbAtZ2qPbvU_2eIDUDcTwuDGMuw:1715842197618&q=Uffizi+Gallery&stick=H4sIAAAAAAAAAONgFuLQz9U3MDasNFICs5LTsgq0FLOTrfRz8pMTSzLz8-AMq8SSkqLEZBCzeBErX2haWmZVpoJ7Yk5OalElAN5z-ilKAAAA&ved=2ahUKEwiWzrelypGGAxU4GjQIHc1bB2cQ2coHegQIFRAD&biw=1179&bih=701&dpr=1",
            "time_usec": 1715842220499833,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://www.uffizi.it/en/the-uffizi",
            "time_usec": 1715842217986809,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Uffizi Gallery - Google Search",
            "url": "https://www.google.com/search?sa=X&sca_esv=862d19b374e0a29b&sxsrf=ADLYWIKrbAtZ2qPbvU_2eIDUDcTwuDGMuw:1715842197618&q=Uffizi+Gallery&stick=H4sIAAAAAAAAAONgFuLQz9U3MDasNFICs5LTsgq0FLOTrfRz8pMTSzLz8-AMq8SSkqLEZBCzeBErX2haWmZVpoJ7Yk5OalElAN5z-ilKAAAA&ved=2ahUKEwiWzrelypGGAxU4GjQIHc1bB2cQ2coHegQIFRAD&biw=1179&bih=701&dpr=1",
            "time_usec": 1715842205039091,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "things to do in florence - Google Search",
            "url": "https://www.google.com/search?sca_esv=862d19b374e0a29b&sxsrf=ADLYWII9ZQkt4JC4xdEweyUsKQxY_Q6dOg:1715842181869&q=&si=ACC90nxxKKbTXA6AgYXOa_EHHb-uzPu4mIg6otNrOy2nEw7wPkGbHfxOY1CqgCH_G6VTIqlxVWs_2keCMf_ggRN6nuKvKu-W8vgz3aRvVYD2UTbOBWdpNDQ%3D&sa=X&ved=2ahUKEwjOpvadypGGAxWQOTQIHa3gCY8Q6toKKAF6BAhYEAI&biw=1179&bih=701&dpr=1#ttdcs=EAE",
            "time_usec": 1715842202669478,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "neighborhoods in florence - Google Search",
            "url": "https://www.google.com/search?q=neighborhoods+in+florence&sca_esv=862d19b374e0a29b&sxsrf=ADLYWIKGQDqebDBKPNIOBHO7Bkhbdx9lvw%3A1715841901640&ei=batFZuPaJqK80PEPyoK5oAQ&ved=0ahUKEwijxaaYyZGGAxUiHjQIHUpBDkQQ4dUDCBE&uact=5&oq=neighborhoods+in+florence&gs_lp=Egxnd3Mtd2l6LXNlcnAiGW5laWdoYm9yaG9vZHMgaW4gZmxvcmVuY2UyEBAAGIAEGJECGIoFGEYY-wEyBRAAGIAEMgUQABiABDIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMhwQABiABBiRAhiKBRhGGPsBGJcFGIwFGN0E2AECSOYtUJIFWKgscAJ4AJABAJgB0QKgAZ47qgEHMi0xMS4xNLgBA8gBAPgBAZgCG6ACnT6oAhHCAgcQIxgnGOoCwgIUEAAYgAQY4wQYtAIY6QQY6gLYAQHCAgoQIxiABBgnGIoFwgIREC4YgAQYkQIY0QMYxwEYigXCAhcQLhiABBiRAhixAxjRAxiDARjHARiKBcICCxAuGIAEGLEDGIMBwgILEAAYgAQYsQMYgwHCAhEQLhiABBixAxjRAxiDARjHAcICDhAAGIAEGLEDGIMBGIoFwgIKEC4YgAQYJxiKBcICFBAuGIAEGJECGLEDGNEDGMcBGIoFwgIQEC4YgAQY0QMYQxjHARiKBcICEBAAGIAEGLEDGEMYgwEYigXCAgoQABiABBhDGIoFwgIPECMYgAQYJxiKBRhGGPsBwgIQEC4YgAQYQxjHARiKBRivAcICExAuGIAEGLEDGEMYgwEY1AIYigXCAg0QABiABBixAxhDGIoFwgIIEC4YgAQYsQPCAhkQABiABBiKBRhGGPsBGJcFGIwFGN0E2AECwgILEAAYgAQYkQIYigXCAgoQABiABBgUGIcCwgILEC4YgAQYsQMY1ALCAg4QLhiABBixAxjRAxjHAcICCBAAGIAEGLEDwgIHEAAYgAQYCsICChAAGIAEGLEDGArCAggQLhiABBjlBMICBxAuGIAEGArCAg0QLhiABBjRAxjHARgKwgILEAAYgAQYkgMYigXCAggQABiABBjJA8ICDxAAGIAEGBQYhwIYRhj7AcICGxAAGIAEGBQYhwIYRhj7ARiXBRiMBRjdBNgBApgDF7oGBggBEAEYAboGBggCEAEYE5IHCDIuMC43LjE4oAfupwI&sclient=gws-wiz-serp",
            "time_usec": 1715842181830323,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "best leather bags affordable in florence - Google Search",
            "url": "https://www.google.com/search?q=best+leather+bags+affordable+in+florence&oq=best+leather+bags+affordable+in+florence&aqs=chrome..69i64j69i57.13353j1j4&sourceid=chrome&ie=UTF-8#ip=1",
            "time_usec": 1715842153311276,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "best leather bags affordable in florence - Google Search",
            "url": "https://www.google.com/search?q=best+leather+bags+affordable+in+florence&oq=best+leather+bags+affordable+in+florence&aqs=chrome..69i64j69i57.13353j1j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715841948345891,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://www.supersavvytravelers.com/where-to-buy-the-best-italian-leather-handbags-in-florence-italy/",
            "time_usec": 1715841945572651,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "best leather bags affordable in florence - Google Search",
            "url": "https://www.google.com/search?q=best+leather+bags+affordable+in+florence&oq=best+leather+bags+affordable+in+florence&aqs=chrome..69i64j69i57.13353j1j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715841904383692,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://d1sigdaua9p397.cloudfront.net/assets/favicon-32-90f0d705ca96b3e979551d806865acce1791add0f3093189bee3e2d5046765b9.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Leather Shopping in Florence: My Advice - Rick Steves Travel Forum",
            "url": "https://community.ricksteves.com/travel-forum/italy/leather-shopping-in-florence-my-advice",
            "time_usec": 1715841609486839,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "best cheap leather in florence - Google Search",
            "url": "https://www.google.com/search?q=best+cheap+leather+in+florence&oq=best+cheap+leather+in+florence&aqs=chrome..69i64j69i57.14199j0j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715841600213244,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Boutique Nadine Vintage - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d2350284-Reviews-Boutique_Nadine_Vintage-Florence_Tuscany.html",
            "time_usec": 1715841424361611,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Tripadvisor",
            "url": "https://www.tripadvisor.com/Search?q=best+vintage+in+florence&geo=187895&ssrc=a&searchNearby=False&searchSessionId=000cdcbf522d4ad3.ssid&blockRedirect=true&offset=0",
            "time_usec": 1715841418163234,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Tripadvisor",
            "url": "https://www.tripadvisor.com/Search?q=best+vintage+in+florence&geo=187895&ssrc=a&searchNearby=False&searchSessionId=000cdcbf522d4ad3.ssid&blockRedirect=true&offset=0",
            "time_usec": 1715841322483394,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Tripadvisor",
            "url": "https://www.tripadvisor.com/Search?q=best+vintage+in+florence&geo=187895&ssrc=a&searchNearby=False&searchSessionId=000cdcbf522d4ad3.ssid&blockRedirect=true&offset=0",
            "time_usec": 1715841320859849,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Tripadvisor",
            "url": "https://www.tripadvisor.com/Search?q=best+vintage+in+florence&geo=187895&searchNearby=False&searchSessionId=000cdcbf522d4ad3.ssid",
            "time_usec": 1715841270820591,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Florence, Italy: All You Must Know Before You Go (2024) - Tripadvisor",
            "url": "https://www.tripadvisor.com/Tourism-g187895-Florence_Tuscany-Vacations.html",
            "time_usec": 1715841221488339,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Florence, Italy: All You Must Know Before You Go (2024) - Tripadvisor",
            "url": "https://www.tripadvisor.com/Tourism-g187895-Florence_Tuscany-Vacations.html",
            "time_usec": 1715840788608487,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Florence, Italy: All You Must Know Before You Go (2024) - Tripadvisor",
            "url": "https://www.tripadvisor.com/Tourism-g187895-Florence_Tuscany-Vacations.html",
            "time_usec": 1715840773167618,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Duomo - Cattedrale di Santa Maria del Fiore, Florence",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d198675-Reviews-Duomo_Cattedrale_di_Santa_Maria_del_Fiore-Florence_Tuscany.html",
            "time_usec": 1715840768073916,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Duomo - Cattedrale di Santa Maria del Fiore, Florence",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d198675-Reviews-Duomo_Cattedrale_di_Santa_Maria_del_Fiore-Florence_Tuscany.html",
            "time_usec": 1715840750193480,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "what is a duomo - Google Search",
            "url": "https://www.google.com/search?q=what+is+a+dumom&oq=what+is+a+dumom&aqs=chrome..69i64j35i39j35i39i512i650j0i512j0i131i433i512i650j0i512l2j0i131i433i512i650j0i512l2.3559j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715840714174093,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715840709192688,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Duomo - Cattedrale di Santa Maria del Fiore, Florence",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d198675-Reviews-Duomo_Cattedrale_di_Santa_Maria_del_Fiore-Florence_Tuscany.html",
            "time_usec": 1715840636138731,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Duomo - Cattedrale di Santa Maria del Fiore, Florence",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d198675-Reviews-Duomo_Cattedrale_di_Santa_Maria_del_Fiore-Florence_Tuscany.html",
            "time_usec": 1715840608206726,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Florence, Italy: All You Must Know Before You Go (2024) - Tripadvisor",
            "url": "https://www.tripadvisor.com/Tourism-g187895-Florence_Tuscany-Vacations.html",
            "time_usec": 1715840604437657,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Florence, Italy: All You Must Know Before You Go (2024) - Tripadvisor",
            "url": "https://www.tripadvisor.com/Tourism-g187895-Florence_Tuscany-Vacations.html",
            "time_usec": 1715840591335637,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Florence, Italy: All You Must Know Before You Go (2024) - Tripadvisor",
            "url": "https://www.tripadvisor.com/Tourism-g187895-Florence_Tuscany-Vacations.html",
            "time_usec": 1715840580821399,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Florence, Italy: All You Must Know Before You Go (2024) - Tripadvisor",
            "url": "https://www.tripadvisor.com/Tourism-g187895-Florence_Tuscany-Vacations.html",
            "time_usec": 1715840542279221,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Mercato delle Cascine - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d196114-Reviews-Mercato_delle_Cascine-Florence_Tuscany.html",
            "time_usec": 1715840541448225,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Nds Leather Factory - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d8015333-Reviews-Nds_Leather_Factory-Florence_Tuscany.html",
            "time_usec": 1715840497341240,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Nds Leather Factory - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d8015333-Reviews-Nds_Leather_Factory-Florence_Tuscany.html",
            "time_usec": 1715840465163868,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Nds Leather Factory - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d8015333-Reviews-Nds_Leather_Factory-Florence_Tuscany.html",
            "time_usec": 1715840457857216,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Nds Leather Factory - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d8015333-Reviews-Nds_Leather_Factory-Florence_Tuscany.html",
            "time_usec": 1715840445622187,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Nds Leather Factory - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d8015333-Reviews-Nds_Leather_Factory-Florence_Tuscany.html",
            "time_usec": 1715840435687620,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Nds Leather Factory - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d8015333-Reviews-Nds_Leather_Factory-Florence_Tuscany.html",
            "time_usec": 1715840431034014,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "THE 5 BEST Florence Flea & Street Markets (Updated 2024)",
            "url": "https://www.tripadvisor.com/Attractions-g187895-Activities-c26-t142-Florence_Tuscany.html",
            "time_usec": 1715840427235117,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Mercato delle Cascine - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d196114-Reviews-Mercato_delle_Cascine-Florence_Tuscany.html",
            "time_usec": 1715840420503473,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Mercato delle Cascine - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d196114-Reviews-Mercato_delle_Cascine-Florence_Tuscany.html",
            "time_usec": 1715840418187209,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Mercato delle Cascine - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d196114-Reviews-Mercato_delle_Cascine-Florence_Tuscany.html",
            "time_usec": 1715840345068914,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Mercato delle Cascine - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d196114-Reviews-Mercato_delle_Cascine-Florence_Tuscany.html",
            "time_usec": 1715840340268761,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Mercato delle Cascine - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d196114-Reviews-Mercato_delle_Cascine-Florence_Tuscany.html",
            "time_usec": 1715840328708727,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "THE 5 BEST Florence Flea & Street Markets (Updated 2024)",
            "url": "https://www.tripadvisor.com/Attractions-g187895-Activities-c26-t142-Florence_Tuscany.html",
            "time_usec": 1715840318305266,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/documents/images/kix-favicon-2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "what to do in florence!!! - Google Docs",
            "url": "https://docs.google.com/document/d/1Jm5HgLuld-TvcrDT0LikBeeGwcOl6HU0LUzGR7iKskw/edit",
            "time_usec": 1715840284261248,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Mercato delle Cascine - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d196114-Reviews-Mercato_delle_Cascine-Florence_Tuscany.html",
            "time_usec": 1715838406648044,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Mercato delle Cascine - All You Need to Know BEFORE You Go (2024)",
            "url": "https://www.tripadvisor.com/Attraction_Review-g187895-d196114-Reviews-Mercato_delle_Cascine-Florence_Tuscany.html",
            "time_usec": 1715838400663250,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "THE 5 BEST Florence Flea & Street Markets (Updated 2024)",
            "url": "https://www.tripadvisor.com/Attractions-g187895-Activities-c26-t142-Florence_Tuscany.html",
            "time_usec": 1715838394260296,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "THE 5 BEST Florence Flea & Street Markets (Updated 2024)",
            "url": "https://www.tripadvisor.com/Attractions-g187895-Activities-c26-t142-Florence_Tuscany.html",
            "time_usec": 1715838381191274,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://static.tacdn.com/favicon.ico?v2",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "THE 5 BEST Florence Flea & Street Markets (Updated 2024)",
            "url": "https://www.tripadvisor.com/Attractions-g187895-Activities-c26-t142-Florence_Tuscany.html",
            "time_usec": 1715838359420955,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "flea market florence italy - Google Search",
            "url": "https://www.google.com/search?q=flea+market+florence+italy&oq=flea+market+florence+italy+&aqs=chrome..69i64j46i175i199i512j0i512l4j0i22i30l3.10256j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715838350224039,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715838337875191,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "dia delle belle donne vintage - Google Search",
            "url": "https://www.google.com/search?q=dia+delle+belle+donne+vintage+&sca_esv=a8657e4f00d25584&sxsrf=ADLYWILsrS2E2OBGOHd3iTgW_8whCItONw%3A1715838266700&ei=Op1FZsCyKrfM0PEPxJW18AY&ved=0ahUKEwjAt4PTu5GGAxU3JjQIHcRKDW4Q4dUDCBE&uact=5&oq=dia+delle+belle+donne+vintage+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIh5kaWEgZGVsbGUgYmVsbGUgZG9ubmUgdmludGFnZSAyBRAhGKABMgUQIRigATIFECEYoAEyBRAhGKABMgUQIRigAUj3GFCNDVjXFXABeAGQAQCYAc8CoAGxFaoBBTItNC41uAEDyAEA-AEBmAIKoAKEFsICChAAGLADGNYEGEfCAgUQIRifBcICCBAhGIsDGJ8FmAMAiAYBkAYIkgcHMS4wLjEuOKAHhDM&sclient=gws-wiz-serp",
            "time_usec": 1715838308369928,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://humanavintage.it/humana-vintage-arriva-a-firenze/",
            "time_usec": 1715838305865487,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "dia delle belle donne - Google Search",
            "url": "https://www.google.com/search?q=dia+delle+belle+donne+&sca_esv=a8657e4f00d25584&sxsrf=ADLYWIKL9Yu2NjFwXxg0U4VQrLaSqtlYpg%3A1715838107579&ei=m5xFZpj0IvXy0PEPu6OpyAo&ved=0ahUKEwjYrZOHu5GGAxV1OTQIHbtRCqkQ4dUDCBE&uact=5&oq=dia+delle+belle+donne+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIhZkaWEgZGVsbGUgYmVsbGUgZG9ubmUgMgUQIRigATIFECEYoAEyBRAhGKABMgUQIRigAUijkAFQhwhYxY4BcA94AZABAJgB9gKgAYNNqgEHMi0xMC4yMrgBA8gBAPgBAZgCL6ACylCoAhTCAgcQIxgnGOoCwgIWEAAYAxi0AhjlAhjqAhiMAxiPAdgBAcICFhAuGAMYtAIY5QIY6gIYjAMYjwHYAQHCAgoQIxiABBgnGIoFwgIREC4YgAQYkQIYxwEYigUYrwHCAhEQLhiABBiRAhjRAxjHARiKBcICDhAAGIAEGLEDGIMBGIoFwgIOEC4YgAQYsQMY0QMYxwHCAhEQLhiABBixAxjRAxiDARjHAcICDhAuGIAEGLEDGIMBGIoFwgIEECMYJ8ICChAAGIAEGEMYigXCAgsQABiABBixAxiDAcICCxAAGIAEGJECGIoFwgIQEC4YgAQYsQMYQxiDARiKBcICCxAuGIAEGLEDGIMBwgINEC4YgAQYsQMYQxiKBcICDRAuGIAEGEMY1AIYigXCAggQABiABBixA8ICIBAuGIAEGJECGNEDGMcBGIoFGJcFGNwEGN4EGOAE2AECwgIPEAAYgAQYQxiKBRhGGPsBwgIQEAAYgAQYsQMYQxiDARiKBcICBBAAGAPCAg4QLhiABBixAxjHARivAcICGxAAGIAEGEMYigUYRhj7ARiXBRiMBRjdBNgBA8ICBRAAGIAEwgIHEAAYgAQYCsICBhAAGBYYHsICCBAAGBYYHhgPwgILEAAYgAQYhgMYigXCAgcQABiABBgTwgIJEAAYgAQYExgKwgIKEAAYExgWGB4YD8ICCBAAGBMYFhgewgIKEAAYExgWGAoYHsICDBAAGBMYFhgKGB4YD8ICBhAAGA0YHsICCBAAGA0YHhgPwgIKEAAYCBgKGA0YHsICCxAAGIAEGKIEGIsDwgIIEAAYFhgKGB7CAggQIRiLAxifBcICBxAhGKABGArCAgQQIRgVmAMaugYGCAEQARgLugYGCAIQARgUugYGCAMQARgTkgcJMTUuMC40LjI4oAfM6wE&sclient=gws-wiz-serp",
            "time_usec": 1715838267844601,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.redditstatic.com/shreddit/assets/favicon/64x64.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "thrifting shops in florence : r/florence",
            "url": "https://www.reddit.com/r/florence/comments/11a3wib/thrifting_shops_in_florence/?rdt=45596",
            "time_usec": 1715838231645166,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "nbest vintage stores in florence italy - Google Search",
            "url": "https://www.google.com/search?q=nbest+vintage+stores+in+florence+italy&oq=nbest+vintage+stores+in+florence+italy+&aqs=chrome..69i64j0i22i30l3j0i390i512i650l4j0i512i546j0i395i512i546.10775j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715838225508868,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "nbest vintage stores in florence italy - Google Search",
            "url": "https://www.google.com/search?q=nbest+vintage+stores+in+florence+italy&oq=nbest+vintage+stores+in+florence+italy+&aqs=chrome..69i64j0i22i30l3j0i390i512i650l4j0i512i546j0i395i512i546.10775j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715838206730286,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715838193272592,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "where to buy sambas in florence italy - Google Search",
            "url": "https://www.google.com/search?q=where+to+buy+sambas+in+florence+italy+&sca_esv=a8657e4f00d25584&sxsrf=ADLYWIJaVDrUs-PV967bWi12hl1CKLf7oA%3A1715838063288&ei=b5xFZs-VEYWv0PEP0aSumA8&ved=0ahUKEwiPiYTyupGGAxWFFzQIHVGSC_MQ4dUDCBE&uact=5&oq=where+to+buy+sambas+in+florence+italy+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIiZ3aGVyZSB0byBidXkgc2FtYmFzIGluIGZsb3JlbmNlIGl0YWx5IDIHEAAYgAQYDTIIEAAYCBgNGB4yCBAAGAgYDRgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGIAEGKIEMgsQABiABBiiBBiLA0i7RlCXCVisRXAFeACQAQKYAcUCoAGfWaoBBjItMzAuObgBA8gBAPgBAZgCKqACtFfCAgoQABiwAxjWBBhHwgIKECMYgAQYJxiKBcICBBAjGCfCAgsQABiABBiRAhiKBcICERAuGIAEGJECGLEDGIMBGIoFwgILEAAYgAQYsQMYgwHCAhEQLhiABBixAxjRAxiDARjHAcICCBAAGIAEGLEDwgIKEAAYgAQYQxiKBcICEBAAGIAEGLEDGEMYgwEYigXCAgUQABiABMICCxAAGIAEGLEDGIoFwgIKEAAYgAQYFBiHAsICCBAAGIAEGMkDwgILEAAYgAQYkgMYigXCAgcQABiABBgKmAMAiAYBkAYIkgcJNS4wLjE2LjIxoAehvwI&sclient=gws-wiz-serp&lqi=CiV3aGVyZSB0byBidXkgc2FtYmFzIGluIGZsb3JlbmNlIGl0YWx5SJ7Z2_uTuYCACFotEAMYAhgFIiV3aGVyZSB0byBidXkgc2FtYmFzIGluIGZsb3JlbmNlIGl0YWx5kgEKc2hvZV9zdG9yZaoBcgoKL20vMDI3enR5ahABKhciE3doZXJlIHRvIGJ1eSBzYW1iYXMoADIeEAEiGvyjwM2A60YeC0qnBdZ9KJKPdUlj8EnZkPmWMikQAiIld2hlcmUgdG8gYnV5IHNhbWJhcyBpbiBmbG9yZW5jZSBpdGFseeABAA#rlimm=11786000633158805671",
            "time_usec": 1715838177637438,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "where to buy sambas in florence italy - Google Search",
            "url": "https://www.google.com/search?q=where+to+buy+sambas+in+florence+italy+&sca_esv=a8657e4f00d25584&sxsrf=ADLYWIJaVDrUs-PV967bWi12hl1CKLf7oA%3A1715838063288&ei=b5xFZs-VEYWv0PEP0aSumA8&ved=0ahUKEwiPiYTyupGGAxWFFzQIHVGSC_MQ4dUDCBE&uact=5&oq=where+to+buy+sambas+in+florence+italy+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIiZ3aGVyZSB0byBidXkgc2FtYmFzIGluIGZsb3JlbmNlIGl0YWx5IDIHEAAYgAQYDTIIEAAYCBgNGB4yCBAAGAgYDRgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGIAEGKIEMgsQABiABBiiBBiLA0i7RlCXCVisRXAFeACQAQKYAcUCoAGfWaoBBjItMzAuObgBA8gBAPgBAZgCKqACtFfCAgoQABiwAxjWBBhHwgIKECMYgAQYJxiKBcICBBAjGCfCAgsQABiABBiRAhiKBcICERAuGIAEGJECGLEDGIMBGIoFwgILEAAYgAQYsQMYgwHCAhEQLhiABBixAxjRAxiDARjHAcICCBAAGIAEGLEDwgIKEAAYgAQYQxiKBcICEBAAGIAEGLEDGEMYgwEYigXCAgUQABiABMICCxAAGIAEGLEDGIoFwgIKEAAYgAQYFBiHAsICCBAAGIAEGMkDwgILEAAYgAQYkgMYigXCAgcQABiABBgKmAMAiAYBkAYIkgcJNS4wLjE2LjIxoAehvwI&sclient=gws-wiz-serp&lqi=CiV3aGVyZSB0byBidXkgc2FtYmFzIGluIGZsb3JlbmNlIGl0YWx5SJ7Z2_uTuYCACFotEAMYAhgFIiV3aGVyZSB0byBidXkgc2FtYmFzIGluIGZsb3JlbmNlIGl0YWx5kgEKc2hvZV9zdG9yZaoBcgoKL20vMDI3enR5ahABKhciE3doZXJlIHRvIGJ1eSBzYW1iYXMoADIeEAEiGvyjwM2A60YeC0qnBdZ9KJKPdUlj8EnZkPmWMikQAiIld2hlcmUgdG8gYnV5IHNhbWJhcyBpbiBmbG9yZW5jZSBpdGFseeABAA#rlimm=11786000633158805671",
            "time_usec": 1715838141990855,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "where to buy sambas in florence italy - Google Search",
            "url": "https://www.google.com/search?q=where+to+buy+sambas+in+florence+italy+&sca_esv=a8657e4f00d25584&sxsrf=ADLYWIJaVDrUs-PV967bWi12hl1CKLf7oA%3A1715838063288&ei=b5xFZs-VEYWv0PEP0aSumA8&ved=0ahUKEwiPiYTyupGGAxWFFzQIHVGSC_MQ4dUDCBE&uact=5&oq=where+to+buy+sambas+in+florence+italy+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIiZ3aGVyZSB0byBidXkgc2FtYmFzIGluIGZsb3JlbmNlIGl0YWx5IDIHEAAYgAQYDTIIEAAYCBgNGB4yCBAAGAgYDRgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGIAEGKIEMgsQABiABBiiBBiLA0i7RlCXCVisRXAFeACQAQKYAcUCoAGfWaoBBjItMzAuObgBA8gBAPgBAZgCKqACtFfCAgoQABiwAxjWBBhHwgIKECMYgAQYJxiKBcICBBAjGCfCAgsQABiABBiRAhiKBcICERAuGIAEGJECGLEDGIMBGIoFwgILEAAYgAQYsQMYgwHCAhEQLhiABBixAxjRAxiDARjHAcICCBAAGIAEGLEDwgIKEAAYgAQYQxiKBcICEBAAGIAEGLEDGEMYgwEYigXCAgUQABiABMICCxAAGIAEGLEDGIoFwgIKEAAYgAQYFBiHAsICCBAAGIAEGMkDwgILEAAYgAQYkgMYigXCAgcQABiABBgKmAMAiAYBkAYIkgcJNS4wLjE2LjIxoAehvwI&sclient=gws-wiz-serp",
            "time_usec": 1715838140377253,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "where to buy sambas in florence italy - Google Search",
            "url": "https://www.google.com/search?q=where+to+buy+sambas+in+florence+italy+&sca_esv=a8657e4f00d25584&sxsrf=ADLYWIJaVDrUs-PV967bWi12hl1CKLf7oA%3A1715838063288&ei=b5xFZs-VEYWv0PEP0aSumA8&ved=0ahUKEwiPiYTyupGGAxWFFzQIHVGSC_MQ4dUDCBE&uact=5&oq=where+to+buy+sambas+in+florence+italy+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIiZ3aGVyZSB0byBidXkgc2FtYmFzIGluIGZsb3JlbmNlIGl0YWx5IDIHEAAYgAQYDTIIEAAYCBgNGB4yCBAAGAgYDRgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGIAEGKIEMgsQABiABBiiBBiLA0i7RlCXCVisRXAFeACQAQKYAcUCoAGfWaoBBjItMzAuObgBA8gBAPgBAZgCKqACtFfCAgoQABiwAxjWBBhHwgIKECMYgAQYJxiKBcICBBAjGCfCAgsQABiABBiRAhiKBcICERAuGIAEGJECGLEDGIMBGIoFwgILEAAYgAQYsQMYgwHCAhEQLhiABBixAxjRAxiDARjHAcICCBAAGIAEGLEDwgIKEAAYgAQYQxiKBcICEBAAGIAEGLEDGEMYgwEYigXCAgUQABiABMICCxAAGIAEGLEDGIoFwgIKEAAYgAQYFBiHAsICCBAAGIAEGMkDwgILEAAYgAQYkgMYigXCAgcQABiABBgKmAMAiAYBkAYIkgcJNS4wLjE2LjIxoAehvwI&sclient=gws-wiz-serp&lqi=CiV3aGVyZSB0byBidXkgc2FtYmFzIGluIGZsb3JlbmNlIGl0YWx5SOW3-NPLq4CACFotEAMYAhgFIiV3aGVyZSB0byBidXkgc2FtYmFzIGluIGZsb3JlbmNlIGl0YWx5kgEKc2hvZV9zdG9yZaoBcgoKL20vMDI3enR5ahABKhciE3doZXJlIHRvIGJ1eSBzYW1iYXMoADIeEAEiGvyjwM2A60YeC0qnBdZ9KJKPdUlj8EnZkPmWMikQAiIld2hlcmUgdG8gYnV5IHNhbWJhcyBpbiBmbG9yZW5jZSBpdGFseeABAA#rlimm=11147952717393776805",
            "time_usec": 1715838125586602,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "where to buy sambas in florence italy - Google Search",
            "url": "https://www.google.com/search?q=where+to+buy+sambas+in+florence+italy+&sca_esv=a8657e4f00d25584&sxsrf=ADLYWIJaVDrUs-PV967bWi12hl1CKLf7oA%3A1715838063288&ei=b5xFZs-VEYWv0PEP0aSumA8&ved=0ahUKEwiPiYTyupGGAxWFFzQIHVGSC_MQ4dUDCBE&uact=5&oq=where+to+buy+sambas+in+florence+italy+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIiZ3aGVyZSB0byBidXkgc2FtYmFzIGluIGZsb3JlbmNlIGl0YWx5IDIHEAAYgAQYDTIIEAAYCBgNGB4yCBAAGAgYDRgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGIAEGKIEMgsQABiABBiiBBiLA0i7RlCXCVisRXAFeACQAQKYAcUCoAGfWaoBBjItMzAuObgBA8gBAPgBAZgCKqACtFfCAgoQABiwAxjWBBhHwgIKECMYgAQYJxiKBcICBBAjGCfCAgsQABiABBiRAhiKBcICERAuGIAEGJECGLEDGIMBGIoFwgILEAAYgAQYsQMYgwHCAhEQLhiABBixAxjRAxiDARjHAcICCBAAGIAEGLEDwgIKEAAYgAQYQxiKBcICEBAAGIAEGLEDGEMYgwEYigXCAgUQABiABMICCxAAGIAEGLEDGIoFwgIKEAAYgAQYFBiHAsICCBAAGIAEGMkDwgILEAAYgAQYkgMYigXCAgcQABiABBgKmAMAiAYBkAYIkgcJNS4wLjE2LjIxoAehvwI&sclient=gws-wiz-serp",
            "time_usec": 1715838107949648,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "sneaker store in florence italy - Google Search",
            "url": "https://www.google.com/search?q=sneaker+store+in+florence+italy+&sca_esv=a8657e4f00d25584&sxsrf=ADLYWIIj2yp32NXKXAEEsXHnhyQzGmTphQ%3A1715838059196&ei=a5xFZo3IC7KA0PEPsN-iuAI&ved=0ahUKEwjNqYrwupGGAxUyADQIHbCvCCcQ4dUDCBE&uact=5&oq=sneaker+store+in+florence+italy+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIiBzbmVha2VyIHN0b3JlIGluIGZsb3JlbmNlIGl0YWx5IDIGEAAYFhgeMgYQABgWGB4yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGKIEGIsDSM8JUN4CWMYJcAF4AZABAJgBvgKgAZsHqgEDMy0zuAEDyAEA-AEBmAIEoALMB8ICChAAGLADGNYEGEfCAgUQABiABJgDAIgGAZAGCJIHBTEuMy0zoAetEA&sclient=gws-wiz-serp",
            "time_usec": 1715838091745913,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://www.wearebasket.net/four-great-sneaker-stores-in-florence/",
            "time_usec": 1715838084971484,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "sneaker store in florence italy - Google Search",
            "url": "https://www.google.com/search?q=sneaker+store+in+florence+italy+&sca_esv=a8657e4f00d25584&sxsrf=ADLYWIIj2yp32NXKXAEEsXHnhyQzGmTphQ%3A1715838059196&ei=a5xFZo3IC7KA0PEPsN-iuAI&ved=0ahUKEwjNqYrwupGGAxUyADQIHbCvCCcQ4dUDCBE&uact=5&oq=sneaker+store+in+florence+italy+&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIiBzbmVha2VyIHN0b3JlIGluIGZsb3JlbmNlIGl0YWx5IDIGEAAYFhgeMgYQABgWGB4yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGKIEGIsDSM8JUN4CWMYJcAF4AZABAJgBvgKgAZsHqgEDMy0zuAEDyAEA-AEBmAIEoALMB8ICChAAGLADGNYEGEfCAgUQABiABJgDAIgGAZAGCJIHBTEuMy0zoAetEA&sclient=gws-wiz-serp",
            "time_usec": 1715838063598014,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "sneaker store in florence - Google Search",
            "url": "https://www.google.com/search?q=sneaker+store+in+florence&sca_esv=a8657e4f00d25584&sxsrf=ADLYWILTPbB8OqlVSwDgCvoLDttnCG-UMg%3A1715838034071&ei=UpxFZrv4A6CE0PEP3OaaiA4&ved=0ahUKEwi76YzkupGGAxUgAjQIHVyzBuEQ4dUDCBE&uact=5&oq=sneaker+store+in+florence&gs_lp=Egxnd3Mtd2l6LXNlcnAiGXNuZWFrZXIgc3RvcmUgaW4gZmxvcmVuY2UyCxAAGIAEGJECGIoFMgUQABiABDIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgsQABiABBiGAxiKBUiAVFCfEVjuUnAQeAGQAQSYAdoCoAHvTaoBBzItMjEuMTK4AQPIAQD4AQGYAi2gAtJHqAITwgIKEAAYsAMY1gQYR8ICBBAjGCfCAgoQIxiABBgnGIoFwgIKEAAYgAQYQxiKBcICERAuGIAEGJECGNEDGMcBGIoFwgIXEC4YgAQYkQIYsQMY0QMYgwEYxwEYigXCAg0QABiABBixAxhDGIoFwgIKEAAYgAQYFBiHAsICCBAAGIAEGLEDwgIHECMYJxjqAsICFBAAGIAEGOMEGLQCGOkEGOoC2AEBwgIaEC4YgAQY4wQYtAIYxwEY6QQY6gIYrwHYAQHCAhYQABgDGLQCGOUCGOoCGIwDGI8B2AECwgIREAAYgAQYkQIYsQMYgwEYigXCAhAQLhiABBjRAxhDGMcBGIoFwgIMEAAYgAQYQxiKBRgKwgILEAAYgAQYsQMYgwHCAg4QABiABBiRAhixAxiKBcICCxAAGIAEGJIDGIoFwgIREAAYgAQYkQIYsQMYyQMYigXCAggQABgWGB4YD5gDEIgGAZAGCLoGBggBEAEYAboGBggCEAEYC5IHCTE2LjAuOC4yMaAH3toB&sclient=gws-wiz-serp",
            "time_usec": 1715838059537411,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "florence shoe store - Google Search",
            "url": "https://www.google.com/search?q=florence+shoe+store&oq=florence+shoe+store+&aqs=chrome..69i64j69i57.6934j0j9&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715838035952868,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "www.google.com",
            "url": "https://www.google.com/search?q=florence+shoe+store&oq=florence+shoe+store+&aqs=chrome..69i64j69i57.6934j0j9&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715838024721909,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715837881064601,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "can you download amovie on amazon prime video - Google Search",
            "url": "https://www.google.com/search?q=can+you+download+amovie+on+amazon+prime+video&oq=can+you+download+amovie+on+amazon+prime+video&aqs=chrome..69i64j0i22i30l2j0i22i30i395j0i390i395i512i650l3j0i395i512i546l2j0i395i546i649.20103j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715801914284783,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715801892767273,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Watch House of Gucci | Prime Video",
            "url": "https://www.amazon.com/House-Gucci-Lady-Gaga/dp/B09NSWH9RH/ref=sr_1_1?crid=L9TI2ALTNIKO&dib=eyJ2IjoiMSJ9.fy_eJiyF5AdtA3wI6QSGQxkYXGc37DfhXSnmyBYb5kXGjHj071QN20LucGBJIEps.YF9Q6kKGA_C9AsIlhcivokLGeMquQKEo8pi_0iLhsiE&dib_tag=se&keywords=house+of+gucci&qid=1715801716&s=instant-video&sprefix=house+of+gucci%2Cinstant-video%2C98&sr=1-1",
            "time_usec": 1715801719309957,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon.com : house of gucci",
            "url": "https://www.amazon.com/s?k=house+of+gucci&i=instant-video&crid=L9TI2ALTNIKO&sprefix=house+of+gucci%2Cinstant-video%2C98&ref=nb_sb_noss_1",
            "time_usec": 1715801716103519,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Prime Video | Watch movies, TV shows, Live TV, and sports",
            "url": "https://www.amazon.com/gp/video/storefront/ref=atv_hom_intercept_c_9zZ8D2_hom",
            "time_usec": 1715801699387949,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon.com : dune",
            "url": "https://www.amazon.com/s?k=dune&i=instant-video&crid=U4FXZ50QLGJN&sprefix=dune%2Cinstant-video%2C78&ref=nb_sb_noss_1",
            "time_usec": 1715801688640363,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Prime Video | Watch movies, TV shows, Live TV, and sports",
            "url": "https://www.amazon.com/gp/video/storefront/ref=atv_hom_intercept_c_9zZ8D2_hom",
            "time_usec": 1715801672536613,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon.com Sign up for Prime Video",
            "url": "https://www.amazon.com/gp/video/offers/intercept?ref=dvm_us_dl_sl_go_s_brsa_mkw_svHxbIxqC-dc&mrntrk=pcrid_690357294689_slid__pgrid_29008589832_pgeo_9004425_x__adext__ptid_kwd-45697133742",
            "time_usec": 1715801662055615,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "amazon prime video - Google Search",
            "url": "https://www.google.com/search?q=amazon+prime+video&oq=amazon+prime+video&aqs=chrome..69i64j0i433i512l2j0i512l6j46i512.5685j0j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715801661055645,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon.com: Amazon Prime",
            "url": "https://www.amazon.com/amazonprime?tag=googhydr-20&hvadid=550213431242&hvpos=&hvexid=&hvnetw=g&hvrand=11121714260443872623&hvpone=&hvptwo=&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9004425&hvtargid=kwd-3151046130&ref=pd_sl_34qfrygf2i_e",
            "time_usec": 1715801649442946,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "amazon prime - Google Search",
            "url": "https://www.google.com/search?q=amazon+prime&oq=amazon+prime&aqs=chrome..69i64j0i131i433i512l2j0i433i512j0i512j0i433i512j0i131i433i512l2j0i433i512l2.29646j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715801640208226,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715801608813403,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Your Account",
            "url": "https://www.amazon.com/gp/css/homepage.html?ref_=nav_AccountFlyout_ya",
            "time_usec": 1715801589406780,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon.com. Spend less. Smile more.",
            "url": "https://www.amazon.com/?ref_=nav_custrec_signin",
            "time_usec": 1715801574032675,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon",
            "url": "https://www.amazon.com/ap/cvf/transactionapproval?arb=5bd2a615-bdaf-4ced-843d-59b479d07db9&openid.assoc_handle=usflex&pageId=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%3Fie%3DUTF8%26clientContext%3D131-0257903-6832646%26arb%3D279cd120-aaa6-4632-b161-40ee491eb872%26openid.pape.max_auth_age%3D0%26use_global_authentication%3DFalse%26openid.return_to%3Dhttps%253A%252F%252Fwww.amazon.com%252F%253Fref_%253Dnav_custrec_signin%26openid.identity%3Dhttps%253A%252F%252Fwww.amazon.com%252Fap%252Fid%252Famzn1.account.AFMOPQ5YDSGKERMQ7PVMTPD3P27A%26openid.assoc_handle%3Dusflex%26openid.mode%3Dcheckid_setup%26openid.claimed_id%3Dhttps%253A%252F%252Fwww.amazon.com%252Fap%252Fid%252Famzn1.account.AFMOPQ5YDSGKERMQ7PVMTPD3P27A%26ignoreAuthState%3D1%26pageId%3Dusflex%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0",
            "time_usec": 1715801539591897,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon Sign-In",
            "url": "https://www.amazon.com/ap/signin",
            "time_usec": 1715801532170821,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon Sign-In",
            "url": "https://www.amazon.com/ap/signin?ie=UTF8&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&switch_account=auth_prompt&ignoreAuthState=1&openid.identity=https%3A%2F%2Fwww.amazon.com%2Fap%2Fid%2Famzn1.account.AFMOPQ5YDSGKERMQ7PVMTPD3P27A&openid.claimed_id=https%3A%2F%2Fwww.amazon.com%2Fap%2Fid%2Famzn1.account.AFMOPQ5YDSGKERMQ7PVMTPD3P27A",
            "time_usec": 1715801511621043,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon Sign-In",
            "url": "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0",
            "time_usec": 1715801509555696,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon.com. Spend less. Smile more.",
            "url": "https://www.amazon.com/",
            "time_usec": 1715801505944167,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon",
            "url": "https://www.amazon.com/ap/cvf/transactionapproval?arb=1a0cacd1-bcd7-40a0-99bc-b3e08e7fdc23&openid.assoc_handle=usflex&pageId=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%3Fie%3DUTF8%26clientContext%3D131-0257903-6832646%26arb%3D047e7200-da9a-49b6-8417-ed4e91fdbd17%26openid.pape.max_auth_age%3D0%26use_global_authentication%3DFalse%26openid.return_to%3Dhttps%253A%252F%252Fwww.amazon.com%252F%253Fref_%253Dnav_signin%26openid.identity%3Dhttps%253A%252F%252Fwww.amazon.com%252Fap%252Fid%252Famzn1.account.AFMOPQ5YDSGKERMQ7PVMTPD3P27A%26openid.assoc_handle%3Dusflex%26openid.mode%3Dcheckid_setup%26openid.claimed_id%3Dhttps%253A%252F%252Fwww.amazon.com%252Fap%252Fid%252Famzn1.account.AFMOPQ5YDSGKERMQ7PVMTPD3P27A%26ignoreAuthState%3D1%26pageId%3Dusflex%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0",
            "time_usec": 1715801500610708,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon",
            "url": "https://www.amazon.com/ap/cvf/transactionapproval?arb=1a0cacd1-bcd7-40a0-99bc-b3e08e7fdc23&openid.assoc_handle=usflex&pageId=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%3Fie%3DUTF8%26clientContext%3D131-0257903-6832646%26arb%3D047e7200-da9a-49b6-8417-ed4e91fdbd17%26openid.pape.max_auth_age%3D0%26use_global_authentication%3DFalse%26openid.return_to%3Dhttps%253A%252F%252Fwww.amazon.com%252F%253Fref_%253Dnav_signin%26openid.identity%3Dhttps%253A%252F%252Fwww.amazon.com%252Fap%252Fid%252Famzn1.account.AFMOPQ5YDSGKERMQ7PVMTPD3P27A%26openid.assoc_handle%3Dusflex%26openid.mode%3Dcheckid_setup%26openid.claimed_id%3Dhttps%253A%252F%252Fwww.amazon.com%252Fap%252Fid%252Famzn1.account.AFMOPQ5YDSGKERMQ7PVMTPD3P27A%26ignoreAuthState%3D1%26pageId%3Dusflex%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0",
            "time_usec": 1715800387895127,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon Sign-In",
            "url": "https://www.amazon.com/ap/signin?ie=UTF8&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&switch_account=auth_prompt&ignoreAuthState=1&openid.identity=https%3A%2F%2Fwww.amazon.com%2Fap%2Fid%2Famzn1.account.AFMOPQ5YDSGKERMQ7PVMTPD3P27A&openid.claimed_id=https%3A%2F%2Fwww.amazon.com%2Fap%2Fid%2Famzn1.account.AFMOPQ5YDSGKERMQ7PVMTPD3P27A",
            "time_usec": 1715800381367259,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon Sign-In",
            "url": "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0",
            "time_usec": 1715800377621873,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon.com. Spend less. Smile more.",
            "url": "https://www.amazon.com/",
            "time_usec": 1715800372859229,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "how do you update a macbook - Google Search",
            "url": "https://www.google.com/search?q=how+do+you+update+a+macbook&oq=how+do+you+update+a+macbook+&aqs=chrome.0.0i512l4j0i22i30l6.10335j0j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715800263533292,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715800251797946,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://support.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Download & install Google Chrome - Computer - Google Chrome Help",
            "url": "https://support.google.com/chrome/answer/95346?visit_id=638513966482970418-3158389734&p=unsupported_mac&rd=1#sysreq_mac&zippy=%2Cmac",
            "time_usec": 1715800248684360,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://support.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Download & install Google Chrome - Computer - Google Chrome Help",
            "url": "https://support.google.com/chrome/answer/95346?visit_id=638513966482970418-3158389734&p=unsupported_mac&rd=1#sysreq_mac&zippy=%2Cmac",
            "time_usec": 1715799881370960,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://support.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Update Google Chrome - Computer - Google Chrome Help",
            "url": "https://support.google.com/chrome/answer/95414",
            "time_usec": 1715799848603752,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://help.nflxext.com/nficon2023.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Netflix says 'Update required' | Netflix Help Center",
            "url": "https://help.netflix.com/en/node/133344",
            "time_usec": 1715799839333084,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://assets.nflxext.com/us/ffe/siteui/common/icons/nficon2023.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Netflix",
            "url": "https://www.netflix.com/",
            "time_usec": 1715799831984329,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://search.funsafetabsearch.com/?pub_id=3000&srcid=A341B_set_bcr&q=netflix",
            "time_usec": 1715799827205151,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715799823629815,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "\"confirmations\" - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#label/confirmations",
            "time_usec": 1715799742378733,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,369) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1715799728542189,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Expedia travel confirmation - Tue, Jul 2 - (Itinerary # 72830971459092) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzGxTNtmXNdbJPhhcknRQBfcnGSJ",
            "time_usec": 1715799719849446,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon.com Page Not Found",
            "url": "https://www.amazon.com/404",
            "time_usec": 1715799640624734,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Expedia travel confirmation - Tue, Jul 2 - (Itinerary # 72830971459092) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox/FMfcgzGxTNtmXNdbJPhhcknRQBfcnGSJ",
            "time_usec": 1715799607944615,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Inbox (1,370) - ryanfrancissteele@gmail.com - Gmail",
            "url": "https://mail.google.com/mail/u/0/#inbox",
            "time_usec": 1715799604862797,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Expedia: Confirmation",
            "url": "https://www.expedia.com/Checkout/V1/HotelBookingConfirmation?tripid=33ced044-5618-51db-85c3-f089ad0c096a&c=81fdb32e-e186-4fcf-8e51-547d9a91e9c3",
            "time_usec": 1715799360833202,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Munich, Bavaria, Germany Hotel Search Results",
            "url": "https://www.expedia.com/Hotel-Search?regionId=2452&locale=en_US&siteid=1&lodging=HOSTEL&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798321660.b1114087969585.g1kwd-844347623.e1c.m1CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE.r1019a80a7971c756d5b827945699f8532082b2c4a72e8bb8a3c915d47830202f9.c12WfmTMjFYINq_7Pa-pgq2w.j19004425.k1.d1484877562231.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&gad_source=1&gclid=CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE&startDate=2024-07-02&endDate=2024-07-05&destination=Munich%2C%20Bavaria%2C%20Germany&theme=&userIntent=&useRewards=true&sort=RECOMMENDED&latLong=&adults=1&children=&pwaDialog=&mapBounds=&allowPreAppliedFilters=False&pwaOverlay=map",
            "time_usec": 1715799135415691,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/spreadsheets/spreadsheets_2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "summer travel 2024 - Google Sheets",
            "url": "https://docs.google.com/spreadsheets/d/1-T5fdMtwH1xCgWqH2apRDq-3nPMUFhOSN-UCKM9j5CI/edit#gid=0",
            "time_usec": 1715799091502270,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Travel - Google Drive",
            "url": "https://drive.google.com/drive/folders/1Q8OZlnqFsux-k-Jz-x2O_d4H2WL3NZjU",
            "time_usec": 1715799082948536,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "My Drive - Google Drive",
            "url": "https://drive.google.com/drive/my-drive",
            "time_usec": 1715799080087545,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Home - Google Drive",
            "url": "https://drive.google.com/drive/home",
            "time_usec": 1715799073897161,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Expedia: Payment",
            "url": "https://www.expedia.com/HotelCheckout?tripid=33ced044-5618-51db-85c3-f089ad0c096a&c=118607d8-7cb9-43cd-8dfa-1139f74f8d7f&swpApplied=False&searchId=0df5d6f5-c62c-4796-b7e2-fc42a6ba3e14",
            "time_usec": 1715799029794173,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Jaeger's Munich - Hostel",
            "url": "https://www.expedia.com/Munich-Hotels-Jaegers-Munich.h24183910.Hotel-Information?chkin=2024-07-02&chkout=2024-07-05&x_pwa=1&rfrr=HSR&pwa_ts=1715798786686&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=2452&destination=Munich%2C%20Bavaria%2C%20Germany&destType=MARKET&neighborhoodId=553248635213031865&latLong=48.13512%2C11.58198&lodging=HOSTEL&sort=RECOMMENDED&top_dp=35&top_cur=USD&gclid=CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798321660.b1114087969585.g1kwd-844347623.e1c.m1CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE.r1019a80a7971c756d5b827945699f8532082b2c4a72e8bb8a3c915d47830202f9.c12WfmTMjFYINq_7Pa-pgq2w.j19004425.k1.d1484877562231.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&userIntent=&selectedRoomType=219923270&selectedRatePlan=395175090&searchId=0df5d6f5-c62c-4796-b7e2-fc42a6ba3e14&propertyName=Jaeger%27s%20Munich%20-%20Hostel&pwaPaymentDialog=payment-5vyqc",
            "time_usec": 1715799008633123,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Jaeger's Munich - Hostel",
            "url": "https://www.expedia.com/Munich-Hotels-Jaegers-Munich.h24183910.Hotel-Information?chkin=2024-07-02&chkout=2024-07-05&x_pwa=1&rfrr=HSR&pwa_ts=1715798786686&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=2452&destination=Munich%2C%20Bavaria%2C%20Germany&destType=MARKET&neighborhoodId=553248635213031865&latLong=48.13512%2C11.58198&lodging=HOSTEL&sort=RECOMMENDED&top_dp=35&top_cur=USD&gclid=CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798321660.b1114087969585.g1kwd-844347623.e1c.m1CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE.r1019a80a7971c756d5b827945699f8532082b2c4a72e8bb8a3c915d47830202f9.c12WfmTMjFYINq_7Pa-pgq2w.j19004425.k1.d1484877562231.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&userIntent=&selectedRoomType=219923270&selectedRatePlan=395175090&searchId=0df5d6f5-c62c-4796-b7e2-fc42a6ba3e14&propertyName=Jaeger%27s%20Munich%20-%20Hostel",
            "time_usec": 1715798951510447,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Jaeger's Munich - Hostel",
            "url": "https://www.expedia.com/Munich-Hotels-Jaegers-Munich.h24183910.Hotel-Information?chkin=2024-07-02&chkout=2024-07-05&x_pwa=1&rfrr=HSR&pwa_ts=1715798786686&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=2452&destination=Munich%2C%20Bavaria%2C%20Germany&destType=MARKET&neighborhoodId=553248635213031865&latLong=48.13512%2C11.58198&lodging=HOSTEL&sort=RECOMMENDED&top_dp=35&top_cur=USD&gclid=CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798321660.b1114087969585.g1kwd-844347623.e1c.m1CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE.r1019a80a7971c756d5b827945699f8532082b2c4a72e8bb8a3c915d47830202f9.c12WfmTMjFYINq_7Pa-pgq2w.j19004425.k1.d1484877562231.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&userIntent=&selectedRoomType=219923270&selectedRatePlan=395175090&searchId=0df5d6f5-c62c-4796-b7e2-fc42a6ba3e14&propertyName=Jaeger%27s%20Munich%20-%20Hostel&pwaThumbnailDialog=thumbnail-gallery",
            "time_usec": 1715798832609099,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Jaeger's Munich - Hostel",
            "url": "https://www.expedia.com/Munich-Hotels-Jaegers-Munich.h24183910.Hotel-Information?chkin=2024-07-02&chkout=2024-07-05&x_pwa=1&rfrr=HSR&pwa_ts=1715798786686&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=2452&destination=Munich%2C%20Bavaria%2C%20Germany&destType=MARKET&neighborhoodId=553248635213031865&latLong=48.13512%2C11.58198&lodging=HOSTEL&sort=RECOMMENDED&top_dp=35&top_cur=USD&gclid=CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798321660.b1114087969585.g1kwd-844347623.e1c.m1CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE.r1019a80a7971c756d5b827945699f8532082b2c4a72e8bb8a3c915d47830202f9.c12WfmTMjFYINq_7Pa-pgq2w.j19004425.k1.d1484877562231.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&userIntent=&selectedRoomType=219923270&selectedRatePlan=395175090&searchId=0df5d6f5-c62c-4796-b7e2-fc42a6ba3e14&propertyName=Jaeger%27s%20Munich%20-%20Hostel",
            "time_usec": 1715798822366391,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Munich, Bavaria, Germany Hotel Search Results",
            "url": "https://www.expedia.com/Hotel-Search?regionId=2452&locale=en_US&siteid=1&lodging=HOSTEL&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798321660.b1114087969585.g1kwd-844347623.e1c.m1CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE.r1019a80a7971c756d5b827945699f8532082b2c4a72e8bb8a3c915d47830202f9.c12WfmTMjFYINq_7Pa-pgq2w.j19004425.k1.d1484877562231.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&gad_source=1&gclid=CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE&startDate=2024-07-02&endDate=2024-07-05&destination=Munich%2C%20Bavaria%2C%20Germany&theme=&userIntent=&useRewards=true&sort=RECOMMENDED&latLong=&adults=1&children=&pwaDialog=&mapBounds=&allowPreAppliedFilters=False",
            "time_usec": 1715798787015064,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Munich, Bavaria, Germany Hotel Search Results",
            "url": "https://www.expedia.com/Hotel-Search?regionId=2452&locale=en_US&siteid=1&lodging=HOSTEL&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798321660.b1114087969585.g1kwd-844347623.e1c.m1CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE.r1019a80a7971c756d5b827945699f8532082b2c4a72e8bb8a3c915d47830202f9.c12WfmTMjFYINq_7Pa-pgq2w.j19004425.k1.d1484877562231.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&gad_source=1&gclid=CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE&startDate=2024-07-02&endDate=2024-07-05&destination=Munich%2C+Bavaria%2C+Germany&theme=&userIntent=&useRewards=true&sort=RECOMMENDED&latLong=&adults=1&children=&pwaDialog=&mapBounds=&allowPreAppliedFilters=False",
            "time_usec": 1715798784858307,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Munich, Bavaria, Germany Hotel Search Results",
            "url": "https://www.expedia.com/Hotel-Search?regionId=2452&locale=en_US&siteid=1&lodging=HOSTEL&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798321660.b1114087969585.g1kwd-844347623.e1c.m1CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE.r1019a80a7971c756d5b827945699f8532082b2c4a72e8bb8a3c915d47830202f9.c12WfmTMjFYINq_7Pa-pgq2w.j19004425.k1.d1484877562231.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&gad_source=1&gclid=CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE&startDate=2024-07-02&endDate=2024-07-05&destination=Munich%2C%20Bavaria%2C%20Germany&theme=&userIntent=&useRewards=true&sort=RECOMMENDED&latLong=&adults=2&children=&pwaDialog=&mapBounds=&allowPreAppliedFilters=False",
            "time_usec": 1715798779081001,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.expedia.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Munich, Bavaria, Germany Hotel Search Results",
            "url": "https://www.expedia.com/Hotel-Search?regionId=2452&locale=en_US&siteid=1&lodging=HOSTEL&semcid=US.UB.GOOGLE.DT-c-EN.HOTEL&semdtl=a111798321660.b1114087969585.g1kwd-844347623.e1c.m1CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE.r1019a80a7971c756d5b827945699f8532082b2c4a72e8bb8a3c915d47830202f9.c12WfmTMjFYINq_7Pa-pgq2w.j19004425.k1.d1484877562231.h1p.i1.l1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&gad_source=1&gclid=CjwKCAjwupGyBhBBEiwA0UcqaBbky6RSPe0_EMrkTENBjKRFwdF-i8YydDkSD3BdUWF6syqoilm1TRoCO6AQAvD_BwE&startDate=2024-05-29&endDate=2024-05-30&destination=Munich%2C%20Bavaria%2C%20Germany&theme=&userIntent=&useRewards=true&sort=RECOMMENDED",
            "time_usec": 1715798758303202,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hostels in munich germany july 2-5 - Google Search",
            "url": "https://www.google.com/search?q=hostels+in+munich+germany+july+2-5&oq=hostels+in+munich+germany+july+2-5&aqs=chrome..69i64j69i57.14869j1j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715798747573467,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.hostelworld.com/st/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Euro Youth Hostel, Munich - 2024 Prices & Reviews - Hostelworld",
            "url": "https://www.hostelworld.com/st/hostels/p/1456/euro-youth-hostel/?source=ppc_gooads_nonbrand_dsk_dsa_pn_en_de&network=g&campaign_id=20796244219&adgroup_id=161092111372&criteria_id=dsa-443313842330&creative_id=681639389959&location_physical_id=9004425&location_interest_id=1004234&adposition&uniqueclickID=10985874929016821479&sub_keyword&sub_ad&sub_publisher=ADW&gclsrc=aw.ds&gad_source=1&gclid=CjwKCAjwupGyBhBBEiwA0UcqaNxHnDMyizULjdGWhPeq1lyHOYHdjO3qwvMT3xTyW1eZl3I6e4hrURoCK4YQAvD_BwE",
            "time_usec": 1715798746813724,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.hostelworld.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hostels in Munich » Find cheap, unique hostels » Hostelworld",
            "url": "https://www.hostelworld.com/pwa/wds/s?q=Munich,%20Germany&country=Germany&city=Munich&type=city&id=20&from=2024-07-02&to=2024-07-05&guests=1&HostelNumber=1456&MoreOptions=true&page=1",
            "time_usec": 1715798741443314,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.hostelworld.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Euro Youth Hostel, Munich - Online Hostel Bookings, Ratings and Reviews",
            "url": "https://www.hostelworld.com/pwa/wds/hosteldetails.php/Euro-Youth-Hostel/Munich/1456?from=2024-07-02&to=2024-07-05&guests=1&origin=microsite",
            "time_usec": 1715798738048109,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.hostelworld.com/st/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Euro Youth Hostel, Munich - 2024 Prices & Reviews - Hostelworld",
            "url": "https://www.hostelworld.com/st/hostels/p/1456/euro-youth-hostel/?source=ppc_gooads_nonbrand_dsk_dsa_pn_en_de&network=g&campaign_id=20796244219&adgroup_id=161092111372&criteria_id=dsa-443313842330&creative_id=681639389959&location_physical_id=9004425&location_interest_id=1004234&adposition&uniqueclickID=10985874929016821479&sub_keyword&sub_ad&sub_publisher=ADW&gclsrc=aw.ds&gad_source=1&gclid=CjwKCAjwupGyBhBBEiwA0UcqaNxHnDMyizULjdGWhPeq1lyHOYHdjO3qwvMT3xTyW1eZl3I6e4hrURoCK4YQAvD_BwE",
            "time_usec": 1715798723446793,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hostels in munich germany july 2-5 - Google Search",
            "url": "https://www.google.com/search?q=hostels+in+munich+germany+july+2-5&oq=hostels+in+munich+germany+july+2-5&aqs=chrome..69i64j69i57.14869j1j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715798716144645,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.hostelworld.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hostels in Munich » Find cheap, unique hostels » Hostelworld",
            "url": "https://www.hostelworld.com/pwa/wds/s?q=Munich,%20Germany&country=Germany&city=Munich&type=city&id=20&from=2024-07-02&to=2024-07-05&guests=1&page=1",
            "time_usec": 1715798686608578,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.hostelworld.com/st/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hostels In Munich from \u20ac12 - Top Rated Hostels 2024",
            "url": "https://www.hostelworld.com/st/hostels/europe/germany/munich/?source=ppc_gooads_nonbrand_dsk_search_ds_en_us&network=g&campaign_id=11166822366&adgroup_id=107797553165&criteria_id=kwd-11676294525&creative_id=595243611266&location_physical_id=9004425&location_interest_id&adposition&uniqueclickID=5784665646652809026&sub_keyword=munich%20germany%20hostel&sub_ad=e&sub_publisher=ADW&gclsrc=aw.ds&gad_source=1&gclid=CjwKCAjwupGyBhBBEiwA0UcqaM7fUr650MA-RYGlnjOSD9puCy_CA8UyJsz8Q5L2X6vgFTHYDrH7qxoCaOUQAvD_BwE",
            "time_usec": 1715798527249024,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hostels in munich centre - Google Search",
            "url": "https://www.google.com/search?q=hostels+in+munich+centre&oq=hostels+in+munich+centre+&aqs=chrome..69i64j0i22i30j0i15i22i30j0i22i30j0i15i22i30j0i390i512i650l5.12601j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715798520431354,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715798505590551,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "neighborhoods of munich - Google Search",
            "url": "https://www.google.com/search?sca_esv=1cbe4b6585e2caa3&sxsrf=ADLYWIIoQ-Kr9kk92DTubkvR0FKavhb2GA:1715798404624&q=neighborhoods+of+munich&uds=ADvngMgiPmsFSnX7QtZmBAeJzn8vrK20meap3aD-Yj8C4-7e5FT_oB2FLDukkjAtP0CY3ufYH81TxkjUlHHBLvz3frgPnKjo1nEj6urg4McvObzp2XWPR4ST1voQ9O5R_x28kl3yNPJM02WB01UO2cLWP_FqK5b5IERJgiLAVpkatahvJeqDHtSneYqgIGEaOHx3WMWTkRojDIRELgUeaHJWP2ZKyEwoRhwCt37oqJFDrppv3HGCyiU0HEKZvHAPvck9kXP7dvpcDNZWaYV8LKJgwibpaMSOEHZQKMbUB-T-ZvEIKckEf34SDk0WBqQ3PZQkKCw5TJ4fkSgwCJpRiumLE3sN9BlP9w&udm=2&prmd=imvnbtz&sa=X&ved=2ahUKEwi1oaeTp5CGAxU1FlkFHRGlDF0QtKgLegQIDhAB&biw=1179&bih=701&dpr=1#vhid=RG8RDERjwUHRQM&vssid=mosaic",
            "time_usec": 1715798495309419,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hotel Stachus - Google Maps",
            "url": "https://www.google.com/maps/place/Hotel+Stachus/@48.1433161,11.51467,12.23z/data=!4m9!3m8!1s0x479e75f76f1fc155:0x83ae38306881a206!5m2!4m1!1i2!8m2!3d48.1391754!4d11.5633128!16s%2Fg%2F11hv448yv?entry=ttu",
            "time_usec": 1715798480052031,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hotel Stachus - Google Maps",
            "url": "https://www.google.com/maps/place/Hotel+Stachus/@48.136068,11.5160845,10z/data=!4m9!3m8!1s0x479e75f76f1fc155:0x83ae38306881a206!5m2!4m1!1i2!8m2!3d48.1391754!4d11.5633128!16s%2Fg%2F11hv448yv?entry=ttu",
            "time_usec": 1715798474888490,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hotel Stachus - Google Maps",
            "url": "https://www.google.com/maps/place/Hotel+Stachus/@48.1391754,11.5633128,15z/data=!4m2!3m1!1s0x0:0x83ae38306881a206?sa=X&ved=1t:2428&ictx=111",
            "time_usec": 1715798469420750,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "neighborhoods of munich - Google Search",
            "url": "https://www.google.com/search?sca_esv=1cbe4b6585e2caa3&sxsrf=ADLYWIIoQ-Kr9kk92DTubkvR0FKavhb2GA:1715798404624&q=neighborhoods+of+munich&uds=ADvngMgiPmsFSnX7QtZmBAeJzn8vrK20meap3aD-Yj8C4-7e5FT_oB2FLDukkjAtP0CY3ufYH81TxkjUlHHBLvz3frgPnKjo1nEj6urg4McvObzp2XWPR4ST1voQ9O5R_x28kl3yNPJM02WB01UO2cLWP_FqK5b5IERJgiLAVpkatahvJeqDHtSneYqgIGEaOHx3WMWTkRojDIRELgUeaHJWP2ZKyEwoRhwCt37oqJFDrppv3HGCyiU0HEKZvHAPvck9kXP7dvpcDNZWaYV8LKJgwibpaMSOEHZQKMbUB-T-ZvEIKckEf34SDk0WBqQ3PZQkKCw5TJ4fkSgwCJpRiumLE3sN9BlP9w&udm=2&prmd=imvnbtz&sa=X&ved=2ahUKEwi1oaeTp5CGAxU1FlkFHRGlDF0QtKgLegQIDhAB&biw=1179&bih=701&dpr=1#vhid=-zR7ANG1BQ5VjM&vssid=mosaic",
            "time_usec": 1715798464782239,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "neighborhoods of munich - Google Search",
            "url": "https://www.google.com/search?sca_esv=1cbe4b6585e2caa3&sxsrf=ADLYWIIoQ-Kr9kk92DTubkvR0FKavhb2GA:1715798404624&q=neighborhoods+of+munich&uds=ADvngMgiPmsFSnX7QtZmBAeJzn8vrK20meap3aD-Yj8C4-7e5FT_oB2FLDukkjAtP0CY3ufYH81TxkjUlHHBLvz3frgPnKjo1nEj6urg4McvObzp2XWPR4ST1voQ9O5R_x28kl3yNPJM02WB01UO2cLWP_FqK5b5IERJgiLAVpkatahvJeqDHtSneYqgIGEaOHx3WMWTkRojDIRELgUeaHJWP2ZKyEwoRhwCt37oqJFDrppv3HGCyiU0HEKZvHAPvck9kXP7dvpcDNZWaYV8LKJgwibpaMSOEHZQKMbUB-T-ZvEIKckEf34SDk0WBqQ3PZQkKCw5TJ4fkSgwCJpRiumLE3sN9BlP9w&udm=2&prmd=imvnbtz&sa=X&ved=2ahUKEwi1oaeTp5CGAxU1FlkFHRGlDF0QtKgLegQIDhAB&biw=1179&bih=701&dpr=1",
            "time_usec": 1715798461583781,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "neighbor hoods of munich - Google Search",
            "url": "https://www.google.com/search?q=neighbor+hoods+of+munich&oq=neighbor+hoods+of+munich&aqs=chrome..69i64j0i13i512j0i22i30j0i390i512i650j0i390i395i512i650l2j0i395i512i546j69i57.14945j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715798427715096,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Munich - Google Maps",
            "url": "https://www.google.com/maps/place/Munich,+Germany/@48.2068372,11.4077003,9.8z/data=!4m6!3m5!1s0x479e75f9a38c5fd9:0x10cb84a7db1987d!8m2!3d48.1351253!4d11.5819805!16s%2Fm%2F02h6_6p?entry=ttu",
            "time_usec": 1715798427477106,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Munich - Google Maps",
            "url": "https://www.google.com/maps/place/Munich,+Germany/@48.2068372,11.4077003,9.8z/data=!4m6!3m5!1s0x479e75f9a38c5fd9:0x10cb84a7db1987d!8m2!3d48.1351253!4d11.5819805!16s%2Fm%2F02h6_6p?entry=ttu",
            "time_usec": 1715798423688721,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Munich - Google Maps",
            "url": "https://www.google.com/maps/place/Munich,+Germany/data=!4m2!3m1!1s0x479e75f9a38c5fd9:0x10cb84a7db1987d?sa=X&ved=1t:242&ictx=111",
            "time_usec": 1715798413587603,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "neighbor hoods of munich - Google Search",
            "url": "https://www.google.com/search?q=neighbor+hoods+of+munich&oq=neighbor+hoods+of+munich&aqs=chrome..69i64j0i13i512j0i22i30j0i390i512i650j0i390i395i512i650l2j0i395i512i546j69i57.14945j1j1&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715798406002637,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715798388936868,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hotel stachus munich - Google Search",
            "url": "https://www.google.com/search?q=hotel+stachus+munich&oq=hotel+stachus+munich&aqs=chrome..69i64j46i175i199i512i664i665j0i22i30l2j0i390i395i512i650l2j0i395i512i546j69i57.9759j1j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715798378644820,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hotel Stachus - Google Maps",
            "url": "https://www.google.com/maps/place/Hotel+Stachus/@48.1485449,11.5496997,14.06z/data=!4m9!3m8!1s0x479e75f76f1fc155:0x83ae38306881a206!5m2!4m1!1i2!8m2!3d48.1391754!4d11.5633128!16s%2Fg%2F11hv448yv?entry=ttu",
            "time_usec": 1715798377742958,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hotel Stachus - Google Maps",
            "url": "https://www.google.com/maps/place/Hotel+Stachus/@48.1485449,11.5496997,14.06z/data=!4m9!3m8!1s0x479e75f76f1fc155:0x83ae38306881a206!5m2!4m1!1i2!8m2!3d48.1391754!4d11.5633128!16s%2Fg%2F11hv448yv?entry=ttu",
            "time_usec": 1715798372086815,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hotel Stachus - Google Maps",
            "url": "https://www.google.com/maps/place/Hotel+Stachus/@48.1449729,11.5551431,14.72z/data=!4m9!3m8!1s0x479e75f76f1fc155:0x83ae38306881a206!5m2!4m1!1i2!8m2!3d48.1391754!4d11.5633128!16s%2Fg%2F11hv448yv?entry=ttu",
            "time_usec": 1715798365508885,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hotel Stachus - Google Maps",
            "url": "https://www.google.com/maps/place/Hotel+Stachus/@48.1459509,11.5565589,14.97z/data=!4m9!3m8!1s0x479e75f76f1fc155:0x83ae38306881a206!5m2!4m1!1i2!8m2!3d48.1391754!4d11.5633128!16s%2Fg%2F11hv448yv?entry=ttu",
            "time_usec": 1715798354014341,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product/ico/maps15_bnuw3a_32dp.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Hotel Stachus - Google Maps",
            "url": "https://www.google.com/maps/place/Hotel+Stachus/@48.1496238,11.5484587,14z/data=!4m9!3m8!1s0x479e75f76f1fc155:0x83ae38306881a206!5m2!4m1!1i2!8m2!3d48.1391754!4d11.5633128!16s%2Fg%2F11hv448yv?entry=ttu",
            "time_usec": 1715798350208287,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google Maps",
            "url": "https://www.google.com/maps?sca_esv=1cbe4b6585e2caa3&output=search&q=hotel+stachus+munich&source=lnms&entry=mc&ved=1t:200715&ictx=111",
            "time_usec": 1715798341655201,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "hotel stachus munich - Google Search",
            "url": "https://www.google.com/search?q=hotel+stachus+munich&oq=hotel+stachus+munich&aqs=chrome..69i64j46i175i199i512i664i665j0i22i30l2j0i390i395i512i650l2j0i395i512i546j69i57.9759j1j4&sourceid=chrome&ie=UTF-8",
            "time_usec": 1715798333851409,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://search.funsafetabsearch.com/?pub_id=3000&srcid=A341B_set_bcr&q=hotel+stachus+munich",
            "time_usec": 1715798319064836,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/spreadsheets/spreadsheets_2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "travel - Google Sheets",
            "url": "https://docs.google.com/spreadsheets/d/1-B8pi1LrUiUDTB0-TFqNW11fdSmS2mB4Jf9NlseaJJs/edit#gid=0",
            "time_usec": 1715798174189175,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715798169061214,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/doclist/images/drive_2022q3_32dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Home - Google Drive",
            "url": "https://drive.google.com/drive/home",
            "time_usec": 1715798153730947,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google",
            "url": "https://www.google.com/",
            "time_usec": 1715798148291974,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google",
            "url": "https://www.google.com/",
            "time_usec": 1715798147220447,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "New Tab",
            "url": "chrome://newtab/",
            "time_usec": 1715798143919681,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon",
            "url": "https://www.amazon.com/ap/cvf/transactionapproval?arb=f7856ff5-cfcf-4f73-b25f-130ea4219053&openid.assoc_handle=usflex&pageId=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fap%2Fsignin%3Fie%3DUTF8%26clientContext%3D131-0257903-6832646%26arb%3De60b00fd-e4d8-4928-b0a8-35e8b29f7cf0%26openid.pape.max_auth_age%3D0%26use_global_authentication%3DFalse%26openid.return_to%3Dhttps%253A%252F%252Fwww.amazon.com%252Fgp%252Fvideo%252Fdetail%252Famzn1.dv.gti.2d9250c0-ea4b-4239-a69f-a0a832e0dae9%253Fautoplay%253D0%2526ref_%253Dnav_custrec_signin%26openid.identity%3Dhttps%253A%252F%252Fwww.amazon.com%252Fap%252Fid%252Famzn1.account.AFMOPQ5YDSGKERMQ7PVMTPD3P27A%26openid.assoc_handle%3Dusflex%26openid.mode%3Dcheckid_setup%26openid.claimed_id%3Dhttps%253A%252F%252Fwww.amazon.com%252Fap%252Fid%252Famzn1.account.AFMOPQ5YDSGKERMQ7PVMTPD3P27A%26ignoreAuthState%3D1%26pageId%3Dusflex%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0",
            "time_usec": 1715798056937599,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon Sign-In",
            "url": "https://www.amazon.com/ap/signin",
            "time_usec": 1715798050551096,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon Sign-In",
            "url": "https://www.amazon.com/ap/signin",
            "time_usec": 1715798024405432,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon Sign-In",
            "url": "https://www.amazon.com/ap/signin?ie=UTF8&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fvideo%2Fdetail%2Famzn1.dv.gti.2d9250c0-ea4b-4239-a69f-a0a832e0dae9%3Fautoplay%3D0%26ref_%3Dnav_custrec_signin&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&switch_account=auth_prompt&ignoreAuthState=1&openid.identity=https%3A%2F%2Fwww.amazon.com%2Fap%2Fid%2Famzn1.account.AFMOPQ5YDSGKERMQ7PVMTPD3P27A&openid.claimed_id=https%3A%2F%2Fwww.amazon.com%2Fap%2Fid%2Famzn1.account.AFMOPQ5YDSGKERMQ7PVMTPD3P27A",
            "time_usec": 1715798020116608,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Amazon Sign-In",
            "url": "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fvideo%2Fdetail%2Famzn1.dv.gti.2d9250c0-ea4b-4239-a69f-a0a832e0dae9%3Fautoplay%3D0%26ref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0",
            "time_usec": 1715798017848358,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.amazon.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Watch House of Gucci | Prime Video",
            "url": "https://www.amazon.com/gp/video/detail/amzn1.dv.gti.2d9250c0-ea4b-4239-a69f-a0a832e0dae9?autoplay=0&ref_=atv_cf_strg_wb",
            "time_usec": 1715798012710229,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "house of gucci - Google Search",
            "url": "https://www.google.com/search?q=house+of+gucci&sca_esv=1cbe4b6585e2caa3&ei=EvhEZqWYIKie5NoPksitYA&ved=0ahUKEwil6aKSnpCGAxUoD1kFHRJkCwwQ4dUDCBA&uact=5&oq=house+of+gucci&gs_lp=Egxnd3Mtd2l6LXNlcnAiDmhvdXNlIG9mIGd1Y2NpMggQLhiABBixAzIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIjEC4YgAQYsQMYlwUY3AQY3gQY4AQY9AMY8QMY9QMY9gPYAQNIlyNQhgJYzCFwB3gBkAEAmAHyAaABqw-qAQU5LjguMbgBA8gBAPgBAZgCGaAC2hKoAhTCAh0QABiABBi0AhjUAxjlAhi3AxiKBRjqAhiKA9gBAcICFhAAGAMYtAIY5QIY6gIYjAMYjwHYAQLCAhYQLhgDGLQCGOUCGOoCGIwDGI8B2AECwgILEAAYgAQYkQIYigXCAhEQLhiABBixAxjRAxiDARjHAcICDhAuGIAEGLEDGIMBGIoFwgIKEAAYgAQYQxiKBcICDhAAGIAEGLEDGIMBGIoFwgILEAAYgAQYsQMYgwHCAgQQIxgnwgIREC4YgAQYsQMYxwEYjgUYrwHCAg4QLhiABBjHARiOBRivAcICDhAuGIAEGLEDGNEDGMcBwgINEC4YgAQY0QMYxwEYCsICBBAAGAPCAiAQLhiABBixAxjHARiOBRivARiXBRjcBBjeBBjgBNgBA8ICFhAuGIAEGLEDGNEDGEMYgwEYxwEYigXCAhAQABiABBixAxhDGMkDGIoFwgILEAAYgAQYkgMYigXCAgsQLhiABBixAxiDAcICChAuGIAEGEMYigXCAhAQABiABBixAxhDGIMBGIoFwgINEAAYgAQYsQMYQxiKBcICDRAuGIAEGLEDGEMYigXCAhAQLhiABBixAxhDGIMBGIoFwgITEAAYgAQYsQMYQxiDARjJAxiKBcICBRAuGIAEwgIdEC4YgAQYxwEYjgUYrwEYlwUY3AQY3gQY4ATYAQPCAggQABiABBixA8ICFBAuGIAEGLEDGIMBGMcBGI4FGK8BwgILEC4YgAQYxwEYrwHCAgsQLhiABBixAxjUAsICIxAuGIAEGLEDGJcFGNwEGN4EGOAEGPQDGPEDGPUDGPYD2AEDmANWugYECAEYB7oGBggCEAEYCroGBggDEAEYFJIHBzExLjEzLjGgB-fCAg&sclient=gws-wiz-serp",
            "time_usec": 1715798002479797,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "is there a way to delete all of your files on a mac in finder - Google Search",
            "url": "https://www.google.com/search?q=is+there+a+way+to+delete+all+of+your+files+on+a+mac+in+finder&sca_esv=1cbe4b6585e2caa3&source=hp&ei=_fdEZsLNFavm1e8P7563KA&iflsig=AL9hbdgAAAAAZkUGDTSYPlbicFYoq2gXwoftNZtOx2sv&ved=0ahUKEwiCwJaInpCGAxUrc_UHHW_PDQUQ4dUDCA8&uact=5&oq=is+there+a+way+to+delete+all+of+your+files+on+a+mac+in+finder&gs_lp=Egdnd3Mtd2l6Ij1pcyB0aGVyZSBhIHdheSB0byBkZWxldGUgYWxsIG9mIHlvdXIgZmlsZXMgb24gYSBtYWMgaW4gZmluZGVyMgQQIRgVSPV9UNEDWLJ9cA54AJABApgB_QGgAYYnqgEGNjIuNC40uAEDyAEA-AEBmAJSoALeKKgCCsICEBAAGAMY5QIY6gIYjAMYjwHCAhAQLhgDGOUCGOoCGIwDGI8BwgIREC4YgAQYsQMY0QMYgwEYxwHCAgsQABiABBixAxiDAcICCxAuGIAEGLEDGIMBwgIFEAAYgATCAggQLhiABBjUAsICDhAuGIAEGLEDGNEDGMcBwgIIEC4YgAQYsQPCAggQABiABBixA8ICDhAuGIAEGLEDGIMBGIoFwgIOEAAYgAQYsQMYgwEYigXCAgUQLhiABMICBxAAGIAEGArCAgcQLhiABBgKwgILEAAYgAQYsQMYigXCAgsQABiABBiGAxiKBcICCBAAGIAEGKIEwgIFECEYoAHCAgUQIRifBZgDE5IHBjc0LjYuMqAHxdUD&sclient=gws-wiz",
            "time_usec": 1715795987538255,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "is there a way to delete all of your files on a mac in finder - Google Search",
            "url": "https://www.google.com/search?q=is+there+a+way+to+delete+all+of+your+files+on+a+mac+in+finder&sca_esv=1cbe4b6585e2caa3&source=hp&ei=_fdEZsLNFavm1e8P7563KA&iflsig=AL9hbdgAAAAAZkUGDTSYPlbicFYoq2gXwoftNZtOx2sv&ved=0ahUKEwiCwJaInpCGAxUrc_UHHW_PDQUQ4dUDCA8&uact=5&oq=is+there+a+way+to+delete+all+of+your+files+on+a+mac+in+finder&gs_lp=Egdnd3Mtd2l6Ij1pcyB0aGVyZSBhIHdheSB0byBkZWxldGUgYWxsIG9mIHlvdXIgZmlsZXMgb24gYSBtYWMgaW4gZmluZGVyMgQQIRgVSPV9UNEDWLJ9cA54AJABApgB_QGgAYYnqgEGNjIuNC40uAEDyAEA-AEBmAJSoALeKKgCCsICEBAAGAMY5QIY6gIYjAMYjwHCAhAQLhgDGOUCGOoCGIwDGI8BwgIREC4YgAQYsQMY0QMYgwEYxwHCAgsQABiABBixAxiDAcICCxAuGIAEGLEDGIMBwgIFEAAYgATCAggQLhiABBjUAsICDhAuGIAEGLEDGNEDGMcBwgIIEC4YgAQYsQPCAggQABiABBixA8ICDhAuGIAEGLEDGIMBGIoFwgIOEAAYgAQYsQMYgwEYigXCAgUQLhiABMICBxAAGIAEGArCAgcQLhiABBgKwgILEAAYgAQYsQMYigXCAgsQABiABBiGAxiKBcICCBAAGIAEGKIEwgIFECEYoAHCAgUQIRifBZgDE5IHBjc0LjYuMqAHxdUD&sclient=gws-wiz",
            "time_usec": 1715795986643750,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://www.google.com/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google",
            "url": "https://www.google.com/",
            "time_usec": 1715795966092953,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Google",
            "url": "https://www.google.com/",
            "time_usec": 1715795965659565,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Privacy error",
            "url": "https://survey3.medallia.com/?PANYNJsurvey&airport=jfk_feedback",
            "time_usec": 1715795957285519,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Redirecting to destination... - Cloud 9 Wireless",
            "url": "http://edge.boingomedia.com/wifi_dest.html?dest_url=https%3a%2f%2fwifi.boingohotspot.net%2fjfk.t7%2fwelcome%3fnas_identifier%3dccg_jfk-via1%26ip%3d100.121.214.168%26mac%3dc8%253a69%253acd%253ab7%253a3d%253a2e%26username%3dboingo%252fbwpromo!3%257cC869CDB73D2E%257c1%257c240%257c0%257c0%257cPromo%257c1%257c10c129610d724433a3271375ba352e43%257cjfk%257ct7%257cm1_a7967efd83dcd2f5bd3f6ae9045ed7d4%257c0%257c30%257c110M%257c110M%257c%257c0%257c1715795949%26GSID%3d897b9c0a-221d-4ddf-a41c-4fa6af8097ce%26vlan_id%3d21%26ap_mac%3d70%253ab3%253a17%253aa3%253a57%253aa0%26is_back_from_url_concat%3d1%26is_redirect_back_from_c9%3d1",
            "time_usec": 1715795956134952,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://wifi.boingohotspot.net/assets/shared/img/favicon.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Boingo Hotspot",
            "url": "https://wifi.boingohotspot.net/ClickCapture.aspx?campaignType=1&hash=930a2fd6f675c4db16e9dba66d33159d5ddd27f224ac2979a7cdc31cb160eb65&adgroup_uuid=10c129610d724433a3271375ba352e43&campaignID=panynj-survey-jfk__panynj-survey-jfk-med&retake=0&timestamp=1715795948&mst=0&timeout=240&linkID=BoingoRadius&external_id=m1_a7967efd83dcd2f5bd3f6ae9045ed7d4",
            "time_usec": 1715795949111232,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "PANYNJ Survey",
            "url": "http://nimbus.boingomedia.com/wifi/promos/f965e400fea242759aa9f5141a63bd57/?__v=Y3A9U0tQJTNEMCUyNm1ib3hTZXNzaW9uJTNEamkxa241azA1bHhwaWt1dGdjZGFhMnd1JTI2U1RPJTNEMjQwJTI2U0NDJTNEQ0NHSkZLJTI2R1NJRCUzRDg5N2I5YzBhLTIyMWQtNGRkZi1hNDFjLTRmYTZhZjgwOTdjZSUyNkFESUQlM0QlMjZhcG1hYyUzRDcwJTI1M0FCMyUyNTNBMTclMjUzQUEzJTI1M0E1NyUyNTNBQTAlMjZTUlQlM0QwJTI2aG90c3BvdElEJTNEdDcmX19zdl9pZD10NyZfX2NpZD0xMGMxMjk2MTBkNzI0NDMzYTMyNzEzNzViYTM1MmU0MyZfX3B2ZHJjbmY9NDUmX19maWQ9Zjk2NWU0MDBmZWEyNDI3NTlhYTlmNTE0MWE2M2JkNTcmX192ZW51ZV9pZD1ib2luZ29famZr&is_single_click=False&uid=m1_a7967efd83dcd2f5bd3f6ae9045ed7d4&login_url=https%3A%2F%2Fwifi.boingohotspot.net%2Fjfk.t7%2F%3Fdst%3Dhttp%253A%252F%252Fsearch.sympatheticface.com%252Fh%253F_pg%253DD3E7679C-DC93-5AEA-BB5D-A9DAFACDA84E%26link_login_only%3Dhttps%253A%252F%252Fvia.boingohotspot.net%252Flogin%26link_login%3Dhttps%253A%252F%252Fvia.boingohotspot.net%252Flogin%253Fdst%253Dhttp%253A%252F%252Fsearch.sympatheticface.com%252Fh%253F_pg%253DD3E7679C-DC93-5AEA-BB5D-A9DAFACDA84E%26link_logout%3Dhttps%253A%252F%252Fvia.boingohotspot.net%252Flogout%26link_status%3Dhttps%253A%252F%252Fvia.boingohotspot.net%252Fstatus%26nas_identifier%3Dccg_jfk-via1%26hostname%3Dvia.boingohotspot.net%26identity%3Dvia-2.0%26ip%3D100.121.214.168%26mac%3DC8%253A69%253ACD%253AB7%253A3D%253A2E%26GSID%3D897b9c0a-221d-4ddf-a41c-4fa6af8097ce%26vlan_id%3D21%26ap_mac%3D70%253AB3%253A17%253AA3%253A57%253AA0%26is_single_click%3DFalse%26__c9adg%3D10c129610d724433a3271375ba352e43%26mboxDefault%3D1%26__c9auth%3D1",
            "time_usec": 1715795944581750,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "https://wifi.boingohotspot.net/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Boingo | Offers",
            "url": "https://wifi.boingohotspot.net/jfk.t7/?dst=http%3A%2F%2Fsearch.sympatheticface.com%2Fh%3F_pg%3DD3E7679C-DC93-5AEA-BB5D-A9DAFACDA84E&link_login_only=https%3A%2F%2Fvia.boingohotspot.net%2Flogin&link_login=https%3A%2F%2Fvia.boingohotspot.net%2Flogin%3Fdst%3Dhttp%3A%2F%2Fsearch.sympatheticface.com%2Fh%3F_pg%3DD3E7679C-DC93-5AEA-BB5D-A9DAFACDA84E&link_logout=https%3A%2F%2Fvia.boingohotspot.net%2Flogout&link_status=https%3A%2F%2Fvia.boingohotspot.net%2Fstatus&nas_identifier=ccg_jfk-via1&hostname=via.boingohotspot.net&identity=via-2.0&ip=100.121.214.168&mac=C8%3A69%3ACD%3AB7%3A3D%3A2E&GSID=897b9c0a-221d-4ddf-a41c-4fa6af8097ce&vlan_id=21&ap_mac=70%3AB3%3A17%3AA3%3A57%3AA0&__c9auth=1&__c9inter=%2Fwifi%2Fpromos%2Ff965e400fea242759aa9f5141a63bd57%2F%3F__v%3DY3A9U0tQJTNEMCUyNm1ib3hTZXNzaW9uJTNEamkxa241azA1bHhwaWt1dGdjZGFhMnd1JTI2U1RPJTNEMjQwJTI2U0NDJTNEQ0NHSkZLJTI2R1NJRCUzRDg5N2I5YzBhLTIyMWQtNGRkZi1hNDFjLTRmYTZhZjgwOTdjZSUyNkFESUQlM0QlMjZhcG1hYyUzRDcwJTI1M0FCMyUyNTNBMTclMjUzQUEzJTI1M0E1NyUyNTNBQTAlMjZTUlQlM0QwJTI2aG90c3BvdElEJTNEdDcmX19zdl9pZD10NyZfX2NpZD0xMGMxMjk2MTBkNzI0NDMzYTMyNzEzNzViYTM1MmU0MyZfX3B2ZHJjbmY9NDUmX19maWQ9Zjk2NWU0MDBmZWEyNDI3NTlhYTlmNTE0MWE2M2JkNTcmX192ZW51ZV9pZD1ib2luZ29famZr%26is_single_click%3DFalse%26uid%3Dm1_a7967efd83dcd2f5bd3f6ae9045ed7d4&is_single_click=False&__c9adg=10c129610d724433a3271375ba352e43&mboxDefault=1&__c9p=f965e400fea242759aa9f5141a63bd57",
            "time_usec": 1715795938587981,
            "client_id": "lYr7xxlf27baT6VALzqSDA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/confirmation",
            "url": "https://www.condor.com/oci/en-EU/confirmation",
            "time_usec": 1715727097695149,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/passenger-review",
            "url": "https://www.condor.com/oci/en-EU/passenger-review",
            "time_usec": 1715727094900123,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/regulatoryRequirements",
            "url": "https://www.condor.com/oci/en-EU/regulatoryRequirements",
            "time_usec": 1715727090972012,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/dangerous-goods",
            "url": "https://www.condor.com/oci/en-EU/dangerous-goods",
            "time_usec": 1715727087074938,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/passenger-details",
            "url": "https://www.condor.com/oci/en-EU/passenger-details",
            "time_usec": 1715726979929049,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Condor Online Check-in",
            "url": "https://www.condor.com/oci/en-EU/passenger-details",
            "time_usec": 1715726953351130,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/nationality",
            "url": "https://www.condor.com/oci/en-EU/nationality",
            "time_usec": 1715726914516041,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment",
            "url": "https://www.condor.com/oci/en-EU/payment",
            "time_usec": 1715726891778627,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=9",
            "url": "https://www.condor.com/oci/en-EU/payment?i=9",
            "time_usec": 1715726891762316,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=8",
            "url": "https://www.condor.com/oci/en-EU/payment?i=8",
            "time_usec": 1715726891748663,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=7",
            "url": "https://www.condor.com/oci/en-EU/payment?i=7",
            "time_usec": 1715726891735156,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=6",
            "url": "https://www.condor.com/oci/en-EU/payment?i=6",
            "time_usec": 1715726891723968,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=5",
            "url": "https://www.condor.com/oci/en-EU/payment?i=5",
            "time_usec": 1715726891711574,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=4",
            "url": "https://www.condor.com/oci/en-EU/payment?i=4",
            "time_usec": 1715726891698385,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=3",
            "url": "https://www.condor.com/oci/en-EU/payment?i=3",
            "time_usec": 1715726891684341,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=2",
            "url": "https://www.condor.com/oci/en-EU/payment?i=2",
            "time_usec": 1715726891668272,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=1",
            "url": "https://www.condor.com/oci/en-EU/payment?i=1",
            "time_usec": 1715726891651911,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=0",
            "url": "https://www.condor.com/oci/en-EU/payment?i=0",
            "time_usec": 1715726891635812,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment",
            "url": "https://www.condor.com/oci/en-EU/payment",
            "time_usec": 1715726878693763,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=9",
            "url": "https://www.condor.com/oci/en-EU/payment?i=9",
            "time_usec": 1715726878670553,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=8",
            "url": "https://www.condor.com/oci/en-EU/payment?i=8",
            "time_usec": 1715726878655242,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=7",
            "url": "https://www.condor.com/oci/en-EU/payment?i=7",
            "time_usec": 1715726878639891,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=6",
            "url": "https://www.condor.com/oci/en-EU/payment?i=6",
            "time_usec": 1715726878622726,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=5",
            "url": "https://www.condor.com/oci/en-EU/payment?i=5",
            "time_usec": 1715726878607286,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=4",
            "url": "https://www.condor.com/oci/en-EU/payment?i=4",
            "time_usec": 1715726878588069,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=3",
            "url": "https://www.condor.com/oci/en-EU/payment?i=3",
            "time_usec": 1715726878573922,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=2",
            "url": "https://www.condor.com/oci/en-EU/payment?i=2",
            "time_usec": 1715726878559900,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=1",
            "url": "https://www.condor.com/oci/en-EU/payment?i=1",
            "time_usec": 1715726878544364,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment?i=0",
            "url": "https://www.condor.com/oci/en-EU/payment?i=0",
            "time_usec": 1715726878483564,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/payment",
            "url": "https://www.condor.com/oci/en-EU/payment",
            "time_usec": 1715726761662149,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/pre-payment",
            "url": "https://www.condor.com/oci/en-EU/pre-payment",
            "time_usec": 1715726761581534,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/pre-payment",
            "url": "https://www.condor.com/oci/en-EU/pre-payment",
            "time_usec": 1715726761513390,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/storage",
            "url": "https://www.condor.com/oci/en-EU/storage",
            "time_usec": 1715726749156958,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/seats",
            "url": "https://www.condor.com/oci/en-EU/seats",
            "time_usec": 1715726731100342,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/overview",
            "url": "https://www.condor.com/oci/en-EU/overview",
            "time_usec": 1715726727423900,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/select",
            "url": "https://www.condor.com/oci/en-EU/select",
            "time_usec": 1715726720627321,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/search",
            "url": "https://www.condor.com/oci/en-EU/search",
            "time_usec": 1715726718792219,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/pre-payment",
            "url": "https://www.condor.com/oci/en-EU/pre-payment",
            "time_usec": 1715726713455180,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/storage",
            "url": "https://www.condor.com/oci/en-EU/storage",
            "time_usec": 1715726693986414,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/seats",
            "url": "https://www.condor.com/oci/en-EU/seats",
            "time_usec": 1715726622891423,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/overview",
            "url": "https://www.condor.com/oci/en-EU/overview",
            "time_usec": 1715726616150590,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.condor.com/oci/en-EU/select",
            "url": "https://www.condor.com/oci/en-EU/select",
            "time_usec": 1715726579713583,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/oci/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Condor Online Check-in",
            "url": "https://www.condor.com/oci/eu/search?surename=STEELE&bookingnumber=N65DPF&agencynumber=50065",
            "time_usec": 1715726576609788,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Condor \u2013 My booking \u2013 Manage my booking",
            "url": "https://www.condor.com/tcibe/eu/mybooking/dashboard",
            "time_usec": 1715726545752491,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/eu/fileadmin/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Condor \u2013 My booking \u2013 Manage my booking",
            "url": "https://www.condor.com/tcibe/eu/mybooking/paxContactInformation",
            "time_usec": 1715726513271991,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://static.cimcontent.net/common-web-assets/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "XFINITY | My Account | EcoBill® Online Bill Pay",
            "url": "https://customer.xfinity.com/#/billing/brite",
            "time_usec": 1715726393904865,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.condor.com/eu/fileadmin/favicon.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Manage my booking",
            "url": "https://www.condor.com/tcibe/eu/mybooking/login?utm_source=condor_colibri&utm_medium=email_system&utm_campaign=oci_pico",
            "time_usec": 1715726384258294,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://static.cimcontent.net/common-web-assets/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "XFINITY | My Account | EcoBill® Online Bill Pay",
            "url": "https://customer.xfinity.com/#/billing/brite",
            "time_usec": 1715726383260820,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://login.xfinity.com/static/images/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "XFINITY | My Account | EcoBill® Online Bill Pay",
            "url": "https://customer.xfinity.com/#/billing/brite",
            "time_usec": 1715279715246889,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://login.xfinity.com/static/images/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign in to Xfinity",
            "url": "https://login.xfinity.com/login",
            "time_usec": 1715279704433231,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://login.xfinity.com/static/images/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign in to Xfinity",
            "url": "https://login.xfinity.com/login?r=comcast.net&s=oauth&continue=https%3A%2F%2Foauth.xfinity.com%2F%2Foauth%2Fauthorize%3Fclient_id%3Dmy-account-web%26prompt%3Dlogin%26redirect_uri%3Dhttps%253A%252F%252Fcustomer.xfinity.com%252Foauth%252Fcallback%26response_type%3Dcode%26state%3Dhttps%253A%252F%252Fcustomer.xfinity.com%252F%2523%252Fbilling%252Fbrite%26response%3D1%26reqId%3Df3c7e844-59d3-49a2-84bc-ba25774378fc&forceAuthn=1&client_id=my-account-web&reqId=0bab6959-8f0b-490a-83f5-4df411e57826&rm=2&ui_style=light&cima_tsig_token=cima_cid%3DLBmTgmiHvrZp9QwR%252FrQVwmHnk%252FA%253D%26cima_dsig%3D%252BW3Tg5i5pzW9l%252B90dL1Q14hbzW4%253D%26cima_nonce%3D5f3e0ffa-a353-4d73-a0d1-c8efaa5af256%26cima_ts%3D1715279689%26cima_uid%3Dajj4xe%2540comcast.net",
            "time_usec": 1715279690708606,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://idm.xfinity.com/myaccount/images/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Security Check",
            "url": "https://idm.xfinity.com/myaccount/reset?execution=e1s7",
            "time_usec": 1715279683735023,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://idm.xfinity.com/myaccount/images/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Comcast ID Account Management",
            "url": "https://idm.xfinity.com/myaccount/reset?execution=e1s6",
            "time_usec": 1715279682181113,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://idm.xfinity.com/myaccount/images/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Reset Your Password",
            "url": "https://idm.xfinity.com/myaccount/reset?execution=e1s5",
            "time_usec": 1715279669094684,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://idm.xfinity.com/myaccount/images/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Comcast ID Account Management",
            "url": "https://idm.xfinity.com/myaccount/reset?execution=e1s4",
            "time_usec": 1715279667800986,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://idm.xfinity.com/myaccount/images/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Reset Your Password",
            "url": "https://idm.xfinity.com/myaccount/reset?execution=e1s3",
            "time_usec": 1715279655703628,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://idm.xfinity.com/myaccount/images/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Reset Your Password",
            "url": "https://idm.xfinity.com/myaccount/reset?execution=e1s2",
            "time_usec": 1715279631844109,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://idm.xfinity.com/myaccount/images/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Reset Your Password",
            "url": "https://idm.xfinity.com/myaccount/reset?execution=e1s1",
            "time_usec": 1715279628930801,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://login.xfinity.com/static/images/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign in to Xfinity",
            "url": "https://login.xfinity.com/login",
            "time_usec": 1715279621718669,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://login.xfinity.com/static/images/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign in to Xfinity",
            "url": "https://login.xfinity.com/login",
            "time_usec": 1715279609431499,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://static.cimcontent.net/common-web-assets/favicon/apple-icon-180x180.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "XFINITY | My Account | EcoBill® Online Bill Pay",
            "url": "https://customer.xfinity.com/#/billing/brite",
            "time_usec": 1715279590495871,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/spreadsheets/spreadsheets_2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "CS3140 Office Hours on Final Week - Google Drive",
            "url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ36etqbk15oe6xF9KQzQvI6wpXWwY2nunkpLEKTeXfL3EWNH4KQ1gFl7euBeEx43yXh_nfY-VPuOeW/pubhtml?gid=0&single=true",
            "time_usec": 1715279589551542,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/spreadsheets/spreadsheets_2023q4.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "CS3140 Office Hours on Final Week - Google Drive",
            "url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ36etqbk15oe6xF9KQzQvI6wpXWwY2nunkpLEKTeXfL3EWNH4KQ1gFl7euBeEx43yXh_nfY-VPuOeW/pubhtml?gid=0&single=true",
            "time_usec": 1715048616284579,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://ssl.gstatic.com/docs/forms/device_home/ios_152.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Important Message Postal Service",
            "url": "https://docs.google.com/forms/d/e/1FAIpQLScFCFw3zWZrFbE7sAgXttiYO97FpxuNDM9IA0zm2k54fhPiOQ/closedform",
            "time_usec": 1715048615660585,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Important Message Postal Service",
            "url": "https://docs.google.com/forms/d/e/1FAIpQLScFCFw3zWZrFbE7sAgXttiYO97FpxuNDM9IA0zm2k54fhPiOQ/closedform",
            "time_usec": 1714283389097427,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product_ios/3x/gsa_ios_60dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "anna cchoneycomb charlotttesville - Google Search",
            "url": "https://www.google.com/search?q=anna+cchoneycomb+charlotttesville&rlz=1CDGOYI_enUS976US998&oq=anna+cchoneycomb+charlotttesville&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAEyCQgDECEYChigAdIBCDQ4MTRqMGo3qAIZsAIB4gMEGAEgXw&hl=en-US&sourceid=chrome-mobile&ie=UTF-8",
            "time_usec": 1714283387713287,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "THE HONEYCOMB",
            "url": "https://www.cvillehoneycomb.com/find-us",
            "time_usec": 1713456665220243,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://images.squarespace-cdn.com/content/v1/5ad51646e2ccd18ebb5bcfa6/1524068409858-XJFNU6YKGTSMS0WJNB5Y/favicon.ico?format=100w",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "THE HONEYCOMB",
            "url": "https://www.cvillehoneycomb.com/",
            "time_usec": 1713456646540024,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://www.google.com/images/branding/product_ios/3x/gsa_ios_60dp.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "anna cchoneycomb charlotttesville - Google Search",
            "url": "https://www.google.com/search?q=anna+cchoneycomb+charlotttesville&rlz=1CDGOYI_enUS976US998&oq=anna+cchoneycomb+charlotttesville&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAEyCQgDECEYChigAdIBCDQ4MTRqMGo3qAIZsAIB4gMEGAEgXw&hl=en-US&sourceid=chrome-mobile&ie=UTF-8",
            "time_usec": 1713456589821852,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://cdn.schedulicity.com/images/apple-touch-icon_v3.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.schedulicity.com/scheduling/THEBJL?CID=51297463",
            "url": "https://www.schedulicity.com/scheduling/THEBJL?CID=51297463",
            "time_usec": 1713456103007738,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://cdn.schedulicity.com/images/apple-touch-icon_v3.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Schedulicity Online Scheduling | Book Appointment\u2026",
            "url": "https://www.schedulicity.com/myappointments?CID=51297463",
            "time_usec": 1713456088804237,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://cdn.schedulicity.com/images/apple-touch-icon_v3.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.schedulicity.com/myappointments",
            "url": "https://www.schedulicity.com/myappointments",
            "time_usec": 1713456088150171,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://cdn.schedulicity.com/images/apple-touch-icon_v3.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.schedulicity.com/account/verify",
            "url": "https://www.schedulicity.com/account/verify",
            "time_usec": 1713456056217064,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://cdn.schedulicity.com/images/apple-touch-icon_v3.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "https://www.schedulicity.com/account/identify",
            "url": "https://www.schedulicity.com/account/identify",
            "time_usec": 1713456043076216,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://cdn.schedulicity.com/images/apple-touch-icon_v3.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Schedulicity Online Scheduling | Book Appointment\u2026",
            "url": "https://www.schedulicity.com/myappointments?CID=51297463",
            "time_usec": 1713456038988792,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://aadcdn.msauth.net/shared/1.0/content/images/favicon_a_eupayfgghqiai7k9sol6lg2.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign in to your account",
            "url": "https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&redirect_uri=https%3A%2F%2Fforms.office.com%2Flanding&state=eyJ2ZXJzaW9uIjoxLCJkYXRhIjp7IklkZW50aXR5UHJvdmlkZXIiOiJBV3RlNUNMU1FZT1hBeV91SS0zSHh4aVFCSFFNZldDMjRjVmdTS21wd3NQaE1GZnE0OXdMbEllMUZkWDB4by05TGRRUHJYTWlUM1lHT3VOeG9RRmNodGsiLCIucmVkaXJlY3QiOiJodHRwczovL2Zvcm1zLm9mZmljZS5jb20vUGFnZXMvUmVzcG9uc2VQYWdlLmFzcHg_aWQ9eDRBMGV3YzNjMGlMZC1JV2N6cGxySk04RFZQb2l0aExvZTBVb29BNENjZFVORVJKTXpkVlVUaFVWVGhWU2poTlRERk5Oa0pVUmtGVU55UWxRQ04wUFdjdSZzaWQ9Zjg2ZGJlZTUtMTMxMi00ZGU2LTgxODYtNDcwMTg3MzBiNDQ0IiwiLnhzcmYiOiJBZjZJMi14S1MyM1hYaVZ1ZTRCU1k2dEFGRnEwVEx1QnlpNmN5OVVueVl5R1VtLVZHMmgxNktQR0dVTGprekFaLUtnRkJMcndBUWJPZm5LMU5xaUpqeGFIM3F4SkJTd3JfQWpSTmc4X0dlSEFaUnd4UV9fTFNnV2NIRFpCVThHekp3IiwiT3BlbklkQ29ubmVjdC5Db2RlLlJlZGlyZWN0VXJpIjoiQVpaa2FJTDFHWDNneV9haHQ5bUd6ZGtEeC10S1NOVkpCeTF6RkNOa0NWb01xRWNjMkVucFoxMG5EWlpYYm1lZ1ZDVHdXUHQ2SDVVdmdGLWJkbE5WTHMtTmZmTmpxZTZnMzVHZldFY2V5NWVGV0J1Ni1oLTJpXzZXNlFVTGxSRHEwQSJ9fQ&response_type=code%20id_token&scope=openid%20profile&response_mode=form_post&nonce=638433620133275161.OGMyY2Q1ZWItMTcyNC00ZDc3LWE2ZGUtMmI4MWJhNWRjNjgxZDQ5YTljYzctOTk0YS00ZTdjLWJiODYtZDcyM2Y1MjJkNzZl&msafed=0&x-client-SKU=ID_NET6_0&x-client-ver=6.34.0.0",
            "time_usec": 1708021866316376,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://uvalentine.com/apple-touch-icon.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "uvalentine",
            "url": "https://uvalentine.com/view",
            "time_usec": 1708021866258603,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://aadcdn.msauth.net/shared/1.0/content/images/favicon_a_eupayfgghqiai7k9sol6lg2.ico",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Sign in to your account",
            "url": "https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&redirect_uri=https%3A%2F%2Fforms.office.com%2Flanding&state=eyJ2ZXJzaW9uIjoxLCJkYXRhIjp7IklkZW50aXR5UHJvdmlkZXIiOiJBV3RlNUNMU1FZT1hBeV91SS0zSHh4aVFCSFFNZldDMjRjVmdTS21wd3NQaE1GZnE0OXdMbEllMUZkWDB4by05TGRRUHJYTWlUM1lHT3VOeG9RRmNodGsiLCIucmVkaXJlY3QiOiJodHRwczovL2Zvcm1zLm9mZmljZS5jb20vUGFnZXMvUmVzcG9uc2VQYWdlLmFzcHg_aWQ9eDRBMGV3YzNjMGlMZC1JV2N6cGxySk04RFZQb2l0aExvZTBVb29BNENjZFVORVJKTXpkVlVUaFVWVGhWU2poTlRERk5Oa0pVUmtGVU55UWxRQ04wUFdjdSZzaWQ9Zjg2ZGJlZTUtMTMxMi00ZGU2LTgxODYtNDcwMTg3MzBiNDQ0IiwiLnhzcmYiOiJBZjZJMi14S1MyM1hYaVZ1ZTRCU1k2dEFGRnEwVEx1QnlpNmN5OVVueVl5R1VtLVZHMmgxNktQR0dVTGprekFaLUtnRkJMcndBUWJPZm5LMU5xaUpqeGFIM3F4SkJTd3JfQWpSTmc4X0dlSEFaUnd4UV9fTFNnV2NIRFpCVThHekp3IiwiT3BlbklkQ29ubmVjdC5Db2RlLlJlZGlyZWN0VXJpIjoiQVpaa2FJTDFHWDNneV9haHQ5bUd6ZGtEeC10S1NOVkpCeTF6RkNOa0NWb01xRWNjMkVucFoxMG5EWlpYYm1lZ1ZDVHdXUHQ2SDVVdmdGLWJkbE5WTHMtTmZmTmpxZTZnMzVHZldFY2V5NWVGV0J1Ni1oLTJpXzZXNlFVTGxSRHEwQSJ9fQ&response_type=code%20id_token&scope=openid%20profile&response_mode=form_post&nonce=638433620133275161.OGMyY2Q1ZWItMTcyNC00ZDc3LWE2ZGUtMmI4MWJhNWRjNjgxZDQ5YTljYzctOTk0YS00ZTdjLWJiODYtZDcyM2Y1MjJkNzZl&msafed=0&x-client-SKU=ID_NET6_0&x-client-ver=6.34.0.0",
            "time_usec": 1707765213729505,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
},
        {
            "favicon_url": "https://cdn.gradescope.com/assets/logo/icons/64x64-3c29e9891a184582f67b6a2cd6c4a96bbfb20bbe7d7249d8f7feaa2ebd13832e.png",
            "page_transition_qualifier": "CLIENT_REDIRECT",
            "title": "Log In | Gradescope",
            "url": "https://www.gradescope.com/login",
            "time_usec": 1707765211075173,
            "client_id": "IAQTOFgxEBlXQbaNAe2BhA=="
}
    ],
    "Typed Url": [],
    "Session": [
        {
            "tab_node_id": 44,
            "tab": {
                        "current_navigation_index": 2,
                        "tab_id": 123416765,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 10,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13381545455189000,
                                                "page_transition": "RELOAD",
                                                "title": "New Tab",
                                                "timestamp_msec": 1737071855189,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "chrome://newtab/",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 11,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13381545455189000,
                                                "page_transition": "RELOAD",
                                                "title": "Tracking | UPS - United States",
                                                "timestamp_msec": 1737071855189,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://www.ups.com/track?loc=en_US&Requester=SBN&tracknum=1Z4051V00399182059&AgreeToTermsAndConditions=yes&WT.z_eCTAid=ct1_eml_Tracking__ct1_eml_tra_eml_auto_missed_delivery&WT.z_edatesent=01162025",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 12,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13381545455189000,
                                                "page_transition": "RELOAD",
                                                "title": "Tracking | UPS - United States",
                                                "timestamp_msec": 1737071855189,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.ups.com/track?loc=en_US&Requester=SBN&tracknum=1Z4051V00399182059&AgreeToTermsAndConditions=yes&WT.z_eCTAid=ct1_eml_Tracking__ct1_eml_tra_eml_auto_missed_delivery&WT.z_edatesent=01162025",
                                                "virtual_url": "https://www.ups.com/track?loc=en_US&Requester=SBN&tracknum=1Z4051V00399182059&AgreeToTermsAndConditions=yes&WT.z_eCTAid=ct1_eml_Tracking__ct1_eml_tra_eml_auto_missed_delivery&WT.z_edatesent=01162025/trackdetails",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1737071855280,
                        "window_id": 123417370,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 19,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123414582,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 84,
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13372283930118000,
                                    "page_transition": "RELOAD",
                                    "title": "App",
                                    "timestamp_msec": 1727810330118,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "",
                                    "virtual_url": "https://clientforms.mindbodyonline.com/?externalFormId=47d4b68c-bc26-4cf3-90fd-580e218af15a&utm_source=ClientForms&utm_campaign=ClientForms&utm_medium=ClientFormsUrl&_branch_referrer=H4sIAAAAAAAAA8soKSkottLXT08t0cvNS0lKqdTLqdRP1bfwM8wJK0yxTPVLsq8rSk1LLSrKzEuPTyrKLy9OLbJ1zijKz00FACuveJU9AAAA&%24web_only=true&_branch_match_id=1368343622437675893",
                                    "correct_referrer_policy": 1,
                                    "navigation_home_page": False
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1727810330177,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 12,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123413988,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 65,
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13364194814284000,
                                    "page_transition": "RELOAD",
                                    "title": "Portale Italolive: Wi-Fi gratis, serie TV, cinema\u2026",
                                    "timestamp_msec": 1719721214284,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "",
                                    "virtual_url": "https://www.italotreno.com/il-treno/portale-italolive",
                                    "correct_referrer_policy": 1,
                                    "navigation_home_page": False
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1719721214359,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 38,
            "tab": {
                        "current_navigation_index": 1,
                        "tab_id": 123415901,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 134,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13376786717234000,
                                                "page_transition": "RELOAD",
                                                "title": "Career Opportunities: Sign In",
                                                "timestamp_msec": 1732313117234,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://career5.successfactors.eu/career?career_ns=job_application&navBarLevel=JOB_MGMT&subNavBarLevel=JOB_APPLIED&fbja_action=fbja_viewApp&company=ALSTOM&career_job_req_id=472321&fbja_appId=4384403&st=79FA6509ED7F77F69E1692410B1A81C537A5B34A&",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 135,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13376786717234000,
                                                "page_transition": "RELOAD",
                                                "title": "",
                                                "timestamp_msec": 1732313117234,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://career5.successfactors.eu/career?career_ns=job_application&navBarLevel=JOB_MGMT&subNavBarLevel=JOB_APPLIED&fbja_action=fbja_viewApp&company=ALSTOM&career_job_req_id=472321&fbja_appId=4384403&st=79FA6509ED7F77F69E1692410B1A81C537A5B34A&",
                                                "virtual_url": "https://career5.successfactors.eu/portalcareer?_s.crb=WAXWHIfDzmElYl3yPT%252bwNSyhBOjN7F8P05MOINStZ0U%253d",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1732313117346,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 3,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123413417,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 27,
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13359753189551000,
                                    "page_transition": "RELOAD",
                                    "title": "CS3140 Office Hours on Final Week - Google Drive",
                                    "timestamp_msec": 1715279589551,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "",
                                    "virtual_url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ36etqbk15oe6xF9KQzQvI6wpXWwY2nunkpLEKTeXfL3EWNH4KQ1gFl7euBeEx43yXh_nfY-VPuOeW/pubhtml?gid=0&single=true",
                                    "correct_referrer_policy": 1,
                                    "navigation_home_page": False
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1715279589622,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 46,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123417219,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 3,
                                    "favicon_url": "https://www.irs.gov/favicon.ico",
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13383064384463000,
                                    "page_transition": "LINK",
                                    "title": "",
                                    "timestamp_msec": 1738590784463,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "",
                                    "virtual_url": "https://www.irs.gov/pub/irs-pdf/fw9.pdf",
                                    "correct_referrer_policy": 1,
                                    "navigation_home_page": False,
                                    "redirect_type": "CLIENT_REDIRECT"
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1738590784513,
                        "window_id": 123417370,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 33,
            "tab": {
                        "current_navigation_index": 1,
                        "tab_id": 123415564,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 125,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374678715837000,
                                                "page_transition": "RELOAD",
                                                "title": "Frye Boots Womens 9 Phillip Studded Harness Ring\u2026",
                                                "timestamp_msec": 1730205115837,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://www.ebay.com/itm/235793133625",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 126,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374678776698000,
                                                "page_transition": "RELOAD",
                                                "title": "Order details | eBay",
                                                "timestamp_msec": 1730205176698,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.ebay.com/itm/235793133625",
                                                "virtual_url": "https://order.ebay.com/ord/show?orderId=10-12250-60397&ssPageName=STRK:MESO:VPS&_trksid=p4429486.m2548.l2673#/",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1730205114860,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 37,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123415764,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 133,
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13376062525580000,
                                    "page_transition": "RELOAD",
                                    "title": "Delta Shelta Secret Santa (again) | Elfster",
                                    "timestamp_msec": 1731588925580,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "https://www.elfster.com/actions/redirect/?redirecturl=%2Fgift-exchanges%2Fdbbc2db7-aaa6-4a3e-8106-f0d08189cc4a%2F%3Futm_source%3Dapp_email%26utm_medium%3Demail%26utm_content%3DCallToActionHtml0%26utm_campaign%3DDrawNotification",
                                    "virtual_url": "https://www.elfster.com/gift-exchanges/dbbc2db7-aaa6-4a3e-8106-f0d08189cc4a/?utm_source=app_email&utm_medium=email&utm_content=CallToActionHtml0&utm_campaign=DrawNotification",
                                    "correct_referrer_policy": 0,
                                    "navigation_home_page": False
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1731588924114,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 7,
            "tab": {
                        "current_navigation_index": 6,
                        "tab_id": 123413628,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 45,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13361280089861000,
                                                "page_transition": "RELOAD",
                                                "title": "Moodle ISI Florence",
                                                "timestamp_msec": 1716806489861,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "http://moodle.isiflorence.org/",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 46,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13361280174210000,
                                                "page_transition": "RELOAD",
                                                "title": "Moodle ISI Florence: Log in to the site",
                                                "timestamp_msec": 1716806574210,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "http://moodle.isiflorence.org/",
                                                "virtual_url": "http://moodle.isiflorence.org/login/index.php",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 47,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13361280246592000,
                                                "page_transition": "RELOAD",
                                                "title": "Moodle ISI Florence: Log in to the site",
                                                "timestamp_msec": 1716806646592,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "http://moodle.isiflorence.org/login/index.php",
                                                "virtual_url": "http://moodle.isiflorence.org/login/index.php",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 48,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13361280252801000,
                                                "page_transition": "RELOAD",
                                                "title": "Forgotten password",
                                                "timestamp_msec": 1716806652801,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "http://moodle.isiflorence.org/login/index.php",
                                                "virtual_url": "http://moodle.isiflorence.org/login/forgot_password.php",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 49,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13361280271178000,
                                                "page_transition": "RELOAD",
                                                "title": "Forgotten password",
                                                "timestamp_msec": 1716806671178,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "http://moodle.isiflorence.org/login/forgot_password.php",
                                                "virtual_url": "http://moodle.isiflorence.org/login/forgot_password.php",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 50,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13361280281040000,
                                                "page_transition": "RELOAD",
                                                "title": "Forgotten password",
                                                "timestamp_msec": 1716806681040,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "http://moodle.isiflorence.org/login/forgot_password.php",
                                                "virtual_url": "http://moodle.isiflorence.org/login/forgot_password.php",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 51,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13361280384045000,
                                                "page_transition": "RELOAD",
                                                "title": "Moodle ISI Florence",
                                                "timestamp_msec": 1716806784045,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "http://moodle.isiflorence.org/login/forgot_password.php",
                                                "virtual_url": "http://moodle.isiflorence.org/index.php?",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1716806487947,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 1,
            "tab": {
                        "current_navigation_index": 1,
                        "tab_id": 123413293,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 22,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13358756987713000,
                                                "page_transition": "RELOAD",
                                                "title": "New Tab",
                                                "timestamp_msec": 1714283387713,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "chrome://newtab/",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 23,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13358756987713000,
                                                "page_transition": "RELOAD",
                                                "title": "anna cchoneycomb charlotttesville - Google Search",
                                                "timestamp_msec": 1714283387713,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://www.google.com/search?q=anna+cchoneycomb+charlotttesville&rlz=1CDGOYI_enUS976US998&oq=anna+cchoneycomb+charlotttesville&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAEyCQgDECEYChigAdIBCDQ4MTRqMGo3qAIZsAIB4gMEGAEgXw&hl=en-US&sourceid=chrome-mobile&ie=UTF-8",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 24,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13358756987713000,
                                                "page_transition": "RELOAD",
                                                "title": "THE HONEYCOMB",
                                                "timestamp_msec": 1714283387713,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.google.com/search?q=anna+cchoneycomb+charlotttesville&rlz=1CDGOYI_enUS976US998&oq=anna+cchoneycomb+charlotttesville&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAEyCQgDECEYChigAdIBCDQ4MTRqMGo3qAIZsAIB4gMEGAEgXw&hl=en-US&sourceid=chrome-mobile&ie=UTF-8",
                                                "virtual_url": "https://www.cvillehoneycomb.com/",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 25,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13358756987713000,
                                                "page_transition": "RELOAD",
                                                "title": "Find & Contact Us \u2014 THE HONEYCOMB",
                                                "timestamp_msec": 1714283387713,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.cvillehoneycomb.com/",
                                                "virtual_url": "https://www.cvillehoneycomb.com/find-us",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1714283387752,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 28,
            "tab": {
                        "current_navigation_index": 1,
                        "tab_id": 123415243,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 111,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372817670690000,
                                                "page_transition": "RELOAD",
                                                "title": "Bring Your Own Device (BYOD) | How To & Deals | V\u2026",
                                                "timestamp_msec": 1728344070690,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://www.verizon.com/bring-your-own-device/?CMP=bac_m_p_140_gdn_acq_24_01_acq_dsc-382979731_207763455&utm_medium=bac&utm_source=gdn&utm_campaign=m:acq&utm_content=acq_dsc&dclid=&wbraid=ClkKCAjw6oi4BhBfEkkAEbrBp61kMMSY4fD9btemb4Tqf5mzmyu6_sWf3y0af0nw1XOyHvafRzsZqPyW-b7U50YaT-fupJI0f67mJesTxYPALZI1O8QWGgK7Pg",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 112,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372818432738000,
                                                "page_transition": "RELOAD",
                                                "title": "Bring Your Own Device (BYOD) | How To & Deals | V\u2026",
                                                "timestamp_msec": 1728344832738,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://www.verizon.com/bring-your-own-device/?CMP=bac_m_p_140_gdn_acq_24_01_acq_dsc-382979731_207763455&utm_medium=bac&utm_source=gdn&utm_campaign=m:acq&utm_content=acq_dsc&dclid=&wbraid=ClkKCAjw6oi4BhBfEkkAEbrBp61kMMSY4fD9btemb4Tqf5mzmyu6_sWf3y0af0nw1XOyHvafRzsZqPyW-b7U50YaT-fupJI0f67mJesTxYPALZI1O8QWGgK7Pg",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1728344069369,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 0,
            "tab": {
                        "current_navigation_index": 5,
                        "tab_id": 123413046,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 15,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13357929638292000,
                                                "page_transition": "RELOAD",
                                                "title": "New Tab",
                                                "timestamp_msec": 1713456038292,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "chrome://newtab/",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 16,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13357929638988000,
                                                "page_transition": "RELOAD",
                                                "title": "Schedulicity Online Scheduling | Book Appointment\u2026",
                                                "timestamp_msec": 1713456038988,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://www.schedulicity.com/myappointments?CID=51297463",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 17,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13357929643076000,
                                                "page_transition": "RELOAD",
                                                "title": "",
                                                "timestamp_msec": 1713456043076,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.schedulicity.com/myappointments?CID=51297463",
                                                "virtual_url": "https://www.schedulicity.com/account/identify",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 18,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13357929656217000,
                                                "page_transition": "RELOAD",
                                                "title": "",
                                                "timestamp_msec": 1713456056217,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.schedulicity.com/account/identify",
                                                "virtual_url": "https://www.schedulicity.com/account/verify",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 19,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13357929688150000,
                                                "page_transition": "RELOAD",
                                                "title": "",
                                                "timestamp_msec": 1713456088150,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.schedulicity.com/account/verify",
                                                "virtual_url": "https://www.schedulicity.com/myappointments",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 20,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13357929688804000,
                                                "page_transition": "RELOAD",
                                                "title": "Schedulicity Online Scheduling | Book Appointment\u2026",
                                                "timestamp_msec": 1713456088804,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.schedulicity.com/account/verify",
                                                "virtual_url": "https://www.schedulicity.com/myappointments?CID=51297463",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 21,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13357929703007000,
                                                "page_transition": "RELOAD",
                                                "title": "THE HONEYCOMB - Hair Stylists in Charlottesville,\u2026",
                                                "timestamp_msec": 1713456103007,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.schedulicity.com/myappointments?CID=51297463",
                                                "virtual_url": "https://www.schedulicity.com/scheduling/THEBJL?CID=51297463",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1713456038386,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 41,
            "tab": {
                        "current_navigation_index": 2,
                        "tab_id": 123416324,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 143,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13379438065073000,
                                                "page_transition": "RELOAD",
                                                "title": "Detailed Tracking",
                                                "timestamp_msec": 1734964465073,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://www.fedex.com/wtrk/track/?trknbr=282441444327&sc_src=email_4967189&sc_lid=544755794&sc_uid=iv4JPtKeT7&sc_llid=792375&sc_eh=e1e424bcba971e311&utm_source=Emarsys&utm_medium=email&utm_id=4967189&utm_campaign=shipping%20confirmation&utm_content=transactional&utm_term=CGA",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 144,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13379438065073000,
                                                "page_transition": "RELOAD",
                                                "title": "Detailed Tracking",
                                                "timestamp_msec": 1734964465073,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.fedex.com/wtrk/track/?trknbr=282441444327&sc_src=email_4967189&sc_lid=544755794&sc_uid=iv4JPtKeT7&sc_llid=792375&sc_eh=e1e424bcba971e311&utm_source=Emarsys&utm_medium=email&utm_id=4967189&utm_campaign=shipping%20confirmation&utm_content=transactional&utm_term=CGA",
                                                "virtual_url": "https://www.fedex.com/wtrk/track/?trknbr=282441444327&trkqual=2460644000~282441444327~FX",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 145,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13379438076840000,
                                                "page_transition": "RELOAD",
                                                "title": "Detailed Tracking",
                                                "timestamp_msec": 1734964476840,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.fedex.com/wtrk/track/?trknbr=282441444327&trkqual=2460644000~282441444327~FX",
                                                "virtual_url": "https://www.fedex.com/fedextrack/?trknbr=282441444327&trkqual=2460644000~282441444327~FX",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1734964465150,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 36,
            "tab": {
                        "current_navigation_index": 1,
                        "tab_id": 123415629,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 130,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13375547633820000,
                                                "page_transition": "RELOAD",
                                                "title": "SIS Home",
                                                "timestamp_msec": 1731074033820,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_GN.H_SPRINGBOARD.FieldFormula.IScript_Main?institution=UVA01&",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 131,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13375547633820000,
                                                "page_transition": "RELOAD",
                                                "title": "student financial services - Google Search",
                                                "timestamp_msec": 1731074033820,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_GN.H_SPRINGBOARD.FieldFormula.IScript_Main?institution=UVA01&",
                                                "virtual_url": "https://www.google.com/search?q=student+financial+services&rlz=1CDGOYI_enUS976US998&oq=student+financial+services&gs_lcrp=EgZjaHJvbWUqCggAEAAY4wIYgAQyCggAEAAY4wIYgAQyEAgBEC4YrwEYxwEYgAQYjgUyCggCEAAYsQMYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyDQgGEC4YrwEYxwEYgAQyDQgHEC4YrwEYxwEYgAQyBwgIEAAYgAQyBwgJEAAYgATSAQg0OTkxajBqNKgCAbACAeIDBBgBIF8&hl=en-US&sourceid=chrome-mobile&ie=UTF-8&dlnr=1&sei=MzAqZ7bPBYbk5NoPhru-oAM#ebo=0",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 132,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13375547633820000,
                                                "page_transition": "RELOAD",
                                                "title": "",
                                                "timestamp_msec": 1731074033820,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://www.google.com/maps/uv?viewerState=lb&pb=!1s0x89b3865ad95ad309:0x1fd9ae158af2caa8&imagekey=!1e10!2sAF1QipM8ohsmzh7myZSBmYUttc5ACuk2TWmBMU0noPWF&cr=tp_14&gsas=1",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1731074033879,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 47,
            "tab": {
                        "current_navigation_index": 4,
                        "tab_id": 123417375,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 4,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13383064386537101,
                                                "page_transition": "LINK",
                                                "title": "Advisor Agreement - Roth IRA | Dropbox Sign",
                                                "timestamp_msec": 1738590786537,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://app.hellosign.com/sign/5869bd035c8fc9662753701f56a6101d1cbff465",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 147,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13383064391745781,
                                                "page_transition": "LINK",
                                                "title": "Advisor Agreement - Roth IRA | Dropbox Sign",
                                                "timestamp_msec": 1738590791745,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://app.hellosign.com/sign/5869bd035c8fc9662753701f56a6101d1cbff465",
                                                "virtual_url": "https://app.hellosign.com/sign/5869bd035c8fc9662753701f56a6101d1cbff465#/sign/component_461407445_1",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 149,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13383064401486329,
                                                "page_transition": "LINK",
                                                "title": "Advisor Agreement - Roth IRA | Dropbox Sign",
                                                "timestamp_msec": 1738590801486,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://app.hellosign.com/sign/5869bd035c8fc9662753701f56a6101d1cbff465#/sign/component_461407445_1",
                                                "virtual_url": "https://app.hellosign.com/sign/5869bd035c8fc9662753701f56a6101d1cbff465#/sign/component_1235421184_2?validate=False",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 151,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13383064436965541,
                                                "page_transition": "LINK",
                                                "title": "Advisor Agreement - Roth IRA | Dropbox Sign",
                                                "timestamp_msec": 1738590836965,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://app.hellosign.com/sign/5869bd035c8fc9662753701f56a6101d1cbff465#/sign/component_1235421184_2?validate=False",
                                                "virtual_url": "https://app.hellosign.com/sign/5869bd035c8fc9662753701f56a6101d1cbff465#/confirm",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 153,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13383064439450168,
                                                "page_transition": "LINK",
                                                "title": "Advisor Agreement - Roth IRA | Dropbox Sign",
                                                "timestamp_msec": 1738590839450,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://app.hellosign.com/sign/5869bd035c8fc9662753701f56a6101d1cbff465#/confirm",
                                                "virtual_url": "https://app.hellosign.com/sign/5869bd035c8fc9662753701f56a6101d1cbff465#/complete",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1738590784857,
                        "window_id": 123417370,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 25,
            "tab": {
                        "current_navigation_index": 6,
                        "tab_id": 123415012,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 100,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372563913675000,
                                                "page_transition": "RELOAD",
                                                "title": "Gradescope",
                                                "timestamp_msec": 1728090313675,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.gradescope.com/login",
                                                "virtual_url": "https://www.gradescope.com/saml",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 101,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372563913675000,
                                                "page_transition": "RELOAD",
                                                "title": "NetBadge",
                                                "timestamp_msec": 1728090313675,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.gradescope.com/saml",
                                                "virtual_url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s2",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 102,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372563913675000,
                                                "page_transition": "RELOAD",
                                                "title": "NetBadge",
                                                "timestamp_msec": 1728090313675,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s2",
                                                "virtual_url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s3",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 103,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372563913675000,
                                                "page_transition": "RELOAD",
                                                "title": "NetBadge",
                                                "timestamp_msec": 1728090313675,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s3",
                                                "virtual_url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s4",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 104,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372563913675000,
                                                "page_transition": "RELOAD",
                                                "title": "Duo Security - Two-Factor Authentication",
                                                "timestamp_msec": 1728090313675,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s4",
                                                "virtual_url": "https://api-58663eb0.duosecurity.com/frame/frameless/v4/auth?sid=frameless-282dfc79-4dab-4591-a513-216f71370fbe&tx=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJkdW9fdW5hbWUiOiJ5a2MzaHAiLCJzY29wZSI6Im9wZW5pZCIsInJlc3BvbnNlX3R5cGUiOiJjb2RlIiwicmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly9zaGliaWRwLml0cy52aXJnaW5pYS5lZHUvaWRwL3Byb2ZpbGUvQXV0aG4vRHVvLzJGQS9kdW8tY2FsbGJhY2siLCJzdGF0ZSI6IjcxMGRlZGVjYjZjYjFjODU0NjY0OTBjNTY4M2E3NmE1LjY1MzE3MzM1IiwiZXhwIjoxNzI4MDg5NTE4LCJjbGllbnRfaWQiOiJESU41WkpQR0JWRzRRWTRGSVZHUSJ9.ZFgQ3JgP7GllW7hf0p8C5P3x86rq7iehW0Nujp2ZCxsN_5qY9L9aAOFTXvc0PEjBoEOFI-mUOp9Lj_a9EByiWQ&req-trace-group=93e0e2f6642ff1fe9a915fd9",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 105,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372563913675000,
                                                "page_transition": "RELOAD",
                                                "title": "Duo Security",
                                                "timestamp_msec": 1728090313675,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://api-58663eb0.duosecurity.com/frame/frameless/v4/auth?sid=frameless-282dfc79-4dab-4591-a513-216f71370fbe&tx=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJkdW9fdW5hbWUiOiJ5a2MzaHAiLCJzY29wZSI6Im9wZW5pZCIsInJlc3BvbnNlX3R5cGUiOiJjb2RlIiwicmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly9zaGliaWRwLml0cy52aXJnaW5pYS5lZHUvaWRwL3Byb2ZpbGUvQXV0aG4vRHVvLzJGQS9kdW8tY2FsbGJhY2siLCJzdGF0ZSI6IjcxMGRlZGVjYjZjYjFjODU0NjY0OTBjNTY4M2E3NmE1LjY1MzE3MzM1IiwiZXhwIjoxNzI4MDg5NTE4LCJjbGllbnRfaWQiOiJESU41WkpQR0JWRzRRWTRGSVZHUSJ9.ZFgQ3JgP7GllW7hf0p8C5P3x86rq7iehW0Nujp2ZCxsN_5qY9L9aAOFTXvc0PEjBoEOFI-mUOp9Lj_a9EByiWQ&req-trace-group=93e0e2f6642ff1fe9a915fd9",
                                                "virtual_url": "https://api-58663eb0.duosecurity.com/frame/v4/auth/prompt?sid=frameless-282dfc79-4dab-4591-a513-216f71370fbe",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 106,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372563913675000,
                                                "page_transition": "RELOAD",
                                                "title": "NetBadge Message",
                                                "timestamp_msec": 1728090313675,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://api-58663eb0.duosecurity.com/frame/v4/auth/prompt?sid=frameless-282dfc79-4dab-4591-a513-216f71370fbe",
                                                "virtual_url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s6",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 107,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372563913675000,
                                                "page_transition": "RELOAD",
                                                "title": "View Submission | Gradescope",
                                                "timestamp_msec": 1728090313675,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s6",
                                                "virtual_url": "https://www.gradescope.com/courses/884802/assignments/5070823/submissions/272931858",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1728090313725,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "header": {
                        "device_form_factor": "DEVICE_FORM_FACTOR_PHONE",
                        "device_type": "TYPE_PHONE",
                        "window": [
                                    {
                                                "selected_tab_index": -1,
                                                "tab": [
                                                            123416469,
                                                            123416616,
                                                            123416765,
                                                            123417064,
                                                            123417219,
                                                            123417375
                                                ],
                                                "browser_type": "TYPE_TABBED",
                                                "window_id": 123417370
                                    },
                                    {
                                                "selected_tab_index": -1,
                                                "tab": [
                                                            123413046,
                                                            123413293,
                                                            123413352,
                                                            123413417,
                                                            123413484,
                                                            123413553,
                                                            123413569,
                                                            123413628,
                                                            123413660,
                                                            123413719,
                                                            123413830,
                                                            123413943,
                                                            123413988,
                                                            123414048,
                                                            123414097,
                                                            123414156,
                                                            123414278,
                                                            123414386,
                                                            123414483,
                                                            123414582,
                                                            123414683,
                                                            123414730,
                                                            123414792,
                                                            123414842,
                                                            123414901,
                                                            123415012,
                                                            123415125,
                                                            123415184,
                                                            123415243,
                                                            123415306,
                                                            123415309,
                                                            123415368,
                                                            123415493,
                                                            123415564,
                                                            123415567,
                                                            123415570,
                                                            123415629,
                                                            123415764,
                                                            123415901,
                                                            123416040,
                                                            123416181,
                                                            123416324
                                                ],
                                                "browser_type": "TYPE_TABBED",
                                                "window_id": 123417372
                                    }
                        ],
                        "client_name": "ryan\u2019s phone"
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 29,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123415306,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 113,
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13372818433862000,
                                    "page_transition": "RELOAD",
                                    "title": "Ticketmaster Sign In",
                                    "timestamp_msec": 1728344833862,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "",
                                    "virtual_url": "https://auth.ticketmaster.com/as/authorization.oauth2?client_id=8bf7204a7e97.web.ticketmaster.us&response_type=code&scope=openid%20profile%20phone%20email%20tm&redirect_uri=https://identity.ticketmaster.com/exchange&visualPresets=tm&lang=en-us&placementId=myAccount&showHeader=true&hideLeftPanel=False&integratorId=prd283.myAccount&intSiteToken=tm-us&deviceId=kQ22i5EgsjE3MjgzNDQ4MzM2Mjn%2FUj3be%2FifVg",
                                    "correct_referrer_policy": 1,
                                    "navigation_home_page": False
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1728344832410,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 17,
            "tab": {
                        "current_navigation_index": 2,
                        "tab_id": 123414386,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 74,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13371277839702000,
                                                "page_transition": "RELOAD",
                                                "title": "New Tab",
                                                "timestamp_msec": 1726804239702,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "chrome://newtab/",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 75,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13371277839702000,
                                                "page_transition": "RELOAD",
                                                "title": "Greek House Chefs",
                                                "timestamp_msec": 1726804239702,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://beta.greekhousechefs.com/users/password/edit?reset_password_token=bD_xSzhMd8Txbhw5iwLy",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 76,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13371277839702000,
                                                "page_transition": "RELOAD",
                                                "title": "The page you were looking for doesn't exist (404)",
                                                "timestamp_msec": 1726804239702,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://beta.greekhousechefs.com/users/password/edit?reset_password_token=bD_xSzhMd8Txbhw5iwLy",
                                                "virtual_url": "https://beta.greekhousechefs.com/users/password",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1726804239806,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 5,
            "tab": {
                        "current_navigation_index": 2,
                        "tab_id": 123413553,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 35,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13360199984258000,
                                                "page_transition": "RELOAD",
                                                "title": "Manage my booking",
                                                "timestamp_msec": 1715726384258,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://www.condor.com/tcibe/eu/mybooking/login?utm_source=condor_colibri&utm_medium=email_system&utm_campaign=oci_pico",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 36,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13360200113271000,
                                                "page_transition": "RELOAD",
                                                "title": "Condor \u2013 My booking \u2013 Manage my booking",
                                                "timestamp_msec": 1715726513271,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.condor.com/tcibe/eu/mybooking/login?utm_source=condor_colibri&utm_medium=email_system&utm_campaign=oci_pico",
                                                "virtual_url": "https://www.condor.com/tcibe/eu/mybooking/paxContactInformation",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 37,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13360200145752000,
                                                "page_transition": "RELOAD",
                                                "title": "Condor \u2013 My booking \u2013 Manage my booking",
                                                "timestamp_msec": 1715726545752,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.condor.com/tcibe/eu/mybooking/paxContactInformation",
                                                "virtual_url": "https://www.condor.com/tcibe/eu/mybooking/dashboard",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1715726383686,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 26,
            "tab": {
                        "current_navigation_index": 1,
                        "tab_id": 123415125,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 108,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372563914591000,
                                                "page_transition": "RELOAD",
                                                "title": "38°02'20.8\"N 78°30'02.0\"W - Google Maps",
                                                "timestamp_msec": 1728090314591,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://www.google.com/maps/?q=38.03911536753252,-78.50055310731386",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 109,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372563983813000,
                                                "page_transition": "RELOAD",
                                                "title": "",
                                                "timestamp_msec": 1728090383813,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.google.com/maps/place/38%C2%B002'20.8%22N+78%C2%B030'02.0%22W/@38.0391154,-78.5005531,16z/data=!4m4!3m3!8m2!3d38.0391154!4d-78.5005531",
                                                "virtual_url": "https://www.google.com/maps/place/38%C2%B002'20.8%22N+78%C2%B030'02.0%22W/@38.0391154,-78.5005531,16z/data=!4m4!3m3!8m2!3d38.0391154!4d-78.5005531",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1728090314002,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 34,
            "tab": {
                        "current_navigation_index": 1,
                        "tab_id": 123415567,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 127,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374678781612000,
                                                "page_transition": "RELOAD",
                                                "title": "Frye Boots Womens 9 Phillip Studded Harness Ring\u2026",
                                                "timestamp_msec": 1730205181612,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://www.ebay.com/itm/235793133625",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 128,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374678796691000,
                                                "page_transition": "RELOAD",
                                                "title": "Frye Phillip Short Black Harness Moto Biker Boots\u2026",
                                                "timestamp_msec": 1730205196691,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.ebay.com/itm/235793133625",
                                                "virtual_url": "https://www.ebay.com/itm/267036625439?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D264184%26meid%3Df8fdedf5072741a789137a218d244c2a%26pid%3D101429%26rk%3D4%26rkt%3D12%26sd%3D235793133625%26itm%3D267036625439%26pmt%3D1%26noa%3D0%26pg%3D2332490%26algv%3DSimPLMWebV1EmbeddedAuctionsCPCAutoManualWithCIIXAIRecallsUpdatedRanker0424NoIMA%26brand%3DFrye&_trksid=p2332490.c101429.m2460&itmprp=cksum%3A267036625439f8fdedf5072741a789137a218d244c2a%7Cenc%3AAQAJAAABMIV5CFHpx8qL94DS2Mo1uCi5RlK%252B6oGF%252Bq%252FvM6onJsyCAS4bVm4MG2DxmngmQBYs7QTou1H5%252BktC9DZbAMWEM%252B%252BdlquESLSCZunJqt41Rd0Jpo%252B961Uv4rJCVp8%252FxvBjYUwREXJW33qPfSLivHzNecR2Jm7p5LGeMZgjT1vf3edYBgwlPnLrVrVi%252BdRwqolWXXz9M3GBG01SXMA2iiWjbVlvvH4L5EOImGTVQWr%252BPu0tV3gDMvZAGSyV2V6iwXozT6HInBm%252Fps1dQm3wfKKCsplt8DBIsXWoXSXw0O1WMOplO6j5SjL2Bepsv8%252FDKscQDNXrzmQbr8mB1oyL3M6Oy2q3bsHTEacNi47sV3hJReAobIMmb%252FUyKnWFChbsLPyUmOwWLcOgwh3%252BAXJBML%252BC4w8%253D%7Campid%3APL_CLK%7Cclp%3A2332490&itmmeta=01JBC47SJ16GGXK4S2ZDT80Z8B",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1730205180680,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 15,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123414156,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 69,
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13365273854052000,
                                    "page_transition": "RELOAD",
                                    "title": "Cheap Flights | Book Direct for Best Deals | Wizz\u2026",
                                    "timestamp_msec": 1720800254052,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "",
                                    "virtual_url": "https://wizzair.com/en-gb?emailVerification=20a9fb52-3329-474c-8e4a-c4454afd5e93",
                                    "correct_referrer_policy": 1,
                                    "navigation_home_page": False
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1720800252981,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 10,
            "tab": {
                        "current_navigation_index": 1,
                        "tab_id": 123413830,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 62,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13364032314979000,
                                                "page_transition": "RELOAD",
                                                "title": "Meeting Registration - Zoom",
                                                "timestamp_msec": 1719558714979,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://virginia.zoom.us/meeting/register/tJcrcu-pqzIvHdGazQvV0Kjqks2tqChs1iD1#/registration",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 63,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13364032314979000,
                                                "page_transition": "RELOAD",
                                                "title": "Meeting Registration - Zoom",
                                                "timestamp_msec": 1719558714979,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://virginia.zoom.us/rest/meeting/registrant/tJcrcu-pqzIvHdGazQvV0Kjqks2tqChs1iD1/info?tk=5QKysB1nRXkdkhr06ZooPSTxXSssOTj8BEojlbysrQyKuY6xS3tTS2Y.srHtPxAEKT9S8C4r&ac=approved&timezone_id=Europe/Rome#/edit",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1719558715022,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 4,
            "tab": {
                        "current_navigation_index": 6,
                        "tab_id": 123413484,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 28,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13360199983260000,
                                                "page_transition": "RELOAD",
                                                "title": "Reset Your Password",
                                                "timestamp_msec": 1715726383260,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://idm.xfinity.com/myaccount/reset?execution=e1s4",
                                                "virtual_url": "https://idm.xfinity.com/myaccount/reset?execution=e1s5",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 29,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13360199983260000,
                                                "page_transition": "RELOAD",
                                                "title": "Comcast ID Account Management",
                                                "timestamp_msec": 1715726383260,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://idm.xfinity.com/myaccount/reset?execution=e1s5",
                                                "virtual_url": "https://idm.xfinity.com/myaccount/reset?execution=e1s6",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 30,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13360199983260000,
                                                "page_transition": "RELOAD",
                                                "title": "Security Check",
                                                "timestamp_msec": 1715726383260,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://idm.xfinity.com/myaccount/reset?execution=e1s6",
                                                "virtual_url": "https://idm.xfinity.com/myaccount/reset?execution=e1s7",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 31,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13360199983260000,
                                                "page_transition": "RELOAD",
                                                "title": "Sign in to Xfinity",
                                                "timestamp_msec": 1715726383260,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://idm.xfinity.com/myaccount/reset?execution=e1s7",
                                                "virtual_url": "https://login.xfinity.com/login?r=comcast.net&s=oauth&continue=https%3A%2F%2Foauth.xfinity.com%2F%2Foauth%2Fauthorize%3Fclient_id%3Dmy-account-web%26prompt%3Dlogin%26redirect_uri%3Dhttps%253A%252F%252Fcustomer.xfinity.com%252Foauth%252Fcallback%26response_type%3Dcode%26state%3Dhttps%253A%252F%252Fcustomer.xfinity.com%252F%2523%252Fbilling%252Fbrite%26response%3D1%26reqId%3Df3c7e844-59d3-49a2-84bc-ba25774378fc&forceAuthn=1&client_id=my-account-web&reqId=0bab6959-8f0b-490a-83f5-4df411e57826&rm=2&ui_style=light&cima_tsig_token=cima_cid%3DLBmTgmiHvrZp9QwR%252FrQVwmHnk%252FA%253D%26cima_dsig%3D%252BW3Tg5i5pzW9l%252B90dL1Q14hbzW4%253D%26cima_nonce%3D5f3e0ffa-a353-4d73-a0d1-c8efaa5af256%26cima_ts%3D1715279689%26cima_uid%3Dajj4xe%2540comcast.net",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 32,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13360199983260000,
                                                "page_transition": "RELOAD",
                                                "title": "Sign in to Xfinity",
                                                "timestamp_msec": 1715726383260,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://login.xfinity.com/login?r=comcast.net&s=oauth&continue=https%3A%2F%2Foauth.xfinity.com%2F%2Foauth%2Fauthorize%3Fclient_id%3Dmy-account-web%26prompt%3Dlogin%26redirect_uri%3Dhttps%253A%252F%252Fcustomer.xfinity.com%252Foauth%252Fcallback%26response_type%3Dcode%26state%3Dhttps%253A%252F%252Fcustomer.xfinity.com%252F%2523%252Fbilling%252Fbrite%26response%3D1%26reqId%3Df3c7e844-59d3-49a2-84bc-ba25774378fc&forceAuthn=1&client_id=my-account-web&reqId=0bab6959-8f0b-490a-83f5-4df411e57826&rm=2&ui_style=light&cima_tsig_token=cima_cid%3DLBmTgmiHvrZp9QwR%252FrQVwmHnk%252FA%253D%26cima_dsig%3D%252BW3Tg5i5pzW9l%252B90dL1Q14hbzW4%253D%26cima_nonce%3D5f3e0ffa-a353-4d73-a0d1-c8efaa5af256%26cima_ts%3D1715279689%26cima_uid%3Dajj4xe%2540comcast.net",
                                                "virtual_url": "https://login.xfinity.com/login",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 33,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13360199993904000,
                                                "page_transition": "RELOAD",
                                                "title": "XFINITY | My Account | EcoBill® Online Bill Pay",
                                                "timestamp_msec": 1715726393904,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://customer.xfinity.com/#/billing/brite",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 34,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13360199998828000,
                                                "page_transition": "RELOAD",
                                                "title": "Sign in to Xfinity",
                                                "timestamp_msec": 1715726398828,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://customer.xfinity.com/",
                                                "virtual_url": "https://login.xfinity.com/login?c_ds_na=c_ds_na%2Cc_ds_no%2Cc_ds_ts%2Cclient_id%2Ccontinue%2CforceAuthn%2Cr%2CreqId%2Cs&c_ds_no=D43F18E082BD1EB4AACEF67C5C555BA2&c_ds_ts=1715726398&c_ds_val=96BAE3B598BA2DD13FFCB29E7239EF01D3085364F9F7771AB6819931896E5F2C&client_id=my-account-web&continue=https%3A%2F%2Foauth.xfinity.com%2F%2Foauth%2Fauthorize%3Fclient_id%3Dmy-account-web%26prompt%3Dlogin%26redirect_uri%3Dhttps%253A%252F%252Fcustomer.xfinity.com%252Foauth%252Fcallback%26response_type%3Dcode%26state%3Dhttps%253A%252F%252Fcustomer.xfinity.com%252F%2523%252Fbilling%252Fbrite%26response%3D1%26reqId%3D5fed0f5e-28a2-451b-b8ac-67ccfdcc097e&forceAuthn=1&r=comcast.net&reqId=9db5dda2-0703-4b49-9463-076f70d471a2&s=oauth",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1715726383330,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 24,
            "tab": {
                        "current_navigation_index": 1,
                        "tab_id": 123414901,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 98,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372559464862000,
                                                "page_transition": "RELOAD",
                                                "title": "Career Destination | Untapped",
                                                "timestamp_msec": 1728085864862,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://www.untapped.io/app/jobs/36b15740-8ee2-4fb2-90fb-755e9a0c0b40/apply?ref=email&utm_source=untapped-esp&utm_medium=email-operational&utm_campaign=Email+%231&utm_content=ctabutton&email=ykc3hp%40virginia.edu&ats_account_link_token=j8KuNX8lsjUvNRgLuSJPcnPmtNJlyjQp&student_full_name=Ryan+Steele&logo_url=https%3A%2F%2Fjumpstart-static.s3.amazonaws.com%2Fbackend%2F__sized__%2Forganizations%2Forganization%2Fz_0v7b8HS3qy4r1ceLDeEQ-thumbnail-200x200.png&organization_id=whatnot&organization_name=Whatnot&role_id=36b15740-8ee2-4fb2-90fb-755e9a0c0b40&role_type=JOB&role_title=Software+Engineer+Intern%2C+Summer+2025",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 99,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372559464862000,
                                                "page_transition": "RELOAD",
                                                "title": "Sign Up | Untapped",
                                                "timestamp_msec": 1728085864862,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.untapped.io/app/jobs/36b15740-8ee2-4fb2-90fb-755e9a0c0b40/apply?ref=email&utm_source=untapped-esp&utm_medium=email-operational&utm_campaign=Email+%231&utm_content=ctabutton&email=ykc3hp%40virginia.edu&ats_account_link_token=j8KuNX8lsjUvNRgLuSJPcnPmtNJlyjQp&student_full_name=Ryan+Steele&logo_url=https%3A%2F%2Fjumpstart-static.s3.amazonaws.com%2Fbackend%2F__sized__%2Forganizations%2Forganization%2Fz_0v7b8HS3qy4r1ceLDeEQ-thumbnail-200x200.png&organization_id=whatnot&organization_name=Whatnot&role_id=36b15740-8ee2-4fb2-90fb-755e9a0c0b40&role_type=JOB&role_title=Software+Engineer+Intern%2C+Summer+2025",
                                                "virtual_url": "https://www.untapped.io/app/join/CANDIDATE",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1728085864927,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 39,
            "tab": {
                        "current_navigation_index": 3,
                        "tab_id": 123416040,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 136,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13376959411198000,
                                                "page_transition": "RELOAD",
                                                "title": "Ticketmaster Sign In",
                                                "timestamp_msec": 1732485811198,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://auth.ticketmaster.com/as/authorization.oauth2?client_id=8bf7204a7e97.web.ticketmaster.us&response_type=code&scope=openid%20profile%20phone%20email%20tm&redirect_uri=https://identity.ticketmaster.com/exchange&visualPresets=tm&lang=en-us&placementId=myAccount&showHeader=true&hideLeftPanel=False&integratorId=prd283.myAccount&intSiteToken=tm-us&TMUO=west_Fe7SODOCjonCFPMHZ60v7wKr0Jc3tyf0lV0Ro5lc5Pw%3D&deviceId=DuLb04fBxrG3s7SzsbOxsbm5s7iRdgTCZMtfEw&doNotTrack=False",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 137,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13376959411198000,
                                                "page_transition": "RELOAD",
                                                "title": "Transfer Accept",
                                                "timestamp_msec": 1732485811198,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://auth.ticketmaster.com/as/authorization.oauth2?client_id=8bf7204a7e97.web.ticketmaster.us&response_type=code&scope=openid%20profile%20phone%20email%20tm&redirect_uri=https://identity.ticketmaster.com/exchange&visualPresets=tm&lang=en-us&placementId=myAccount&showHeader=true&hideLeftPanel=False&integratorId=prd283.myAccount&intSiteToken=tm-us&TMUO=west_Fe7SODOCjonCFPMHZ60v7wKr0Jc3tyf0lV0Ro5lc5Pw%3D&deviceId=DuLb04fBxrG3s7SzsbOxsbm5s7iRdgTCZMtfEw&doNotTrack=False",
                                                "virtual_url": "https://my.ticketmaster.com/transfer/accept?v=CQzPVEeC4Fq5LtdbPRdK3O9UuzcXHHw5erdwpnZ3gvaUhrHQSlieghIljKFqFKgooAyM_90-PcUNEq81_jn62CrQgqjQz7GNN1L9giGVyca_kZ7mYaGDerDv-QLxD6Kaw0qFve-2-xn943ViseQmSOqpuZc5AoLwDkuJsKc&lang=en-us&wt.mc_id=EML_TMNT767759_6634590_0%5BPP_Accept_Ticket&et_cid=TM_767759&et_rid=&efeat_seg=0&utm_source=sfmc&utm_medium=tmemail&utm_campaign=PP_XferRec_Email_NEMSv2.1_v01.5_Prod&utm_term=767759&utm_content=PP_Accept_Ticket&j=767759&l=21_HTML&sfmc_sub=733864742&jb=6634590&mid=7222895&landing=c",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 138,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13376959411198000,
                                                "page_transition": "RELOAD",
                                                "title": "Orders",
                                                "timestamp_msec": 1732485811198,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://my.ticketmaster.com/transfer/accept?v=CQzPVEeC4Fq5LtdbPRdK3O9UuzcXHHw5erdwpnZ3gvaUhrHQSlieghIljKFqFKgooAyM_90-PcUNEq81_jn62CrQgqjQz7GNN1L9giGVyca_kZ7mYaGDerDv-QLxD6Kaw0qFve-2-xn943ViseQmSOqpuZc5AoLwDkuJsKc&lang=en-us&wt.mc_id=EML_TMNT767759_6634590_0%5BPP_Accept_Ticket&et_cid=TM_767759&et_rid=&efeat_seg=0&utm_source=sfmc&utm_medium=tmemail&utm_campaign=PP_XferRec_Email_NEMSv2.1_v01.5_Prod&utm_term=767759&utm_content=PP_Accept_Ticket&j=767759&l=21_HTML&sfmc_sub=733864742&jb=6634590&mid=7222895&landing=c",
                                                "virtual_url": "https://my.ticketmaster.com/order/Z7IVgZOxvZ16ke976v4/view",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 139,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13376959411198000,
                                                "page_transition": "RELOAD",
                                                "title": "Orders",
                                                "timestamp_msec": 1732485811198,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://my.ticketmaster.com/order/Z7IVgZOxvZ16ke976v4/view",
                                                "virtual_url": "https://my.ticketmaster.com/order/Z7IVgZOxvZ16ke976v4/tickets?eventId=3B006158C64B1D76",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1732485811244,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 6,
            "tab": {
                        "current_navigation_index": 6,
                        "tab_id": 123413569,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 38,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13361280087427000,
                                                "page_transition": "RELOAD",
                                                "title": "Condor Online Check-in",
                                                "timestamp_msec": 1716806487427,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.condor.com/oci/en-EU/nationality",
                                                "virtual_url": "https://www.condor.com/oci/en-EU/passenger-details",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 39,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13361280087427000,
                                                "page_transition": "RELOAD",
                                                "title": "",
                                                "timestamp_msec": 1716806487427,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.condor.com/oci/en-EU/passenger-details",
                                                "virtual_url": "https://www.condor.com/oci/en-EU/passenger-details",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 40,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13361280087427000,
                                                "page_transition": "RELOAD",
                                                "title": "",
                                                "timestamp_msec": 1716806487427,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.condor.com/oci/en-EU/passenger-details",
                                                "virtual_url": "https://www.condor.com/oci/en-EU/dangerous-goods",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 41,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13361280087427000,
                                                "page_transition": "RELOAD",
                                                "title": "",
                                                "timestamp_msec": 1716806487427,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.condor.com/oci/en-EU/dangerous-goods",
                                                "virtual_url": "https://www.condor.com/oci/en-EU/regulatoryRequirements",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 42,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13361280087427000,
                                                "page_transition": "RELOAD",
                                                "title": "",
                                                "timestamp_msec": 1716806487427,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.condor.com/oci/en-EU/regulatoryRequirements",
                                                "virtual_url": "https://www.condor.com/oci/en-EU/passenger-review",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 43,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13361280087427000,
                                                "page_transition": "RELOAD",
                                                "title": "Condor Online Check-in",
                                                "timestamp_msec": 1716806487427,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.condor.com/oci/en-EU/passenger-review",
                                                "virtual_url": "https://www.condor.com/oci/en-EU/confirmation",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 44,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13361280096019000,
                                                "page_transition": "RELOAD",
                                                "title": "",
                                                "timestamp_msec": 1716806496019,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.condor.com/oci/en-EU/confirmation",
                                                "virtual_url": "https://www.condor.com/oci/en-EU/search",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1716806487469,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 22,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123414792,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 96,
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13372284376425000,
                                    "page_transition": "RELOAD",
                                    "title": "Education Abroad in Your Major or Minor | Educati\u2026",
                                    "timestamp_msec": 1727810776425,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "",
                                    "virtual_url": "https://educationabroad.virginia.edu/education-abroad-your-major-or-minor",
                                    "correct_referrer_policy": 1,
                                    "navigation_home_page": False
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1727810775990,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 45,
            "tab": {
                        "current_navigation_index": 1,
                        "tab_id": 123417064,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 13,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13382547367121000,
                                                "page_transition": "RELOAD",
                                                "title": "Tracking | UPS - United States",
                                                "timestamp_msec": 1738073767121,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://www.ups.com/track?loc=en_US&Requester=SBN&tracknum=1Z4051V00399182059&AgreeToTermsAndConditions=yes&WT.z_eCTAid=ct1_eml_Tracking__ct1_eml_tra_eml_auto_missed_delivery&WT.z_edatesent=01162025",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 14,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13382547367121000,
                                                "page_transition": "RELOAD",
                                                "title": "Tracking | UPS - United States",
                                                "timestamp_msec": 1738073767121,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.ups.com/track?loc=en_US&Requester=SBN&tracknum=1Z4051V00399182059&AgreeToTermsAndConditions=yes&WT.z_eCTAid=ct1_eml_Tracking__ct1_eml_tra_eml_auto_missed_delivery&WT.z_edatesent=01162025",
                                                "virtual_url": "https://www.ups.com/track?loc=en_US&Requester=SBN&tracknum=1Z4051V00399182059&AgreeToTermsAndConditions=yes&WT.z_eCTAid=ct1_eml_Tracking__ct1_eml_tra_eml_auto_missed_delivery&WT.z_edatesent=01162025/trackdetails",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1738073767173,
                        "window_id": 123417370,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 21,
            "tab": {
                        "current_navigation_index": 4,
                        "tab_id": 123414730,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 91,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372284374923000,
                                                "page_transition": "RELOAD",
                                                "title": "Join meeting - Zoom",
                                                "timestamp_msec": 1727810774923,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://virginia.zoom.us/j/97016206234?pwd=mHz1XU3tiFpVj4sxaV0EQ0V5zUJ9IM.1",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 92,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372284374923000,
                                                "page_transition": "RELOAD",
                                                "title": "Zoom meeting on web - Zoom",
                                                "timestamp_msec": 1727810774923,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://virginia.zoom.us/j/97016206234?pwd=mHz1XU3tiFpVj4sxaV0EQ0V5zUJ9IM.1",
                                                "virtual_url": "https://virginia.zoom.us/wc/97016206234/join?fromPWA=1&wpk=wcpk%7B0%7D%26%26%26%26wcpke654ebef1cd9ec028a38ae70b0da817b&_x_zm_rtaid=pdWfbmC1QZma11qN6oKxBg.1727810330808.3ad01db7bba9dea92188bc9a8f7312f6&_x_zm_rhtaid=287",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 93,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372284374923000,
                                                "page_transition": "RELOAD",
                                                "title": "Sign In | Zoom",
                                                "timestamp_msec": 1727810774923,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://virginia.zoom.us/wc/97016206234/join?fromPWA=1&wpk=wcpk%7B0%7D%26%26%26%26wcpke654ebef1cd9ec028a38ae70b0da817b&_x_zm_rtaid=pdWfbmC1QZma11qN6oKxBg.1727810330808.3ad01db7bba9dea92188bc9a8f7312f6&_x_zm_rhtaid=287",
                                                "virtual_url": "https://zoom.us/signin#/login",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 94,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372284374923000,
                                                "page_transition": "RELOAD",
                                                "title": "NetBadge",
                                                "timestamp_msec": 1727810774923,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s1",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 95,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372284374923000,
                                                "page_transition": "RELOAD",
                                                "title": "NetBadge Message",
                                                "timestamp_msec": 1727810774923,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s1",
                                                "virtual_url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s1",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1727810774993,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 2,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123413352,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 26,
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13359522215660000,
                                    "page_transition": "RELOAD",
                                    "title": "Important Message Postal Service",
                                    "timestamp_msec": 1715048615660,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "",
                                    "virtual_url": "https://docs.google.com/forms/d/e/1FAIpQLScFCFw3zWZrFbE7sAgXttiYO97FpxuNDM9IA0zm2k54fhPiOQ/closedform",
                                    "correct_referrer_policy": 1,
                                    "navigation_home_page": False
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1715048615709,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 23,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123414842,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 97,
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13372483643328000,
                                    "page_transition": "RELOAD",
                                    "title": "Programs-Brochure-International Studies Office",
                                    "timestamp_msec": 1728010043328,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "",
                                    "virtual_url": "https://apps.educationabroad.virginia.edu/index.cfm?FuseAction=Programs.ViewProgram&Program_ID=10050",
                                    "correct_referrer_policy": 1,
                                    "navigation_home_page": False
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1728010043367,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 42,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123416469,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 6,
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13381172791231000,
                                    "page_transition": "RELOAD",
                                    "title": "Purdue Global - An Accredited Online University",
                                    "timestamp_msec": 1736699191231,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "",
                                    "virtual_url": "https://www.purdueglobal.edu/?source=SC48413&ve=62296&utm_source=google&utm_medium=display&utm_campaign=pg_demandgen_con_gen-bus-it&utm_content=PG_CON_General_Images&dclid=&wbraid=CloKCQiAjp-7BhDZARJJAJjLeK9BH72Ki3e-QhdVfhQFwhckobC5TjcyDdDPciISyF4wAsk2fFVBCxN8LVqvazrytiYHDG4U_7dNreu1ENrI7wJ-5yigaxoCG4g",
                                    "correct_referrer_policy": 1,
                                    "navigation_home_page": False
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1736699191299,
                        "window_id": 123417370,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 9,
            "tab": {
                        "current_navigation_index": 5,
                        "tab_id": 123413719,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 56,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13363741162452000,
                                                "page_transition": "RELOAD",
                                                "title": "SUMMER I 2024 WEEKEND LOCATION FORM",
                                                "timestamp_msec": 1719267562452,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://docs.google.com/forms/d/e/1FAIpQLSfJAFy6pC94QTfbI3cz75SBzq12nuJc5nQWXzy-GZ5sJEm1MQ/viewform?usp=send_form",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 57,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13363741162452000,
                                                "page_transition": "RELOAD",
                                                "title": "SUMMER I 2024 WEEKEND LOCATION FORM",
                                                "timestamp_msec": 1719267562452,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://docs.google.com/forms/d/e/1FAIpQLSfJAFy6pC94QTfbI3cz75SBzq12nuJc5nQWXzy-GZ5sJEm1MQ/viewform?fbzx=-7025329500242433050",
                                                "virtual_url": "https://docs.google.com/forms/d/e/1FAIpQLSfJAFy6pC94QTfbI3cz75SBzq12nuJc5nQWXzy-GZ5sJEm1MQ/formResponse",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 58,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13363741162452000,
                                                "page_transition": "RELOAD",
                                                "title": "SUMMER I 2024 WEEKEND LOCATION FORM",
                                                "timestamp_msec": 1719267562452,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://docs.google.com/forms/d/e/1FAIpQLSfJAFy6pC94QTfbI3cz75SBzq12nuJc5nQWXzy-GZ5sJEm1MQ/formResponse",
                                                "virtual_url": "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfJAFy6pC94QTfbI3cz75SBzq12nuJc5nQWXzy-GZ5sJEm1MQ/formResponse",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 59,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13363741162452000,
                                                "page_transition": "RELOAD",
                                                "title": "best atm in florence - Google Search",
                                                "timestamp_msec": 1719267562452,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfJAFy6pC94QTfbI3cz75SBzq12nuJc5nQWXzy-GZ5sJEm1MQ/formResponse",
                                                "virtual_url": "https://www.google.com/search?q=best+atm+in+florence&rlz=1CDGOYI_enUS976US998&oq=best+atm+in+florence&gs_lcrp=EgZjaHJvbWUqCQgAEAAYExiABDIJCAAQABgTGIAEMgoIARAAGBMYFhgeMgoIAhAAGBMYFhgeMgcIAxAhGJ8FMgcIBBAhGJ8FMgcIBRAhGJ8F0gEINjM4OGowajSoAhOwAgHiAwQYASBf&hl=en-US&sourceid=chrome-mobile&ie=UTF-8",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 60,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13363741162452000,
                                                "page_transition": "RELOAD",
                                                "title": "indoor cash withdrawal atm in florence - Google S\u2026",
                                                "timestamp_msec": 1719267562452,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.google.com/search?q=best+atm+in+florence&rlz=1CDGOYI_enUS976US998&oq=best+atm+in+florence&gs_lcrp=EgZjaHJvbWUqCQgAEAAYExiABDIJCAAQABgTGIAEMgoIARAAGBMYFhgeMgoIAhAAGBMYFhgeMgcIAxAhGJ8FMgcIBBAhGJ8FMgcIBRAhGJ8F0gEINjM4OGowajSoAhOwAgHiAwQYASBf&hl=en-US&sourceid=chrome-mobile&ie=UTF-8",
                                                "virtual_url": "https://www.google.com/search?q=indoor+cash+withdrawl+atm+in+flirence&sca_esv=3fd026c1a73d8e9b&rlz=1CDGOYI_enUS976US998&hl=en-US&sxsrf=ADLYWIKlyovk5EraeXxxEfVtz2pQ23yH2A%3A1718353976377&ei=OABsZvO6E9SZi-gP75Gx8Ag&oq=indoor+cash+withdrawl+atm+in+flirence&gs_lp=EhNtb2JpbGUtZ3dzLXdpei1zZXJwIiVpbmRvb3IgY2FzaCB3aXRoZHJhd2wgYXRtIGluIGZsaXJlbmNlMgcQIRigARgKMgcQIRigARgKSIZVULEPWK9TcAR4AZABAJgBfqABlRyqAQUyMy4xNLgBA8gBAPgBAZgCKKAC7hyoAg_CAgoQABiwAxjWBBhHwgIHECMYJxjqAsICChAjGIAEGCcYigXCAgQQIxgnwgILEAAYgAQYkQIYigXCAgoQLhiABBhDGIoFwgIKEAAYgAQYQxiKBcICBRAAGIAEwgIQEC4YgAQY0QMYQxjHARiKBcICFBAuGIAEGJECGMcBGIoFGI4FGK8BwgIIEAAYgAQYkgPCAg0QABiABBhDGMkDGIoFwgIHEAAYgAQYCsICDRAuGIAEGMcBGAoYrwHCAggQABgWGAoYHsICBhAAGBYYHsICCxAAGIAEGIYDGIoFwgIFECEYoAHCAgUQIRifBcICBBAhGArCAgYQIRgVGArCAgUQIRiSA5gDCIgGAZAGCJIHBTI1LjE1oAfpgQI&sclient=mobile-gws-wiz-serp",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 61,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13363741162452000,
                                                "page_transition": "RELOAD",
                                                "title": "can you make a withdrawal from any banks atm - Go\u2026",
                                                "timestamp_msec": 1719267562452,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.google.com/search?q=indoor+cash+withdrawl+atm+in+flirence&sca_esv=3fd026c1a73d8e9b&rlz=1CDGOYI_enUS976US998&hl=en-US&sxsrf=ADLYWIKlyovk5EraeXxxEfVtz2pQ23yH2A%3A1718353976377&ei=OABsZvO6E9SZi-gP75Gx8Ag&oq=indoor+cash+withdrawl+atm+in+flirence&gs_lp=EhNtb2JpbGUtZ3dzLXdpei1zZXJwIiVpbmRvb3IgY2FzaCB3aXRoZHJhd2wgYXRtIGluIGZsaXJlbmNlMgcQIRigARgKMgcQIRigARgKSIZVULEPWK9TcAR4AZABAJgBfqABlRyqAQUyMy4xNLgBA8gBAPgBAZgCKKAC7hyoAg_CAgoQABiwAxjWBBhHwgIHECMYJxjqAsICChAjGIAEGCcYigXCAgQQIxgnwgILEAAYgAQYkQIYigXCAgoQLhiABBhDGIoFwgIKEAAYgAQYQxiKBcICBRAAGIAEwgIQEC4YgAQY0QMYQxjHARiKBcICFBAuGIAEGJECGMcBGIoFGI4FGK8BwgIIEAAYgAQYkgPCAg0QABiABBhDGMkDGIoFwgIHEAAYgAQYCsICDRAuGIAEGMcBGAoYrwHCAggQABgWGAoYHsICBhAAGBYYHsICCxAAGIAEGIYDGIoFwgIFECEYoAHCAgUQIRifBcICBBAhGArCAgYQIRgVGArCAgUQIRiSA5gDCIgGAZAGCJIHBTI1LjE1oAfpgQI&sclient=mobile-gws-wiz-serp",
                                                "virtual_url": "https://www.google.com/search?q=can+you+make+a+withdrawal+from+any+banks+atm&rlz=1CDGOYI_enUS976US998&oq=can+you+make+a+withdrawal+from+any+banks+atm&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yDQgCEAAYhgMYgAQYigUyDQgDEAAYhgMYgAQYigUyDQgEEAAYhgMYgAQYigUyDQgFEAAYhgMYgAQYigUyDQgGEAAYhgMYgAQYigUyBwgHECEYoAEyBwgIECEYoAEyBwgJECEYoAHSAQg5OTMyajBqOagCE7ACAeIDBBgBIF8&hl=en-US&sourceid=chrome-mobile&ie=UTF-8",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1719267562524,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 31,
            "tab": {
                        "current_navigation_index": 3,
                        "tab_id": 123415368,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 118,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374678683579000,
                                                "page_transition": "RELOAD",
                                                "title": "Free Piano Masterclass by Stephen Ridley",
                                                "timestamp_msec": 1730205083579,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://go.masterclass-piano.com/free-masterclass-piano-giveway-a?gc_id=20148695203&h_ad_id=715805256915&wbraid=ClkKCAjw7Py4BhAqEkkA8OBQP0DjD19ZrvIQF6GaWMun3VuhAOYM467sMULs_bfNn7KeKOjE0HRFVROP8rlRe5eoCQuhzLARHjvb9LbfRJn1l3bLSTSmGgJe6Q",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 119,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374678683579000,
                                                "page_transition": "RELOAD",
                                                "title": "mater class - Google Search",
                                                "timestamp_msec": 1730205083579,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://go.masterclass-piano.com/free-masterclass-piano-giveway-a?gc_id=20148695203&h_ad_id=715805256915&wbraid=ClkKCAjw7Py4BhAqEkkA8OBQP0DjD19ZrvIQF6GaWMun3VuhAOYM467sMULs_bfNn7KeKOjE0HRFVROP8rlRe5eoCQuhzLARHjvb9LbfRJn1l3bLSTSmGgJe6Q",
                                                "virtual_url": "https://www.google.com/search?q=mater+class&rlz=1CDGOYI_enUS976US998&oq=mater+class&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQABgKGLEDGIAEMgYIAhAFGEAyDAgDEAAYChixAxiABDIMCAQQLhgKGLEDGIAEMgkIBRAAGAoYgAQyDAgGEAAYChixAxiABDIJCAcQABgKGIAEMgkICBAAGAoYgAQyCQgJEAAYChiABNIBCDIwNjFqMGo0qAITsAIB4gMEGAEgXw&hl=en-US&sourceid=chrome-mobile&ie=UTF-8",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 120,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374678683579000,
                                                "page_transition": "RELOAD",
                                                "title": "MasterClass Online Classes",
                                                "timestamp_msec": 1730205083579,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.google.com/search?q=mater+class&rlz=1CDGOYI_enUS976US998&oq=mater+class&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQABgKGLEDGIAEMgYIAhAFGEAyDAgDEAAYChixAxiABDIMCAQQLhgKGLEDGIAEMgkIBRAAGAoYgAQyDAgGEAAYChixAxiABDIJCAcQABgKGIAEMgkICBAAGAoYgAQyCQgJEAAYChiABNIBCDIwNjFqMGo0qAITsAIB4gMEGAEgXw&hl=en-US&sourceid=chrome-mobile&ie=UTF-8",
                                                "virtual_url": "https://www.masterclass.com/?&campaignid=20654081747&adgroupid=160260243731&adid=710854529245&utm_term=masterclass&utm_campaign=%5BMC%5D+%7C+Search+%7C+Brand+%7C+Keywords_Consolidated_EM_PM_BM+%7C+ROW_US+%7C+EN+%7C+MAX+%7C+EG&utm_source=google&utm_medium=search&utm_content=710854529245&hsa_acc=9801000675&hsa_cam=16376419640&hsa_grp=160260243731&hsa_ad=710854529245&hsa_src=g&hsa_tgt=kwd-66880027&hsa_kw=masterclass&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gbraid=0AAAAADjLLoGorLVOu9BdHu179AVc7Fpw5&gclid=Cj0KCQjw7Py4BhCbARIsAMMx-_IzDL3lcxEkZ0tcqrvWFYRWGPJgedj0DwQE2ohk4Z7Nixv16XLy8mAaAvz5EALw_wcB&gclsrc=aw.ds",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 121,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374678683579000,
                                                "page_transition": "RELOAD",
                                                "title": "MasterClass Online Classes",
                                                "timestamp_msec": 1730205083579,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.masterclass.com/?&campaignid=20654081747&adgroupid=160260243731&adid=710854529245&utm_term=masterclass&utm_campaign=%5BMC%5D+%7C+Search+%7C+Brand+%7C+Keywords_Consolidated_EM_PM_BM+%7C+ROW_US+%7C+EN+%7C+MAX+%7C+EG&utm_source=google&utm_medium=search&utm_content=710854529245&hsa_acc=9801000675&hsa_cam=16376419640&hsa_grp=160260243731&hsa_ad=710854529245&hsa_src=g&hsa_tgt=kwd-66880027&hsa_kw=masterclass&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gbraid=0AAAAADjLLoGorLVOu9BdHu179AVc7Fpw5&gclid=Cj0KCQjw7Py4BhCbARIsAMMx-_IzDL3lcxEkZ0tcqrvWFYRWGPJgedj0DwQE2ohk4Z7Nixv16XLy8mAaAvz5EALw_wcB&gclsrc=aw.ds",
                                                "virtual_url": "https://www.masterclass.com/find-my-classes?categories=315&wq=t",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1730205083639,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 27,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123415184,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 110,
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13372817668817000,
                                    "page_transition": "RELOAD",
                                    "title": "DoorDash Support",
                                    "timestamp_msec": 1728344068817,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "",
                                    "virtual_url": "https://help.doordash.com/s/?language=en_US",
                                    "correct_referrer_policy": 1,
                                    "navigation_home_page": False
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1728344068886,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 14,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123414097,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 68,
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13365273852732000,
                                    "page_transition": "RELOAD",
                                    "title": "",
                                    "timestamp_msec": 1720800252732,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "",
                                    "virtual_url": "https://mfb-fb-pdf-prod.s3.eu-central-1.amazonaws.com/3440e8nc8z8f6ba78orndeedetv4ng43rn446b211wdva2qf0k/Ticket-Dubrovnik-Split-3172778160.pdf",
                                    "correct_referrer_policy": 1,
                                    "navigation_home_page": False
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1720800252784,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 18,
            "tab": {
                        "current_navigation_index": 6,
                        "tab_id": 123414483,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 77,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13371950367686000,
                                                "page_transition": "RELOAD",
                                                "title": "NetBadge",
                                                "timestamp_msec": 1727476767686,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://www.mathworks.com/login?uri=https%3A%2F%2Fgrader.mathworks.com%2Fcourses%2F150999-fall-2024-apma-3080-linear-algebra-projects-all-sections%2Fview%2F83Tzn2lLYwLclAO7Eh4BWzcII_Si8J8p4xaINZ2w68g",
                                                "virtual_url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s1",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 78,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13371950367686000,
                                                "page_transition": "RELOAD",
                                                "title": "Duo Security - Two-Factor Authentication",
                                                "timestamp_msec": 1727476767686,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s1",
                                                "virtual_url": "https://api-58663eb0.duosecurity.com/frame/frameless/v4/auth?sid=frameless-7db4eae0-736f-4a2c-a5f5-578b6e442829&tx=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJkdW9fdW5hbWUiOiJ5a2MzaHAiLCJzY29wZSI6Im9wZW5pZCIsInJlc3BvbnNlX3R5cGUiOiJjb2RlIiwicmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly9zaGliaWRwLml0cy52aXJnaW5pYS5lZHUvaWRwL3Byb2ZpbGUvQXV0aG4vRHVvLzJGQS9kdW8tY2FsbGJhY2siLCJzdGF0ZSI6ImIxZDkzMmFkYTQwZDFkNTAzZTJhZGY3NWJjNDQyZWI2LjY1MzI3MzMyIiwiZXhwIjoxNzI2ODA3OTIwLCJjbGllbnRfaWQiOiJESU41WkpQR0JWRzRRWTRGSVZHUSJ9.tU85CURbHUZpxpREBC831tlqY3sRRtThlA2oTa3r0-4h52MjN-9f2s5lt5Gd3typFy1fektZF-opngzMLU4mAw&req-trace-group=f0c352eac894753356e6c683",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 79,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13371950367686000,
                                                "page_transition": "RELOAD",
                                                "title": "Duo Security",
                                                "timestamp_msec": 1727476767686,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://api-58663eb0.duosecurity.com/frame/frameless/v4/auth?sid=frameless-7db4eae0-736f-4a2c-a5f5-578b6e442829&tx=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJkdW9fdW5hbWUiOiJ5a2MzaHAiLCJzY29wZSI6Im9wZW5pZCIsInJlc3BvbnNlX3R5cGUiOiJjb2RlIiwicmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly9zaGliaWRwLml0cy52aXJnaW5pYS5lZHUvaWRwL3Byb2ZpbGUvQXV0aG4vRHVvLzJGQS9kdW8tY2FsbGJhY2siLCJzdGF0ZSI6ImIxZDkzMmFkYTQwZDFkNTAzZTJhZGY3NWJjNDQyZWI2LjY1MzI3MzMyIiwiZXhwIjoxNzI2ODA3OTIwLCJjbGllbnRfaWQiOiJESU41WkpQR0JWRzRRWTRGSVZHUSJ9.tU85CURbHUZpxpREBC831tlqY3sRRtThlA2oTa3r0-4h52MjN-9f2s5lt5Gd3typFy1fektZF-opngzMLU4mAw&req-trace-group=f0c352eac894753356e6c683",
                                                "virtual_url": "https://api-58663eb0.duosecurity.com/frame/v4/auth/prompt?sid=frameless-7db4eae0-736f-4a2c-a5f5-578b6e442829",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 80,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13371950367686000,
                                                "page_transition": "RELOAD",
                                                "title": "NetBadge Reminder",
                                                "timestamp_msec": 1727476767686,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://api-58663eb0.duosecurity.com/frame/v4/auth/prompt?sid=frameless-7db4eae0-736f-4a2c-a5f5-578b6e442829",
                                                "virtual_url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s3",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 81,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13371950367686000,
                                                "page_transition": "RELOAD",
                                                "title": "MATLAB Grader",
                                                "timestamp_msec": 1727476767686,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e2s3",
                                                "virtual_url": "https://grader.mathworks.com/courses/150999-fall-2024-apma-3080-linear-algebra-projects-all-sections",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 82,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13371950367686000,
                                                "page_transition": "RELOAD",
                                                "title": "MATLAB Grader",
                                                "timestamp_msec": 1727476767686,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://grader.mathworks.com/courses/150999-fall-2024-apma-3080-linear-algebra-projects-all-sections",
                                                "virtual_url": "https://grader.mathworks.com/",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 83,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13371950367686000,
                                                "page_transition": "RELOAD",
                                                "title": "MATLAB Grader",
                                                "timestamp_msec": 1727476767686,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://grader.mathworks.com/",
                                                "virtual_url": "https://grader.mathworks.com/courses/150999",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1727476767734,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 32,
            "tab": {
                        "current_navigation_index": 2,
                        "tab_id": 123415493,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 122,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374678684941000,
                                                "page_transition": "RELOAD",
                                                "title": "Sign in or Register | eBay",
                                                "timestamp_msec": 1730205084941,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Forder.ebay.com%2Ford%2Fshow%3FitemId%3D235793133625%26transactionId%3D2204552407013%26mkpid%3D0%26emsid%3De11400.m144671.l152966%26mkcid%3D7%26ch%3Dosgood%26euid%3D1f3a1c98aaad47359aa60fa24e324d18%26bu%3D45329030891%26exe%3D0%26ext%3D0%26osub%3D-1%257E1%26crd%3D20241028111656%26segname%3D11400&sgfl=sm&smuid=9cc027b5cbdb4f07bc29e146cca0498c",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 123,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374678692235000,
                                                "page_transition": "RELOAD",
                                                "title": "eBay",
                                                "timestamp_msec": 1730205092235,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://signin.ebay.com/",
                                                "virtual_url": "https://accounts.ebay.com/acctsec/authn-register?srt=AQAJAAABAP46q9XIOPYRAKRN17PhSGeUB7JWaMNzLS5JcjznCpExD2uMFT4KQaATR8ZP-JN6FXv787EX9vfXhpX-kMgLQDbbPSfcxbgG6tTDl50oFGA6BPjbIXi2EPiflaCJK7H5eD03GPziuyYozn4AvFL43_a7M755eAvIuA_YssjOfyDt8tvhc2UPdmyxnfGfx2tc6ZNNtuyapuqtk__eKHC8hZcHvZfj5IESdHwT1VPBvaZcnACWjxdVriYwcQhlt_xn5c1MezWnvQhh0yP5vc7X9aDrWa-u_D-F8SSUCFAJUjpsd-mxrBhrq1PSqgduXJDbATd4IR5SzywuCC2_Fcw_u_Q&ru=https%3A%2F%2Forder.ebay.com%2Ford%2Fshow%3FitemId%3D235793133625%26transactionId%3D2204552407013%26mkpid%3D0%26emsid%3De11400.m144671.l152966%26mkcid%3D7%26ch%3Dosgood%26euid%3D1f3a1c98aaad47359aa60fa24e324d18%26bu%3D45329030891%26exe%3D0%26ext%3D0%26osub%3D-1%257E1%26crd%3D20241028111656%26segname%3D11400",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 124,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374678695818000,
                                                "page_transition": "RELOAD",
                                                "title": "Order details | eBay",
                                                "timestamp_msec": 1730205095818,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://accounts.ebay.com/",
                                                "virtual_url": "https://order.ebay.com/ord/show?itemId=235793133625&transactionId=2204552407013&mkpid=0&emsid=e11400.m144671.l152966&mkcid=7&ch=osgood&euid=1f3a1c98aaad47359aa60fa24e324d18&bu=45329030891&exe=0&ext=0&osub=-1%7E1&crd=20241028111656&segname=11400#/",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1730205083960,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 11,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123413943,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 64,
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13364032515384000,
                                    "page_transition": "RELOAD",
                                    "title": "www.google.com",
                                    "timestamp_msec": 1719558915384,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "",
                                    "virtual_url": "https://www.google.com/url?q=http://ablink.comms.trainline.com/uni/ls/click?upn%3Du001.rq1wXUQ2ffVnSIpB7X2dPPq-2BWUYoCggxX-2F4o8Lzpy4n2tecDPp4JIRzE8GXEJCptaS5g0waRZTGj1FpfLSgem5UzmcSNmSf-2BcGMyIyzrmUS68McVk41FtGmGZTL1ogvEOyGCFETAfKPJxz4LMIqUsF-2BO4dVaRjgTIBkJRiu6I1IszRtipwcRrDT4auf2Yk1puqwSPQggu9JLXJwOiCHrIbBg92D6YDb-2FZAnA8FL9ETEigTLhSg1f7JNOEN1nMm7eSnm-2FZ42MwR0WKaSfUc9o1M8YItd6fe4W57GXZZWsOLf8-2BILr2KloOpzZ4eWgjIpLnPP58PE0XIeBDBzqpY24gtpM2TQs5nH76TP00ux10F1fxUEMm-2BXXlWBdWrgJsDQg-PJd_yYYchzRL67-2B2SzF6lXMxlvD9911LR-2FByVEukodQFugi8yRmmTn8vVMhiLjFeC-2Fg0UK9mN-2B0Su8kkv6ww7r-2FB9IKU1qSs-2FP8ZRtULo4Yh0xccQMIc-2FOs7R9ndGAi-2BVWbDCRjQo8-2FKaOtSms8UMvTLpxM4ome9HinoR0qRNwN4hxEGakRCtfBY-2BbdD-2Bp505l5AaJBD4-2F4-2BL2WHnamlJDNR-2FrHQ2pMK2Dm7ChlaF95CBag3qH8qJf5uwXaCniVlIxwUbVXdc4g2-2B-2Bz1vxu2oyAQbov9XPjkHoDHpweHqnB3Kge1QjvWhv1HlPYxYoPKrqaLKLJprIDamracOw9EvvO0UVhiqdtVdwaEuv8sHmmB4JT3A4JNbWxjWJPCQFP-2FPDDYqcz-2FK-2Ff8l6YWSZdBLplJWz4y91KLQshD43CV-2BOYuXNjQxWDyT5M0t2L6Wj7omTEH4w0eFLxbUJE7c4irShBXyfU8qiyGiOaeg5-2B4xU4BpQBOehEPcOA3PLGdXR-2FnVrejXewff3Y-2F2OXlOCxOl9XmD1Ao0plbDP5cHEyR-2BkMG2Ov2liLUDd2Bit2NFLv-2FDpEITLXv1NgkU2hOJHAe-2FPrAXYSF-2FfbTfIS3WJfiH-2FkWGlaQk6ij-2F7aElPlESRP2ev4226E8g80OafGo52kJZgLgbg1ugYNNzovy4zLNFVQ8EX-2BSQl1ADGITrncGJVZh8Iap0Fn21ykoMF7WnycZWgso1MdMkQBzIZfusThG1Dz1DjU2gv5uzuCp0EJzxHcNStHP&source=gmail&ust=1719642643532000&usg=AOvVaw34XgVHwcNUcw2UxI2s-DO-&rct=i",
                                    "correct_referrer_policy": 1,
                                    "navigation_home_page": False
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1719558715293,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 30,
            "tab": {
                        "current_navigation_index": 3,
                        "tab_id": 123415309,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 114,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374647502684000,
                                                "page_transition": "RELOAD",
                                                "title": "Ticketmaster Sign In",
                                                "timestamp_msec": 1730173902684,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://auth.ticketmaster.com/as/authorization.oauth2?client_id=8bf7204a7e97.web.ticketmaster.us&response_type=code&scope=openid%20profile%20phone%20email%20tm&redirect_uri=https://identity.ticketmaster.com/exchange&visualPresets=tm&lang=en-us&placementId=myAccount&showHeader=true&hideLeftPanel=False&integratorId=prd283.myAccount&intSiteToken=tm-us&TMUO=west_Fe7SODOCjonCFPMHZ60v7wKr0Jc3tyf0lV0Ro5lc5Pw%3D&deviceId=kQ22i5EgsjE3MjgzNDQ4MzM2Mjn%2FUj3be%2FifVg&doNotTrack=False",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 115,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374647502685000,
                                                "page_transition": "RELOAD",
                                                "title": "Transfer Accept",
                                                "timestamp_msec": 1730173902685,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://auth.ticketmaster.com/as/authorization.oauth2?client_id=8bf7204a7e97.web.ticketmaster.us&response_type=code&scope=openid%20profile%20phone%20email%20tm&redirect_uri=https://identity.ticketmaster.com/exchange&visualPresets=tm&lang=en-us&placementId=myAccount&showHeader=true&hideLeftPanel=False&integratorId=prd283.myAccount&intSiteToken=tm-us&TMUO=west_Fe7SODOCjonCFPMHZ60v7wKr0Jc3tyf0lV0Ro5lc5Pw%3D&deviceId=kQ22i5EgsjE3MjgzNDQ4MzM2Mjn%2FUj3be%2FifVg&doNotTrack=False",
                                                "virtual_url": "https://my.ticketmaster.com/transfer/accept?lang=en-us&transferToken=6f9136240e3dccf030fcf84381fb44622ef5e266b9b48dc01287fa7964c651aa85ac43efac030021029adae67d23c0d400b04550f1cc9e4fab2db8a8404948a2e1cf82a85b0462667934f3be2e0b44c1767737b6757b150b29ee288d6303d4f3",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 116,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374647502685000,
                                                "page_transition": "RELOAD",
                                                "title": "Orders",
                                                "timestamp_msec": 1730173902685,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://my.ticketmaster.com/transfer/accept?lang=en-us&transferToken=6f9136240e3dccf030fcf84381fb44622ef5e266b9b48dc01287fa7964c651aa85ac43efac030021029adae67d23c0d400b04550f1cc9e4fab2db8a8404948a2e1cf82a85b0462667934f3be2e0b44c1767737b6757b150b29ee288d6303d4f3",
                                                "virtual_url": "https://my.ticketmaster.com/order/Z7IVgZOxvZ16kZYPPa4/view",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 117,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13374647502685000,
                                                "page_transition": "RELOAD",
                                                "title": "Orders",
                                                "timestamp_msec": 1730173902685,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://my.ticketmaster.com/order/Z7IVgZOxvZ16kZYPPa4/view",
                                                "virtual_url": "https://my.ticketmaster.com/order/Z7IVgZOxvZ16kZYPPa4/tickets?eventId=01006090DA1B5E70",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1730173902759,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 8,
            "tab": {
                        "current_navigation_index": 3,
                        "tab_id": 123413660,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 52,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13362825222182000,
                                                "page_transition": "RELOAD",
                                                "title": "Forgotten password",
                                                "timestamp_msec": 1718351622182,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "http://moodle.isiflorence.org/login/forgot_password.php",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 53,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13362825222182000,
                                                "page_transition": "RELOAD",
                                                "title": "Moodle ISI Florence: Log in to the site",
                                                "timestamp_msec": 1718351622182,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "http://moodle.isiflorence.org/login/forgot_password.php",
                                                "virtual_url": "http://moodle.isiflorence.org/login/index.php",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 54,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13362825222182000,
                                                "page_transition": "RELOAD",
                                                "title": "Moodle ISI Florence: Log in to the site",
                                                "timestamp_msec": 1718351622182,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "http://moodle.isiflorence.org/login/index.php",
                                                "virtual_url": "http://moodle.isiflorence.org/login/index.php",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 55,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13362825222182000,
                                                "page_transition": "RELOAD",
                                                "title": "Moodle ISI Florence: Log in to the site",
                                                "timestamp_msec": 1718351622182,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "http://moodle.isiflorence.org/login/index.php",
                                                "virtual_url": "http://moodle.isiflorence.org/login/index.php",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1718351622248,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 40,
            "tab": {
                        "current_navigation_index": 2,
                        "tab_id": 123416181,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 140,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13377564125147000,
                                                "page_transition": "RELOAD",
                                                "title": "Ticketmaster Sign In",
                                                "timestamp_msec": 1733090525147,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://auth.ticketmaster.com/as/authorization.oauth2?redirect_uri=https%3A%2F%2Fam.ticketmaster.com%2Fmsg%2Fam-sso%3Fdeeplink%3DL21zZy9pbnZpdGVzL2I2cDMyNTc2bjNkcHVnOTBsNDhqMTZtcXFvbzIyaHEyNnBtMGtlNTRxZW0xZHUzYg%3D%3D&response_type=code&lang=en-us&integratorId=NAM&placementId=homepage&visualPresets=msg&hideLeftPanel=true&client_id=4c81b8c6f059.web.msg-msg.us&scope=openid%20profile%20phone%20email%20tm",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 141,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13377564125147000,
                                                "page_transition": "RELOAD",
                                                "title": "Invite Dashboard page | MSG Sports & Entertainment",
                                                "timestamp_msec": 1733090525147,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://auth.ticketmaster.com/as/authorization.oauth2?redirect_uri=https%3A%2F%2Fam.ticketmaster.com%2Fmsg%2Fam-sso%3Fdeeplink%3DL21zZy9pbnZpdGVzL2I2cDMyNTc2bjNkcHVnOTBsNDhqMTZtcXFvbzIyaHEyNnBtMGtlNTRxZW0xZHUzYg%3D%3D&response_type=code&lang=en-us&integratorId=NAM&placementId=homepage&visualPresets=msg&hideLeftPanel=true&client_id=4c81b8c6f059.web.msg-msg.us&scope=openid%20profile%20phone%20email%20tm",
                                                "virtual_url": "https://am.ticketmaster.com/msg/dashboard/invites/b6p32576n3dpug90l48j16mqqoo22hq26pm0ke54qem1du3b",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 142,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13377564125147000,
                                                "page_transition": "RELOAD",
                                                "title": "Ticketmaster Sign In",
                                                "timestamp_msec": 1733090525147,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://am.ticketmaster.com/msg/dashboard/invites/b6p32576n3dpug90l48j16mqqoo22hq26pm0ke54qem1du3b",
                                                "virtual_url": "https://auth.ticketmaster.com/as/authorization.oauth2?redirect_uri=https%3A%2F%2Fam.ticketmaster.com%2Fmsg%2Fam-sso%3Fdeeplink%3DL21zZy9lbi9teS1ldmVudHMvNjQ3Njg%3D&response_type=code&lang=en-us&integratorId=NAM&placementId=homepage&visualPresets=msg&hideLeftPanel=true&client_id=4c81b8c6f059.web.msg-msg.us&scope=openid%20profile%20phone%20email%20tm",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1733090525248,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 43,
            "tab": {
                        "current_navigation_index": 2,
                        "tab_id": 123416616,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 7,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13381432092315000,
                                                "page_transition": "RELOAD",
                                                "title": "MyVote",
                                                "timestamp_msec": 1736958492315,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://app.pnmvote.com/forgot-password/6783ed0b964d83000ffa7ad3",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 8,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13381432092315000,
                                                "page_transition": "RELOAD",
                                                "title": "MyVote",
                                                "timestamp_msec": 1736958492315,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://app.pnmvote.com/forgot-password/6783ed0b964d83000ffa7ad3",
                                                "virtual_url": "https://app.pnmvote.com/login",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 9,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13381432092315000,
                                                "page_transition": "RELOAD",
                                                "title": "MyVote",
                                                "timestamp_msec": 1736958492315,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://app.pnmvote.com/login",
                                                "virtual_url": "https://app.pnmvote.com/",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1736958492443,
                        "window_id": 123417370,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 35,
            "tab": {
                        "current_navigation_index": 0,
                        "tab_id": 123415570,
                        "pinned": False,
                        "navigation": [{
                                    "navigation_from_address_bar": False,
                                    "unique_id": 129,
                                    "navigation_forward_back": False,
                                    "http_status_code": 0,
                                    "global_id": 13375291477626000,
                                    "page_transition": "RELOAD",
                                    "title": "HireVue",
                                    "timestamp_msec": 1730817877626,
                                    "password_state": "PASSWORD_STATE_UNKNOWN",
                                    "referrer": "",
                                    "virtual_url": "https://app.hirevue.com/ui/learn-more/#/interview/Pkyy5pb-g5iskc/",
                                    "correct_referrer_policy": 1,
                                    "navigation_home_page": False
                        }],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1730817877688,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 13,
            "tab": {
                        "current_navigation_index": 1,
                        "tab_id": 123414048,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 66,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13364194816340000,
                                                "page_transition": "RELOAD",
                                                "title": "Manage My Booking | FlixBus",
                                                "timestamp_msec": 1719721216340,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://shop.global.flixbus.com/rebooking/login?utm_source=tripcycle&utm_medium=email&utm_campaign=..predrive&utm_content=com.flixbus",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 67,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13364194863528000,
                                                "page_transition": "RELOAD",
                                                "title": "",
                                                "timestamp_msec": 1719721263528,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://shop.global.flixbus.com/rebooking/login?utm_source=tripcycle&utm_medium=email&utm_campaign=..predrive&utm_content=com.flixbus",
                                                "virtual_url": "https://shop.global.flixbus.com/rebooking",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1719721214775,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 20,
            "tab": {
                        "current_navigation_index": 4,
                        "tab_id": 123414683,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 85,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372283930859000,
                                                "page_transition": "RELOAD",
                                                "title": "Join meeting - Zoom",
                                                "timestamp_msec": 1727810330859,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://virginia.zoom.us/j/97016206234?pwd=mHz1XU3tiFpVj4sxaV0EQ0V5zUJ9IM.1",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 86,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372283937110000,
                                                "page_transition": "RELOAD",
                                                "title": "Zoom meeting on web - Zoom",
                                                "timestamp_msec": 1727810337110,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://virginia.zoom.us/j/97016206234?pwd=mHz1XU3tiFpVj4sxaV0EQ0V5zUJ9IM.1",
                                                "virtual_url": "https://virginia.zoom.us/wc/97016206234/join?fromPWA=1&wpk=wcpk%7B0%7D%26%26%26%26wcpke654ebef1cd9ec028a38ae70b0da817b&_x_zm_rtaid=pdWfbmC1QZma11qN6oKxBg.1727810330808.3ad01db7bba9dea92188bc9a8f7312f6&_x_zm_rhtaid=287",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 87,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372283940263000,
                                                "page_transition": "RELOAD",
                                                "title": "Sign In | Zoom",
                                                "timestamp_msec": 1727810340263,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://virginia.zoom.us/",
                                                "virtual_url": "https://zoom.us/signin#/login",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 88,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372283975390000,
                                                "page_transition": "RELOAD",
                                                "title": "NetBadge",
                                                "timestamp_msec": 1727810375390,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s1",
                                                "virtual_url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s2",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 89,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372283984743000,
                                                "page_transition": "RELOAD",
                                                "title": "NetBadge Message",
                                                "timestamp_msec": 1727810384743,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s2",
                                                "virtual_url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s3",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 90,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13372284032960000,
                                                "page_transition": "RELOAD",
                                                "title": "NetBadge Message",
                                                "timestamp_msec": 1727810432960,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s3",
                                                "virtual_url": "https://shibidp.its.virginia.edu/idp/profile/SAML2/Redirect/SSO?execution=e1s3",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1727810330528,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
},
        {
            "tab_node_id": 16,
            "tab": {
                        "current_navigation_index": 3,
                        "tab_id": 123414278,
                        "pinned": False,
                        "navigation": [
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 70,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13368679154726000,
                                                "page_transition": "RELOAD",
                                                "title": "New Tab",
                                                "timestamp_msec": 1724205554726,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "chrome://newtab/",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 71,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13368679155558000,
                                                "page_transition": "RELOAD",
                                                "title": "Select a time · Canaan Harris - Global Teaching P\u2026",
                                                "timestamp_msec": 1724205555558,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "",
                                                "virtual_url": "https://canaan-harris.youcanbook.me/",
                                                "correct_referrer_policy": 1,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 72,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13368679189667000,
                                                "page_transition": "RELOAD",
                                                "title": "Confirm booking · Canaan Harris - Global Teaching\u2026",
                                                "timestamp_msec": 1724205589667,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://canaan-harris.youcanbook.me/?jumpDate=2024-08-21&i=itt_d7d2dcaf-6d39-46b5-96e1-d77dd4315ceb",
                                                "virtual_url": "https://canaan-harris.youcanbook.me/form?i=itt_d7d2dcaf-6d39-46b5-96e1-d77dd4315ceb",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    },
                                    {
                                                "navigation_from_address_bar": False,
                                                "unique_id": 73,
                                                "navigation_forward_back": False,
                                                "http_status_code": 0,
                                                "global_id": 13368679306535000,
                                                "page_transition": "RELOAD",
                                                "title": "Booking confirmed · Canaan Harris - Global Teachi\u2026",
                                                "timestamp_msec": 1724205706535,
                                                "password_state": "PASSWORD_STATE_UNKNOWN",
                                                "referrer": "https://canaan-harris.youcanbook.me/form?i=itt_d7d2dcaf-6d39-46b5-96e1-d77dd4315ceb",
                                                "virtual_url": "https://canaan-harris.youcanbook.me/thanks?i=itt_d7d2dcaf-6d39-46b5-96e1-d77dd4315ceb",
                                                "correct_referrer_policy": 0,
                                                "navigation_home_page": False
                                    }
                        ],
                        "extension_app_id": "",
                        "browser_type": "TYPE_TABBED",
                        "last_active_time_unix_epoch_millis": 1724205554232,
                        "window_id": 123417372,
                        "tab_visual_index": 0
            },
            "session_tag": "session_syncB6tgaK18eUHyYWzbkYqN6w=="
}
    ]
}

# Step 2: Extract and Convert Timestamps
timestamps = [entry['time_usec'] for entry in data['Browser History']]
dates = [datetime.fromtimestamp(time / 1e6) for time in timestamps]

# Create DataFrame
df = pd.DataFrame(dates, columns=['Datetime'])
df['Hour'] = df['Datetime'].dt.hour  # Extract hour for hourly analysis
df['Month'] = df['Datetime'].dt.month  # Extract month for quarterly grouping

# Define quarters
def assign_quarter(month):
    if 1 <= month <= 3:
        return 'Q1: Jan-Mar'
    elif 4 <= month <= 6:
        return 'Q2: Apr-Jun'
    elif 7 <= month <= 9:
        return 'Q3: Jul-Sep'
    elif 10 <= month <= 12:
        return 'Q4: Oct-Dec'

df['Quarter'] = df['Month'].apply(assign_quarter)

# Ensure all hours are represented
all_hours = pd.DataFrame(range(24), columns=['Hour'])  # DataFrame of all hours

# Plot data for each quarter
for quarter in df['Quarter'].unique():
    if quarter is not None:  # Filter out None if any months are out of range (sanity check)
        quarter_data = df[df['Quarter'] == quarter]
        hourly_counts = quarter_data['Hour'].value_counts().reindex(all_hours['Hour'], fill_value=0)

        hourly_counts.sort_index().plot(kind='bar')
        plt.title(f'Hourly Browsing Activity - {quarter}')
        plt.xlabel('Hour of Day')
        plt.ylabel('Number of Browsing Sessions per Hour')
        plt.grid(True)
        plt.xticks(range(24), rotation=0)  # Ensure all hours are labeled
        plt.show()
