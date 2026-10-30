# Dealer Evaluation (IBM Skills Network source, Render deployment)

This project adapts the official [backend](https://github.com/ibm-developer-skills-network/dealer_evaluation_backend) and [frontend](https://github.com/ibm-developer-skills-network/dealer_evaluation_frontend) repositories. The three original services are kept in separate folders. Changes make file paths and ports work on Render, let the frontend read API URLs from environment variables, fix the original `Tech city` name mismatch, and update the Node dependencies.

## Run locally

Install Python packages from `products_list/requirements.txt` and `dealer_evaluation_frontend/requirements.txt`, and run `npm ci` in `dealer_details`. Start each service in its own terminal:

```text
cd products_list                 ; python app.py            # port 5000
cd dealer_details                ; npm start                # port 8080
cd dealer_evaluation_frontend   ; python app.py            # port 5001
```

Open `http://localhost:5001`. The frontend defaults to the two local API URLs.

## Deploy on Render

1. Push the **contents of this folder** to a GitHub repository you control. Keep `render.yaml` at the repository root.
2. In Render, choose **New > Blueprint**, connect that repository, and apply the three free web services from `render.yaml`.
3. Wait until both APIs are live. Visit their actual URLs at `/products` and `/allprice/Headphones`.
4. In the frontend service settings, set `PRODUCT_API_URL` and `DEALER_API_URL` to the **actual** API base URLs assigned by Render, without trailing slashes. The values in `render.yaml` assume the requested service names are available; Render may assign different URLs. Redeploy the frontend after changing them.
5. Open the frontend URL. Confirm products load, selecting `Laptop` shows dealers, selecting `Tech City` shows a price, and `All Dealers` shows a table.

Render free web services can sleep when idle. The first request after idle may take about a minute.

## Genuine submission evidence

For `product_details_deploy.png`, capture the **actual Render Product Details service page** after deployment, with the service name, live status, and successful deploy visible. Save the original screenshot under that filename. Do not substitute a local test or an edited image for deployment proof.

The Coursera rubric specifically asks for **IBM Code Engine** deployment screenshots. A Render screenshot may not earn those marks unless the course staff accepts Render as an alternative. No deployment screenshot is included here because no Render deployment has been performed.
