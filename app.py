import streamlit as st
from fin_agent_tools import StockDisplayTool, YFinanceDataTool
from prompts import REPORTER_TASK_PROMPT, ReportOutput
from crewai import Agent, Task, Crew, LLM
from crewai.tools import BaseTool
import yfinance as yf
from datetime import datetime
#from crewai.utilities import TaskOutput
from typing import Optional

st.set_page_config(
    page_title="IT Operations Assistant",
    page_icon="🌆",
    layout="wide"
)


# Streamlit app setup
st.subheader("🌆 Financial Analysis Crew", divider='green')

# Retrieve API key from secrets
GROQ_API_KEY = st.secrets["GROQ_API"]

# Define LLMs
llm = LLM(
    api_key=GROQ_API_KEY,
    model="groq/gemma2-9b-it",
    temperature=0.1,
)

llm_groq_mixtral = LLM(
    api_key=GROQ_API_KEY,
    model="groq/mixtral-8x7b-32768",
    temperature=0.2,
    max_tokens=4000,
    response_format={"type": "json"},
)

# Tool
yfinance_tool = YFinanceDataTool()

# Agents
collector = Agent(
    role='Financial Data Collector',
    goal='Collect comprehensive financial data for the given stock ticker',
    backstory='A financial data specialist with expertise in gathering market information.',
    llm=llm,
    tools=[yfinance_tool],
    allow_delegation=False,
    max_iter=1,
    verbose=True
)

reporter = Agent(
    role='Financial Analyst',
    goal='Analyze financial data and create detailed financial reports',
    backstory='An experienced financial analyst specializing in stock market analysis and financial reporting.',
    llm=llm,
    allow_delegation=False,
    max_iter=3,
    verbose=True
)

# Callbacks
def task_callback(output):
    if output.raw:
        st.caption(f"☑️ {output.summary}")
    else :
        st.write("No Output")

# Tasks
collect_data = Task(
    description="Collect financial data for the specified stock {ticker} using yfinance.",
    expected_output='A comprehensive dictionary containing all available financial data for the stock.',
    agent=collector,
    callback=task_callback
)

analyze_data = Task(
    description="""
    Analyze the collected {ticker} financial data and create a detailed financial report including:
    1. Company Overview
    2. Financial Ratios Analysis
    3. Market Performance
    4. Risk Assessment
    5. Investment Recommendation
    Use the data provided by the collector to support your analysis.
    """,
    expected_output = REPORTER_TASK_PROMPT,
    #output_pydantic = ReportOutput,
    #expected_output='A detailed financial analysis report with clear sections and supporting data, in markdown format with sections, titles, some tables and emojies.',
    agent=reporter,
    context=[collect_data],
    callback=task_callback
)

# Crew
def create_crew():
    crew = Crew(
    agents=[collector, reporter],
    tasks=[collect_data, analyze_data],
    verbose=True
    )
    return crew

# Input for ticker
ticker = st.text_input("Enter stock ticker:", "IONQ")

# Run analysis on button click
if st.button("Analyze Stock, Generate Financial Report", use_container_width=True):
    with st.spinner(f"Generating :orange[{ticker}] Financial Report..."):
        crew = create_crew()
        stock_display = StockDisplayTool(ticker)
        result = crew.kickoff(inputs={'ticker': ticker})
        st.divider()
        stock_display.display_all()
        st.divider()
        st.markdown(result)
        st.divider()
        st.caption("** AI generated Report ** NFA, Please DYOR before investing.")
