from pyknow import *

class Interaction(Fact):
    consent = Field(list)
    nonConsent = Field(list)
    inappropriateBehavior = Field(list)
    responseToInappropriateBehavior = Field(list)

class InteractionAnalysis(KnowledgeEngine):
    @DefFacts()
    def init_interaction_analysis(self, interaction):
        yield interaction

    @Rule(Interaction(consent=MATCH.consent))
    def consent_analysis(self, consent):
        if len(consent) >= 2:
            print("A abordagem informada foi consentida inicialmente...")
        else:
            print("A pessoa abordada demonstrou poucos ou quase nenhum gesto que denote que está se sentindo confortável com aquela abordagem inicialmente...")

    @Rule(Interaction(nonConsent=MATCH.nonConsent))
    def non_consent_analysis(self, nonConsent):
        if len(nonConsent) <= 1:
            print("Dando o prosseguimento da análise da interação informada, a pessoa abordada basicamente não apresentou sinais que denotem um não consentimento explícito.")
        else:
            print("Dando o prosseguimento da análise da interação informada, a pessoa abordada demonstrou EXPLICITAMENTE o seu desconforto com aquela situação.")

    @Rule(Interaction(inappropriateBehavior=MATCH.inappropriateBehavior))
    def inappropriate_behavior_analysis(self, inappropriateBehavior):
        if len(inappropriateBehavior) < 1:
            print("A pessoa que foi responsável pela abordagem não apresentou nenhum comportamento inadequado.")
        elif len(inappropriateBehavior) == 1:
            print("A pessoa responsável pela abordagem agiu de forma inadequada, porém, ainda não o suficiente para considerar ela responsável por uma interação desconfortável...")
        else:
            print("Durante a abordagem, a pessoa responsável por ela agiu de forma inadequada e está responsável por uma abordagem desconfortável...")

    @Rule(Interaction(responseToInappropriateBehavior=MATCH.responseToInappropriateBehavior))        
    def response_to_inappropriate_behavior_analysis(self, responseToInappropriateBehavior):
        if len(responseToInappropriateBehavior) == 0:
            print("Logo, nada a ser considerado sobre a análise da situação informada, apenas uma interação normal e consensual entre duas pessoas!")
        elif len(responseToInappropriateBehavior) > 0:
            print("A pessoa abordada explicitou, mais uma vez, seu desconforto com a situação.")
