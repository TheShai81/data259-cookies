# Research on how websites prompt for cookie acceptance


## Sources
1. *HCI in Business, Government and Organizations* (July 2022)
2. *Exploring the Cookieverse:A Multi-Perspective Analysis of Web Cookies* (2023)


## Info

### HCI

The study compared two common types of cookie notices, binary-choice (accept all or update preferences) and category-choice (displaying all cookie categories on one screen).

The experiment revealed that the binary-choice notice achieved a slightly higher overall opt-in rate for all cookies compared to the category-choice notice. This effect was even more pronounced on mobile devices, where users were most likely to accept all cookies when presented with a binary-choice notice.

However, the follow-up survey indicated that users' preferences differed from the observed opt-in rates. More than half of the respondents (53.5%) preferred the category-choice cookie notice. Their reasons for this preference included:
- Better overview and transparency of the cookies being used.
- The ability to make all decisions on the first level of the notice without requiring additional clicks.
- A perception of greater trustworthiness due to the transparent presentation of cookie options.


Respondents who preferred the binary-choice notice (37%) cited:
- Easier navigation.
- Faster selection due to its perceived simplicity.
- The perception of the notice being clearer with only two initial choices.


The study also identified several external factors that influence users' decisions when presented with cookie notices. The most frequently mentioned factors were:
- Simplicity of use of the cookie notice, which had a generally positive effect on user attitudes.
- The speed with which the cookie notice could be dismissed, also generally having a positive effect.
- Time pressure when surfing, which had a predominantly negative effect on users' attitudes.


Despite the higher opt-in rate for binary-choice notices, the preference for category-choice notices suggests that users value transparency and control.

The study also found that the majority of respondents found cookie notices annoying (87.9%) and often clicked the most prominent button to dismiss them quickly. Interestingly, over half of the respondents associated the presence of a cookie notice with the credibility or trustworthiness of the website (58.5%).


***while simplifying the cookie notice and making it easy to dismiss might increase opt-in rates, website operators should also consider that overly complicated notices with "digital nudges" could further annoy users and that cookie notice variants that make users feel like they do not have control over their choices undermine user trust.***

*They suggest making all possible choices visible on the first layer of the cookie notice.*



### Cookieverse

The study conducted a comprehensive measurement analysis of web cookies across the Tranco top-10k websites, considering various perspectives such as the client's location, interaction with cookie banners, and the operating system used.


One of the key findings is the significantly higher prevalence of cookie banners (56% more) when visiting websites from within the EU region compared to non-EU regions. The researchers developed a tool, BannerClick, to automatically detect and interact with these banners with high accuracy (99% for detection, 97% for accepting, and 87% for rejecting).
The study highlights the critical impact of interacting with cookie banners on the number of cookies set. They observed that websites send, on average, 5.5 times more third-party cookies after clicking "accept" on a banner. Additionally, there is a significant increase in tracking cookies upon acceptance. This underscores the importance of considering banner interaction in web measurement studies. Conversely, rejecting banners in the EU led to a low number of tracking cookies, indicating the effectiveness of GDPR in reducing tracking when consent is withheld.

The research also examined the deployment of Consent Management Platforms (CMPs), noting a slight increase in their usage over time. However, they found that not all websites with CMP banners properly implement the standardized APIs, which hinders automated banner interaction.

The study revealed substantial differences in cookie behavior based on the geographic location of the client. Without banner interaction, a significant percentage of websites set more tracking cookies when accessed from non-EU regions compared to the EU. Even after accepting a banner, most websites sent more tracking cookies in non-EU countries. This suggests a positive impact of GDPR on reducing the number of third-party and tracking cookies in the EU.
Analysis of website cookie consistency showed that websites tend to exhibit more consistent cookie behavior when accessed multiple times from within the EU. Significant statistical differences in cookie numbers were frequently observed between EU and non-EU locations.

The study also found notable differences in cookies between landing and inner pages of a website. A considerable percentage of websites showed different third-party and tracking cookie behavior between these page types, indicating that analyzing only landing pages may not provide a complete picture of the cookie landscape.
Furthermore, the research quantified cookie differences when a website is accessed from desktop and mobile browsers. Differences in the number of third-party and tracking cookies were observed between these platforms, highlighting the need to consider both in future research.

*Interestingly, the study's initial analysis suggests that the California Consumer Privacy Act (CCPA) does not have a direct positive impact on reducing third-party and tracking cookies.* ***In fact, websites overtly adhering to CCPA (by including a "Do Not Sell My Personal Information" link) tended to send more third-party and tracking cookies compared to others.*** These CCPA-compliant websites were also more likely to show cookie banners.


- emphasizes that a multi-perspective approach is crucial when studying web cookies, as factors like banner interaction, client location, page type, and browsing platform significantly impact the cookie landscape. The findings highlight the influence of privacy regulations like GDPR and the complexities of cookie management on the web.