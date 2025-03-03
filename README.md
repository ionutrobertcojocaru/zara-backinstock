# Zara Product Availability Checker

This tool helps you retrieve the availability data of Zara products and get notified through email.

TODO: Encrypt the data

## How to Get Product URLs

1. Open the Zara product page in your browser.
2. Open **Developer Tools** (Press `F12` or `Ctrl + Shift + I` in Chrome).
3. Go to the **Network** tab.
4. Filter requests by selecting **Fetch/XHR**.
5. Look for a request containing **"availability"** in the name.
6. Right-click on the request and select **Copy > Copy URL**.
7. Use the copied URL for fetching product availability data.
