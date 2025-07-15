# 🛍️ Diwali Sales Data Analysis

This project involves exploratory data analysis (EDA) on a sample dataset of Diwali sales to extract insights into customer behavior and sales patterns. The analysis includes demographic segmentation, top performers (states, customers, products), and visualization of spending patterns.

---

## 📁 Dataset Information

The dataset (`Diwali Sales Data.csv`) contains transactional and demographic data including:

- Customer ID, Name, Gender, Age Group, Marital Status  
- Product Category, Orders, Amount  
- State and City of the customer  
- Some irrelevant or unnamed columns used for basic cleaning practice

---

## 🔧 Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  

---

## 🧼 Data Cleaning

- Handled null values in `Status`, `unnamed1`, and `Amount` columns  
- Converted `Amount` from string to numeric for analysis  
- Replaced `Marital_Status` values from 0/1 to 'Single'/'Married'  

---

## 📊 Exploratory Data Analysis (EDA)

The analysis includes the following:

### 1. **Gender Distribution**
- Pie chart representing the proportion of male and female customers

### 2. **Age Group Distribution**
- Bar chart showing the number of customers in each age group

### 3. **Marital Status**
- Pie chart showing proportions of single vs. married customers

### 4. **Orders by Marital Status**
- Bar chart comparing total orders by single vs. married customers

### 5. **Top 5 States by Order Volume**
- Horizontal bar chart showing states with the most orders

### 6. **Top 5 Customers by Purchase Amount**
- Horizontal bar chart of customers who spent the most

### 7. **Top 5 Revenue-Generating Product Categories**
- Horizontal bar chart showing which product categories generated the most revenue

### 8. **Average Order Value by Gender**
- Pie chart comparing average order value for males vs. females

### 9. **Spending by Age Group**
- Bar chart showing which age group spent the most money

---

## 📁 Output

All plots are saved as `.png` images in the working directory for future reporting or dashboard usage:
- `Gender Distribution.png`  
- `Age_group_distribution.png`  
- `marital_status_distribution.png`  
- `orders_based_on_marital_status.png`  
- `top_5_states_by_order.png`  
- `top_5_customers_based_on_amount.png`  
- `top_revenue_generating_product.png`  
- `Average_order_on_gender_basis.png`  
- `Most_money_spending_agegroup.png`  

---

## 📌 Conclusion

This project demonstrates a foundational level of data analysis skills using Python. The key findings include:

1. **Most spending age group is 26–35**  
2. **On average, females spend more than males**  
3. **Singles place more orders than married customers**  
4. **Top 5 states that spend the most are**: Uttar Pradesh, Maharashtra, Karnataka, Delhi, and Madhya Pradesh  
5. **Top 5 revenue-generating product categories are**: Food, Clothing and Apparel, Electronics and Gadgets, Footwear and Shoes, and Furniture  

---

## 🚀 Future Improvements (for practice)

- Incorporate time-series trends if `Order_Date` is available  
- Perform deeper product analysis if more SKU-level details exist  
- Build an interactive dashboard using Power BI or Plotly  

---

## 📎 Author

**Dipin Silwal**  
Practicing data analysis using Python  
📂 GitHub: [404dipin](https://github.com/404dipin)  
