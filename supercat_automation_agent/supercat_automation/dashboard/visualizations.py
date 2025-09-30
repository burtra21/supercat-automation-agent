# dashboard/visualizations.py
"""
Chart generation for dashboard
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from database.connection import db

class ChartGenerator:
    def create_tam_distribution(self):
        """Create TAM tier distribution pie chart"""
        
        # Get tier distribution
        companies = db.client.table('companies').select('tam_tier').execute()
        
        if companies.data:
            df = pd.DataFrame(companies.data)
            tier_counts = df['tam_tier'].value_counts()
            
            fig = px.pie(
                values=tier_counts.values,
                names=tier_counts.index,
                color_discrete_map={
                    'TIER_1_IMMEDIATE': '#FF4444',
                    'TIER_2_QUARTERLY': '#FFA500',
                    'TIER_3_NURTURE': '#4169E1',
                    'TIER_4_MONITOR': '#808080'
                }
            )
            
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(height=300)
            
            return fig
        
        return go.Figure()
    
    def create_pain_distribution(self):
        """Create pain signal distribution bar chart"""
        
        # Get EDP distribution
        companies = db.client.table('companies').select('primary_edp').execute()
        
        if companies.data:
            df = pd.DataFrame(companies.data)
            edp_counts = df['primary_edp'].value_counts()
            
            # Clean labels
            edp_counts.index = [x.replace('_', ' ').title() for x in edp_counts.index]
            
            fig = px.bar(
                x=edp_counts.values,
                y=edp_counts.index,
                orientation='h',
                color=edp_counts.values,
                color_continuous_scale='Reds'
            )
            
            fig.update_layout(
                height=300,
                showlegend=False,
                xaxis_title="Count",
                yaxis_title=""
            )
            
            return fig
        
        return go.Figure()
    
    def create_pipeline_chart(self):
        """Create pipeline velocity funnel"""
        
        stages = ['Identified', 'Analyzed', 'Qualified', 'Campaign Created', 'Outreach Sent', 'Response']
        values = [150, 120, 45, 38, 35, 8]  # Mock data
        
        fig = go.Figure(go.Funnel(
            y=stages,
            x=values,
            textinfo="value+percent initial"
        ))
        
        fig.update_layout(height=300)
        
        return fig
    
    def create_campaign_performance(self):
        """Create campaign performance metrics"""
        
        # Mock data - you'd pull from real campaign metrics
        dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
        sent = [20, 22, 25, 23, 28, 30, 32, 35, 33, 38, 40, 42, 45, 43, 48,
                50, 52, 55, 53, 58, 60, 62, 65, 63, 68, 70, 72, 75, 73, 78]
        
        responses = [2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8,
                     8, 9, 9, 9, 10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=dates,
            y=sent,
            mode='lines',
            name='Outreach Sent',
            line=dict(color='blue', width=2)
        ))
        
        fig.add_trace(go.Scatter(
            x=dates,
            y=responses,
            mode='lines',
            name='Responses',
            line=dict(color='green', width=2)
        ))
        
        fig.update_layout(
            height=300,
            xaxis_title="Date",
            yaxis_title="Count",
            hovermode='x unified'
        )
        
        return fig