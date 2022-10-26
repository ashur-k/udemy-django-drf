from django.db import models
from django.contrib.auth import get_user_model
from core_apps.articles.models import Article
from core_apps.common.models import TimeStampedUUIDModel


User = get_user_model()


class Favorite(TimeStampedUUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='article_favorites'
    )

    def __Str__(self):
        return f"{self.user.username} favorited {self.article.title}"

    def is_favorited(self, user, article):
        
        try:
            article = self.article
            user = self.user
        except Article.DoesNotExist:
            pass

        queryset = Favorite.objects.filter(article_id=article, user_id=user)

        if queryset:
            return True
        return False

        
