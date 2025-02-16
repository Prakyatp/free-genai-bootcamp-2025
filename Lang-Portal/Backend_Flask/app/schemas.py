from app import ma
from app.models.word import Word
from app.models.group import Group
from app.models.study_session import StudySession
from app.models.word_review import WordReview

class WordSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Word

    word_id = ma.auto_field()
    kannada_word = ma.auto_field()
    english_word = ma.auto_field()
    parts = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()
    groups = ma.Nested('GroupSchema', many=True, only=('id', 'name'))

class GroupSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Group

    id = ma.auto_field()
    name = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()
    word_count = ma.Function(lambda obj: len(obj.words))
    words = ma.Nested(WordSchema, many=True, exclude=('groups',))

class StudySessionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = StudySession

    id = ma.auto_field()
    group_id = ma.auto_field()
    activity_type = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()
    group = ma.Nested(GroupSchema, only=('id', 'name'))
    stats = ma.Method('get_stats')

    def get_stats(self, obj):
        reviews = obj.word_reviews
        total = len(reviews)
        correct = sum(1 for r in reviews if r.is_correct)
        return {
            'total_words': total,
            'correct_count': correct,
            'accuracy': (correct / total * 100) if total > 0 else 0
        }

class WordReviewSchema(ma.SQLAlchemySchema):
    class Meta:
        model = WordReview

    id = ma.auto_field()
    is_correct = ma.auto_field()
    created_at = ma.auto_field()
    word = ma.Nested(WordSchema, only=('word_id', 'kannada_word', 'english_word')) 