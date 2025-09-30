# analysis/customer_language.py
'''Customer language patterns from won deals'''

class CustomerLanguageLibrary:
    '''Proven language patterns from 14 won deals'''
    
    def __init__(self):
        # Actual customer quotes by pain type
        self.pain_language = {
            'sales_enablement_collapse': {
                'customer_words': [
                    "taking 1-3 hours daily just for basic reporting",
                    "reps spending 20% time selling, 80% on admin",
                    "manually go through spreadsheets",
                    "can't work without WiFi at shows",
                    "no simple way to figure out top sellers"
                ],
                'impact_statements': [
                    "losing 4 out of 5 opportunities",
                    "3 hours daily per rep wasted",
                    "30% order error rate",
                    "missing critical selling time"
                ]
            },
            'technology_obsolescence': {
                'customer_words': [
                    "old SAP system not set up for modern",
                    "SFTP is ancient technology",
                    "asking CSV files around is not state of the art",
                    "can't import customers",
                    "ERP company went bankrupt"
                ],
                'impact_statements': [
                    "40-50% slower than competitors",
                    "embarrassing to customers",
                    "losing to digital-native companies",
                    "can't compete anymore"
                ]
            },
            'rep_performance_crisis': {
                'customer_words': [
                    "top reps logging in 10-12 times daily",
                    "others barely using it",
                    "60+ year old reps don't want to learn",
                    "zero visibility into what reps are doing",
                    "need to know if salespeople are hustling"
                ],
                'impact_statements': [
                    "10x usage difference between reps",
                    "can't coach effectively",
                    "no data for territory decisions",
                    "flying blind on performance"
                ]
            },
            'sku_complexity': {
                'customer_words': [
                    "5 different combinations per item",
                    "20 different option sets",
                    "2,000-3,000 SKUs with colors",
                    "19 levels for fabrics",
                    "tearing structure complexity"
                ],
                'impact_statements': [
                    "25% return rate from errors",
                    "quotes take hours",
                    "constantly shipping wrong products",
                    "margin erosion from mistakes"
                ]
            }
        }
        
        # Proven discovery questions
        self.discovery_questions = {
            'qualifying': [
                "Walk me through what happens when a rep takes an order at a trade show today?",
                "How long does it take from customer interest to confirmed order?",
                "What percentage of your reps are consistently hitting quota?",
                "How do you currently know what your reps are doing day-to-day?",
                "When did you last lose a deal to a faster competitor?"
            ],
            'pain_probing': [
                "How many hours daily do your reps spend on non-selling activities?",
                "What's your current order error rate?",
                "How often do pricing mistakes happen?",
                "Can your reps access inventory in real-time?",
                "How many systems do reps check for one quote?"
            ],
            'impact': [
                "What does each order error cost you?",
                "How much revenue do you generate at trade shows?",
                "What percentage of annual sales comes from your top 3 shows?",
                "How many deals do you lose to faster competitors?",
                "What's the productivity difference between top and bottom reps?"
            ]
        }
        
        # Objection handlers that worked
        self.objection_responses = {
            'too_expensive': {
                'response': "You're losing 3 hours daily per rep. At $100/hour loaded cost, that's $75,000 annually per rep.",
                'success_rate': 0.67
            },
            'need_it_approval': {
                'response': "This replaces spreadsheets, not your ERP. Most deploy without IT.",
                'success_rate': 0.73
            },
            'reps_wont_adopt': {
                'response': "Your top reps are begging for this. Start with them - the others will follow.",
                'success_rate': 0.81
            }
        }
    
    def get_pain_language(self, pain_type: str) -> dict:
        '''Get customer language for specific pain'''
        return self.pain_language.get(pain_type, self.pain_language['sales_enablement_collapse'])
    
    def get_discovery_question(self, stage: str = 'qualifying') -> list:
        '''Get discovery questions by stage'''
        return self.discovery_questions.get(stage, self.discovery_questions['qualifying'])
    
    def get_objection_response(self, objection: str) -> dict:
        '''Get proven objection response'''
        return self.objection_responses.get(objection, {
            'response': 'Let me show you the ROI calculation...',
            'success_rate': 0.5
        })
