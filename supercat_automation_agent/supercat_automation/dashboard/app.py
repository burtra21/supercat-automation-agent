# dashboard/app.py
"""
Streamlit dashboard for SuperCat GTM monitoring
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from database.connection import db
from dashboard.metrics import MetricsCalculator
from dashboard.visualizations import ChartGenerator

st.set_page_config(
    page_title="SuperCat GTM Dashboard",
    page_icon="🚀",
    layout="wide"
)

class SupercatDashboard:
    def __init__(self):
        self.metrics_calc = MetricsCalculator()
        self.chart_gen = ChartGenerator()
    
    def run(self):
        st.title("🚀 SuperCat GTM Automation Dashboard")
        
        # Sidebar
        with st.sidebar:
            st.header("Controls")
            date_range = st.date_input(
                "Date Range",
                value=(datetime.now() - timedelta(days=30), datetime.now()),
                max_value=datetime.now()
            )
            
            refresh = st.button("🔄 Refresh Data")
        
        # Main metrics row
        col1, col2, col3, col4 = st.columns(4)
        
        metrics = self.metrics_calc.get_current_metrics()
        
        with col1:
            st.metric(
                "Companies Analyzed",
                metrics['companies_analyzed'],
                delta=metrics.get('companies_delta')
            )
        
        with col2:
            st.metric(
                "Qualified (T1/T2)",
                metrics['qualified_companies'],
                delta=metrics.get('qualified_delta')
            )
        
        with col3:
            st.metric(
                "Campaigns Active",
                metrics['active_campaigns'],
                delta=metrics.get('campaigns_delta')
            )
        
        with col4:
            st.metric(
                "Response Rate",
                f"{metrics['response_rate']:.1f}%",
                delta=f"{metrics.get('response_delta', 0):.1f}%"
            )
        
        # Charts row 1
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 TAM Distribution")
            tam_chart = self.chart_gen.create_tam_distribution()
            st.plotly_chart(tam_chart, use_container_width=True)
        
        with col2:
            st.subheader("💔 Pain Signal Distribution")
            pain_chart = self.chart_gen.create_pain_distribution()
            st.plotly_chart(pain_chart, use_container_width=True)
        
        # Charts row 2
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📈 Pipeline Velocity")
            pipeline_chart = self.chart_gen.create_pipeline_chart()
            st.plotly_chart(pipeline_chart, use_container_width=True)
        
        with col2:
            st.subheader("🎯 Campaign Performance")
            campaign_chart = self.chart_gen.create_campaign_performance()
            st.plotly_chart(campaign_chart, use_container_width=True)
        
        # Detailed tables
        st.header("📋 Detailed Views")
        
        tab1, tab2, tab3 = st.tabs(["Hot Prospects", "Active Campaigns", "Recent Activity"])
        
        with tab1:
            self.show_hot_prospects()
        
        with tab2:
            self.show_active_campaigns()
        
        with tab3:
            self.show_recent_activity()
    
    def show_hot_prospects(self):
        """Show tier 1 prospects table"""
        prospects = self.metrics_calc.get_hot_prospects()
        
        if prospects:
            df = pd.DataFrame(prospects)
            
            # Format columns
            column_config = {
                "company_name": "Company",
                "psi_score": st.column_config.ProgressColumn(
                    "Pain Score",
                    min_value=0,
                    max_value=100,
                ),
                "primary_edp": "Primary Pain",
                "trade_shows": "Trade Shows",
                "action": st.column_config.LinkColumn("Action")
            }
            
            st.dataframe(
                df,
                column_config=column_config,
                hide_index=True,
                use_container_width=True
            )
        else:
            st.info("No hot prospects found. Run analysis to identify opportunities.")
    
    def show_active_campaigns(self):
        """Show active campaigns"""
        campaigns = self.metrics_calc.get_active_campaigns()
        
        if campaigns:
            df = pd.DataFrame(campaigns)
            
            st.dataframe(
                df,
                hide_index=True,
                use_container_width=True
            )
            
            # Campaign actions
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("📤 Send to Clay"):
                    st.success("Campaigns sent to Clay webhook!")
            
            with col2:
                if st.button("⏸️ Pause Selected"):
                    st.info("Selected campaigns paused")
            
            with col3:
                if st.button("📊 Export Report"):
                    st.download_button(
                        label="Download CSV",
                        data=df.to_csv(index=False),
                        file_name=f"campaigns_{datetime.now().strftime('%Y%m%d')}.csv",
                        mime="text/csv"
                    )
        else:
            st.info("No active campaigns. Generate campaigns for qualified companies.")
    
    def show_recent_activity(self):
        """Show recent system activity"""
        activities = self.metrics_calc.get_recent_activities()
        
        for activity in activities:
            with st.container():
                col1, col2 = st.columns([1, 4])
                
                with col1:
                    st.write(activity['timestamp'])
                
                with col2:
                    if activity['type'] == 'analysis':
                        st.success(f"✅ Analyzed {activity['company_name']} - Tier: {activity['tier']}")
                    elif activity['type'] == 'campaign':
                        st.info(f"📧 Campaign created for {activity['company_name']}")
                    elif activity['type'] == 'outreach':
                        st.warning(f"🚀 Outreach sent to {activity['contact_name']}")

if __name__ == "__main__":
    dashboard = SupercatDashboard()
    dashboard.run()