from django.forms import ModelForm
from community.models import Article, Bookmark

class ArticleForm(ModelForm):
	class Meta:
		model = Article

class BookmarkForm(ModelForm):
	class Meta:
		model = Bookmark
