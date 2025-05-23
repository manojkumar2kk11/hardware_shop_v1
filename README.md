# FH Building Supplies

Your one-stop shop for quality building materials! FH Building Supplies offers an extensive range of construction supplies, tools, and DIY essentials to meet every project need. Whether you're a professional contractor or a DIY enthusiast, our online platform makes it easy to explore, order, and receive your materials quickly and securely.

**[Visit FH Building Supplies Here!](https://fh-building-supplies-4710f10b810d.herokuapp.com/)**

## Purpose

FH Building Supplies aims to provide a seamless, efficient online shopping experience for purchasing building materials, tools, and accessories.

## Responsive Design

The website is fully responsive, providing an optimal experience whether users browse on desktops, tablets, or smartphones.

## Project Goals

### User Goals
- Explore a wide catalog of high-quality building supplies.
- Add products to a shopping bag and checkout easily.
- Manage user profiles, order history, and subscriptions.
- Receive automated confirmation emails after purchases.

### Site Owner Goals
- Drive product sales through an online channel.
- Build brand reputation for quality and reliability.
- Provide a frictionless user experience to encourage customer loyalty.

## Features

### Dynamic Navigation Bar
- **Navigation Changes:** Based on user login status.
- **Logged-Out Users:** See basic navigation with login and signup prompts.
- **Logged-In Users:** Access Profile, My Orders, and Logout options.

### Product Catalog
- **Category Filtering:** Products organized and filterable by category.
- **Product Details:** Images, descriptions, and prices displayed for each product.

### Shopping Bag Management
- **Real-Time Management:** Add, update, and delete items in the shopping bag.
- **Instant Feedback:** Immediate updates on item quantity changes.

### Secure Checkout
- **Stripe Integration:** Secure payment processing with Stripe.
- **Order Confirmation:** Automatic email confirmations after purchase.

### User Authentication
- **Django-AllAuth:** Secure login, logout, and signup functionality.
- **Profile Management:** Users can view and manage their orders from profile pages.

### Contact Page and Newsletter Signup
- **Customer Support:** Easy access to contact forms.
- **Subscription Option:** Users can sign up for newsletters.

### Responsive Design
- **Device Compatibility:** Fully responsive for desktops, tablets, and mobile devices.

### Validation
- **W3C Validation:** All HTML and CSS files pass W3C validation.

### Dynamic Behavior
- **Stock Management:** Purchase buttons disabled when products are out of stock.
- **Authentication Checks:** Profile management actions are restricted unless authenticated.

## Validation Testing  

The W3C validator was utilized to validate all HTML and CSS files in this project. Each page has been rigorously tested to ensure compliance with web standards.  

---

## HTML Validation  

| Page                     | Validation Result |  
|---------------------------|-------------------|  
| Home Page                 | Passed            |  
| Products Page             | Passed            |  
| Product Detail Page       | Passed            |  
| Shopping Bag Page         | Passed            |  
| Checkout Page             | Passed            |  
| Profile Page              | Passed            |  
| Login Page                | Passed            |  
| Signup Page               | Passed            |  

---

## CSS Validation  

The `style.css` file located in the `static` directory passed validation using the W3C CSS Validator without any errors or warnings.  

---![Valid CSS!](/media/w3c_css_rd.png)  

## Wireframes  

### Homepage   
The homepage features a clean and modern design with a search bar, product categories, and navigation options that direct users to key parts of the site, such as the product catalog and their cart.

### Product Catalog  

The product catalog is simple and intuitive, displaying categories for easy navigation. Each product includes an image, description, and price for easy browsing.

### Checkout Page  
 
The checkout page is designed for a smooth and quick purchase experience. The user can review their items, enter shipping information, and complete their purchase using a secure payment method.

---

## Technologies Used  

### Languages and Libraries  
The following technologies were used to develop this project:

- **Languages:**  
  - HTML  
  - CSS  
  - Python

- **Frameworks and Libraries:**  
  - **Django:** A full-stack Python web framework.  
  - **Bootstrap:** A front-end framework for responsive web design.  
  - **jQuery:** A JavaScript library for DOM manipulation.  
  - **Font Awesome:** Used for icons via CDN.  
  - **Django-AllAuth:** Handles user authentication and account management.  
  - **WhiteNoise:** Simplifies serving static files during deployment.  
  - **Gunicorn:** A WSGI HTTP server used in deployment.  
  - **psycopg2-binary:** A PostgreSQL adapter for Python.  
  - **python-decouple:** Manages environment variables for easier configuration.  
  - **dj-database-url:** Parses the database URL for deployment.

---

## Database Schema  
This project utilized a relational database, which was the most suitable choice for its requirements. The schema, as illustrated below, was designed using. For additional details about the User table and its objects, please refer to the AllAuth Documentation.

---

## Features by Page

### Home Page
![Dynamic Navbar Login](/media/login_rd.png)
![Dynamic Navbar Logout](/media/logout_rd.png)

* The home page features a dynamic navigation bar that adjusts based on the user's login status. Unauthenticated users will not be able to view their cart.
<hr>

### Product Catalog
![Product Catalog](/media/allplumbing_rd.png)

* The catalog is filterable by categories, allowing users to find products quickly. Each item is displayed with an image, description, and price.
<hr>

### Checkout Process
![Checkout Page](/media/checkout_rd.png)

* Users can review their cart and proceed to checkout with secure payment options. Confirmation emails are sent after successful orders.
<hr>

### Profile Page
![Profile Page](/media/profile_rd.png)

* Users can manage their profile and view their order history in a secure, user-friendly layout.
<hr>

---

## Forking or Cloning the Repository  

### How to Fork  
1. Navigate to the repository URL: [https://github.com/your-repo-link](https://github.com/your-repo-link).  
2. Click the **Fork** button located in the top right corner of the page.  
3. Create a new fork by providing a name and an optional description.  
4. Once done, click **Create Fork**.  
5. Congratulations! You’ve successfully created a fork of this repository.  

### How to Clone  
1. Visit the repository URL: [https://github.com/your-repo-link](https://github.com/your-repo-link).  
2. Click the **Code** button and select the desired format for cloning (HTTPS, SSH, or GitHub CLI).  
3. Copy the provided link.  
4. Open your terminal in your preferred IDE and navigate to the directory where you want to clone the repository.  
5. Use the following command to clone the repository:  
   ```bash
   git clone <copied-link>




# Deployment & Local Development

## Deployment

### PostgreSQL Database Setup
This project uses PostgreSQL for its database. Follow the steps below to set up the database:

1. Set up a PostgreSQL database either locally or using a cloud service such as **Heroku Postgres**.
2. If using Heroku, add the **Heroku Postgres** add-on to your app from the Heroku Dashboard to create a new PostgreSQL database.
3. Copy the database URL from your PostgreSQL service (e.g., Heroku or your local setup).

### Heroku Web Hosting
The application is hosted on **Heroku**. You can deploy your application by following these steps:

1. From the **Heroku Dashboard**, click **"New"** to create a new app.
2. Choose a unique name for your app and click **Create App**.
3. Once the app is created, go to the app settings and under **Config Vars**, create a new variable called `DATABASE_URL`. Set the value to the PostgreSQL database URL that you copied earlier.

### AWS S3 Setup for Static Files
To store static files (like images, CSS, and JavaScript) securely in the cloud, **AWS S3** is integrated for this project. Follow these steps to set up S3:

#### 1. Create an S3 Bucket:
   - Go to the **AWS S3 Dashboard**.
   - Click on **"Create Bucket"** and give it a unique name.
   - Choose a region and configure the rest of the settings as needed.
   - Click **Create Bucket**.

#### 2. Configure IAM for Access:
   - Navigate to **IAM** in AWS and create a new user with programmatic access.
   - Attach a policy that allows access to your S3 bucket (e.g., `AmazonS3FullAccess`).
   - Save the **Access Key ID** and **Secret Access Key** for later use.

#### 3. Configure Django to Use S3:
   - Install `django-storages` and `boto3`:
     ```bash
     pip install django-storages boto3
     ```
   - In **`settings.py`**, configure Django to use S3 for static and media files:
     ```python
     AWS_ACCESS_KEY_ID = '<your-access-key>'
     AWS_SECRET_ACCESS_KEY = '<your-secret-key>'
     AWS_STORAGE_BUCKET_NAME = '<your-bucket-name>'
     AWS_S3_REGION_NAME = '<your-region>'
     AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

     STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
     ```

#### 4. Update ALLOWED_HOSTS in `settings.py`:
   - Make sure to add the domain of your app (e.g., `herokuapp.com`) to **ALLOWED_HOSTS** in `settings.py`:
     ```python
     ALLOWED_HOSTS = ['your-app-name.herokuapp.com', 'www.yourdomain.com']
     ```

#### 5. Push to Heroku:
   - Ensure all changes are committed to your local Git repository.
   - Push to Heroku:
     ```bash
     git push heroku main
     ```

#### 6. Check your static files:
   - After deployment, static files (like product images) will be served via **AWS S3**, reducing the load on Heroku and ensuring scalability.

---

# Credits
- I am also grateful to my online peers on Slack who shared their opinions and project insights, which greatly inspired and helped shape my own project.
- This project was inspired by and uses code from the **E-commerce Walkthrough Project**. I have taken inspiration from its structure, design, and features to build this hardware shop project. The knowledge gained from this project has been incredibly helpful in developing the features and functionality of this application.
