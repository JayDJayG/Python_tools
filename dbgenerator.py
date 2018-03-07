import random

'''

    DROP TABLE IF EXISTS `cars_vehicles`;
    CREATE TABLE `cars_vehicles` (
      `id` int(10) UNSIGNED NOT NULL,
      `ad_id` int(11) DEFAULT NULL,
      `transmission` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `fuel_type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `engine_cc` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `mileage` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `build_year` date DEFAULT NULL,
      `created_at` timestamp NULL DEFAULT NULL,
      `updated_at` timestamp NULL DEFAULT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

    --
    -- Dumping data for table `cars_vehicles`
    --

    INSERT INTO `cars_vehicles` (`id`, `ad_id`, `transmission`, `fuel_type`, `engine_cc`, `mileage`, `build_year`, `created_at`, `updated_at`) VALUES
    (1, 15, 'automatic', 'diesel', '2500', '6', '2016-01-01', '2017-08-12 11:58:05', '2017-08-12 12:38:36');
    (2,14,"manual","diesel",2031,12,"2017-10-25", '2017-08-12 11:58:05', '2017-08-12 12:38:36');
    (3,1,"manual","diesel",2218,30,"2017-06-22", '2017-08-12 11:58:05', '2017-08-12 12:38:36');
    (4,3,"manual","diesel",2228,25,"2017-09-08", '2017-08-12 11:58:05', '2017-08-12 12:38:36');
    (5,3,"manual","diesel",2903,8,"2017-03-29", '2017-08-12 11:58:05', '2017-08-12 12:38:36');
    (6,13,"manual","diesel",2046,8,"2018-02-09", '2017-08-12 11:58:05', '2017-08-12 12:38:36');
    (7,2,"manual","diesel",2464,17,"2017-07-11", '2017-08-12 11:58:05', '2017-08-12 12:38:36');
    (8,14,"manual","diesel",2898,6,"2017-10-18", '2017-08-12 11:58:05', '2017-08-12 12:38:36');
    (9,4,"manual","diesel",2935,8,"2018-05-13", '2017-08-12 11:58:05', '2017-08-12 12:38:36');
    (10,7,"manual","diesel",2606,29,"2018-02-14", '2017-08-12 11:58:05', '2017-08-12 12:38:36');
    (11,9,"manual","diesel",2823,7,"2017-06-27", '2017-08-12 11:58:05', '2017-08-12 12:38:36');


'''
ad_id = []
mileage = []
transmission = ['manual', 'automatic']

fuel_type = ['gasoline','diesel','naft', 'ethanol', 'biodiesel', 'electricity']
brand = ['HYUNDAI','TOYOTA','KIA','NISSAN','SUZUKI','HONDA', 'MAZDA', 'CHEVROLET', 'MITSUBISHI', 'FORD' ]
engine_cc = ["1500", "2000", "2500", "3000", "3500", "4000"]
build_year = ["2017-10-25", "2017-05-17", "2014-09-25", "2013-03-21", "2012-06-27", "2011-09-30", "2003-12-31","2017-06-27"]


created_at = '2017-08-12 11:58:05'
updated_at = '2017-08-12 11:58:05'

for i in range (1, 20):
    ad_id.append(i)
    mileage.append(i * 10000)

print("INSERT INTO `cars_vehicles` (`id`, `ad_id`, `brand`,`transmission`, `fuel_type`, `engine_cc`, `mileage`, `build_year`, `created_at`, `updated_at`) VALUES")

for j in range(2, 1000):

    print( '(' + str(j) + ',' + str(ad_id[random.randint(0,18)])  + ',\'' + str(brand[random.randint(0, len(transmission) - 1)]) + '\',\'' + str(transmission[random.randint(0, len(transmission) - 1)]) + '\',\'' + str(fuel_type[random.randint(0, len(fuel_type) - 1)]) +
          '\',\'' + str(engine_cc[random.randint(0,5)]) + '\',\'' + str(mileage[random.randint(0, len(transmission) - 1)]) + '\',\'' + str(build_year[random.randint(0, 7)]) + '\',\'' + created_at +'\',\'' + updated_at + '\'),')
