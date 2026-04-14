# SenticMoney Help Reference

> Complete reference documentation for all SenticMoney features. Use this as a source for writing blog articles and content.

---

## Table of Contents

1. [Dashboard](#dashboard)
2. [Transactions](#transactions)
3. [Budgets](#budgets)
4. [Categories & Mappings](#categories--mappings)
5. [Income Sources](#income-sources)
6. [Financial Goals](#financial-goals)
7. [Reminders](#reminders)
8. [Tags](#tags)
9. [Bills & Accounts Payable](#bills--accounts-payable)
10. [Backup Management](#backup-management)
11. [Reconciliation](#reconciliation)
12. [Financial Health](#financial-health)
13. [Financial Calendar](#financial-calendar)
14. [Accounting Dashboard](#accounting-dashboard) *(includes Money Flow Sankey)*
15. [AI Financial Insights](#ai-financial-insights)
16. [Financial Calculators](#financial-calculators) *(Free tier)*
17. [Runway Cash Flow Planning](#runway-cash-flow-planning) *(Standard tier)*
18. [Currency Support](#currency-support)

---

# Dashboard

## Understanding Your Financial Dashboard

The Dashboard is your financial command center, providing a comprehensive overview of your current financial status at a glance.

### What is the Dashboard?

The Dashboard is your financial home base in SenticMoney, designed to provide:
- A snapshot of your current financial situation
- Alerts about upcoming financial events
- Visual representations of your spending and income
- Insights into your financial patterns and health

### Accessing Your Dashboard

You can reach your Dashboard in two ways:
- Click on **Dashboard** in the main navigation menu
- Click on the SenticMoney logo in the top-left corner

### Dashboard Organization

The Dashboard is organized into distinct sections:
- **Financial Summary**: Key metrics at the top of the page
- **Upcoming Events**: Bills, income, and reminders approaching soon
- **Financial Charts**: Visual representations of your data
- **AI Insights**: Personalized observations about your finances
- **Recent Transactions**: Your most recent financial activity

### Financial Summary Cards

#### Current Balance
Shows your current total available funds across all tracked accounts:
- Combines balances from all active accounts
- Updates based on recorded transactions
- Shows a comparison to the previous month

#### Monthly Income
Displays your expected income for the current month:
- Includes all active income sources
- Shows actual income received so far this month
- Displays expected remaining income
- Compares to previous month's total

#### Monthly Expenses
Shows your spending for the current month:
- **Total Bills**: Sum of all bill amounts (from your Bills page)
- **Bills Paid**: Amount of bills paid so far this month (calculated from actual transactions matched to bills)
- **Other Expenses**: All expenses NOT matched to bills (includes discretionary spending, one-time purchases)

**Tip**: For bills to be recognized as "paid," ensure the transaction description includes the bill name and the amount matches exactly.

#### Available to Spend
Shows how much cash you have available right now after accounting for unpaid bills:
- **Formula**: Current Balance - Unpaid Bills
- Real-time calculation based on your actual account balance
- Subtracts only the bills you haven't paid yet this month
- Does NOT try to predict future income
- Updates immediately with every transaction

### Dashboard Charts

#### Income vs. Expenses
- Shows monthly totals for both income and expenses
- Visualizes the gap between earning and spending
- Illustrates trends in your income-expense ratio
- Hover over any month to see exact figures

#### Spending by Category
- Shows the proportion of spending in each category
- Uses different colors to distinguish categories
- Displays the percentage and amount for each slice
- Click on any slice to see a detailed breakdown

#### Budget Progress
- Displays each budget category as a progress bar
- Shows percentage of budget used and amounts (spent/total)
- Color-codes status (green = under budget, yellow = near limit, red = over budget)
- **Supports ongoing budgets**: Budgets without end dates track indefinitely
- **Handles refunds/returns**: Credits automatically reduce spent amounts
- **Totals footer**: Shows Total Budget, Total Spent, and Total Remaining

### Dashboard Best Practices

1. **Check daily** - Make reviewing your Dashboard part of your daily routine
2. **Prioritize upcoming events** - Pay special attention to bills and reminders due soon
3. **Monitor trends** - Watch the Income vs. Expenses chart to track your savings rate over time
4. **Use Quick Actions** - Take advantage of one-click access to common financial tasks
5. **Respond to insights** - Act on the AI-generated financial observations

---

# Transactions

## Managing Your Financial Transactions

The Transactions feature is the core of SenticMoney, allowing you to track all money coming in and going out of your accounts.

### What are Transactions?

Transactions represent the movement of money in and out of your accounts:
- **Income transactions**: Money you receive (paychecks, gifts, refunds, etc.)
- **Expense transactions**: Money you spend (bills, groceries, entertainment, etc.)

### Benefits of Tracking Transactions

- Know exactly where your money is going
- Identify spending patterns and habits
- Ensure you stay within your budget
- Prepare accurate tax information
- Detect fraud or unauthorized charges
- Enable powerful financial analysis and planning

### Transactions Main Page Features

**Input Actions:**
- **Add Transaction**: Manually enter a new expense or income
- **Import Bank Statement**: Upload transactions from bank files (CSV, XLSX, OFX, QFX, PDF)
- **Upload Receipt Image**: Import receipts with itemized details (email .eml, text .txt, or photos)
- **Upload Bill**: Import utility bills with line-item parsing

**View/Search Actions:**
- **View All Transactions**: See your complete transaction history
- **Monthly Summary**: View monthly totals and analysis
- **Search Transactions**: Find specific transactions with filters
- **Find Duplicates**: Identify potential duplicate entries

**Bulk Actions:**
- Select multiple transactions using checkboxes
- **Change Category**: Update category for all selected transactions
- **Change Type**: Switch between Income and Expense
- **Delete Selected**: Remove multiple transactions at once

### Adding Transactions

1. Navigate to the Transactions page and click **Add Transaction**
2. Select the transaction type (Expense or Income)
3. Fill in required information:
   - **Amount**: How much money was involved
   - **Date**: When the transaction occurred
   - **Category**: Which spending or income category it belongs to
   - **Description**: What the transaction was for
   - **Payment Method**: How the transaction was paid
   - **Tags**: (Optional) Custom labels to organize transactions
   - **Notes**: (Optional) Additional information
4. Click **Save Transaction**

### Split Transactions (Standard Tier)

Split a single transaction across multiple budget categories (e.g., a $150 Costco trip → $100 Groceries + $50 Household):

1. Open a transaction and click **Split**
2. Add 2+ allocation rows, each with a category and amount
3. Allocation rows must sum to the original transaction total
4. Click **Save Split**

The primary category is set to the largest split for backward compatibility. Split amounts are tracked separately in budget and Runway calculations.

### Importing Bank Statements

1. Click **Import Bank Statement**
2. Upload a CSV, Excel, OFX, QFX, or PDF file from your bank
3. Specify the account name
4. Identify which columns contain the date, description, and amount
5. Optionally select a default category
6. Check the option to save column mappings for future imports
7. Click **Upload and Process**

**Important Note about Import Formats**: For best categorization results, consistently use the same import format (CSV/Excel or OFX). Merchant names appear differently in different formats.

### Uploading Receipts

**Email Receipts (.eml)** - 100% Accurate, Recommended:
1. Open receipt email in Gmail
2. Click 3-dot menu > "Download message"
3. Upload the .eml file
4. All items extracted perfectly

**Text Receipts (.txt)** - 100% Accurate:
1. Open receipt on your store's website
2. Select all text (Ctrl+A), copy
3. Paste into Notepad, save as .txt
4. Upload the .txt file

**Photos (AI Vision)** - Fast & Accurate:
1. Take clear photo of paper receipt
2. Upload .jpg or .png file
3. AI extracts items in seconds
4. Review and edit if needed

**Privacy Note**: When you upload a receipt photo, only the receipt image is sent to Google's Gemini AI. Your name, payment card details, bank account, or other transactions are never sent. Email and text receipts are processed entirely on your computer.

### Mobile Receipt Capture

Capture receipts on the go from any phone or tablet on your home network:

1. Open SenticMoney in your phone's browser (using your local network address, e.g., 192.168.x.x:5007)
2. Tap the receipt capture button
3. Take a photo of the receipt
4. The receipt queues locally on the phone

When you return home and your phone reconnects to your home Wi-Fi, queued receipts sync with SenticMoney automatically. No cloud account required, no login on the phone, no data transmitted outside your local network.

**Key Points:**
- Works from any device with a browser and camera on the home network
- Receipts queue if captured while on the local network and the app processes them on reconnection
- No internet required for the capture itself — only the local network connection to SenticMoney
- Photo receipts are processed by Gemini AI Vision for line-item extraction once synced
- The privacy model is maintained: receipt images go to Gemini for OCR, but your transaction database never leaves your device

### Category Mappings

Automatically categorize imported transactions with keyword-based rules:
1. Click **Category Mappings** on the Transactions page
2. Create rules that match transaction descriptions to categories
3. Examples:
   - "AMAZON" -> Shopping category
   - "DUKE ENERGY" -> Electric subcategory (under Utilities)
4. These rules apply to all future imports

**Important - Merchant Name Variations**: Bank statements format merchant names differently. You must create a mapping for each variation:
- "WALMART" -> Groceries
- "WAL-MART" -> Groceries
- "WM SUPERCENTER" -> Groceries

### Transaction Reports and Analysis

**Transaction Summary** shows:
- **Income**: Total money received for the selected period
- **Expenses**: Total money spent
- **Net**: The difference between income and expenses

**Monthly Summary** provides:
- Monthly totals for income, expenses, net, and number of transactions
- Yearly totals at the bottom
- Top expense categories for the year

### Best Practices

1. **Be consistent with data entry** - Use the same description formats
2. **Record transactions frequently** - Daily or weekly is better than monthly
3. **Use detailed descriptions** - "Kroger - Weekly Groceries" is better than just "Groceries"
4. **Categorize everything** - Avoid leaving transactions uncategorized
5. **Use tags strategically** - Tags are perfect for cross-category grouping
6. **Reconcile regularly** - Compare your records with bank statements monthly
7. **Set up category mappings** - Automate categorization for recurring merchants

---

# Budgets

## Managing Your Budgets

The Budgets feature helps you plan your spending, track your progress, and achieve your financial goals by creating spending limits for different categories.

### What are Budgets?

Budgets represent planned spending limits for different categories of expenses:
- Plan how to allocate your income
- Limit overspending in specific categories
- Track your progress throughout the month
- Identify areas where you might need to adjust spending
- Ensure you're saving enough for your goals

### Types of Budgets

- **Category Budgets**: Set spending limits for specific categories
- **Custom Period Budgets**: Create budgets for specific time periods with start and end dates
- **Income-Linked Budgets**: Connect budgets to specific income sources

### Creating a Budget

1. Navigate to the Budgets page and click **Add Budget**
2. Fill in required information:
   - **Category**: Which spending category this budget applies to
   - **Budget Amount**: Maximum amount you want to spend
   - **Income Source**: (Optional) Link to a specific income source
   - **Start Date**: When the budget period begins
   - **End Date**: When it ends (leave blank for ongoing budgets)
   - **Notes**: (Optional) Additional details
3. Click **Save Budget**

**Ongoing Budgets**: You can create budgets without end dates for recurring expenses like Groceries, Gas, or Entertainment that you want to track continuously month-over-month.

### Progress Bar Indicators

- **Green**: Spending is below 70% of budget
- **Yellow**: Spending is between 70% and 100% of budget
- **Red**: Spending has exceeded the budget limit

### How Refunds and Returns Are Handled

Budget tracking intelligently handles refunds and returns:
- **Automatic credit back**: When you record a refund in a budget category, it reduces your "Spent" amount
- **Example**: Budget $500 for Groceries, spend $300, return $50 worth of items = "Spent" becomes $250

**Tip**: When you return items or receive refunds, categorize those income transactions with the same category as the original purchase to automatically credit your budget.

### Popular Budgeting Methods

**50/30/20 Budget**:
- 50% of income for needs (housing, food, utilities)
- 30% of income for wants (entertainment, dining out)
- 20% of income for savings and debt reduction

**Zero-Based Budget**:
- Give every dollar a job so income minus expenses equals zero
- Create a budget for every spending category
- Include savings and debt payments as "expenses"

**Envelope System**:
- Create a separate budget for each spending category
- When the budget for a category is depleted, stop spending
- No "borrowing" from one category to another

### Best Practices

1. **Start realistic** - Begin with budget amounts based on actual spending
2. **Include everything** - Create budgets for all regular spending categories
3. **Don't forget irregular expenses** - Budget for annual/quarterly expenses by dividing by months
4. **Build in flexibility** - Allow some room for unexpected expenses
5. **Review weekly** - Check budget progress at least once a week
6. **Adjust as needed** - If a budget consistently doesn't work, change it
7. **Align with income cycles** - Set budget periods that correspond to pay periods

---

# Budgeting Method Implementation Guide

> How users implement each major budgeting method using SenticMoney features. Use this as a reference when writing articles about budgeting methods — it maps abstract concepts to concrete app features.

## Zero-Based Budgeting in SenticMoney

**Core Principle:** Every dollar of income is assigned to a category until the remaining balance is $0.

**Setup Steps:**
1. **Income Sources** — Add all income sources with amounts and pay schedules
2. **Categories** — Create categories for every spending area, including savings and debt payments
3. **Budgets** — Create a budget for each category. Total of all budgets should equal total monthly income
4. **Dashboard** — "Available to Spend" card shows remaining unallocated money (goal: $0)
5. **AI Genie** — Ask "Am I using zero-based budgeting correctly?" and the Genie will check if your budgets cover your full income

**Key Features Used:** Budgets, Income Sources, Dashboard, Categories, AI Genie

## Envelope Budgeting in SenticMoney

**Core Principle:** Each spending category is a virtual "envelope" with a fixed amount. When empty, stop spending.

**Setup Steps:**
1. **Categories** — Create a category for each envelope (Groceries, Gas, Dining Out, Entertainment, etc.)
2. **Budgets** — Create a budget per category. The budget amount IS the envelope amount
3. **Budget Progress Bars** — Green/Yellow/Red indicators show envelope status at a glance
4. **Dashboard Budget Progress** — See all envelopes on one screen with remaining amounts
5. **AI Genie** — Ask "How much is left in my groceries envelope?" for instant status

**Key Difference from Physical Envelopes:** SenticMoney tracks digital transactions automatically via imports, so users don't need cash. The budget progress bar replaces the physical envelope.

**Key Features Used:** Budgets, Budget Progress Bars, Categories, Dashboard, AI Genie

## 50/30/20 Rule in SenticMoney

**Core Principle:** Allocate 50% of after-tax income to needs, 30% to wants, 20% to savings/debt.

**Setup Steps:**
1. **Categories** — Organize categories into three groups: Needs (housing, utilities, groceries, insurance, minimum debt payments), Wants (dining out, entertainment, subscriptions, shopping), Savings (emergency fund, investments, extra debt payments)
2. **Budgets** — Create budgets that total 50% of income for Needs categories, 30% for Wants, 20% for Savings
3. **Spending by Category Chart** — Dashboard pie chart visually shows the percentage split
4. **AI Genie** — Ask "What percentage of my spending goes to needs vs wants vs savings?" for an instant breakdown

**Key Features Used:** Categories, Budgets, Dashboard Charts, AI Genie

## Pay-Yourself-First in SenticMoney

**Core Principle:** Prioritize savings by setting money aside before spending on anything else.

**Setup Steps:**
1. **Financial Goals** — Create savings goals with target amounts and dates (emergency fund, vacation, down payment)
2. **Income Sources** — Track when paychecks arrive
3. **Runway Reserves** — Add savings transfers as "Reserve" items in each Runway period, marked as first priority
4. **Budgets** — Budget remaining income after savings allocation
5. **AI Genie** — Ask "Am I on track with my savings goals?" for progress updates

**Key Features Used:** Financial Goals, Runway (Reserves), Income Sources, AI Genie

## Paycheck-to-Paycheck Cash Flow (Runway Method)

**Core Principle:** Plan finances around pay periods, not calendar months. Know exactly what you have to live on between paychecks.

**Setup Steps:**
1. **Runway** — Create a period aligned with your pay dates
2. **Auto-Populate** — Pull in income, bills, and prorated budgets automatically
3. **Living Money** — Monitor your true spending cushion after all obligations
4. **$/Day** — Know your daily safe-to-spend amount
5. **Generate Periods** — Project 2-3 pay periods ahead to spot cash crunches before they happen

**This is SenticMoney's unique innovation.** No other consumer budgeting app offers payday-to-payday cash flow planning with Living Money and $/Day metrics. The Runway feature is exclusive to SenticMoney.

**Key Features Used:** Runway (all features), Income Sources, Bills, Budgets

## Hybrid Approaches

Most real-world budgeters combine methods. Common hybrids that SenticMoney supports:

- **Pay-Yourself-First + Envelope:** Set savings goals first (Goals + Runway Reserves), then use envelope-style budgets for remaining spending categories
- **Zero-Based + Cash Flow:** Allocate every dollar (Budgets), but plan around pay periods instead of calendar months (Runway)
- **50/30/20 + Envelope:** Use percentage splits as guardrails, then manage individual categories as envelopes with hard limits
- **Any Method + AI Genie:** Regardless of methodology, the Genie analyzes your actual spending patterns and provides insights tailored to however you've set up the app

---

# Categories & Mappings

## Managing Categories & Automatic Mappings

Categories help you organize your transactions into meaningful groups for better financial tracking and reporting.

### What are Categories?

Categories organize financial data by grouping related transactions:
- Track where your money goes
- Create meaningful reports and visualizations
- Set up effective budgets
- Identify spending patterns
- Tax preparation and planning

### Default Categories

SenticMoney includes:
- **Income** - Salary, interest, dividends
- **Housing** - Rent, mortgage, property taxes
- **Transportation** - Car payments, gas, public transit
- **Food** - Groceries, restaurants
- **Utilities** - Electricity, water, gas, internet
- **Entertainment** - Streaming services, movies, hobbies
- **Healthcare** - Insurance, doctor visits, prescriptions
- **Personal** - Clothing, haircuts, gym memberships
- **Debt Payments** - Credit card payments, student loans
- **Savings** - Contributions to savings or investments
- **Miscellaneous** - Expenses that don't fit other categories

### Understanding Subcategories

Subcategories allow hierarchical organization without cluttering your top-level category list:
- **Two-level hierarchy**: Parent -> Child (e.g., Utilities -> Electric)
- **Flexible organization**: Group related expenses under a parent
- **Parent categories selectable**: Choose "Utilities (All)" for combined bills or specific subcategories
- **Clean dropdowns**: Transaction forms show organized optgroups

**Example Subcategory Structures**:

**Utilities**: Electric, Water, Sewer, Trash, Gas, Internet, Phone

**Entertainment**: Streaming Services, Movies & Theater, Gaming, Concerts & Events, Hobbies

**Government Services**: Post Office, Passport Fees, License Renewals, Permits, Taxes

### Creating a Subcategory

1. Click **Add Category/Subcategory**
2. Enter the subcategory name (e.g., "Post Office")
3. In **Parent Category** dropdown, select the parent (e.g., "Government Services")
4. Add description, icon, and color
5. Click **Save**

### Category Mappings

Category Mappings are rules that automatically assign categories to transactions based on keywords:
- Saves time by eliminating manual categorization
- Ensures consistent categorization
- Improves accuracy of reports and budgets
- Trains the system to become smarter over time

**How Mappings Work**:
1. System scans the transaction description for keywords
2. Checks if keywords match your defined mappings
3. If match found, automatically assigns the corresponding category
4. If multiple matches, uses the most specific mapping

### Creating a Mapping

1. Navigate to Categories page and click **Mappings** tab
2. Click **Add Mapping**
3. Enter:
   - **Keyword**: Word or phrase in transaction descriptions (e.g., "STARBUCKS")
   - **Category**: Which category to assign when keyword is found
4. Click **Save**

### Mapping Best Practices

1. **Be specific with keywords** - Use unique portions of merchant names
2. **Start with frequent transactions** - Focus on merchants you use regularly
3. **Use consistent capitalization** - Mappings are case-insensitive but consistency helps
4. **Review transaction imports** - Check for uncategorized items and create mappings
5. **Use partial keywords strategically** - "AMZN" catches "AMZN MKTP", "AMZN.COM", etc.

---

# Income Sources

## Managing Your Income Sources

The Income Sources feature helps you track all your income streams, providing a clear picture of how much money you're bringing in and when to expect it.

### What are Income Sources?

Income Sources represent all the ways you earn money:
- Regular employment salary or wages
- Social Security benefits
- Pension payments
- Rental income
- Investment income
- Side hustles or freelance work
- Business income
- Retirement account distributions

### Benefits of Tracking Income Sources

- Know exactly how much money you're earning each month
- Plan for upcoming expenses based on when income will arrive
- Easily see how your income compares to expenses
- Track changes in your income over time
- Link budgets to specific income sources

### Adding an Income Source

1. Navigate to Income Sources page and click **Add Income Source**
2. Fill in required information:
   - **Name**: Descriptive name (e.g., "Main Job Salary")
   - **Amount**: Payment amount
   - **Frequency**: How often you receive income (weekly, bi-weekly, monthly)
   - **Payment Day**: Which day you receive income
   - **Category**: Usually "Income"
   - **Notes**: (Optional) Additional information
3. Click **Save**

**Tip**: For variable income like freelance or commission-based work, enter an average or base amount. You can update actual amounts when recording transactions.

### Income Source Status Indicators

- **Active**: Included in income calculations
- **Inactive**: Temporarily paused or no longer receiving

**Tip**: Instead of deleting an income source you no longer receive, mark it as Inactive. This preserves financial history for accurate reporting.

### Payment Schedule Options

**Weekly Payments**: Select the day of the week you receive payment; system calculates payment dates for every week.

**Bi-Weekly Payments**: Select day of the week and set "next payment date" to ensure correct pay weeks.

**Monthly Payments**: Select day of the month; for "last day of month" select 31 (system adjusts for shorter months).

### Linking Income to Budgets

1. Go to the **Budgets** page
2. Click **Add Budget** or **Edit** existing budget
3. Find **Income Source** dropdown
4. Select which income source should fund this budget
5. Save the budget

**Benefits**:
- **Better Cash Flow Management**: Know which expenses are covered by which income
- **Improved Planning**: Align expense timing with income timing
- **Household Coordination**: Track which partner's income covers which expenses

---

# Financial Goals

## Setting and Achieving Your Financial Goals

The Financial Goals feature helps you set, track, and achieve important financial milestones.

### What are Financial Goals?

Financial Goals are specific objectives you want to achieve:
- Building an emergency fund
- Saving for a down payment on a home
- Paying off credit card debt or student loans
- Saving for retirement
- Setting aside money for a vacation
- Funding education
- Building investment portfolio value
- Making a major purchase (car, appliance)

### Benefits of Setting Financial Goals

- Provides clear direction for financial decisions
- Helps prioritize spending and saving
- Gives a sense of progress and accomplishment
- Increases chances of financial success
- Makes abstract financial concepts tangible
- Helps stay motivated with visual progress tracking

### Creating a Financial Goal

1. Navigate to Financial Goals page and click **Add New Goal**
2. Fill in required information:
   - **Name**: Descriptive name (e.g., "Emergency Fund")
   - **Description**: Details about what you're saving for
   - **Target Amount**: Total amount needed
   - **Current Amount**: How much already saved
   - **Target Date**: (Optional) Deadline for achieving goal
   - **Priority**: High, Medium, or Low
   - **Category**: (Optional)
   - **Status**: Usually "In Progress"
   - **Notes**: (Optional) Additional details
3. Click **Save**

### Goal Status Indicators

- **In Progress**: Actively working toward goal
- **Completed**: Reached target amount
- **On Hold**: Temporarily paused progress

### Priority Levels

- **High Priority** (Red): Most important financial goals
- **Medium Priority** (Yellow): Important but not urgent
- **Low Priority** (Blue): Nice-to-have, not urgent

### Progress Tracking

- **Progress Bar**: Visual representation of progress toward target
- **Percentage Complete**: Exact percentage of goal reached
- **Current Amount**: How much saved so far
- **Target Amount**: Ultimate goal
- **Days Remaining**: If target date set, shows days left
- **On Track Indicator**: Shows whether you're on pace

### SMART Goal Framework

- **Specific**: Clearly define what you want ("Save $10,000" instead of "Save money")
- **Measurable**: Include a way to track progress
- **Achievable**: Set realistic goals you can actually reach
- **Relevant**: Choose goals that align with your broader financial plan
- **Time-bound**: Set a target date to create urgency

### Goal Types and Examples

**Short-Term Goals (0-1 year)**:
- Emergency Fund Phase 1: $1,000 - $5,000
- Vacation Fund: $1,000 - $3,000
- Holiday Savings: $500 - $1,500
- Major Purchase: $500 - $2,000

**Medium-Term Goals (1-5 years)**:
- Full Emergency Fund (3-6 months): $5,000 - $30,000
- Vehicle Purchase: $2,000 - $20,000
- Debt Elimination: Variable
- Home Renovation: $5,000 - $30,000

**Long-Term Goals (5+ years)**:
- Home Down Payment: $20,000 - $100,000+
- Retirement: $500,000 - $2,000,000+
- College Fund: $20,000 - $150,000 per child
- Starting a Business: $10,000 - $100,000+

### Best Practices

1. **Automate contributions** - Set up automatic transfers to goal accounts
2. **Track progress regularly** - Update goals at least monthly
3. **Start small and build** - Begin with achievable goals to build momentum
4. **Celebrate milestones** - Recognize when you hit 25%, 50%, 75%
5. **Review and adjust** - Life changes, so should your goals
6. **Visualize success** - Add images or vision boards to descriptions
7. **Share selected goals** - Tell others for accountability
8. **Use windfalls wisely** - Dedicate tax refunds, bonuses to goal progress

---

# Reminders

## Managing Your Financial Reminders

The Reminders feature helps you stay on top of important financial events, ensuring you never miss a payment or financial opportunity.

### What are Financial Reminders?

Reminders are notifications that alert you about important financial events:
- Upcoming bill payments
- Subscription renewals
- Pending financial goals
- Irregular but important financial tasks (tax deadlines, insurance renewals)
- Budget reviews
- Account balance checks

### Benefits of Using Reminders

- Avoid late payment fees
- Maintain a good credit score by paying bills on time
- Stay mindful of financial obligations
- Remember important but infrequent financial tasks
- Keep financial management proactive rather than reactive

### Creating a Reminder

1. Navigate to Reminders page and click **Add Reminder**
2. Fill in required information:
   - **Title**: Clear, descriptive title
   - **Description**: (Optional) More details
   - **Due Date**: When the task is due
   - **Amount**: (Optional) Dollar amount if for a payment
   - **Category**: (Optional) Associate with a financial category
   - **Notification Date**: When you want to be reminded (typically days before due date)
   - **Recurring**: Toggle on if reminder should repeat
   - **Recurrence Pattern**: If recurring, select Daily, Weekly, Monthly, or Yearly
3. Click **Save**

### Reminder Types and Timing

| Reminder Type | Example Title | Suggested Timing |
|---------------|---------------|------------------|
| Bill Payment | Pay Credit Card Bill | 5 days before due date |
| Subscription | Review Netflix Subscription | 7 days before renewal |
| Financial Review | Monthly Budget Review | Last day of each month |
| Tax-Related | Submit Quarterly Tax Payment | 1 week before deadline |
| Insurance | Renew Auto Insurance | 14 days before expiration |

### Recurrence Patterns

- **Daily**: Repeats every day (useful for daily financial check-ins)
- **Weekly**: Repeats on the same day each week
- **Monthly**: Repeats on the same day each month (e.g., 15th)
- **Yearly**: Repeats on the same date each year (ideal for annual renewals)

### How Completed Recurring Reminders Work

1. Current instance is marked as completed
2. New instance is automatically generated for next occurrence
3. Completed instance moves to reminder history

### Best Practices

1. **Use clear, action-oriented titles** - "Pay Home Insurance Premium" is better than "Insurance"
2. **Set appropriate notification dates** - Give yourself enough time to prepare
3. **Include amount information** - Helps with financial planning
4. **Assign categories** - Helps organize your financial life
5. **Use the description field** - Add account numbers, website URLs, instructions
6. **Mark complete promptly** - Update reminders as soon as you complete tasks
7. **Review periodically** - Ensure reminders are still relevant

### Comprehensive Reminder System

**Weekly Reminders**:
- Review recent transactions
- Check account balances
- Process pending bills

**Monthly Reminders**:
- Pay all monthly bills
- Review budget performance
- Transfer money to savings
- Check credit card statements

**Quarterly Reminders**:
- Pay estimated taxes (if applicable)
- Review investment performance
- Check credit reports
- Adjust budget as needed

**Annual Reminders**:
- File tax returns
- Renew insurance policies
- Review financial goals
- Conduct annual financial review
- Check for unused subscriptions to cancel

---

# Tags

## Using Tags to Organize Your Finances

Tags provide a flexible way to organize financial data beyond traditional categories, allowing custom groupings and tracking spending across multiple dimensions.

### What are Tags?

Tags are flexible labels you can apply to transactions. Unlike categories (where a transaction can only belong to one category), you can apply multiple tags to a single transaction.

### Tags vs. Categories

| Categories | Tags |
|-----------|------|
| One category per transaction | Multiple tags per transaction |
| Hierarchical structure | Flat structure |
| Used for budget tracking | Used for flexible grouping |
| Example: "Groceries" or "Dining Out" | Example: "Vacation", "Tax Deductible", "Kids" |

### Benefits of Using Tags

- **Cross-category tracking**: Track expenses spanning multiple categories
- **Project-based tracking**: Group all expenses related to a specific project
- **Person-specific tracking**: Tag transactions by family member
- **Tax preparation**: Mark tax-deductible expenses across categories
- **Temporary tracking needs**: Create ad-hoc groupings without changing category structure
- **Reimbursable expenses**: Track expenses that will be reimbursed

### Adding Tags to Transactions

1. Fill in standard transaction details (date, amount, etc.)
2. In the **Tags** field, type your desired tags
3. Start each tag with a # symbol (e.g., #Vacation)
4. Separate multiple tags with commas (e.g., #Vacation, #Family, #Summer2023)
5. Save the transaction

### Recommended Tag Systems

**Project-Based Tags**:
- #HomeRenovation: All home improvement expenses
- #Wedding: All wedding-related expenses
- #Vacation2023: All expenses for a specific trip
- #NewBaby: All expenses related to a new child

**Person-Based Tags**:
- #John, #Mary: Tag by person who made purchase
- #Kids: All child-related expenses
- #Shared: Expenses benefiting entire household

**Financial Purpose Tags**:
- #TaxDeductible: Expenses you can deduct on taxes
- #Investment: Purchases that appreciate or generate income
- #Reimbursable: Expenses you expect to be paid back for
- #DebtPayoff: Payments toward reducing debt

**Quality of Life Tags**:
- #Need: Essential expenses
- #Want: Discretionary spending
- #Splurge: Luxury or impulse purchases
- #SelfCare: Expenses related to health and wellbeing

**Temporal Tags**:
- #Holiday: Seasonal or holiday-related expenses
- #Birthday: Gift and celebration expenses
- #Summer2023: Seasonal tracking
- #OneTime: Non-recurring expenses

### Common Use Cases

**Tax Preparation**:
- Tag all potentially deductible expenses with #TaxDeductible
- Create specific tags like #MedicalExpense or #CharitableDonation
- At tax time, search by these tags to find all relevant transactions

**Vacation and Trip Tracking**:
- Create a unique tag for each trip (e.g., "#Italy2023")
- Tag all related expenses, regardless of category
- After the trip, search by tag to see total cost breakdown

**Business Expense Reimbursement**:
- Tag work expenses with #Reimbursable
- Add tags for specific projects or clients
- Add #Reimbursed once paid back

---

# Bills & Accounts Payable

## Managing Your Bills and Accounts Payable

The Bills feature helps you track all your recurring expenses, ensuring you never miss a payment.

### What are Accounts Payable?

"Accounts Payable" or "Bills" represent any regular payment obligation:
- Monthly subscriptions (Netflix, Spotify)
- Utility bills (electricity, water, internet)
- Rent or mortgage payments
- Insurance premiums
- Credit card minimum payments
- Loan installments
- Annual memberships

### Adding a New Bill

1. Navigate to Bills page and click **Add Account Payable**
2. Fill in required information:
   - **Subscription Name**: Descriptive name (e.g., "Netflix Subscription")
   - **Amount**: Payment amount
   - **Category**: Appropriate category (helps with budget tracking)
   - **Billing Cycle**: Monthly or Yearly
   - **Start Date**: When subscription begins
   - **End Date**: (Optional) If subscription has known end date
   - **Next Payment Date**: When next payment is due
   - **Description**: (Optional) Details about what bill covers
   - **Notes**: (Optional) Additional information
   - **Vendor URL**: (Optional) Website for making payment
   - **Link to Income Source**: (Optional) Connect to specific income source
3. Click **Save**

**Tip**: For bills that vary in amount each month (like utilities), enter an average or estimated amount. You can update when you receive the actual bill.

### Bill Status Indicators

- **Active**: Bill is active and included in expenses
- **Inactive**: Bill is inactive (temporarily paused or cancelled)
- **Due today**: Payment is due today
- **Overdue**: Payment is past due
- **Coming up**: Payment is due soon
- **Paid**: Bill has been paid for current period

### Bill Payment Tracking

**Automatic Detection**: When you record a transaction that matches a bill (by name or description), SenticMoney automatically marks that bill as paid when:
- Transaction description contains the bill name
- Transaction amount matches or is close to bill amount
- Transaction date is within reasonable window of due date

**Manual Marking**: Click the check button next to any bill to manually mark as paid.

### Next Payment Date Calculation

When a bill is marked as paid:
- **Monthly bills**: Next payment set to one month after current due date
- **Yearly bills**: Next payment set to one year after current due date

### Best Practices

1. **Be comprehensive** - Add ALL recurring bills, even small ones
2. **Be precise with due dates** - Set exact payment due date to avoid late fees
3. **Use consistent naming** - Name bills to match transaction history
4. **Review regularly** - Check Bills dashboard weekly
5. **Batch your bills** - Align payment dates around the same time when possible
6. **Include vendor URLs** - Add payment website links
7. **Set up reminders** - Use Reminders feature for notifications before due
8. **Audit annually** - Review all subscriptions to identify ones you no longer use

### Subscription Management Strategy

- Consider rotating entertainment subscriptions instead of all active at once
- Look for annual payment options that offer discounts vs monthly
- Share family plans where appropriate to reduce per-person costs
- Set a "subscription budget" and stick to it
- Use monthly equivalent view to understand true cost

---

# Backup Management

## Backup System Overview

The SenticMoney backup system helps protect your financial data by creating copies of your database and application files.

### Types of Backups

- **Database Backup**: Creates a copy of your database file only (transactions, categories, budgets, etc.)
- **Full Application Backup**: Creates a complete backup of your entire SenticMoney application including database, code, and configuration

### Two-Location Backup System

SenticMoney uses a dual-backup approach for maximum data protection:

- **Primary Backup (Automatic)**: Always saved to safe location in AppData folder. Happens automatically, no configuration needed.
- **Secondary Backup (Recommended)**: Add a second backup location for extra protection. We strongly recommend an external drive, USB drive, or cloud-synced folder (Google Drive, OneDrive).

**Why use a secondary backup?** If your computer's main drive fails, you can reinstall SenticMoney and restore data from the secondary location.

### Creating Backups

**Database Backup**:
1. Navigate to Backup Management
2. Click **Database Backup** button
3. System creates backup file: `app_backup_YYYYMMDD_HHMMSS.db`
4. Confirmation message when complete

**Full Application Backup**:
1. Navigate to Backup Management
2. Click **Full Application Backup** button
3. System creates: `sentic_money_full_backup_YYYYMMDD_HHMMSS.zip`
4. Process may take longer than database-only backup
5. Confirmation shows how many locations successfully backed up

### Configuring Backup Locations

**Primary Backup Location (Automatic)**:
`C:\Users\YourName\AppData\Local\SenticMoneyMoney\backups`
No configuration needed.

**Adding a Secondary Backup Location**:
1. Navigate to Backup Management
2. Click **Backup Settings**
3. Enter full path to secondary backup location
4. Click **Save Settings**

**Recommended Secondary Locations**:
- External Hard Drive: `E:\Backups\SenticMoneyMoney`
- USB Thumb Drive: `F:\SenticMoneyMoney`
- Google Drive: `C:\Users\YourName\Google Drive\Backups`
- OneDrive: `C:\Users\YourName\OneDrive\Backups`
- Dropbox: `C:\Users\YourName\Dropbox\Backups`

### Disaster Recovery

**If Your Computer Fails**:
1. Install SenticMoney on new computer
2. Locate backup files from secondary backup location
3. Copy database backup file (.db) to: `C:\Users\YourName\AppData\Local\SenticMoneyMoney\`
4. Rename backup file to `sentic_money.db`
5. Start SenticMoney - your data will be restored

**Restoring on Same Computer**:
1. Download desired database backup from Backup Management
2. Shut down SenticMoney completely
3. Navigate to `C:\Users\YourName\AppData\Local\SenticMoneyMoney\`
4. Rename current `sentic_money.db` to `sentic_money_old.db`
5. Rename downloaded backup to `sentic_money.db`
6. Restart SenticMoney

**Tip**: To quickly open AppData folder, press Win + R, type `%LOCALAPPDATA%\SenticMoneyMoney` and press Enter.

### Backup Best Practices

**Backup Frequency**:
- **Regular Users**: Full backup monthly, database backup weekly
- **Heavy Users**: Full backup weekly, database backup daily or after significant data entry

**Backup Retention**:
- Keep at least last three full backups
- Maintain rotation of database backups covering last month
- Periodically archive older backups to long-term storage

**When to Create Extra Backups**:
- Before upgrading application
- Before importing large amounts of data
- Before database maintenance
- After completing annual financial reconciliation
- Before making significant changes to categories or structure

---

# Reconciliation

## Balance Reconciliation

The Reconcile feature helps you adjust your SenticMoney balance to match your actual bank account balance.

### What is Balance Reconciliation?

Balance reconciliation compares your SenticMoney's total balance with your actual bank account balance and makes adjustments to ensure they match:
- Correct discrepancies between recorded and actual balances
- Account for transactions you might have missed
- Ensure your financial data is accurate
- Maintain integrity of budgets and reports
- Prevent financial planning based on incorrect information

### When to Reconcile

- At least once a month when you receive bank statements
- Before making major financial decisions
- When you notice discrepancies in account balance
- After importing transactions from external sources

### How Reconciliation Works

1. App shows your current total balance (all income minus all expenses ever recorded)
2. You enter your actual bank account balance
3. App calculates the difference
4. An adjustment transaction is created to account for this difference

### Types of Adjustments

- **Positive Adjustment**: If actual balance is higher than app balance, income adjustment created
- **Negative Adjustment**: If actual balance is lower than app balance, expense adjustment created
- **No Adjustment**: If balances already match, no adjustment needed

### Performing a Reconciliation

1. Access Reconcile page (More > Reconcile or from Transactions page)
2. Review current app balance (automatically displayed)
3. Enter actual bank balance
4. Review adjustment preview
5. Add optional description (e.g., "Monthly reconciliation")
6. Click **Reconcile Balance**

### The Adjustment Transaction

When you complete reconciliation, SenticMoney:
- Creates new transaction in "Adjustments" category
- Sets amount to difference between app and actual balances
- Adds description prefixed with "Adjustment (increase)" or "Adjustment (decrease)"
- Tags transaction with "adjustment" and "reconciliation" tags
- Includes notes with starting and ending balance details

### Common Causes of Discrepancies

| Discrepancy | Common Cause |
|-------------|--------------|
| Small positive amounts | Interest payments or small refunds |
| Small negative amounts | Bank fees or service charges |
| Large discrepancies | Major transactions not recorded |
| Recurring discrepancies | Automatic payments or subscriptions not tracked |
| Gradually increasing discrepancies | Consistent small transactions being missed |

### Best Practices

1. **Reconcile regularly** - Monthly helps catch errors early
2. **Check for pending transactions** - Note transactions that haven't cleared
3. **Use descriptive adjustment notes** - Add details to remember why adjustment was made
4. **Investigate large discrepancies** - Identify specific missing transactions before large adjustment
5. **Update records first** - If you know what's causing discrepancy, add those transactions before reconciling
6. **Verify the adjustment** - After reconciling, check that app balance matches actual balance

---

# Financial Health

## Understanding Your Financial Health

The Financial Health feature provides a comprehensive assessment of your overall financial wellbeing, helping you identify strengths, weaknesses, and opportunities for improvement.

### What is Financial Health?

Financial health refers to the overall condition of your financial situation:
- How well you manage day-to-day finances
- Your ability to absorb financial shocks
- Whether you're on track to meet financial goals
- The freedom you have to make choices that improve your life

### Why Financial Health Matters

- Provides a holistic view beyond individual transactions or accounts
- Helps identify areas needing improvement
- Measures progress toward long-term financial security
- Connects daily financial decisions to big-picture outcomes
- Reduces financial stress by giving clarity and direction

### Financial Health Dimensions

SenticMoney evaluates financial health across multiple dimensions:
- **Spending Management**: How well you live within your means
- **Savings Rate**: How much of your income you save
- **Debt Management**: How effectively you manage and reduce debt
- **Emergency Preparedness**: Your ability to handle unexpected expenses
- **Goal Progress**: How well you're tracking toward financial goals
- **Financial Behaviors**: Consistency of positive financial habits

### Your Financial Health Score

The Financial Health Score is a numeric rating from 0-100:
- **80-100**: Excellent - Strong financial management across all dimensions
- **60-79**: Good - Solid financial habits with some areas for improvement
- **40-59**: Fair - Managing in some areas but significant opportunities for improvement
- **0-39**: Needs Attention - Several key areas requiring immediate focus

### How Your Score is Calculated

Your score is derived from four key dimensions, each contributing up to 25 points:

| Dimension | Weight | What It Measures | Target |
|-----------|--------|------------------|--------|
| Savings Rate | 25% | How much of income you save | 20% or higher |
| Debt-to-Income Ratio | 25% | Proportion of monthly income going to debt | Below 36% |
| Emergency Fund | 25% | How many months of expenses emergency fund covers | 3-6 months |
| Expense-to-Income Ratio | 25% | Proportion of income going to regular expenses | Below 50% |

### Understanding Each Dimension

**Savings Rate**:
- **Calculation**: (Income - Expenses) / Income x 100%
- **Target**: 20% or higher saved
- **Why it matters**: Foundation of wealth building and future financial security

**Debt-to-Income Ratio**:
- **Calculation**: Monthly Debt Payments / Monthly Income x 100%
- **Target**: Below 36%
- **Why it matters**: Lower debt ratios mean more financial flexibility

**Emergency Fund**:
- **Calculation**: Emergency Fund Amount / Monthly Expenses
- **Target**: 3-6 months of expenses covered
- **Setup**: Create a Financial Goal named "Emergency Fund" to track
- **Why it matters**: Prevents going into debt when unexpected expenses arise

**Expense-to-Income Ratio**:
- **Calculation**: Monthly Expenses / Monthly Income x 100%
- **Target**: Below 50%
- **Why it matters**: Lower fixed expenses provide more flexibility

### Improving Your Financial Health

**Recommendation Triggers**:
- Savings Rate: Recommendation triggered if below 15%
- Debt-to-Income Ratio: Recommendation triggered if above 30%
- Emergency Fund: Recommendation triggered if below 3 months of expenses
- Expense-to-Income Ratio: Recommendation triggered if above 70%

**Improvement Strategies by Dimension**:

*Improving Savings Rate*:
- Track all income
- Properly categorize expenses
- Increase income gap
- Automate savings
- Follow the 50/30/20 rule

*Reducing Debt-to-Income Ratio*:
- List all debts
- Use debt reduction strategies (snowball or avalanche method)
- Avoid new debt
- Refinance when possible
- Increase income

*Building Emergency Fund*:
- Create an Emergency Fund goal
- Start small ($1,000)
- Update progress
- Build gradually (1 month, then 3, then 6)
- Use separate accounts

*Optimizing Expense-to-Income Ratio*:
- Audit subscriptions
- Negotiate rates
- Consolidate services
- Track fixed expenses
- Rethink housing costs (aim for 25-30% of income)

---

# Financial Calendar

## Using Your Financial Calendar

The Financial Calendar provides a visual timeline of your upcoming bills, income payments, and financial reminders, helping you plan and prepare for important financial events.

### What is the Financial Calendar?

The Financial Calendar:
- Displays all upcoming financial events in calendar format
- Helps visualize when bills are due, income arrives, and reminders occur
- Allows you to anticipate cash flow needs throughout the month
- Provides centralized view of your financial timeline
- Helps prevent missed payments and financial surprises

### Calendar Event Types

- **Income**: Expected money coming in from your defined income sources
- **Subscriptions**: Recurring bill payments you need to make
- **Expenses**: One-time expenses from transactions
- **Reminders**: Financial tasks and deadlines you've set
- **Notifications**: Alerts for upcoming reminders

### Calendar View

The Financial Calendar provides a three-month rolling view:
- See three months at once in traditional calendar grid format
- View events color-coded by type
- Quickly spot busy financial days and plan around them
- Perfect for both immediate and forward planning
- Today's date highlighted for quick reference

### Color Coding

| Event Type | Color | Description |
|------------|-------|-------------|
| Income | Green | Money coming in from income sources |
| Expense | Red | One-time expenses from transactions |
| Subscription | Yellow | Recurring subscription and bill payments |
| Reminder | Yellow | Bill and task reminders |
| Notification | Light green | Notifications for upcoming reminders |

### Calendar Benefits and Use Cases

**Cash Flow Planning**:
- Identify days when multiple bills are due
- See when income arrives relative to bill due dates
- Plan discretionary spending around financial commitments
- Spot potential cash flow problems before they occur

**Avoiding Late Payments**:
- See upcoming bills and due dates at a glance
- Get visual notifications for important reminders
- Plan ahead for recurring bills and subscriptions
- Ensure sufficient funds available before bills are due

**Financial Decision-Making**:
- Identify best times to make large purchases
- Schedule transactions when balance will be highest
- Avoid scheduling new bills near existing payment clusters
- Plan future financial commitments with better timing

### Best Practices

1. **Regular reviews** - Check calendar weekly to prepare for upcoming events
2. **Maintain data accuracy** - Keep income sources, bills, and reminders up-to-date
3. **Add buffer days** - Set reminders a few days before actual deadlines
4. **Use notification dates** - Take advantage of reminder notification dates
5. **Balance bill scheduling** - Stagger bills throughout month when possible
6. **Add descriptive details** - Use clear names for reminders, income sources, subscriptions
7. **Include amounts** - Always include accurate amounts to see financial impact

---

# Accounting Dashboard

## Understanding Your Accounting Dashboard

The Accounting Dashboard provides a comprehensive overview of your financial position with financial statements and reports.

### What is the Accounting Dashboard?

The Accounting Dashboard is a financial reporting interface providing:
- A view of your financial position from an accounting perspective
- Basic financial statements (Income Statement, Balance Sheet, Cash Flow)
- Tax reporting capabilities
- Data export functionality
- Money Flow Sankey chart (income-to-expense visualization with Planned and Actual views)

### Available Financial Statements

**Income Statement**:
Shows your income, expenses, and net income over a specified period:
- Summary of total income, expenses, and net income
- Breakdown of income by source with percentage distribution
- Breakdown of expenses by category with percentage distribution
- Visual representations of income and expense distributions
- Detailed transaction listings

**Balance Sheet**:
This simplified balance sheet provides:
- Summary of total assets (income) and liabilities (expenses)
- Calculation of net worth
- Listing of income sources as assets with monthly and annual amounts
- Listing of active subscriptions as liabilities
- Visual representation of asset and liability distributions
- Basic financial health indicators including income-to-expense ratio

**Cash Flow Statement**:
Tracks your daily cash flow:
- Daily record of income and expenses for selected month
- Running balance calculation
- Month and year selection for historical data viewing
- Net cash flow calculation (positive or negative)

### Financial Health Indicators

**Income/Expense Ratio**:
Calculated as: Total Monthly Income / Monthly Expenses
- **2.0 or higher**: Excellent (income more than twice expenses)
- **1.5 to 1.99**: Good (income significantly higher than expenses)
- **1.0 to 1.49**: Adequate (income covers expenses with little margin)
- **Below 1.0**: Concerning (expenses exceed income)

**Net Worth Status**:
- Calculated as: Total Assets - Total Liabilities
- Positive net worth indicates assets exceed liabilities
- Negative net worth indicates liabilities exceed assets

### Tax Reports

The Tax Report feature helps organize financial information for tax preparation:
- Annual summary by tax year
- Total income calculation with breakdown by source
- Total expenses calculation with breakdown by category
- Visual charts showing income and expense distributions
- Detailed transaction listings filterable by type and category

**Note**: The tax report is designed to help organize financial information but should not be considered tax advice. Always consult with a tax professional.

### Data Export

Export financial data for use in external software:

**Export Options**:
- **Date Range Selection**: Choose the time period
- **Format Options**:
  - **JSON**: Best for web applications or programming environments
  - **CSV**: Compatible with most spreadsheet applications and financial software
  - **Excel**: Ready to use in Microsoft Excel

**Common Export Uses**:
- Importing transactions into accounting software
- Creating custom reports in spreadsheet applications
- Sharing financial data with advisors or accountants
- Creating data backups
- Performing advanced analysis using specialized tools

### Money Flow Sankey Chart

The Accounting Dashboard includes an interactive Sankey diagram that visualizes how your income flows through your expense categories. This is a Standard tier feature.

**Two Views:**

**Planned View:**
- Maps budget allocations and bill amounts to their linked income sources
- Shows how you intend your income to be distributed across spending categories
- Income sources appear on the left, expense categories on the right
- Flow width represents the dollar amount allocated
- Useful for seeing whether your planned budget accounts for all income

**Actual View:**
- Shows real transaction data for a selected month
- Income flows on the left, actual expense categories on the right
- Includes a savings rate calculation (income minus expenses)
- Dollar totals displayed on each node for easy reading
- Hover for tooltips with exact amounts and percentages

**How Income Linking Works:**
- Budgets and bills can be linked to specific income sources
- Budgets support multi-source income linking (e.g., groceries funded by both paychecks)
- Income transactions can be linked to income sources on Add/Edit Transaction
- Imported income is auto-matched to sources by amount
- Unlinked expenses appear in a general flow

**How to Read the Chart:**
- Wider flows = more money moving through that path
- Left side = where money comes from (income sources)
- Right side = where money goes (expense categories)
- The gap between income and expenses represents your savings
- A "How to Read" guide is available directly on the page

**Use Cases:**
- Visualize whether specific paychecks cover specific obligations
- Identify which expense categories consume the most income
- Compare planned vs. actual spending distribution
- Show clients or partners a clear picture of household cash flow
- Spot savings rate changes month over month

### Best Practices

**Recommended Review Process**:
1. Review Income Statement monthly
2. Check Balance Sheet for significant changes
3. Review Cash Flow statement to understand daily patterns
4. Check Income/Expense ratio for financial stability
5. Update tax report quarterly
6. Export data monthly for backup purposes

**Quarterly Actions**:
- Generate financial statements for the quarter
- Review quarterly tax report
- Check progress on financial goals
- Verify income sources and subscriptions are accurate

**Annual Actions**:
- Generate annual financial statements
- Prepare annual tax report
- Export complete annual data
- Review all income sources and subscriptions
- Save annual reports for long-term records

---

# SenticMoney Genie (AI Financial Insights)

## Understanding the SenticMoney Genie

The SenticMoney Genie is an AI-powered financial assistant that analyzes your financial data and provides personalized recommendations, observations, and opportunities. Powered by Google's Gemini 3.1 Pro model.

### What is the SenticMoney Genie?

The Genie analyzes your financial data to provide:
- Detection of unusual spending patterns
- Identification of saving opportunities
- Recommendations for budget adjustments
- Analysis of spending trends
- Personalized financial advice based on transaction history
- Answers to specific questions about your finances
- Search through transaction notes and #tags for context-aware answers
- Page-aware responses (knows what page you're on)
- Receipt scanning via AI Vision (photos, email .eml, text .txt — line-item extraction)
- Onboarding guidance and setup progress tracking
- File attachment analysis (bank statements, receipts, documents)

### Privacy: Financial Snapshot Architecture

**Your financial data stays on your computer.** The Genie uses a Financial Snapshot approach:
- On every query, an **aggregated financial summary** (~2-4K tokens) is generated from your local data
- This summary includes totals, categories, trends, and patterns — not individual transaction details
- The summary is sent to Google Gemini 3.1 Pro via SenticMoney's cloud proxy for processing
- **Receipt photos** and **file attachments** are processed by Gemini to extract information — the AI only sees the uploaded content
- No raw transaction data, bank credentials, or account numbers ever leave your device

### Accessing the SenticMoney Genie

**Floating Chat Widget (Quick Access)**:
- Look for the pulsing robot icon in the bottom-right corner
- Click to open chat window instantly
- Ask questions without leaving current page
- Genie knows what page you're on for context-aware help
- Conversation persists when you navigate between pages
- Drag to reposition anywhere on screen (PC/tablet)
- Resize the chat window (dimensions remembered across pages)
- Minimize to header bar when you need more screen space

**Full AI Page**:
- Navigate to Insights > AI Insights
- Access all advanced analysis options
- Use quick analysis buttons and date range selection
- Best for in-depth financial reviews

### Contextual Knowledge System

The Genie has deep knowledge of every SenticMoney feature through a conditional prompt system. When you're on a specific page, the Genie automatically loads relevant knowledge:

- **Dashboard**: Summary cards, Payment Timeline, chart types, "Three Numbers" distinction (Current Balance vs Available to Spend vs Living Money)
- **Runway**: Period setup, Auto-populate vs Sync Amounts, Living Money metric, $/Day calculations
- **Budgets**: Budget periods, carry forward, budgets vs bills distinction
- **Bills/Subscriptions**: Billing cycles, quick-pay, seasonal toggling, Private Information field
- **Import**: File formats, saved mappings, AI detection wizard, PDF vision
- **Goals, Income, Reconcile**: Feature-specific guidance and Q&As

### Onboarding Guide

For new users (setup less than 30% complete), the Genie automatically provides onboarding assistance:
- Setup progress tracking across 7 areas (profile, categories, income, bills, budgets, transactions, goals)
- Step-by-step guidance for initial setup
- Setup Guide compass button in chatbot header
- Proactive welcome message on first open

### File Attachments (v2.2)

Users can attach files directly in the Genie chat via paperclip button or drag-and-drop:

| File Type | Processing Method | Limits |
|-----------|------------------|--------|
| CSV, XLSX, TXT | Extracted locally, injected as text | 100 rows / 50K chars |
| PDF (text-based) | Extracted locally via pdfplumber | 20 pages |
| PDF (scanned/image) | Gemini 3.1 Pro vision | 20 pages |
| Images (JPG, PNG, GIF, WEBP) | Gemini 3.1 Pro multimodal vision | 10 MB |

The Genie compares attached files against your financial snapshot — flagging budget exceedances, identifying matching bills, and noting missing categories.

### Voice Input (v2.2)

Voice input via microphone button in the chat. Available on localhost or HTTPS connections only (browser security requirement). Mobile devices accessing via LAN IP (e.g., 192.168.x.x) over plain HTTP do not get voice input.

### Multilingual Support

The Genie converses in any language. Ask questions in Spanish, French, German, Japanese, or any other supported language — the Genie responds in the same language. No configuration required.

### Chatbot Features

**Conversation Persistence**:
- Your conversations stay intact as you browse
- Chatbot automatically reopens if it was open when you navigated
- Genie maintains context from previous questions
- Conversation clears when you close browser (privacy-friendly)

**Draggable Positioning** (PC/Tablet):
- Click and hold chatbot header
- Drag to any position on screen
- Position remembered across page navigation
- Double-click header to reset to default position and size

**Resizable Window**:
- Drag corner/edge to resize
- Dimensions saved to localStorage
- Double-click header resets both position and size

**Minimize Feature** (All Devices):
- Click minus (-) button to minimize
- Shows only header bar - conversation preserved
- Click plus (+) button to expand
- Minimize state persists across navigation

**Tags & Notes Access**:
- Genie can see and search transaction notes and #tags
- Find expenses with specific tags
- More contextual and accurate query results

### Free Tier Experience

Free/unlicensed users see a teaser experience when clicking the Genie button:
- Real-looking chat window opens with a static Genie message
- Previews Standard tier AI capabilities
- Input field visible but disabled
- "Upgrade to Standard" button links to upgrade page
- No API calls or tokens used

### Analysis Types

**Spending Analysis**:
- Breakdown of expenses by category
- Identification of spending trends over time
- Comparison of current spending to historical patterns
- Analysis of spending at specific merchants

**Budget Suggestions**:
- Recommendations for adjusting category budgets
- Identification of categories where you consistently overspend
- Suggestions for categories where you might reduce budgets
- Comparison to recommended budget guidelines (50/30/20 rule)

**Saving Opportunities**:
- Detection of recurring expenses that could be reduced
- Identification of spending categories with unusual increases
- Suggestions for cost-saving alternatives
- Analysis of subscription services and recurring charges

**Spending Trends**:
- Month-over-month comparison
- Identification of seasonal spending patterns
- Analysis of spending growth or reduction over time
- Comparison of different spending categories

**Anomaly Detection**:
- Identification of unusual transactions
- Detection of spending spikes in specific categories
- Recognition of potential duplicate charges
- Alerts for atypical payment amounts

**Prediction & Forecasting**:
- Estimation of future spending based on historical patterns
- Projection of when you'll reach savings goals
- Forecast of upcoming bill amounts
- Prediction of end-of-month balance

### Example Questions

- "How much did I spend on groceries last month?"
- "What are my most expensive recurring charges?"
- "Show me all transactions over $100 in October"
- "Compare my restaurant spending: this month vs last month"
- "Show me all #vacation expenses"
- "Find transactions with notes about 'car repair'"

### Device-Specific Behavior

| Device | Draggable | Minimize | Persistence |
|--------|-----------|----------|-------------|
| Mobile (<=768px) | No | Yes | Yes |
| Tablet/Desktop (>768px) | Yes | Yes | Yes |

### Pro Tips

- **Position chatbot** before starting analysis to avoid covering data you want to reference
- **Minimize chatbot** when viewing detailed tables or charts, then expand to ask questions
- **Navigate freely** while thinking about your next question - conversation will be there
- **Use tags liberally** in transactions - makes AI searches much more powerful

---

# Financial Calculators

## Free Financial Planning Tools

The Calculators page provides four interactive financial planning tools, all available on the Free tier with no subscription required. All calculators use Decimal arithmetic for precision with money calculations.

**Note**: Financial Calculators are a Free tier feature — accessible to all users.

### Accessing Calculators

Navigate to **Insights > Calculators** in the main navigation menu. Each calculator is presented as a tab on the Calculators page.

### Loan/Mortgage Payoff Calculator

Calculates how extra payments can accelerate your loan payoff and save on interest:

- **Inputs**: Loan balance, interest rate (APR), monthly payment, extra monthly payment
- **Outputs**:
  - Original payoff timeline (months and years)
  - New payoff timeline with extra payments
  - Time saved (months)
  - Total interest without extra payments
  - Total interest with extra payments
  - **Interest savings** from making extra payments

**Use cases**: Mortgage payoff planning, auto loan acceleration, student loan paydown strategy

### Credit Card Payoff Calculator

Shows how long it will take to pay off credit card debt and suggests an accelerated payment amount:

- **Inputs**: Credit card balance, interest rate (APR), monthly payment
- **Outputs**:
  - Months to pay off at current payment
  - Total interest paid
  - Total amount paid (principal + interest)
  - **Suggested payment** to pay off in 12 months
  - Interest saved with suggested payment

**Use cases**: Debt payoff planning, understanding true cost of carrying a balance, setting payment goals

### Compound Interest / Savings Calculator

Projects future value of savings with regular contributions and compound interest:

- **Inputs**: Initial deposit, monthly contribution, annual interest rate, time period (years)
- **Outputs**:
  - Future value of savings
  - Total contributions over the period
  - Total interest earned
  - **Interest as percentage** of final balance

**Use cases**: Emergency fund planning, retirement projections, savings goal feasibility, understanding the power of compounding

### Debt Snowball vs Avalanche Comparison

Compares the two most popular debt payoff strategies side by side:

- **Inputs**: List of debts with name, balance, interest rate, and minimum payment; plus extra monthly payment amount
- **Outputs for each strategy**:
  - Total months to become debt-free
  - Total interest paid
  - Payoff order of debts
  - **Comparison summary** showing which method saves more money vs. which provides faster psychological wins

**Snowball method**: Pay minimums on all debts, put extra money toward the smallest balance first. Provides quick wins for motivation.

**Avalanche method**: Pay minimums on all debts, put extra money toward the highest interest rate first. Mathematically optimal — saves the most money.

**Use cases**: Choosing a debt payoff strategy, understanding the cost difference between methods, creating a debt-free plan

### Best Practices

1. **Run scenarios** - Try different extra payment amounts to find what fits your budget
2. **Compare strategies** - Use the Snowball vs Avalanche calculator before committing to a debt payoff plan
3. **Be realistic** - Use actual interest rates from your statements, not estimates
4. **Revisit regularly** - As balances change, re-run calculators to update your plan
5. **Combine with budgets** - Use calculator results to set budget amounts for debt payments

---

# Runway Cash Flow Planning

## Planning Your Cash Flow Payday-to-Payday

The Runway feature helps you answer the critical question: "How much do I have to live on until my next paycheck?" It transforms budgeting from a monthly calendar view into a cash flow perspective where you see exactly how much discretionary money you have available after all obligations are met.

**Note**: Runway is a Standard tier feature.

### What is Runway?

The name comes from aviation: just like an airplane needs enough runway to take off and land safely, your finances need enough "runway" to get from one paycheck to the next. Runway is a payday-to-payday planning system that tracks:

- Your starting bank balance
- Expected income during the period
- Bills and fixed expenses due
- Prorated budget allocations
- Money set aside as reserves
- Your true "Living Money" - what's left for unexpected expenses

### Why Runway is Different from Traditional Budgeting

Traditional monthly budgeting has a flaw: it doesn't account for when money arrives and when bills are due. You might have a "balanced" monthly budget but still overdraft because a big bill hits before your paycheck.

Runway solves this by:
- Aligning planning periods with your actual pay schedule
- Showing your real cash position at any point in the period
- Calculating how much you can safely spend per day
- Projecting future periods so you can plan ahead

### Key Concepts

**Periods**: A Runway period is typically a payday-to-payday span (often 2 weeks). Each period has:
- Start and end dates
- Starting bank balance
- Line items for income, bills, budget, and reserves

**Living Money**: This is the key metric - your true spending cushion after all obligations:
```
Living Money = Starting Balance + Income - Bills - Budget - Done Reserves
```
This represents discretionary cash available for unexpected expenses, not your total bank balance (which includes money already earmarked for budget categories).

**Dollars Per Day ($/Day)**: Shows your daily spending cushion:
```
$/Day = Living Money ÷ Days Remaining in Period
```
This tells you how much you can spend each day on true incidentals (things not covered by your budget categories).

### The Four Item Types

**Income**: Money coming in during the period
- Paychecks from your defined income sources
- Both pending and received income count toward Living Money

**Bills/Expenses**: Fixed payments with specific due dates
- Rent, mortgage, utilities, subscriptions
- Both pending and paid bills count (you need the money either way)
- Can mark as "Skipped" if you're not paying this period

**Budget**: Prorated planned spending
- Categories like groceries, gas, dining out
- Calculated as: Monthly budget ÷ 30 × days in period
- Pending and done count; skipped excluded

**Reserves**: Money intentionally set aside
- Savings transfers, future expense funds
- **Only "Done" status counts** - prevents counting money you haven't actually moved yet

### Item Status Tracking

Each item can have three statuses:
- **Pending**: Not yet completed
- **Done**: Completed/paid
- **Skipped**: Won't happen this period

How status affects calculations:
| Item Type | Pending | Done | Skipped |
|-----------|---------|------|---------|
| Income | Counts | Counts | Excluded |
| Bills | Counts | Counts | Excluded |
| Budget | Counts | Counts | Excluded |
| Reserves | NOT counted | Counts | Excluded |

**Why Reserves work differently**: You don't want to count savings you haven't actually transferred yet. Mark reserves as "Done" only when you've moved the money.

### Smart Features

**Auto-Populate**: Automatically adds items to a period based on:
- Income sources with payment dates falling within the period
- Bills and subscriptions due during the period
- Prorated budget categories

**Generate Multiple Periods**: Creates 1-3 future periods with intelligence:
- Auto-calculates payday-to-payday dates from your income sources
- Carries forward projected Living Money as next period's starting balance
- Auto-populates all items

**Sync Amounts**: Updates all items in a period to match current bill, income, and budget amounts (useful after you update your bills or budgets elsewhere).

**Sync All**: Updates amounts across ALL periods and cascades corrected starting balances forward - essential after reconciling a period.

**Actual vs Planned Budget Spending**: Each budget item on the period page shows actual transaction spending below the planned amount. Color-coded indicators show how much of the budget has been used:
- **Green**: Under 70% spent
- **Yellow**: 70-100% spent
- **Red**: Over budget
- Hover info icon for tooltip explaining the comparison

**Living Money Trend Chart**: The Runway index page displays a dual-axis line chart showing Living Money and $/Day across all periods. Appears automatically when you have 2 or more periods. Helps visualize whether your cash flow position is improving or declining over time.

**Close Period**: End-of-period reconciliation:
1. Enter your actual bank balance
2. System calculates variance from projected Living Money
3. Creates adjustment item if needed
4. Corrects future period starting balances

### Credit Card Log

Each period includes a Credit Card Log to track whether you're paying off what you charge:
- **Charges**: Credit card spending during the period
- **Payments**: Payments made to credit cards
- **Net Position**: Positive = paying down debt, Negative = adding to debt

This helps you stay aware of credit card debt accumulation, which traditional cash flow planning often misses.

### Getting Started with Runway

1. **Create your first period**: Click "New Period" and set dates spanning your current pay period
2. **Enter starting balance**: Your actual bank account balance right now
3. **Auto-populate**: Click to pull in income, bills, and budget items
4. **Review and adjust**: Toggle items on/off, adjust amounts if needed
5. **Check your Living Money**: This is your true spending cushion
6. **Monitor $/Day**: Use this as your daily spending guide

### Best Practices

1. **Align periods with paydays** - Start each period on payday for clearest cash flow picture
2. **Update starting balance accurately** - This is the foundation for all calculations
3. **Mark items Done promptly** - Update status as bills are paid and income received
4. **Don't double-count** - If something is in Bills, don't also put it in Budget
5. **Use Close Period** - Reconcile at end of each period for accuracy
6. **Generate future periods** - Plan 2-3 periods ahead to catch potential cash crunches
7. **Check $/Day before discretionary spending** - Know your daily cushion

### Common Questions

**Q: How is Runway different from my budget?**
A: Budgets track monthly spending limits. Runway tracks cash flow timing - when money arrives vs. when it's needed. You can have a "balanced" monthly budget but still run short mid-month if timing doesn't align.

**Q: Should I use Runway AND budgets?**
A: Yes! Budgets set your spending limits by category. Runway ensures you have the cash to cover those budgets when bills are due. They work together.

**Q: What if my income is irregular?**
A: Create periods based on when you expect income. You can always adjust dates and amounts as your situation becomes clearer.

**Q: Why do reserves only count when "Done"?**
A: To prevent over-counting. If you plan to save $500 but haven't transferred it yet, that money is still available. Mark it Done only after you've actually moved it to savings.

---

# Currency Support

## Display Currency Preference

SenticMoney supports three display currencies, configurable per user in Edit Profile.

### Supported Currencies

| Currency | Symbol | Region |
|----------|--------|--------|
| USD | $ | United States |
| EUR | € | Eurozone |
| GBP | £ | United Kingdom |

### Where Currency Symbol Appears

The selected currency symbol updates throughout:
- All transaction amounts (add, edit, list views)
- Budget amounts and progress bars
- Bill and subscription amounts
- Income source amounts
- Goal amounts and progress
- Dashboard summary cards and charts
- Runway Living Money, $/Day, and all line items
- Genie AI responses
- Financial calculators
- Reports (Income Statement, Balance Sheet, Cash Flow, Tax Summary)
- Money Flow Sankey chart node labels
- Transaction entry form input-group addons

### Setting Your Currency

1. Navigate to **Edit Profile** (click your username in the top nav)
2. Select your preferred currency from the Currency dropdown
3. Click **Save**
4. Currency symbol updates immediately across the entire app

### Important Notes

- Currency selection affects **display only** — it does not convert amounts between currencies
- All amounts are stored in the database as entered; only the symbol changes
- Users should enter all transactions in their chosen currency
- Switching currency mid-use changes all displayed symbols retroactively (amounts stay the same)
- The Genie uses the selected currency symbol in all AI responses

---

*Last updated: April 2026*
*This document is a reference for writing blog articles about SenticMoney features.*
