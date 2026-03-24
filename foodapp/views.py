from django.views import View
from .models import Food, FoodCategory, FoodListSerializer
from django.http import JsonResponse
from django.db.models import Prefetch


class FoodView(View):
    def get(self, request):
        foodlist = FoodCategory.objects.filter(
            food__is_publish=True
        ).prefetch_related(
            Prefetch('food', queryset=Food.objects.filter(is_publish=True))
        ).distinct()
        serialized_data = FoodListSerializer(foodlist, many=True).data
        return JsonResponse(serialized_data, safe=False, json_dumps_params={"ensure_ascii": False})
