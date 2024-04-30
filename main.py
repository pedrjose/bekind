from pyknow import *
from rules import Interaction, InteractionAnalysis

inter = Interaction(consent=["gesto de aprovação", "sorriso"],
                    nonConsent=["expressão facial de desconforto", "recuo"],
                    inappropriateBehavior=["toque não solicitado"],
                    responseToInappropriateBehavior=["pedir para parar"])

engine = InteractionAnalysis()

engine.reset()  
engine.declare(inter)  
engine.run()  