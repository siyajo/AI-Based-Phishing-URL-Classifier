Phishing URL Detection Web App

This is a machine learning-based web application built with Streamlit that classifies URLs as Phishing or Legitimate. 
It uses a trained Random Forest model and intelligent feature extraction to detect suspicious URLs automatically.

How It Works

1.You input any URL (e.g., https://example.com)

2.The app extracts features from the URL using custom rules

3.The trained model predicts whether it's Phishing (-1) or Legitimate (1)

4.The result is displayed instantly with color-coded output

Features used for detection:

| Feature                       | Description                                                |
| ----------------------------- | ---------------------------------------------------------- |
| `having_IP_Address`           | Whether the URL has an IP address instead of a domain name |
| `URL_Length`                  | Length of the URL                                          |
| `Shortining_Service`          | Use of URL shortening services like bit.ly                 |
| `having_At_Symbol`            | Presence of `@` symbol in the URL                          |
| `double_slash_redirecting`    | Redirection using `//`                                     |
| `Prefix_Suffix`               | Presence of `-` in domain name                             |
| `having_Sub_Domain`           | Number of subdomains                                       |
| `SSLfinal_State`              | SSL certificate status                                     |
| `Domain_registeration_length` | Duration of domain registration                            |
| `Favicon`                     | Consistency of favicon source with domain                  |
| `port`                        | Unusual port usage                                         |
| `HTTPS_token`                 | Misleading HTTPS token in URL                              |
| `Request_URL`                 | External object request ratio                              |
| `URL_of_Anchor`               | External anchor URL ratio                                  |
| `Links_in_tags`               | Links in `<script>`, `<meta>`, etc.                        |
| `SFH`                         | Server form handler address legitimacy                     |
| `Submitting_to_email`         | Presence of "mailto:" for submissions                      |
| `Abnormal_URL`                | Mismatch between domain and whois                          |
| `Redirect`                    | Number of redirections                                     |
| `on_mouseover`                | Scripts that change status bar on hover                    |
| `RightClick`                  | Right-click disabled on the site                           |
| `popUpWidnow`                 | Use of popup windows                                       |
| `Iframe`                      | Invisible iframe usage                                     |
| `age_of_domain`               | Age of domain (newer = suspicious)                         |
| `DNSRecord`                   | Availability of DNS record                                 |
| `web_traffic`                 | Website popularity (Alexa rank)                            |
| `Page_Rank`                   | Google's page rank                                         |
| `Google_Index`                | Whether URL is indexed by Google                           |
| `Links_pointing_to_page`      | Number of backlinks                                        |
| `Statistical_report`          | Blacklist detection                                        |


How to Run Locally in Command Prompt: 

Install dependencies(if needed):

pip install streamlit

Run the app:

streamlit run app.py

Model Info

Model Type: Random Forest Classifier

Accuracy: ~96.7%

Trained On: 30 manually extracted URL features

Dataset: phishing urldataset.csv

