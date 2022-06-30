from datetime import *


def year(request):
    """Добавляет переменную с текущим годом."""
    return {
        'year': datetime.now().year
    }
