from django.db.models.signals import pre_save
from django.dispatch import receiver
from app_main.models import CustomUser

POINTS_PER_LEVEL = 10

@receiver(pre_save, sender=CustomUser)
def update_user_level(sender, instance, **kwargs):

    """
    Atualiza o nível do usuário com base nos pontos acumulados.
    """

    if instance.points >= POINTS_PER_LEVEL:
        instance.level = int(instance.points // 10) 
    
    
