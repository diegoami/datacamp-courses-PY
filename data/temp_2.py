from pandas import Timestamp
from numpy import nan
from pandas import DataFrame

ts_dict = \
{Timestamp('2010-12-11 04:00:00'): 45.799999999999997,
 Timestamp('2010-12-11 05:00:00'): 45.5,
 Timestamp('2010-12-11 06:00:00'): 45.799999999999997,
 Timestamp('2010-12-11 07:00:00'): 45.299999999999997,
 Timestamp('2010-12-11 08:00:00'): 46.5,
 Timestamp('2010-12-11 09:00:00'): 49.799999999999997,
 Timestamp('2010-12-11 10:00:00'): 53.100000000000001,
 Timestamp('2010-12-11 11:00:00'): 55.899999999999999,
 Timestamp('2010-12-11 12:00:00'): 58.399999999999999,
 Timestamp('2010-12-11 13:00:00'): 60.100000000000001,
 Timestamp('2010-12-11 14:00:00'): 61.399999999999999,
 Timestamp('2010-12-11 15:00:00'): 62.100000000000001,
 Timestamp('2010-12-11 16:00:00'): 61.600000000000001,
 Timestamp('2010-12-11 17:00:00'): 60.100000000000001,
 Timestamp('2010-12-11 18:00:00'): 56.700000000000003,
 Timestamp('2010-12-11 19:00:00'): 53.399999999999999,
 Timestamp('2010-12-11 20:00:00'): 51.5,
 Timestamp('2010-12-11 21:00:00'): 50.299999999999997,
 Timestamp('2010-12-11 22:00:00'): 49.399999999999999,
 Timestamp('2010-12-11 23:00:00'): 48.299999999999997,
 Timestamp('2010-12-12 00:00:00'): 48.200000000000003,
 Timestamp('2010-12-12 01:00:00'): 47.200000000000003,
 Timestamp('2010-12-12 02:00:00'): 46.600000000000001,
 Timestamp('2010-12-12 03:00:00'): 46.100000000000001,
 Timestamp('2010-12-12 04:00:00'): 45.700000000000003,
 Timestamp('2010-12-12 05:00:00'): 45.399999999999999,
 Timestamp('2010-12-12 06:00:00'): 45.700000000000003,
 Timestamp('2010-12-12 07:00:00'): 45.200000000000003,
 Timestamp('2010-12-12 08:00:00'): 46.299999999999997,
 Timestamp('2010-12-12 09:00:00'): 49.600000000000001,
 Timestamp('2010-12-12 10:00:00'): 53.0,
 Timestamp('2010-12-12 11:00:00'): 55.799999999999997,
 Timestamp('2010-12-12 12:00:00'): 58.200000000000003,
 Timestamp('2010-12-12 13:00:00'): 60.0,
 Timestamp('2010-12-12 14:00:00'): 61.200000000000003,
 Timestamp('2010-12-12 15:00:00'): 62.0,
 Timestamp('2010-12-12 16:00:00'): 61.5,
 Timestamp('2010-12-12 17:00:00'): 60.0,
 Timestamp('2010-12-12 18:00:00'): 56.600000000000001,
 Timestamp('2010-12-12 19:00:00'): 53.299999999999997,
 Timestamp('2010-12-12 20:00:00'): 51.399999999999999,
 Timestamp('2010-12-12 21:00:00'): 50.299999999999997,
 Timestamp('2010-12-12 22:00:00'): 49.399999999999999,
 Timestamp('2010-12-12 23:00:00'): 48.200000000000003,
 Timestamp('2010-12-13 00:00:00'): 48.200000000000003,
 Timestamp('2010-12-13 01:00:00'): 47.200000000000003,
 Timestamp('2010-12-13 02:00:00'): 46.600000000000001,
 Timestamp('2010-12-13 03:00:00'): 46.200000000000003,
 Timestamp('2010-12-13 04:00:00'): 45.799999999999997,
 Timestamp('2010-12-13 05:00:00'): 45.399999999999999,
 Timestamp('2010-12-13 06:00:00'): 45.700000000000003,
 Timestamp('2010-12-13 07:00:00'): 45.299999999999997,
 Timestamp('2010-12-13 08:00:00'): 46.299999999999997,
 Timestamp('2010-12-13 09:00:00'): 49.600000000000001,
 Timestamp('2010-12-13 10:00:00'): 52.899999999999999,
 Timestamp('2010-12-13 11:00:00'): 55.700000000000003,
 Timestamp('2010-12-13 12:00:00'): 58.0,
 Timestamp('2010-12-13 13:00:00'): 59.799999999999997,
 Timestamp('2010-12-13 14:00:00'): 61.0,
 Timestamp('2010-12-13 15:00:00'): 61.700000000000003,
 Timestamp('2010-12-13 16:00:00'): 61.299999999999997,
 Timestamp('2010-12-13 17:00:00'): 59.899999999999999,
 Timestamp('2010-12-13 18:00:00'): 56.5,
 Timestamp('2010-12-13 19:00:00'): 53.299999999999997,
 Timestamp('2010-12-13 20:00:00'): 51.5,
 Timestamp('2010-12-13 21:00:00'): 50.299999999999997,
 Timestamp('2010-12-13 22:00:00'): 49.5,
 Timestamp('2010-12-13 23:00:00'): 48.399999999999999,
 Timestamp('2010-12-14 00:00:00'): 48.299999999999997,
 Timestamp('2010-12-14 01:00:00'): 47.399999999999999,
 Timestamp('2010-12-14 02:00:00'): 46.700000000000003,
 Timestamp('2010-12-14 03:00:00'): 46.299999999999997,
 Timestamp('2010-12-14 04:00:00'): 45.799999999999997,
 Timestamp('2010-12-14 05:00:00'): 45.5,
 Timestamp('2010-12-14 06:00:00'): 45.799999999999997,
 Timestamp('2010-12-14 07:00:00'): 45.200000000000003,
 Timestamp('2010-12-14 08:00:00'): 46.200000000000003,
 Timestamp('2010-12-14 09:00:00'): 49.5,
 Timestamp('2010-12-14 10:00:00'): 52.700000000000003,
 Timestamp('2010-12-14 11:00:00'): 55.399999999999999,
 Timestamp('2010-12-14 12:00:00'): 57.799999999999997,
 Timestamp('2010-12-14 13:00:00'): 59.5,
 Timestamp('2010-12-14 14:00:00'): 60.700000000000003,
 Timestamp('2010-12-14 15:00:00'): 61.399999999999999,
 Timestamp('2010-12-14 16:00:00'): 61.0,
 Timestamp('2010-12-14 17:00:00'): 59.600000000000001,
 Timestamp('2010-12-14 18:00:00'): 56.200000000000003,
 Timestamp('2010-12-14 19:00:00'): 53.0,
 Timestamp('2010-12-14 20:00:00'): 51.200000000000003,
 Timestamp('2010-12-14 21:00:00'): 50.100000000000001,
 Timestamp('2010-12-14 22:00:00'): 49.100000000000001,
 Timestamp('2010-12-14 23:00:00'): 48.200000000000003,
 Timestamp('2010-12-15 00:00:00'): 48.0,
 Timestamp('2010-12-15 01:00:00'): 47.200000000000003,
 Timestamp('2010-12-15 02:00:00'): 46.5,
 Timestamp('2010-12-15 03:00:00'): 46.0,
 Timestamp('2010-12-15 04:00:00'): 45.600000000000001,
 Timestamp('2010-12-15 05:00:00'): 45.299999999999997,
 Timestamp('2010-12-15 06:00:00'): 45.600000000000001,
 Timestamp('2010-12-15 07:00:00'): 45.0,
 Timestamp('2010-12-15 08:00:00'): 45.799999999999997,
 Timestamp('2010-12-15 09:00:00'): 49.100000000000001,
 Timestamp('2010-12-15 10:00:00'): 52.200000000000003,
 Timestamp('2010-12-15 11:00:00'): 54.899999999999999,
 Timestamp('2010-12-15 12:00:00'): 57.200000000000003,
 Timestamp('2010-12-15 13:00:00'): 58.899999999999999,
 Timestamp('2010-12-15 14:00:00'): 60.200000000000003,
 Timestamp('2010-12-15 15:00:00'): 60.899999999999999,
 Timestamp('2010-12-15 16:00:00'): 60.5,
 Timestamp('2010-12-15 17:00:00'): 59.100000000000001,
 Timestamp('2010-12-15 18:00:00'): 55.799999999999997,
 Timestamp('2010-12-15 19:00:00'): 52.5,
 Timestamp('2010-12-15 20:00:00'): 50.700000000000003,
 Timestamp('2010-12-15 21:00:00'): 49.600000000000001,
 Timestamp('2010-12-15 22:00:00'): 48.600000000000001,
 Timestamp('2010-12-15 23:00:00'): 47.700000000000003,
 Timestamp('2010-12-16 00:00:00'): 47.600000000000001,
 Timestamp('2010-12-16 01:00:00'): 46.700000000000003,
 Timestamp('2010-12-16 02:00:00'): 46.100000000000001,
 Timestamp('2010-12-16 03:00:00'): 45.600000000000001,
 Timestamp('2010-12-16 04:00:00'): 45.200000000000003,
 Timestamp('2010-12-16 05:00:00'): 44.799999999999997,
 Timestamp('2010-12-16 06:00:00'): 45.100000000000001,
 Timestamp('2010-12-16 07:00:00'): 44.399999999999999,
 Timestamp('2010-12-16 08:00:00'): 45.299999999999997,
 Timestamp('2010-12-16 09:00:00'): 48.700000000000003,
 Timestamp('2010-12-16 10:00:00'): 51.700000000000003,
 Timestamp('2010-12-16 11:00:00'): 54.5,
 Timestamp('2010-12-16 12:00:00'): 56.700000000000003,
 Timestamp('2010-12-16 13:00:00'): 58.399999999999999,
 Timestamp('2010-12-16 14:00:00'): 59.700000000000003,
 Timestamp('2010-12-16 15:00:00'): 60.399999999999999,
 Timestamp('2010-12-16 16:00:00'): 60.0,
 Timestamp('2010-12-16 17:00:00'): 58.600000000000001,
 Timestamp('2010-12-16 18:00:00'): 55.200000000000003,
 Timestamp('2010-12-16 19:00:00'): 51.899999999999999,
 Timestamp('2010-12-16 20:00:00'): 50.100000000000001,
 Timestamp('2010-12-16 21:00:00'): 49.100000000000001,
 Timestamp('2010-12-16 22:00:00'): 48.100000000000001,
 Timestamp('2010-12-16 23:00:00'): 47.299999999999997,
 Timestamp('2010-12-17 00:00:00'): 47.100000000000001,
 Timestamp('2010-12-17 01:00:00'): 46.299999999999997,
 Timestamp('2010-12-17 02:00:00'): 45.600000000000001,
 Timestamp('2010-12-17 03:00:00'): 45.100000000000001,
 Timestamp('2010-12-17 04:00:00'): 44.700000000000003,
 Timestamp('2010-12-17 05:00:00'): 44.399999999999999,
 Timestamp('2010-12-17 06:00:00'): 44.600000000000001,
 Timestamp('2010-12-17 07:00:00'): 44.0,
 Timestamp('2010-12-17 08:00:00'): 44.799999999999997,
 Timestamp('2010-12-17 09:00:00'): 48.200000000000003,
 Timestamp('2010-12-17 10:00:00'): 51.299999999999997,
 Timestamp('2010-12-17 11:00:00'): 54.0,
 Timestamp('2010-12-17 12:00:00'): 56.299999999999997,
 Timestamp('2010-12-17 13:00:00'): 57.899999999999999,
 Timestamp('2010-12-17 14:00:00'): 59.299999999999997,
 Timestamp('2010-12-17 15:00:00'): 60.0,
 Timestamp('2010-12-17 16:00:00'): 59.600000000000001,
 Timestamp('2010-12-17 17:00:00'): 58.200000000000003,
 Timestamp('2010-12-17 18:00:00'): 54.899999999999999,
 Timestamp('2010-12-17 19:00:00'): 51.5,
 Timestamp('2010-12-17 20:00:00'): 49.600000000000001,
 Timestamp('2010-12-17 21:00:00'): 48.600000000000001,
 Timestamp('2010-12-17 22:00:00'): 47.600000000000001,
 Timestamp('2010-12-17 23:00:00'): 46.899999999999999,
 Timestamp('2010-12-18 00:00:00'): 46.700000000000003,
 Timestamp('2010-12-18 01:00:00'): 45.799999999999997,
 Timestamp('2010-12-18 02:00:00'): 45.100000000000001,
 Timestamp('2010-12-18 03:00:00'): 44.600000000000001,
 Timestamp('2010-12-18 04:00:00'): 44.100000000000001,
 Timestamp('2010-12-18 05:00:00'): 43.899999999999999,
 Timestamp('2010-12-18 06:00:00'): 44.0,
 Timestamp('2010-12-18 07:00:00'): 43.5,
 Timestamp('2010-12-18 08:00:00'): 44.299999999999997,
 Timestamp('2010-12-18 09:00:00'): 47.600000000000001,
 Timestamp('2010-12-18 10:00:00'): 50.700000000000003,
 Timestamp('2010-12-18 11:00:00'): 53.399999999999999,
 Timestamp('2010-12-18 12:00:00'): 55.600000000000001,
 Timestamp('2010-12-18 13:00:00'): 57.299999999999997,
 Timestamp('2010-12-18 14:00:00'): 58.700000000000003,
 Timestamp('2010-12-18 15:00:00'): 59.399999999999999,
 Timestamp('2010-12-18 16:00:00'): 59.0,
 Timestamp('2010-12-18 17:00:00'): 57.700000000000003,
 Timestamp('2010-12-18 18:00:00'): 54.399999999999999,
 Timestamp('2010-12-18 19:00:00'): 50.899999999999999,
 Timestamp('2010-12-18 20:00:00'): 49.100000000000001,
 Timestamp('2010-12-18 21:00:00'): 48.100000000000001,
 Timestamp('2010-12-18 22:00:00'): 47.100000000000001,
 Timestamp('2010-12-18 23:00:00'): 46.399999999999999,
 Timestamp('2010-12-19 00:00:00'): 46.200000000000003,
 Timestamp('2010-12-19 01:00:00'): 45.299999999999997,
 Timestamp('2010-12-19 02:00:00'): 44.600000000000001,
 Timestamp('2010-12-19 03:00:00'): 44.100000000000001,
 Timestamp('2010-12-19 04:00:00'): 43.700000000000003,
 Timestamp('2010-12-19 05:00:00'): 43.399999999999999,
 Timestamp('2010-12-19 06:00:00'): 43.5,
 Timestamp('2010-12-19 07:00:00'): 42.899999999999999,
 Timestamp('2010-12-19 08:00:00'): 43.700000000000003,
 Timestamp('2010-12-19 09:00:00'): 47.100000000000001,
 Timestamp('2010-12-19 10:00:00'): 50.299999999999997,
 Timestamp('2010-12-19 11:00:00'): 53.0,
 Timestamp('2010-12-19 12:00:00'): 55.299999999999997,
 Timestamp('2010-12-19 13:00:00'): 57.0,
 Timestamp('2010-12-19 14:00:00'): 58.399999999999999,
 Timestamp('2010-12-19 15:00:00'): 59.0,
 Timestamp('2010-12-19 16:00:00'): 58.799999999999997,
 Timestamp('2010-12-19 17:00:00'): 57.399999999999999,
 Timestamp('2010-12-19 18:00:00'): 54.100000000000001,
 Timestamp('2010-12-19 19:00:00'): 50.600000000000001,
 Timestamp('2010-12-19 20:00:00'): 48.700000000000003,
 Timestamp('2010-12-19 21:00:00'): 47.700000000000003,
 Timestamp('2010-12-19 22:00:00'): 46.700000000000003,
 Timestamp('2010-12-19 23:00:00'): 46.0,
 Timestamp('2010-12-20 00:00:00'): 45.899999999999999,
 Timestamp('2010-12-20 01:00:00'): 44.899999999999999,
 Timestamp('2010-12-20 02:00:00'): 44.200000000000003,
 Timestamp('2010-12-20 03:00:00'): 43.799999999999997,
 Timestamp('2010-12-20 04:00:00'): 43.399999999999999,
 Timestamp('2010-12-20 05:00:00'): 43.100000000000001,
 Timestamp('2010-12-20 06:00:00'): 43.200000000000003,
 Timestamp('2010-12-20 07:00:00'): 42.700000000000003,
 Timestamp('2010-12-20 08:00:00'): 43.399999999999999,
 Timestamp('2010-12-20 09:00:00'): 46.899999999999999,
 Timestamp('2010-12-20 10:00:00'): 50.200000000000003,
 Timestamp('2010-12-20 11:00:00'): 53.0,
 Timestamp('2010-12-20 12:00:00'): 55.299999999999997,
 Timestamp('2010-12-20 13:00:00'): 57.100000000000001,
 Timestamp('2010-12-20 14:00:00'): 58.5,
 Timestamp('2010-12-20 15:00:00'): 59.100000000000001,
 Timestamp('2010-12-20 16:00:00'): 58.899999999999999,
 Timestamp('2010-12-20 17:00:00'): 57.600000000000001,
 Timestamp('2010-12-20 18:00:00'): 54.299999999999997,
 Timestamp('2010-12-20 19:00:00'): 50.899999999999999,
 Timestamp('2010-12-20 20:00:00'): 49.0,
 Timestamp('2010-12-20 21:00:00'): 47.899999999999999,
 Timestamp('2010-12-20 22:00:00'): 46.899999999999999,
 Timestamp('2010-12-20 23:00:00'): 46.200000000000003,
 Timestamp('2010-12-21 00:00:00'): 46.100000000000001,
 Timestamp('2010-12-21 01:00:00'): 45.0,
 Timestamp('2010-12-21 02:00:00'): 44.299999999999997,
 Timestamp('2010-12-21 03:00:00'): 43.799999999999997,
 Timestamp('2010-12-21 04:00:00'): 43.5,
 Timestamp('2010-12-21 05:00:00'): 43.200000000000003,
 Timestamp('2010-12-21 06:00:00'): 43.299999999999997,
 Timestamp('2010-12-21 07:00:00'): 42.799999999999997,
 Timestamp('2010-12-21 08:00:00'): 43.399999999999999,
 Timestamp('2010-12-21 09:00:00'): 46.899999999999999,
 Timestamp('2010-12-21 10:00:00'): 50.100000000000001,
 Timestamp('2010-12-21 11:00:00'): 52.899999999999999,
 Timestamp('2010-12-21 12:00:00'): 55.100000000000001,
 Timestamp('2010-12-21 13:00:00'): 56.899999999999999,
 Timestamp('2010-12-21 14:00:00'): 58.200000000000003,
 Timestamp('2010-12-21 15:00:00'): 58.799999999999997,
 Timestamp('2010-12-21 16:00:00'): 58.700000000000003,
 Timestamp('2010-12-21 17:00:00'): 57.399999999999999,
 Timestamp('2010-12-21 18:00:00'): 54.100000000000001,
 Timestamp('2010-12-21 19:00:00'): 50.700000000000003,
 Timestamp('2010-12-21 20:00:00'): 48.899999999999999,
 Timestamp('2010-12-21 21:00:00'): 47.799999999999997,
 Timestamp('2010-12-21 22:00:00'): 46.700000000000003,
 Timestamp('2010-12-21 23:00:00'): 46.0,
 Timestamp('2010-12-22 00:00:00'): 45.799999999999997,
 Timestamp('2010-12-22 01:00:00'): 44.700000000000003,
 Timestamp('2010-12-22 02:00:00'): 44.100000000000001,
 Timestamp('2010-12-22 03:00:00'): 43.600000000000001,
 Timestamp('2010-12-22 04:00:00'): 43.399999999999999,
 Timestamp('2010-12-22 05:00:00'): 43.100000000000001,
 Timestamp('2010-12-22 06:00:00'): 43.100000000000001,
 Timestamp('2010-12-22 07:00:00'): 42.700000000000003,
 Timestamp('2010-12-22 08:00:00'): 43.200000000000003,
 Timestamp('2010-12-22 09:00:00'): 46.700000000000003,
 Timestamp('2010-12-22 10:00:00'): 49.899999999999999,
 Timestamp('2010-12-22 11:00:00'): 52.700000000000003,
 Timestamp('2010-12-22 12:00:00'): 54.899999999999999,
 Timestamp('2010-12-22 13:00:00'): 56.799999999999997,
 Timestamp('2010-12-22 14:00:00'): 58.100000000000001,
 Timestamp('2010-12-22 15:00:00'): 58.700000000000003,
 Timestamp('2010-12-22 16:00:00'): 58.700000000000003,
 Timestamp('2010-12-22 17:00:00'): 57.399999999999999,
 Timestamp('2010-12-22 18:00:00'): 54.0,
 Timestamp('2010-12-22 19:00:00'): 50.700000000000003,
 Timestamp('2010-12-22 20:00:00'): 48.799999999999997,
 Timestamp('2010-12-22 21:00:00'): 47.600000000000001,
 Timestamp('2010-12-22 22:00:00'): 46.600000000000001,
 Timestamp('2010-12-22 23:00:00'): 45.899999999999999,
 Timestamp('2010-12-23 00:00:00'): 45.799999999999997,
 Timestamp('2010-12-23 01:00:00'): 44.600000000000001,
 Timestamp('2010-12-23 02:00:00'): 44.0,
 Timestamp('2010-12-23 03:00:00'): 43.600000000000001,
 Timestamp('2010-12-23 04:00:00'): 43.399999999999999,
 Timestamp('2010-12-23 05:00:00'): 43.0,
 Timestamp('2010-12-23 06:00:00'): 43.100000000000001,
 Timestamp('2010-12-23 07:00:00'): 42.5,
 Timestamp('2010-12-23 08:00:00'): 43.100000000000001,
 Timestamp('2010-12-23 09:00:00'): 46.600000000000001,
 Timestamp('2010-12-23 10:00:00'): 49.799999999999997,
 Timestamp('2010-12-23 11:00:00'): 52.600000000000001,
 Timestamp('2010-12-23 12:00:00'): 54.899999999999999,
 Timestamp('2010-12-23 13:00:00'): 56.700000000000003,
 Timestamp('2010-12-23 14:00:00'): 58.100000000000001,
 Timestamp('2010-12-23 15:00:00'): 58.700000000000003,
 Timestamp('2010-12-23 16:00:00'): 58.700000000000003,
 Timestamp('2010-12-23 17:00:00'): 57.399999999999999,
 Timestamp('2010-12-23 18:00:00'): 54.0,
 Timestamp('2010-12-23 19:00:00'): 50.799999999999997,
 Timestamp('2010-12-23 20:00:00'): 48.799999999999997,
 Timestamp('2010-12-23 21:00:00'): 47.600000000000001,
 Timestamp('2010-12-23 22:00:00'): 46.600000000000001,
 Timestamp('2010-12-23 23:00:00'): 45.899999999999999,
 Timestamp('2010-12-24 00:00:00'): 45.899999999999999,
 Timestamp('2010-12-24 01:00:00'): 44.700000000000003,
 Timestamp('2010-12-24 02:00:00'): 44.0,
 Timestamp('2010-12-24 03:00:00'): 43.700000000000003,
 Timestamp('2010-12-24 04:00:00'): 43.5,
 Timestamp('2010-12-24 05:00:00'): 43.100000000000001,
 Timestamp('2010-12-24 06:00:00'): 43.299999999999997,
 Timestamp('2010-12-24 07:00:00'): 42.5,
 Timestamp('2010-12-24 08:00:00'): 43.200000000000003,
 Timestamp('2010-12-24 09:00:00'): 46.700000000000003,
 Timestamp('2010-12-24 10:00:00'): 50.0,
 Timestamp('2010-12-24 11:00:00'): 52.799999999999997,
 Timestamp('2010-12-24 12:00:00'): 55.100000000000001,
 Timestamp('2010-12-24 13:00:00'): 56.899999999999999,
 Timestamp('2010-12-24 14:00:00'): 58.299999999999997,
 Timestamp('2010-12-24 15:00:00'): 58.899999999999999,
 Timestamp('2010-12-24 16:00:00'): 58.799999999999997,
 Timestamp('2010-12-24 17:00:00'): 57.5,
 Timestamp('2010-12-24 18:00:00'): 54.100000000000001,
 Timestamp('2010-12-24 19:00:00'): 50.799999999999997,
 Timestamp('2010-12-24 20:00:00'): 48.899999999999999,
 Timestamp('2010-12-24 21:00:00'): 47.799999999999997,
 Timestamp('2010-12-24 22:00:00'): 46.700000000000003,
 Timestamp('2010-12-24 23:00:00'): 46.0,
 Timestamp('2010-12-25 00:00:00'): 45.899999999999999,
 Timestamp('2010-12-25 01:00:00'): 44.700000000000003,
 Timestamp('2010-12-25 02:00:00'): 44.0,
 Timestamp('2010-12-25 03:00:00'): 43.700000000000003,
 Timestamp('2010-12-25 04:00:00'): 43.5,
 Timestamp('2010-12-25 05:00:00'): 43.0,
 Timestamp('2010-12-25 06:00:00'): 43.200000000000003,
 Timestamp('2010-12-25 07:00:00'): 42.5,
 Timestamp('2010-12-25 08:00:00'): 43.100000000000001,
 Timestamp('2010-12-25 09:00:00'): 46.700000000000003,
 Timestamp('2010-12-25 10:00:00'): 49.899999999999999,
 Timestamp('2010-12-25 11:00:00'): 52.799999999999997,
 Timestamp('2010-12-25 12:00:00'): 55.0,
 Timestamp('2010-12-25 13:00:00'): 57.0,
 Timestamp('2010-12-25 14:00:00'): 58.299999999999997,
 Timestamp('2010-12-25 15:00:00'): 58.899999999999999,
 Timestamp('2010-12-25 16:00:00'): 58.899999999999999,
 Timestamp('2010-12-25 17:00:00'): 57.600000000000001,
 Timestamp('2010-12-25 18:00:00'): 54.200000000000003,
 Timestamp('2010-12-25 19:00:00'): 50.899999999999999,
 Timestamp('2010-12-25 20:00:00'): 49.0,
 Timestamp('2010-12-25 21:00:00'): 47.799999999999997,
 Timestamp('2010-12-25 22:00:00'): 46.799999999999997,
 Timestamp('2010-12-25 23:00:00'): 46.100000000000001,
 Timestamp('2010-12-26 00:00:00'): 46.0,
 Timestamp('2010-12-26 01:00:00'): 44.600000000000001,
 Timestamp('2010-12-26 02:00:00'): 44.0,
 Timestamp('2010-12-26 03:00:00'): 43.600000000000001,
 Timestamp('2010-12-26 04:00:00'): 43.399999999999999,
 Timestamp('2010-12-26 05:00:00'): 43.0,
 Timestamp('2010-12-26 06:00:00'): 43.100000000000001,
 Timestamp('2010-12-26 07:00:00'): 42.399999999999999,
 Timestamp('2010-12-26 08:00:00'): 43.0,
 Timestamp('2010-12-26 09:00:00'): 46.399999999999999,
 Timestamp('2010-12-26 10:00:00'): 49.700000000000003,
 Timestamp('2010-12-26 11:00:00'): 52.5,
 Timestamp('2010-12-26 12:00:00'): 54.700000000000003,
 Timestamp('2010-12-26 13:00:00'): 56.799999999999997,
 Timestamp('2010-12-26 14:00:00'): 58.200000000000003,
 Timestamp('2010-12-26 15:00:00'): 58.799999999999997,
 Timestamp('2010-12-26 16:00:00'): 58.700000000000003,
 Timestamp('2010-12-26 17:00:00'): 57.5,
 Timestamp('2010-12-26 18:00:00'): 54.200000000000003,
 Timestamp('2010-12-26 19:00:00'): 50.899999999999999,
 Timestamp('2010-12-26 20:00:00'): 48.899999999999999,
 Timestamp('2010-12-26 21:00:00'): 47.899999999999999,
 Timestamp('2010-12-26 22:00:00'): 46.799999999999997,
 Timestamp('2010-12-26 23:00:00'): 46.100000000000001,
 Timestamp('2010-12-27 00:00:00'): 46.100000000000001,
 Timestamp('2010-12-27 01:00:00'): 44.700000000000003,
 Timestamp('2010-12-27 02:00:00'): 44.100000000000001,
 Timestamp('2010-12-27 03:00:00'): 43.799999999999997,
 Timestamp('2010-12-27 04:00:00'): 43.5,
 Timestamp('2010-12-27 05:00:00'): 43.100000000000001,
 Timestamp('2010-12-27 06:00:00'): 43.299999999999997,
 Timestamp('2010-12-27 07:00:00'): 42.399999999999999,
 Timestamp('2010-12-27 08:00:00'): 42.899999999999999,
 Timestamp('2010-12-27 09:00:00'): 46.299999999999997,
 Timestamp('2010-12-27 10:00:00'): 49.600000000000001,
 Timestamp('2010-12-27 11:00:00'): 52.399999999999999,
 Timestamp('2010-12-27 12:00:00'): 54.600000000000001,
 Timestamp('2010-12-27 13:00:00'): 56.700000000000003,
 Timestamp('2010-12-27 14:00:00'): 58.100000000000001,
 Timestamp('2010-12-27 15:00:00'): 58.700000000000003,
 Timestamp('2010-12-27 16:00:00'): 58.600000000000001,
 Timestamp('2010-12-27 17:00:00'): 57.399999999999999,
 Timestamp('2010-12-27 18:00:00'): 54.100000000000001,
 Timestamp('2010-12-27 19:00:00'): 50.799999999999997,
 Timestamp('2010-12-27 20:00:00'): 48.899999999999999,
 Timestamp('2010-12-27 21:00:00'): 47.899999999999999,
 Timestamp('2010-12-27 22:00:00'): 46.799999999999997,
 Timestamp('2010-12-27 23:00:00'): 46.100000000000001,
 Timestamp('2010-12-28 00:00:00'): 46.0,
 Timestamp('2010-12-28 01:00:00'): 44.600000000000001,
 Timestamp('2010-12-28 02:00:00'): 44.0,
 Timestamp('2010-12-28 03:00:00'): 43.600000000000001,
 Timestamp('2010-12-28 04:00:00'): 43.200000000000003,
 Timestamp('2010-12-28 05:00:00'): 42.799999999999997,
 Timestamp('2010-12-28 06:00:00'): 43.0,
 Timestamp('2010-12-28 07:00:00'): 42.100000000000001,
 Timestamp('2010-12-28 08:00:00'): 42.600000000000001,
 Timestamp('2010-12-28 09:00:00'): 46.0,
 Timestamp('2010-12-28 10:00:00'): 49.299999999999997,
 Timestamp('2010-12-28 11:00:00'): 52.200000000000003,
 Timestamp('2010-12-28 12:00:00'): 54.5,
 Timestamp('2010-12-28 13:00:00'): 56.600000000000001,
 Timestamp('2010-12-28 14:00:00'): 58.0,
 Timestamp('2010-12-28 15:00:00'): 58.600000000000001,
 Timestamp('2010-12-28 16:00:00'): 58.5,
 Timestamp('2010-12-28 17:00:00'): 57.200000000000003,
 Timestamp('2010-12-28 18:00:00'): 53.899999999999999,
 Timestamp('2010-12-28 19:00:00'): 50.600000000000001,
 Timestamp('2010-12-28 20:00:00'): 48.600000000000001,
 Timestamp('2010-12-28 21:00:00'): 47.5,
 Timestamp('2010-12-28 22:00:00'): 46.399999999999999,
 Timestamp('2010-12-28 23:00:00'): 45.700000000000003,
 Timestamp('2010-12-29 00:00:00'): 45.700000000000003,
 Timestamp('2010-12-29 01:00:00'): 44.200000000000003,
 Timestamp('2010-12-29 02:00:00'): 43.700000000000003,
 Timestamp('2010-12-29 03:00:00'): 43.299999999999997,
 Timestamp('2010-12-29 04:00:00'): 43.0,
 Timestamp('2010-12-29 05:00:00'): 42.600000000000001,
 Timestamp('2010-12-29 06:00:00'): 42.700000000000003,
 Timestamp('2010-12-29 07:00:00'): 41.799999999999997,
 Timestamp('2010-12-29 08:00:00'): 42.299999999999997,
 Timestamp('2010-12-29 09:00:00'): 45.700000000000003,
 Timestamp('2010-12-29 10:00:00'): 49.100000000000001,
 Timestamp('2010-12-29 11:00:00'): 52.0,
 Timestamp('2010-12-29 12:00:00'): 54.299999999999997,
 Timestamp('2010-12-29 13:00:00'): 56.399999999999999,
 Timestamp('2010-12-29 14:00:00'): 57.799999999999997,
 Timestamp('2010-12-29 15:00:00'): 58.399999999999999,
 Timestamp('2010-12-29 16:00:00'): 58.299999999999997,
 Timestamp('2010-12-29 17:00:00'): 57.100000000000001,
 Timestamp('2010-12-29 18:00:00'): 53.799999999999997,
 Timestamp('2010-12-29 19:00:00'): 50.600000000000001,
 Timestamp('2010-12-29 20:00:00'): 48.600000000000001,
 Timestamp('2010-12-29 21:00:00'): 47.600000000000001,
 Timestamp('2010-12-29 22:00:00'): 46.5,
 Timestamp('2010-12-29 23:00:00'): 45.799999999999997,
 Timestamp('2010-12-30 00:00:00'): 45.700000000000003,
 Timestamp('2010-12-30 01:00:00'): 44.200000000000003,
 Timestamp('2010-12-30 02:00:00'): 43.700000000000003,
 Timestamp('2010-12-30 03:00:00'): 43.299999999999997,
 Timestamp('2010-12-30 04:00:00'): 43.100000000000001,
 Timestamp('2010-12-30 05:00:00'): 42.600000000000001,
 Timestamp('2010-12-30 06:00:00'): 42.700000000000003,
 Timestamp('2010-12-30 07:00:00'): 41.899999999999999,
 Timestamp('2010-12-30 08:00:00'): 42.299999999999997,
 Timestamp('2010-12-30 09:00:00'): 45.799999999999997,
 Timestamp('2010-12-30 10:00:00'): 49.200000000000003,
 Timestamp('2010-12-30 11:00:00'): 52.200000000000003,
 Timestamp('2010-12-30 12:00:00'): 54.600000000000001,
 Timestamp('2010-12-30 13:00:00'): 56.799999999999997,
 Timestamp('2010-12-30 14:00:00'): 58.200000000000003,
 Timestamp('2010-12-30 15:00:00'): 58.799999999999997,
 Timestamp('2010-12-30 16:00:00'): 58.700000000000003,
 Timestamp('2010-12-30 17:00:00'): 57.5,
 Timestamp('2010-12-30 18:00:00'): 54.100000000000001,
 Timestamp('2010-12-30 19:00:00'): 50.899999999999999,
 Timestamp('2010-12-30 20:00:00'): 49.0,
 Timestamp('2010-12-30 21:00:00'): 47.899999999999999,
 Timestamp('2010-12-30 22:00:00'): 46.899999999999999,
 Timestamp('2010-12-30 23:00:00'): 46.100000000000001,
 Timestamp('2010-12-31 00:00:00'): 46.100000000000001,
 Timestamp('2010-12-31 01:00:00'): 44.5,
 Timestamp('2010-12-31 02:00:00'): 44.100000000000001,
 Timestamp('2010-12-31 03:00:00'): 43.700000000000003,
 Timestamp('2010-12-31 04:00:00'): 43.5,
 Timestamp('2010-12-31 05:00:00'): 42.899999999999999,
 Timestamp('2010-12-31 06:00:00'): 43.0,
 Timestamp('2010-12-31 07:00:00'): 42.200000000000003,
 Timestamp('2010-12-31 08:00:00'): 42.5,
 Timestamp('2010-12-31 09:00:00'): 46.0,
 Timestamp('2010-12-31 10:00:00'): 49.399999999999999,
 Timestamp('2010-12-31 11:00:00'): 52.399999999999999,
 Timestamp('2010-12-31 12:00:00'): 54.700000000000003,
 Timestamp('2010-12-31 13:00:00'): 56.899999999999999,
 Timestamp('2010-12-31 14:00:00'): 58.200000000000003,
 Timestamp('2010-12-31 15:00:00'): 58.799999999999997,
 Timestamp('2010-12-31 16:00:00'): 58.799999999999997,
 Timestamp('2010-12-31 17:00:00'): 57.600000000000001,
 Timestamp('2010-12-31 18:00:00'): 54.299999999999997,
 Timestamp('2010-12-31 19:00:00'): 51.100000000000001,
 Timestamp('2010-12-31 20:00:00'): 49.0,
 Timestamp('2010-12-31 21:00:00'): 47.899999999999999,
 Timestamp('2010-12-31 22:00:00'): 46.899999999999999,
 Timestamp('2010-12-31 23:00:00'): 46.200000000000003}

ts_df = DataFrame.from_dict(ts_dict,orient='index')