from djchoices import DjangoChoices, ChoiceItem

class StatusKanBan(DjangoChoices):
    toDo = ChoiceItem(u'toDo', u'toDo')
    doing = ChoiceItem(u'doing', u'doing')
    done = ChoiceItem(u'done', u'done')