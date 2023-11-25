class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        if 'chat_selected' not in context:
            context['chat_selected'] = 0
        return context
    