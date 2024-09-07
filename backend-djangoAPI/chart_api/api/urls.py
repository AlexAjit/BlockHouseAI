# api/urls.py
from django.urls import path
from .views import CandlestickDataView, LineChartDataView, BarChartDataView, PieChartDataView

urlpatterns = [
    path('candlestick-data/', CandlestickDataView.as_view()),
    path('line-chart-data/', LineChartDataView.as_view()),
    path('bar-chart-data/', BarChartDataView.as_view()),
    path('pie-chart-data/', PieChartDataView.as_view()),
]