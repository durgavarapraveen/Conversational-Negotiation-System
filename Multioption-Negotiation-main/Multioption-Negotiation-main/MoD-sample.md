Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, here are three options: Rosa's Bed and Breakfast, The Bridge Guest House, and Aylesbray Lodge Guest House. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between them? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse with luxurious rooms, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | How much does each option cost? | Add_aspect_price
10 | Bot | Rosa's Bed and Breakfast is currently offering a 33% discount, with double rooms priced at £100, family rooms at £150, and single rooms at £75. The Bridge Guest House has double rooms at £75, family rooms at £90, and single rooms at £50. Aylesbray Lodge Guest House is currently offering a 30% discount, with double rooms priced at £105, family rooms at £135, and single rooms at £80. | Provide_differences
11 | User | Can you suggest more options? | Ask_alternatives
12 | Bot | Sure, how about The Lensfield Hotel? It's a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. | Multioption_suggestion
13 | User | How much does it cost? | Add_aspect_price
14 | Bot | The Lensfield Hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. | Provide_differences
15 | User | I'm interested in Rosa's Bed and Breakfast. Can you negotiate the price? | Negotiation
16 | Bot | I can negotiate up to 10% of the suggested price, but some facilities might get removed. | Provide_negotiation
17 | User | Can you remove the gym and pool facilities? | Negotiation
18 | Bot | Sure, I can remove those facilities. The new price for a single room will be £67.50. | Provide_negotiation
19 | User | That's still a bit high. Can you lower it to £60? | Negotiation
20 | Bot | I'm sorry, but I can't lower it that much. The best I can do is £65. | Provide_negotiation
21 | User | Alright, I'll take it. | Selection
22 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for the booking. | Confirmation, Ask_details
23 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
24 | Bot | Thank you, John. Your booking has been confirmed. You will receive an email with the details shortly. Is there anything else I can help you with? | Confirmation
25 | User | Can you tell me more about the breakfast options at Rosa's Bed and Breakfast? | Add_aspect_breakfast
26 | Bot | The breakfast options at Rosa's Bed and Breakfast are extensive and include both continental and cooked options. | Provide_details
27 | User | Can I add a late check-out option? | Add_aspect_late_check_out
28 | Bot | I'm sorry, but late check-out is not available at Rosa's Bed and Breakfast. | Provide_details
29 | User | Can you suggest some nearby attractions? | Add_aspect_nearby_attractions
30 | Bot | Sure, some nearby attractions include the Cambridge University Botanic Garden, the Fitzwilliam Museum, and the Cambridge Corn Exchange. | Provide_details
31 | User | Thanks for your help. | Goodbye
32 | Bot | You're welcome. Have a great stay at Rosa's Bed and Breakfast! | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, here are three options: Rosa's Bed and Breakfast, The Bridge Guest House, and Aylesbray Lodge Guest House. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between them? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse with luxurious rooms, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | How much does each option cost? | Add_aspect_price
10 | Bot | Rosa's Bed and Breakfast is currently offering a 33% discount, with double rooms priced at £100, family rooms at £150, and single rooms at £75. The Bridge Guest House has double rooms at £75, family rooms at £90, and single rooms at £50. Aylesbray Lodge Guest House is currently offering a 30% discount, with double rooms priced at £105, family rooms at £135, and single rooms at £80. | Provide_differences
11 | User | Can you suggest more options? | Ask_alternatives
12 | Bot | Sure, how about The Lensfield Hotel? It's a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. | Multioption_suggestion
13 | User | How much does it cost? | Add_aspect_price
14 | Bot | The Lensfield Hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. | Provide_differences
15 | User | I'm interested in Rosa's Bed and Breakfast. Can you negotiate the price? | Negotiation
16 | Bot | I can negotiate up to 10% of the suggested price, but some facilities might get removed. | Provide_negotiation
17 | User | Can you remove the gym and pool facilities? | Add_aspect_facilities
18 | Bot | Sure, I can remove those facilities. The new price for a single room will be £67.50. | Provide_negotiation
19 | User | That's still a bit high. Can you lower it to £60? | Negotiation
20 | Bot | I'm sorry, but I can only go as low as £65. | Provide_negotiation
21 | User | Alright, I'll take it. | Selection
22 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for the booking. | Confirmation, Ask_details
23 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
24 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation
25 | User | Can you suggest some good restaurants in the area? | Add_aspect_restaurants
26 | Bot | Sure, how about The Cambridge Chop House, The Oak Bistro, and The Pint Shop? | Multioption_suggestion
27 | User | What are the differences between them? | Ask_differences
28 | Bot | The Cambridge Chop House is a traditional British restaurant with a cozy atmosphere and great food. The Oak Bistro is a French restaurant with a romantic ambiance and delicious cuisine. The Pint Shop is a gastropub with a wide selection of beers and tasty bar food. | Provide_differences
29 | User | How much do they cost? | Add_aspect_price
30 | Bot | The Cambridge Chop House has main courses priced at around £20, The Oak Bistro has main courses priced at around £30, and The Pint Shop has bar food priced at around £10. | Provide_differences
31 | User | I think I'll go with The Cambridge Chop House. Can you make a reservation for me? | Selection
32 | Bot | I'm sorry, but I'm not able to make restaurant reservations. However, I can provide you with their contact information. | Inform
33 | User | That's alright, please give me their contact information. | Inform
34 | Bot | The Cambridge Chop House's phone number is 01223 359506 and their email is info@cambridgechophouse.co.uk. Enjoy your stay in Cambridge! | Inform, Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_details
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Ask_alternatives
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_details
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_details
13 | User | Can you tell me more about the Huntingdon Marriott Hotel's food festival? | Add_aspect_X
14 | Bot | The Huntingdon Marriott Hotel is currently running a food festival with free dinner for guests. | Provide_details
15 | User | I'm interested in the Cambridge Belfry, but it's a bit expensive. Can you offer a lower price? | Negotiation
16 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
17 | User | Can you remove the jacuzzi? | Negotiation
18 | Bot | Sure, I can remove the jacuzzi. The new price will be £135 per night. | Provide_negotiation
19 | User | That's still a bit high. Can you offer a lower price? | Negotiation
20 | Bot | I'm sorry, but £135 is the best I can do. | Provide_negotiation
21 | User | Alright, I'll take it. | Selection
22 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details
23 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
24 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Confirmation
25 | User | Actually, can you tell me more about the Finches Bed and Breakfast? | Ask_alternatives
26 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_details
27 | User | That sounds great, but how much does it cost? | Add_aspect_X
28 | Bot | Finches Bed and Breakfast offers double rooms for £120, single rooms for £90, and family rooms for £150. | Provide_details
29 | User | Can you tell me more about the family rooms? | Add_aspect_X
30 | Bot | The family rooms are spacious and can accommodate up to 4 people. They have a separate living area and a kitchenette. | Provide_details
31 | User | That sounds perfect. Can I book a family room for the same dates as before? | Selection
32 | Bot | I'm sorry, but all the family rooms are booked for those dates. Would you like me to suggest some other dates? | Ask_alternatives
33 | User | No, that's alright. I'll stick with the Cambridge Belfry. | Selection
34 | Bot | Great, your booking is confirmed. Is there anything else I can help you with? | Confirmation
35 | User | No, that's all. Thank you for your help. | Goodbye
36 | Bot | You're welcome. Have a great day! | Goodbye
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have 3 options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive but has luxurious rooms, a gym, and a pool. The A and B Guest House has a BBQ grill and Jacuzzi. Allenbell guesthouse is affordable and has a bar. | Provide_differences |
| 9 | User | Can you suggest more options? | Ask_alternatives |
| 10 | Bot | Sure, I have two more options for you. The first is Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. The second is Autumn House, a 4-star guesthouse with a 37% discount on bookings for the next 2 days and free dinner. | Multioption_suggestion |
| 11 | User | What are the differences between Carolina Bed and Breakfast and Autumn House? | Ask_differences |
| 12 | Bot | Carolina Bed and Breakfast has a pool, BBQ grill, and Jacuzzi. Autumn House has a DJ floor and fully safe, sanitary, and secure rooms. | Provide_differences |
| 13 | User | I'm interested in Leverton House, but it's over my budget. Can you offer a lower price? | Negotiation |
| 14 | Bot | I can offer a 10% discount, but some facilities like the gym and pool might not be available. | Provide_negotiation |
| 15 | User | Okay, I'll take the offer. | Affirm, Selection |
| 16 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details |
| 17 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform |
| 18 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye |
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is also a 4-star hotel with a food festival and DJ floor. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a luxurious hotel with spacious rooms, free breakfast, and 24/7 room service. It has received prestigious awards and has hosted celebrities like Virat Kholi and Eminem. | Provide_differences
9 | User | What about the Huntingdon Marriott Hotel? | Add_aspect_X
10 | Bot | The Huntingdon Marriott Hotel is a luxurious hotel with excellent 24/7 room service, a food festival, and a DJ floor. It has received prestigious awards and has hosted celebrities like Virat Kholi and Tom Holland. | Provide_differences
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a guesthouse with clean rooms, friendly staff, and a 32% discount. It offers free breakfast and 24/7 room service. | Provide_differences
13 | User | I'm interested in the Huntingdon Marriott Hotel. Can you negotiate the price? | Negotiation
14 | Bot | I can offer a 10% discount, but some facilities might get removed. | Provide_negotiation
15 | User | Can you remove the DJ floor? | Negotiation
16 | Bot | Sure, I can remove the DJ floor. The new price is £270. | Provide_negotiation
17 | User | That's still a bit high. Can you offer a better price? | Negotiation
18 | Bot | I can offer a 15% discount, but the food festival will be removed. | Provide_negotiation
19 | User | Alright, I'll take it. | Selection
20 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and number of people. | Confirmation, Ask_details
21 | User | My name is John Smith, email is johnsmith@gmail.com, and there will be 2 people. | Inform
22 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Confirmation
23 | User | Can you suggest more options? | Ask_alternatives
24 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse with great facilities. | Multioption_suggestion
25 | User | Can you tell me more about it? | Add_aspect_X
26 | Bot | Finches Bed and Breakfast is a luxurious guesthouse with spacious rooms, free breakfast, and 24/7 room service. It has a gym, pool, bar, BBQ grill, and Jacuzzi. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi and Eminem. | Provide_differences
27 | User | What's the price range? | Add_aspect_X
28 | Bot | The double rooms are £120, single rooms are £90, and family rooms are £180. | Add_aspect_X
29 | User | That's a bit expensive. Can you suggest something cheaper? | Ask_alternatives
30 | Bot | How about Hobsons House? It's a 3-star guesthouse with a 32% discount and free dinner. | Multioption_suggestion
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The first is Rosa's Bed and Breakfast, a 4-star guesthouse with a 33% discount for the next 4 days. The second is The Bridge Guest House, a 3-star guesthouse with moderate pricing. The third is Aylesbray Lodge Guest House, a 4-star hotel with a 30% discount for the next 2 days. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
10 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you negotiate the price? | Negotiation
12 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. Would you like to proceed with the booking? | Provide_negotiation
13 | User | Can you tell me more about The Bridge Guest House? | Selection
14 | Bot | The Bridge Guest House is a 3-star guesthouse located in the south area of Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also provides parking and internet facilities. The hotel has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. The hotel offers moderate pricing with double rooms at £75, family rooms at £90, and single rooms at £50. | Selection
15 | User | That sounds good. Can I see more options? | Ask_alternatives
16 | Bot | Sure, what other criteria would you like to add? | Add_aspect_X
17 | User | I'd like a hotel with a pool. | Add_aspect_X
18 | Bot | I have two options for you. The first is Rosa's Bed and Breakfast, a 4-star guesthouse with a pool, gym, bar, and BBQ grill. The second is Aylesbray Lodge Guest House, a 4-star hotel with a pool, gym, bar, and BBQ grill. Which one would you like to know more about? | Multioption_suggestion
19 | User | What are the differences between the options? | Ask_differences
20 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
21 | User | Can you tell me more about Aylesbray Lodge Guest House? | Selection
22 | Bot | Aylesbray Lodge Guest House is a 4-star hotel located in South with free internet and parking. The hotel offers moderate prices for single, double, and family rooms. It has excellent 24/7 room service, free breakfast, and free wifi. The hotel features a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms that are fully safe, sanitary, and secure. Aylesbray Lodge Guest House has been recognized by famous magazines, tour agencies, and critics. It has hosted celebrities like Ronaldo, Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named Dine with Me. The hotel is currently offering a 30% discount on bookings for the next 2 days, with only 2 rooms left. It is popular with locals, tour agencies, and has a huge social media presence with an 8/10 rating. | Selection
23 | User | That sounds good. Can I negotiate the price? | Negotiation
24 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. Would you like to proceed with the booking? | Provide_negotiation
25 | User | Can you tell me more about the facilities at Aylesbray Lodge Guest House? | Ask_details
26 | Bot | Aylesbray Lodge Guest House has a gym, pool, bar, and BBQ grill. The hotel also offers free breakfast, free wifi, and excellent 24/7 room service. | Ask_details
27 | User | Can I see more options? | Ask_alternatives
28 | Bot | Sure, what other criteria would you like to add? | Add_aspect_X
29 | User | I'd like a hotel with a bar. | Add_aspect_X
30 | Bot | I have two options for you. The first is Rosa's Bed and Breakfast, a 4-star guesthouse with a pool, gym, bar, and BBQ grill. The second is Aylesbray Lodge Guest House, a 4-star hotel with a pool, gym, bar, and BBQ grill. Which one would you like to know more about? | Multioption_suggestion
31 | User | What are the differences between the options? | Ask_differences
32 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
33 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
34 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Selection
35 | User | Can I negotiate the price for Rosa's Bed and Breakfast? | Negotiation
36 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. Would you like to proceed with the booking? | Provide_negotiation
37 | User | Can you tell me more about the facilities at Rosa's Bed and Breakfast? | Ask_details
38 | Bot | Rosa's Bed and Breakfast has a gym, pool, bar, and BBQ grill. The hotel also offers free breakfast, free wifi, and excellent 24/7 room service. | Ask_details
39 | User | Can I see more options? | Ask_alternatives
40 | Bot | Sure, what other criteria would you like to add? | Add_aspect_X
41 | User | I'd like a hotel with free parking. | Add_aspect_X
42 | Bot | I have two options for you. The first is Rosa's Bed and Breakfast, a 4-star guesthouse with free parking, pool, gym, bar, and BBQ grill. The second is Aylesbray Lodge Guest House, a 4-star hotel with free parking, pool, gym, bar, and BBQ grill. Which one would you like to know more about? | Multioption_suggestion
43 | User | What are the differences between the options? | Ask_differences
44 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
45 | User | Can you tell me more about Aylesbray Lodge Guest House? | Selection
46 | Bot | Aylesbray Lodge Guest House is a 4-star hotel located in South with free internet and parking. The hotel offers moderate prices for single, double, and family rooms. It has excellent 24/7 room service, free breakfast, and free wifi. The hotel features a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms that are fully safe, sanitary, and secure. Aylesbray Lodge Guest House has been recognized by famous magazines, tour agencies, and critics. It has hosted celebrities like Ronaldo, Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named Dine with Me. The hotel is currently offering a 30% discount on bookings for the next 2 days, with only 2 rooms left. It is popular with locals, tour agencies, and has a huge social media presence with an 8/10 rating. | Selection
47 | User | Can I negotiate the price for Aylesbray Lodge Guest House? | Negotiation
48 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. Would you like to proceed with the booking? | Provide_negotiation
49 | User | Can you tell me more about the facilities at Aylesbray Lodge Guest House? | Ask_details
50 | Bot | Aylesbray Lodge Guest House has a gym, pool, bar, and BBQ grill. The hotel also offers free breakfast, free wifi, and excellent 24/7 room service. | Ask_details
51 | User | I need some time to decide. | Inform
52 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
53 | User | Can you tell me more about the location of Rosa's Bed and Breakfast? | Ask_details
54 | Bot | Rosa's Bed and Breakfast is located in the South area of Cambridge. It is easily accessible by public transport and is close to many tourist attractions. | Ask_details
55 | User | Can I see more options? | Ask_alternatives
56 | Bot | Sure, what other criteria would you like to add? | Add_aspect_X
57 | User | I'd like a hotel with a view. | Add_aspect_X
58 | Bot | I'm sorry, but none of the hotels I have suggested have a view. Is there anything else I can help you with? | Deny
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | Can you tell me the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is also a 4-star hotel with a food festival and DJ floor. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a luxurious hotel with spacious rooms, free breakfast, and 24/7 room service. It has received prestigious awards and has hosted celebrities. | Provide_differences
9 | User | How much does it cost per night? | Add_aspect_X
10 | Bot | The Cambridge Belfry costs £120 per night for a double room, £100 for a single room, and £150 for a family room. | Provide_differences
11 | User | That's a bit expensive. Can you suggest a cheaper option? | Ask_alternatives
12 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse with free breakfast, 24/7 room service, and a gym. | Multioption_suggestion
13 | User | Can you tell me more about Finches Bed and Breakfast? | Add_aspect_X
14 | Bot | Finches Bed and Breakfast is a luxurious guesthouse with spacious rooms, a gym, pool, and jacuzzi. It has received prestigious awards and has hosted celebrities. | Provide_differences
15 | User | How much does it cost per night? | Add_aspect_X
16 | Bot | Finches Bed and Breakfast costs £130 per night for a double room, £110 for a single room, and £170 for a family room. | Provide_differences
17 | User | That's still a bit expensive. Can you negotiate the price for me? | Negotiation
18 | Bot | I can negotiate up to 10% of the suggested price, but some facilities might get removed. Which option would you like to negotiate for? | Provide_negotiation
19 | User | I'd like to negotiate for Finches Bed and Breakfast. | Selection
20 | Bot | Alright, I can offer you a 10% discount on the family room, but the pool and jacuzzi won't be available. | Provide_negotiation
21 | User | That sounds good. Can I book it now? | Selection
22 | Bot | Sure, I just need your name, email, and number of people staying. | Ask_details
23 | User | My name is John Smith, my email is johnsmith@gmail.com, and there will be 4 people staying. | Inform
24 | Bot | Great, your booking has been confirmed. Your registration number is 123456. The address is 123 Main Street. Is there anything else I can help you with? | Confirmation
25 | User | Actually, can you suggest another option with a pool and jacuzzi? | Ask_alternatives
26 | Bot | How about The Cambridge Belfry? It has a pool and jacuzzi. | Multioption_suggestion
27 | User | Can you tell me more about The Cambridge Belfry? | Add_aspect_X
28 | Bot | The Cambridge Belfry is a luxurious hotel with spacious rooms, free breakfast, and 24/7 room service. It has a gym, pool, and jacuzzi. It has received prestigious awards and has hosted celebrities. | Provide_differences
29 | User | How much does it cost per night? | Add_aspect_X
30 | Bot | The Cambridge Belfry costs £120 per night for a double room, £100 for a single room, and £150 for a family room. | Provide_differences
31 | User | That's still a bit expensive. Can you negotiate the price for me? | Negotiation
32 | Bot | I can offer you a 5% discount on the family room, but the gym won't be available. | Provide_negotiation
33 | User | Can you make it a 10% discount? | Negotiation
34 | Bot | I'm sorry, but I can only offer a 5% discount. | Provide_negotiation
35 | User | Alright, I'll take it. Can I book it now? | Selection
36 | Bot | Sure, I just need your name, email, and number of people staying. | Ask_details
37 | User | My name is John Smith, my email is johnsmith@gmail.com, and there will be 4 people staying. | Inform
38 | Bot | Great, your booking has been confirmed. Your registration number is 654321. The address is 456 Main Street. Is there anything else I can help you with? | Confirmation
39 | User | No, that's all. Thank you. | Goodbye
40 | Bot | You're welcome. Have a great day! | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, and a pool. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Selection
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Provide_details
9 | User | Can you suggest a cheaper option? | Ask_alternatives
10 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Cityroomz has no parking, but offers affordable prices for single, double, and family rooms. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices. | Multioption_suggestion
11 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
12 | Bot | Cityroomz has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse with a 0-star rating and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. | Provide_differences
13 | User | Can you tell me more about the University Arms Hotel? | Selection
14 | Bot | The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, a pool, and spacious rooms. The hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_details
15 | User | Can you suggest another option? | Ask_alternatives
16 | Bot | Sure, I have The Gonville Hotel, Alexander Bed and Breakfast, and El Shaddai. Which one would you like to know more about? | Multioption_suggestion
17 | User | Can you tell me more about the Alexander Bed and Breakfast? | Selection
18 | Bot | The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_details
19 | User | Can you suggest a cheaper option? | Ask_alternatives
20 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Cityroomz has no parking, but offers affordable prices for single, double, and family rooms. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices. | Multioption_suggestion
21 | User | I'm interested in the University Arms Hotel, but it's a bit expensive. Can you offer a discount? | Negotiation
22 | Bot | I'm sorry, but the prices are fixed. However, I can offer you a 10% discount on the University Arms Hotel, but some of the facilities provided might get removed. | Provide_negotiation
23 | User | Can you remove the gym and pool facilities? | Negotiation
24 | Bot | Sure, I can remove the gym and pool facilities. The new price for the University Arms Hotel will be £270 for a single room and £360 for a family room. | Provide_negotiation
25 | User | That's still a bit expensive. Can you offer a better price? | Negotiation
26 | Bot | I'm sorry, but the prices are already discounted. However, I can offer you a free dinner and a 5% discount on the University Arms Hotel. | Provide_negotiation
27 | User | Okay, I'll take the University Arms Hotel. | Selection
28 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for the booking. | Confirmation
29 | User | My name is John Smith, my email is johnsmith@email.com, and my contact number is 0123456789. | Inform
30 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a 31% discount for the next 2 days and free dinner. The third is Lovell Lodge, a 2-star hotel with a moderate price range. Which one would you like to know more about? | Multioption_suggestion
7 | User | Can you tell me more about Kirkwood House? | Ask_differences
8 | Bot | Kirkwood House is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, BBQ grill, and Jacuzzi. It has spacious and luxurious rooms and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies and has received prestigious awards such as the Michelin Star. It has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. | Provide_differences
9 | User | What about Home from Home? | Ask_differences
10 | Bot | Home from Home is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and spacious luxurious rooms. It is fully safe, sanitary, and secure. It has been recognized by popular magazines and tour agencies and has hosted celebrities such as Ronaldo, Virat Kholi, and Tom Holland. It offers a moderate price range with double rooms at £75, family rooms at £105, and single rooms at £50. | Provide_differences
11 | User | And Lovell Lodge? | Ask_differences
12 | Bot | Lovell Lodge is a 2-star hotel with free breakfast, free wifi, and good room service. It has parking and internet facilities and takes bookings. The price range is moderate, with double rooms costing £65, family rooms £70, and single rooms £50. It has been endorsed by local tour agencies TourMe and has received local awards such as Food fest. | Provide_differences
13 | User | Can you suggest more options? | Ask_alternatives
14 | Bot | Sure, I have two more options for you. The first is Limehouse guesthouse, a 4-star hotel with free breakfast, 24/7 room service, free wifi, and great food. It has spacious and luxurious rooms, a gym, a pool, and a DJ floor. It has received prestigious awards such as Michelin Star and The Gold List and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. The second is Acorn Guest House, a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel has a gym and pool. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Ronaldo and Eminem. Which one would you like to know more about? | Multioption_suggestion
15 | User | Can you tell me more about Limehouse guesthouse? | Ask_differences
16 | Bot | Limehouse guesthouse is a 4-star hotel with free breakfast, 24/7 room service, free wifi, and great food. It has spacious and luxurious rooms, a gym, a pool, and a DJ floor. It has received prestigious awards such as Michelin Star and The Gold List and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. | Provide_differences
17 | User | And Acorn Guest House? | Ask_differences
18 | Bot | Acorn Guest House is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel has a gym and pool. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Ronaldo and Eminem. The head chef has a cookbook named "How to Burger." | Provide_differences
19 | User | Can you suggest more options? | Ask_alternatives
20 | Bot | I'm sorry, those are all the options available in the North area of Cambridge. Which one do you prefer? | Selection
21 | User | I'm interested in Kirkwood House, but the price is a bit high. Can you offer a discount? | Negotiation
22 | Bot | I'm sorry, but the price is already discounted by 36%. However, I can offer a 10% discount on the original price, but some facilities might get removed. | Provide_negotiation
23 | User | Can you remove the BBQ grill and Jacuzzi? | Negotiation
24 | Bot | Sure, I can remove those facilities and offer you a 10% discount on the original price. | Provide_negotiation
25 | User | Alright, I'll take it. | Affirm, Selection
26 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for the booking. | Confirmation, Ask_details
27 | User | My name is John Smith, my email is johnsmith@email.com, and my contact number is 1234567890. | Inform
28 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye
29 | User | Actually, can you tell me more about the gym at Kirkwood House? | Add_aspect_X
30 | Bot | The gym at Kirkwood House is fully equipped with state-of-the-art machines and equipment. It is open 24/7 and is free for all guests. | Provide_differences
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, based on your criteria, I have three options: Kirkwood House, Home from Home, and Lovell Lodge. | Multioption_suggestion
7 | User | Can you tell me the differences between the options? | Ask_differences
8 | Bot | Kirkwood House is a 4-star guesthouse with a gym, pool, bar, and Jacuzzi. Home from Home is also a 4-star guesthouse with a gym, pool, and bar. Lovell Lodge is a 2-star hotel with free breakfast and wifi. | Provide_differences
9 | User | What's the price range for each option? | Add_aspect_X
10 | Bot | Kirkwood House is currently offering a 36% discount, with prices starting at £90 per night. Home from Home has double rooms at £75, family rooms at £105, and single rooms at £50. Lovell Lodge has double rooms at £65, family rooms at £70, and single rooms at £50. | Add_aspect_X
11 | User | Can you suggest more options? | Ask_alternatives
12 | Bot | Sure, based on your criteria, I have two more options: The Limehouse guesthouse and Acorn Guest House. | Multioption_suggestion
13 | User | What are the differences between these options? | Ask_differences
14 | Bot | The Limehouse guesthouse is a 4-star hotel with a gym, pool, and DJ floor. Acorn Guest House is also a 4-star guesthouse with a gym and pool. | Provide_differences
15 | User | What's the price range for these options? | Add_aspect_X
16 | Bot | The Limehouse guesthouse has prices starting at £120 per night. Acorn Guest House has prices starting at £95 per night. | Add_aspect_X
17 | User | Can you tell me more about Kirkwood House? | Selection
18 | Bot | Kirkwood House is a 4-star guesthouse located in North Cambridge. It offers free breakfast, 24/7 room service, free wifi, a gym, pool, bar, BBQ grill, and Jacuzzi. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as the Michelin Star. The hotel has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. | Provide_details
19 | User | That sounds great, but can you lower the price to match Lovell Lodge? | Negotiation
20 | Bot | I'm sorry, but the price is already discounted by 36%. However, I can offer a 10% discount on the original price, but some facilities may be removed. | Provide_negotiation
21 | User | Okay, I'll go with Kirkwood House. | Selection
22 | Bot | Great, the hotel has been reserved for you. Your registration number is 12345. Please provide your name, email, and contact number for the booking. | Confirmation, Ask_details
23 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
24 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye
25 | User | Actually, can you tell me more about Home from Home? | Ask_alternatives
26 | Bot | Home from Home is a 4-star guesthouse located in North Cambridge. It offers free breakfast, 24/7 room service, free wifi, a gym, pool, and bar. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by popular magazines and tour agencies and has hosted celebrities such as Ronaldo, Virat Kholi, and Tom Holland. | Provide_details
27 | User | That sounds good too. Can you match the price of Lovell Lodge? | Negotiation
28 | Bot | I'm sorry, but the prices are fixed. However, I can offer a 5% discount on the original price, but some facilities may be removed. | Provide_negotiation
29 | User | Okay, I'll stick with Kirkwood House. | Selection
30 | Bot | Great, your booking is confirmed. Thank you for choosing our service. | Confirmation, Goodbye
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a 31% discount for the next 2 days and free dinner. The third is Lovell Lodge, a 2-star hotel with a moderate price range. Which one would you like to know more about? | Multioption_suggestion
7 | User | Can you tell me more about Kirkwood House? | Ask_differences
8 | Bot | Kirkwood House is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, BBQ grill, and Jacuzzi. It has spacious and luxurious rooms and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies and has received prestigious awards such as the Michelin Star. It has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. | Provide_differences
9 | User | What about Home from Home? | Ask_differences
10 | Bot | Home from Home is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and spacious luxurious rooms. It is fully safe, sanitary, and secure. It has been recognized by popular magazines and tour agencies and has hosted celebrities such as Ronaldo, Virat Kholi, and Tom Holland. It offers a moderate price range with double rooms at £75, family rooms at £105, and single rooms at £50. | Provide_differences
11 | User | And Lovell Lodge? | Ask_differences
12 | Bot | Lovell Lodge is a 2-star hotel with free breakfast, free wifi, and good room service. It has parking and internet facilities and takes bookings. The price range is moderate, with double rooms costing £65, family rooms £70, and single rooms £50. It has been endorsed by local tour agencies TourMe and has received local awards such as Food fest. | Provide_differences
13 | User | Can you suggest more options? | Ask_alternatives
14 | Bot | Sure, I have two more options for you. The first is Limehouse guesthouse, a 4-star hotel with free breakfast, 24/7 room service, free wifi, and great food. It has spacious and luxurious rooms, a gym, a pool, and a DJ floor. It has received prestigious awards such as Michelin Star and The Gold List and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. The second is Acorn Guest House, a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel has a gym and pool. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Ronaldo and Eminem. Which one would you like to know more about? | Multioption_suggestion
15 | User | Can you tell me more about Limehouse guesthouse? | Ask_differences
16 | Bot | Limehouse guesthouse is a 4-star hotel with free breakfast, 24/7 room service, free wifi, and great food. It has spacious and luxurious rooms, a gym, a pool, and a DJ floor. It has received prestigious awards such as Michelin Star and The Gold List and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. | Provide_differences
17 | User | And Acorn Guest House? | Ask_differences
18 | Bot | Acorn Guest House is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel has a gym and pool. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Ronaldo and Eminem. The head chef has a cookbook named "How to Burger." | Provide_differences
19 | User | Can you suggest more options? | Ask_alternatives
20 | Bot | I'm sorry, those are all the options available in the North area of Cambridge. Which one do you prefer? | Selection
21 | User | I'm interested in Kirkwood House, but the price is a bit high. Can you offer a discount? | Negotiation
22 | Bot | I'm sorry, but the price is already discounted by 36%. However, I can offer a 10% discount on the original price, but some facilities might get removed. | Provide_negotiation
23 | User | Can you remove the BBQ grill and Jacuzzi? | Negotiation
24 | Bot | Sure, I can remove those facilities and offer you a 10% discount on the original price. | Provide_negotiation
25 | User | Alright, I'll take it. | Affirm, Selection
26 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for the booking. | Confirmation, Ask_details
27 | User | My name is John Smith, my email is johnsmith@email.com, and my contact number is 1234567890. | Inform
28 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye
29 | User | Actually, can you tell me more about the gym at Kirkwood House? | Add_aspect_X
30 | Bot | The gym at Kirkwood House is fully equipped with state-of-the-art machines and equipment. It is open 24/7 and is free for all guests. | Provide_differences
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the centre of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, The University Arms Hotel, and The Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between them? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, and a pool. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. | Provide_differences
7 | User | Can you tell me more about The Gonville Hotel? | Selection
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Provide_details
9 | User | Can you tell me more about The University Arms Hotel? | Ask_alternatives
10 | Bot | The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, a pool, and spacious rooms. The hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_details
11 | User | What about The Alexander Bed and Breakfast? | Ask_alternatives
12 | Bot | The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_details
13 | User | I'm interested in The University Arms Hotel, but it's a bit expensive. Can you suggest something cheaper? | Negotiation
14 | Bot | I understand your concern. How much is your estimated budget? | Add_aspect_X
15 | User | My budget is around £80 per night. | Add_aspect_X
16 | Bot | I have two options for you. Cityroomz and El Shaddai. Which one would you like to know more about? | Multioption_suggestion
17 | User | What are the differences between them? | Ask_differences
18 | Bot | Cityroomz is a moderate hotel with internet access and affordable prices for single, double, and family rooms. The hotel has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse with internet and parking facilities, and takes bookings. The hotel has a 0-star rating and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
19 | User | Can you tell me more about Cityroomz? | Selection
20 | Bot | Cityroomz has affordable prices for single, double, and family rooms. The hotel has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. | Provide_details
21 | User | Can you tell me more about El Shaddai? | Ask_alternatives
22 | Bot | El Shaddai is a cheap guesthouse with internet and parking facilities, and takes bookings. The hotel has a 0-star rating and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_details
23 | User | I'm still not sure. Can you give me some time to think? | Inform
24 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
25 | User | Can you tell me more about the free dinner offer at The Gonville Hotel? | Ask_details
26 | Bot | The free dinner offer is available for bookings made in the next 4 days. The dinner includes a three-course meal with a choice of starter, main course, and dessert. | Provide_details
27 | User | Can I negotiate for a higher priced option for the price of the cheaper option? | Negotiation
28 | Bot | Negotiation is possible to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
29 | User | Can I negotiate for The University Arms Hotel? | Negotiation
30 | Bot | I'm sorry, negotiation is not possible for The University Arms Hotel. | Deny
31 | User | Okay, I'll go with The Gonville Hotel. | Selection
32 | Bot | Great, The Gonville Hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference for the final booking. | Confirmation
| Utterance # | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the centre of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan on staying? | Ask_details |
| 3 | User | I'll be there next week. | Inform |
| 4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details |
| 5 | User | Just me. | Inform |
| 6 | Bot | Alright, based on your criteria, I have 3 options for you. The Gonville Hotel, The University Arms Hotel, and The Alexander Bed and Breakfast. | Multioption_suggestion |
| 7 | User | What's the difference between them? | Ask_differences |
| 8 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, 24/7 room service, free wifi, a gym, a pool, and spacious rooms. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. | Provide_differences |
| 9 | User | How much does each one cost? | Ask_details |
| 10 | Bot | The Gonville Hotel ranges from £79 for a single room to £119 for a family room. The University Arms Hotel ranges from £150 for a single room to £250 for a family room. The Alexander Bed and Breakfast ranges from £100 for a single room to £150 for a family room. | Provide_differences |
| 11 | User | That's quite expensive. Do you have any cheaper options? | Ask_alternatives |
| 12 | Bot | I have two more options for you. Cityroomz and El Shaddai. Cityroomz has affordable prices for single, double, and family rooms, and El Shaddai offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. | Multioption_suggestion |
| 13 | User | What's the difference between Cityroomz and El Shaddai? | Ask_differences |
| 14 | Bot | Cityroomz has internet access and takes bookings, but has no parking. El Shaddai offers internet and parking facilities, and takes bookings. | Provide_differences |
| 15 | User | I think I'll go with The University Arms Hotel. | Selection |
| 16 | Bot | Great choice! The University Arms Hotel is a luxurious 4-star hotel with free breakfast, 24/7 room service, free wifi, a gym, a pool, and spacious rooms. | Affirm |
| 17 | User | The price is a bit high. Can you offer a discount? | Negotiation |
| 18 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation |
| 19 | User | Can you remove the gym and pool facilities? | Negotiation |
| 20 | Bot | Sure, I can remove those facilities and offer you a 10% discount. | Provide_negotiation |
| 21 | User | That sounds good. Can you reserve the hotel for me? | Selection |
| 22 | Bot | The hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation |
| 23 | User | My name is John Smith, my email is johnsmith@email.com, and my contact number is 0123456789. | Inform |
| 24 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye |
| 25 | User | Actually, can you recommend some good restaurants near the hotel? | Add_aspect_X |
| 26 | Bot | Sure, there are many great restaurants near The University Arms Hotel. Some popular options are Midsummer House, Parker's Tavern, and The Cambridge Chop House. | Provide_differences |
| 27 | User | Can you tell me more about Midsummer House? | Ask_details |
| 28 | Bot | Midsummer House is a Michelin-starred restaurant that offers modern British cuisine. It's located on Midsummer Common, just a short walk from The University Arms Hotel. | Provide_differences |
| 29 | User | That sounds great. Can you make a reservation for me? | Add_aspect_X |
| 30 | Bot | I'm sorry, but I'm not able to make restaurant reservations. However, I can provide you with the contact information for Midsummer House so you can make a reservation yourself. | Deny |
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a moderate price range and a 31% discount for the next 2 days. The third is Lovell Lodge, a 2-star hotel with a moderate price range and only 4 rooms left. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Kirkwood House is a 4-star guesthouse with a gym, pool, bar, BBQ grill, and Jacuzzi. Home from Home is also a 4-star guesthouse with a gym, pool, and bar. Lovell Lodge is a 2-star hotel with free breakfast and wifi. | Provide_differences
9 | User | Can you tell me more about Kirkwood House? | Selection
10 | Bot | Kirkwood House is a luxurious guesthouse with spacious rooms and has been recognized by famous magazines and tour agencies. It has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. It is currently offering a 36% discount on bookings for the next 3 days. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you offer a better price? | Negotiation
12 | Bot | I can offer a 10% discount, but some facilities like the BBQ grill and Jacuzzi might not be available. Would you like to proceed with the booking? | Provide_negotiation
13 | User | Hmm, can you tell me more about Home from Home? | Ask_alternatives
14 | Bot | Home from Home is a 4-star guesthouse with a moderate price range. It offers free breakfast, 24/7 room service, free wifi, a gym, pool, and bar. It has been recognized by popular magazines and tour agencies and has hosted celebrities such as Ronaldo, Virat Kholi, and Tom Holland. It is currently offering a 31% discount on bookings for the next 2 days and free dinner. | Selection
15 | User | That sounds good. Can I book it now? | Selection
16 | Bot | Sure, the hotel has been reserved. Please provide your name, email, and contact number for confirmation. | Confirmation
17 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
18 | Bot | Thank you, John. Your registration number is 1234. Is there anything else I can help you with? | Confirmation
19 | User | Actually, can you suggest one more option? | Ask_alternatives
20 | Bot | Sure, I have two more options for you. The first is Limehouse guesthouse, a 4-star hotel with a gym, pool, and DJ floor. The second is Acorn Guest House, a 4-star guesthouse with a gym, pool, and free dinner. Which one would you like to know more about? | Multioption_suggestion
21 | User | Can you tell me more about Limehouse guesthouse? | Selection
22 | Bot | Limehouse guesthouse is a luxurious 4-star hotel with spacious rooms, great food, and a DJ floor. It has received prestigious awards such as Michelin Star and The Gold List and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. It is fully safe, sanitary, and secure. | Selection
23 | User | That sounds amazing, but it's a bit over my budget. Can you offer a better price? | Negotiation
24 | Bot | I can offer a 10% discount, but some facilities like the DJ floor might not be available. Would you like to proceed with the booking? | Provide_negotiation
25 | User | I'll think about it. Can you tell me more about Acorn Guest House? | Ask_alternatives
26 | Bot | Acorn Guest House is a 4-star guesthouse with a gym, pool, and free dinner. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Ronaldo and Eminem. The head chef has a cookbook named "How to Burger." It is fully safe, sanitary, and secure. | Selection
27 | User | That sounds good. Can you tell me the price range? | Add_aspect_X
28 | Bot | The price range is moderate, with double rooms costing £85, family rooms £120, and single rooms £65. | Add_aspect_X
29 | User | That's a bit over my budget. Can you offer a better price? | Negotiation
30 | Bot | I can offer a 10% discount, but some facilities like the free dinner might not be available. Would you like to proceed with the booking? | Provide_negotiation
31 | User | I'll think about it. Can you suggest one more option? | Ask_alternatives
32 | Bot | I'm sorry, but those are all the available options in the North area of Cambridge within your budget. Is there anything else I can help you with? | Inform
33 | User | No, that's all. Thank you for your help. | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, and a pool. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Selection
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Provide_details
9 | User | Can you suggest a cheaper option? | Ask_alternatives
10 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Cityroomz has no parking, but offers affordable prices for single, double, and family rooms. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices. | Multioption_suggestion
11 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
12 | Bot | Cityroomz has internet access and takes bookings, but has no parking. El Shaddai offers internet and parking facilities, and takes bookings. El Shaddai is cheaper, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
13 | User | Can you tell me more about the University Arms Hotel? | Selection
14 | Bot | The University Arms Hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_details
15 | User | Can you suggest another option? | Ask_alternatives
16 | Bot | Sure, I have The Gonville Hotel, Cityroomz, and El Shaddai. Which one would you like to know more about? | Multioption_suggestion
17 | User | Can you negotiate the price of The Gonville Hotel? | Negotiation
18 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. The hotel is already offering 38% off on bookings for the next 4 days and free dinner. | Provide_negotiation
19 | User | Can you remove the gym and safe facilities? | Negotiation
20 | Bot | Sure, I can remove the gym and safe facilities. The new price for a single room will be £71.10 and for a family room will be £107.10. | Provide_negotiation
21 | User | Can you suggest another option? | Ask_alternatives
22 | Bot | Sure, I have The Gonville Hotel, Cityroomz, and El Shaddai. Which one would you like to know more about? | Multioption_suggestion
23 | User | Can you tell me more about the Alexander Bed and Breakfast? | Selection
24 | Bot | The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_details
25 | User | Can you suggest another option? | Ask_alternatives
26 | Bot | Sure, I have The Gonville Hotel, Cityroomz, and El Shaddai. Which one would you like to know more about? | Multioption_suggestion
27 | User | Can you tell me more about Cityroomz? | Selection
28 | Bot | Cityroomz is a moderate hotel located in the centre of Cambridge, with internet access and takes bookings. Although it has no parking, it offers affordable prices for single, double, and family rooms. The hotel has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. | Provide_details
29 | User | Can you suggest another option? | Ask_alternatives
30 | Bot | Sure, I have The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
31 | User | Can you tell me more about El Shaddai? | Selection
32 | Bot | El Shaddai is a cheap guesthouse located in the centre of Cambridge. It offers internet and parking facilities, and takes bookings. The hotel has a 0-star rating and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. Contact the hotel at 01223327978 or visit 41 Warkworth Street, CB11EG. | Provide_details
33 | User | Can you suggest another option? | Ask_alternatives
34 | Bot | I'm sorry, those are all the options I have for your criteria. Have you made a decision? | Inform
35 | User | I need some time to think. | Inform
36 | Bot | Sure, take your time. Let me know if you have any other questions. | Inform
37 | User | Can you tell me more about the free dinner offer at The Gonville Hotel? | Ask_details
38 | Bot | The free dinner offer is available for bookings made in the next 4 days. The hotel offers a set menu with a choice of vegetarian and non-vegetarian options. The dinner includes a starter, main course, and dessert. | Provide_details
39 | User | Can I book The Gonville Hotel? | Lookup
40 | Bot | Sure, The Gonville Hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation
41 | User | My name is John Smith, email is johnsmith@gmail.com, there will be 2 people, and we prefer a family room. | Inform
42 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation
43 | User | No, that's all. Thank you. | Goodbye
44 | Bot | You're welcome, John. Have a great day! | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The Cambridge Belfry is £120 per night, Huntingdon Marriott Hotel is £150 per night, and Hobsons House is £75 per night. | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
9 | User | Can you suggest more options? | Ask_alternatives
10 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse with a gym, pool, and BBQ grill. It's £130 per night. | Multioption_suggestion
11 | User | What are the differences between the options? | Ask_differences
12 | Bot | The Cambridge Belfry and Finches Bed and Breakfast are both 4-star hotels with a gym, pool, and jacuzzi. Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
13 | User | I'm interested in Huntingdon Marriott Hotel. Can you negotiate the price? | Negotiation
14 | Bot | I can offer you a 10% discount, but some facilities like the DJ floor and free dinner will be removed. | Provide_negotiation
15 | User | Can you suggest more options? | Ask_alternatives
16 | Bot | Sure, how about The Varsity Hotel & Spa? It's a 4-star hotel with a spa, gym, and rooftop bar. It's £180 per night. | Multioption_suggestion
17 | User | What are the differences between Huntingdon Marriott Hotel and The Varsity Hotel & Spa? | Ask_differences
18 | Bot | Huntingdon Marriott Hotel has a DJ floor and free dinner, while The Varsity Hotel & Spa has a spa and rooftop bar. | Provide_differences
19 | User | I'll go with Huntingdon Marriott Hotel. | Selection
20 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details
21 | User | My name is John Smith, email is johnsmith@gmail.com, and contact number is 1234567890. | Inform
22 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_details
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Ask_alternatives
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_details
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_details
13 | User | Can you tell me more about the Huntingdon Marriott Hotel's food festival? | Add_aspect_X
14 | Bot | The Huntingdon Marriott Hotel is currently running a food festival with free dinner for guests. | Provide_details
15 | User | I'm interested in the Cambridge Belfry, but it's a bit expensive. Can you offer a lower price? | Negotiation
16 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
17 | User | Can you remove the jacuzzi? | Negotiation
18 | Bot | Sure, I can remove the jacuzzi. The new price will be £135 per night. | Provide_negotiation
19 | User | That's still a bit high. Can you offer a lower price? | Negotiation
20 | Bot | I'm sorry, but £135 is the best I can do. | Provide_negotiation
21 | User | Alright, I'll take it. | Selection
22 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details
23 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
24 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Confirmation
25 | User | Actually, can you tell me more about the Finches Bed and Breakfast? | Ask_alternatives
26 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_details
27 | User | That sounds great, but how much does it cost? | Add_aspect_X
28 | Bot | Finches Bed and Breakfast offers double rooms for £120, single rooms for £90, and family rooms for £150. | Provide_details
29 | User | Can you tell me more about the Huntingdon Marriott Hotel's Michelin Star? | Add_aspect_X
30 | Bot | The Michelin Star is a prestigious award given to restaurants with exceptional quality. The Huntingdon Marriott Hotel has received this award for its excellent food and service. | Provide_details
31 | User | I'm still deciding between the Cambridge Belfry and Finches Bed and Breakfast. Can you give me a moment? | Selection
32 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_details
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Ask_alternatives
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_details
11 | User | Can you tell me more about the food festival at Huntingdon Marriott Hotel? | Add_aspect_X
12 | Bot | The food festival at Huntingdon Marriott Hotel offers free dinner for guests. It's a great opportunity to try out some delicious food. | Provide_details
13 | User | I'm not sure which one to choose. Can you suggest another option? | Ask_alternatives
14 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Multioption_suggestion
15 | User | What are the prices for Finches Bed and Breakfast? | Add_aspect_X
16 | Bot | Finches Bed and Breakfast offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_details
17 | User | Can you negotiate the price for Huntingdon Marriott Hotel? | Negotiation
18 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
19 | User | Can you remove the DJ floor and still keep the free dinner? | Negotiation
20 | Bot | I can remove the DJ floor, but the free dinner is part of the food festival package and cannot be removed. | Provide_negotiation
21 | User | Okay, I'll go with Huntingdon Marriott Hotel. | Selection
22 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation, Ask_details
23 | User | My name is John Smith, email is johnsmith@gmail.com, there will be 2 people, and we prefer a double room. | Inform
24 | Bot | Thank you, John. Your booking is confirmed. You will receive a confirmation email shortly. | Confirmation
25 | User | Can I add a request for a room with a view? | Add_aspect_X
26 | Bot | Sure, I'll add that to your booking. Is there anything else you need? | Ask_details
27 | User | No, that's all. | Affirm
28 | Bot | Thank you for booking with us, John. Have a great stay at Huntingdon Marriott Hotel. | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, here are three options: Rosa's Bed and Breakfast, The Bridge Guest House, and Aylesbray Lodge Guest House. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between them? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse with luxurious rooms, a gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, a gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | How much does each option cost? | Add_aspect_price
10 | Bot | Rosa's Bed and Breakfast is currently offering a 33% discount, with double rooms priced at £100, family rooms at £150, and single rooms at £75. The Bridge Guest House has double rooms at £75, family rooms at £90, and single rooms at £50. Aylesbray Lodge Guest House is currently offering a 30% discount, with double rooms priced at £105, family rooms at £135, and single rooms at £80. | Provide_differences
11 | User | Can you suggest more options? | Ask_alternatives
12 | Bot | Sure, how about The Lensfield Hotel? It's a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. | Multioption_suggestion
13 | User | How much does it cost? | Add_aspect_price
14 | Bot | The Lensfield Hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It's currently offering a 30% discount for the next 3 days. | Provide_differences
15 | User | I'm interested in Rosa's Bed and Breakfast. Can you negotiate the price? | Negotiation
16 | Bot | I can offer a 10% discount, but some facilities like the gym and pool might not be available. | Provide_negotiation
17 | User | Can you remove the BBQ grill instead? | Negotiation
18 | Bot | Sure, I can remove the BBQ grill and offer a 10% discount. The new price for a single room will be £67.5. | Provide_negotiation
19 | User | That sounds good. Can I book it now? | Selection
20 | Bot | Sure, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details
21 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
22 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a 31% discount for the next 2 days and free dinner. The third is Lovell Lodge, a 2-star hotel with a moderate price range and only 4 rooms left. Which one would you like to know more about? | Multioption_suggestion
7 | User | Can you tell me more about Kirkwood House? | Add_aspect_X
8 | Bot | Kirkwood House is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, BBQ grill, and Jacuzzi. It has spacious and luxurious rooms and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies and has received prestigious awards such as the Michelin Star. The hotel has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. | Provide_differences
9 | User | What about Home from Home? | Add_aspect_X
10 | Bot | Home from Home is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and spacious luxurious rooms. It is fully safe, sanitary, and secure. It has been recognized by popular magazines and tour agencies and has hosted celebrities such as Ronaldo, Virat Kholi, and Tom Holland. | Provide_differences
11 | User | And Lovell Lodge? | Add_aspect_X
12 | Bot | Lovell Lodge is a 2-star hotel with free breakfast, free wifi, and good room service. It has parking and internet facilities and takes bookings. The price range is moderate, with double rooms costing £65, family rooms £70, and single rooms £50. Lovell Lodge has been endorsed by local tour agencies TourMe and has received local awards such as Food fest. | Provide_differences
13 | User | Can you tell me more about the discounts for Kirkwood House and Home from Home? | Ask_differences
14 | Bot | Kirkwood House has a 36% discount for the next 3 days, while Home from Home has a 31% discount for the next 2 days and free dinner. | Provide_differences
15 | User | I'm interested in Kirkwood House, but the price is a bit high. Can you offer a lower price? | Negotiation
16 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
17 | User | Can you remove the BBQ grill and Jacuzzi? | Negotiation
18 | Bot | Sure, I can remove those facilities. The new price will be £150 per night. | Provide_negotiation
19 | User | That's still a bit high. Can you offer a lower price? | Negotiation
20 | Bot | I'm sorry, but £150 is the best I can do. | Provide_negotiation
21 | User | Alright, I'll think about it. Can you give me more options? | Ask_alternatives
22 | Bot | Sure, what criteria would you like me to use for the new options? | Ask_details
23 | User | Can you find me a 4-star hotel with a food festival? | Add_aspect_X
24 | Bot | I have two options for you. The first is Limehouse guesthouse, a 4-star hotel with a food festival and a DJ floor. The second is Acorn Guest House, a 4-star guesthouse with a food festival and a head chef with a cookbook named "How to Burger." Which one would you like to know more about? | Multioption_suggestion
25 | User | Can you tell me more about Limehouse guesthouse? | Add_aspect_X
26 | Bot | Limehouse guesthouse is a 4-star hotel with free breakfast, 24/7 room service, free wifi, and great food. It has spacious and luxurious rooms, a gym, a pool, and a DJ floor. It has received prestigious awards such as Michelin Star and The Gold List and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. | Provide_differences
27 | User | And Acorn Guest House? | Add_aspect_X
28 | Bot | Acorn Guest House is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel has a gym and pool. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Ronaldo and Eminem. The head chef has a cookbook named "How to Burger." | Provide_differences
29 | User | Can you tell me more about the prices for Limehouse guesthouse and Acorn Guest House? | Ask_differences
30 | Bot | I'm sorry, but I don't have any discounts available for those hotels. Limehouse guesthouse costs £200 per night, while Acorn Guest House costs £175 per night. | Provide_differences
31 | User | I'll need some time to think about it. Can I get back to you later? | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The first is Rosa's Bed and Breakfast, a 4-star guesthouse with a 33% discount for the next 4 days. The second is The Bridge Guest House, a 3-star guesthouse with moderate pricing. The third is Aylesbray Lodge Guest House, a 4-star hotel with a 30% discount for the next 2 days. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
10 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you negotiate the price? | Negotiation
12 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
13 | User | Can you remove the gym and pool facilities? | Negotiation
14 | Bot | Sure, I can remove the gym and pool facilities. The new price for Rosa's Bed and Breakfast will be £95 per night. | Provide_negotiation
15 | User | That's still a bit over my budget. Can you suggest another option? | Ask_alternatives
16 | Bot | Sure, I have one more option for you. The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Multioption_suggestion
17 | User | What are the differences between the Lensfield Hotel and the Bridge Guest House? | Ask_differences
18 | Bot | The Lensfield Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The Bridge Guest House is a 3-star guesthouse with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. | Provide_differences
19 | User | Can you tell me more about the Lensfield Hotel? | Selection
20 | Bot | The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Selection
21 | User | Can you negotiate the price for the Lensfield Hotel? | Negotiation
22 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Which facilities would you like to remove? | Provide_negotiation
23 | User | Can you remove the parking facility? | Negotiation
24 | Bot | Sure, I can remove the parking facility. The new price for the Lensfield Hotel will be £81 per night. | Provide_negotiation
25 | User | That sounds good. I'll go with the Lensfield Hotel. | Selection
26 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation, Ask_details
27 | User | My name is John Smith, my email is johnsmith@gmail.com, and there will be two people staying in the room. We prefer a double room. | Inform
28 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation, Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The first is Rosa's Bed and Breakfast, a 4-star guesthouse with a 33% discount for the next 4 days. The second is The Bridge Guest House, a 3-star guesthouse with moderate pricing. The third is Aylesbray Lodge Guest House, a 4-star hotel with a 30% discount for the next 2 days. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
10 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you negotiate the price? | Negotiation
12 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. Would you like to proceed with the booking? | Provide_negotiation
13 | User | Can you tell me more about The Bridge Guest House? | Selection
14 | Bot | The Bridge Guest House is a 3-star guesthouse located in the south area of Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also provides parking and internet facilities. The hotel has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. The hotel offers moderate pricing with double rooms at £75, family rooms at £90, and single rooms at £50. | Selection
15 | User | That sounds good. Can you suggest more options? | Ask_alternatives
16 | Bot | Sure, I have one more option for you. The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel has received recognitions such as appearing in local magazines like FoodVilla and Food and Beyond, being endorsed by local tour agencies TourMe, and receiving local awards such as Food Fest, Budget, and Great and Escape. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Multioption_suggestion
17 | User | Can you tell me more about The Lensfield Hotel? | Selection
18 | Bot | The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel has received recognitions such as appearing in local magazines like FoodVilla and Food and Beyond, being endorsed by local tour agencies TourMe, and receiving local awards such as Food Fest, Budget, and Great and Escape. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Selection
19 | User | I'm still not sure which one to choose. Can you give me some time to decide? | Inform
20 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
21 | User | Can you tell me more about the facilities at Aylesbray Lodge Guest House? | Selection
22 | Bot | Aylesbray Lodge Guest House is a 4-star hotel located in South with free internet and parking. The hotel offers moderate prices for single, double, and family rooms. It has excellent 24/7 room service, free breakfast, and free wifi. The hotel features a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms that are fully safe, sanitary, and secure. Aylesbray Lodge Guest House has been recognized by famous magazines, tour agencies, and critics. It has hosted celebrities like Ronaldo, Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named Dine with Me. The hotel is currently offering a 30% discount on bookings for the next 2 days, with only 2 rooms left. It is popular with locals, tour agencies, and has a huge social media presence with an 8/10 rating. | Selection
23 | User | Can you tell me more about the food at The Bridge Guest House? | Add_aspect_X
24 | Bot | The Bridge Guest House has delicious food that has been recognized by local magazines like MrHotel and Food and beyond. | Add_aspect_X
25 | User | Can you tell me more about the parking at Rosa's Bed and Breakfast? | Add_aspect_X
26 | Bot | Rosa's Bed and Breakfast offers free parking. | Add_aspect_X
27 | User | Can you tell me more about the public image rating of The Lensfield Hotel? | Add_aspect_X
28 | Bot | The Lensfield Hotel has a public image rating of 6/10. | Add_aspect_X
29 | User | I've decided to go with The Bridge Guest House. Can you book it for me? | Inform
30 | Bot | Sure, The Bridge Guest House has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation, Ask_details
31 | User | My name is John Smith, my email is johnsmith@gmail.com, and there will be two people staying in a double room. | Inform
32 | Bot | Great, your booking has been confirmed. You will receive an email with the details shortly. Thank you for choosing our service. | Confirmation, Goodbye
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. What's your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | Okay, I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a 31% discount for the next 2 days and free dinner. The third is Lovell Lodge, a 2-star hotel with a moderate price range. Which one would you like to know more about? | Multioption_suggestion
7 | User | What's the difference between Kirkwood House and Home from Home? | Ask_differences
8 | Bot | Kirkwood House is a bit more expensive, but it offers a gym, pool, bar, BBQ grill, and Jacuzzi. Home from Home doesn't have a BBQ grill or Jacuzzi, but it's a bit cheaper and offers free dinner. | Provide_differences
9 | User | Can you tell me more about Lovell Lodge? | Ask_alternatives
10 | Bot | Sure, Lovell Lodge is a 2-star hotel with free breakfast and wifi. It's a bit cheaper than the other two options, but it doesn't have as many amenities. | Provide_differences
11 | User | I think I'm interested in Kirkwood House. Can you tell me more about it? | Selection
12 | Bot | Kirkwood House is a 4-star guesthouse with free breakfast, 24/7 room service, and free wifi. It's fully safe, sanitary, and secure, and has spacious and luxurious rooms. It's been recognized by famous magazines and tour agencies, and has received prestigious awards such as the Michelin Star. It's hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. | Provide_differences
13 | User | The price is a bit high. Can you offer a discount? | Negotiation
14 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. Would you still like to proceed? | Provide_negotiation
15 | User | Can you remove the BBQ grill and Jacuzzi? | Negotiation
16 | Bot | Sure, I can remove those facilities and offer you a 10% discount. The final price would be £135 per night. Would you like to proceed? | Provide_negotiation
17 | User | That sounds good. How do I book? | Inform
18 | Bot | The hotel has been reserved for you. Your registration number is 12345. Please provide your name, email, and contact number for confirmation. | Confirmation
19 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
20 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye
| Utterance # | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the centre of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan on staying? | Ask_details |
| 3 | User | I'll be there next week. | Inform |
| 4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details |
| 5 | User | Just me. | Inform |
| 6 | Bot | Alright, based on your criteria, I have 3 options for you. The Gonville Hotel, The University Arms Hotel, and The Alexander Bed and Breakfast. | Multioption_suggestion |
| 7 | User | What's the difference between them? | Ask_differences |
| 8 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, 24/7 room service, free wifi, a gym, a pool, and spacious rooms. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. | Provide_differences |
| 9 | User | How much does each one cost? | Ask_details |
| 10 | Bot | The Gonville Hotel ranges from £79 for a single room to £119 for a family room. The University Arms Hotel ranges from £150 for a single room to £250 for a family room. The Alexander Bed and Breakfast ranges from £100 for a single room to £150 for a family room. | Provide_differences |
| 11 | User | That's quite expensive. Do you have any cheaper options? | Ask_alternatives |
| 12 | Bot | I have two more options for you. Cityroomz and El Shaddai. Cityroomz has affordable prices for single, double, and family rooms, and El Shaddai offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. | Multioption_suggestion |
| 13 | User | What's the difference between Cityroomz and El Shaddai? | Ask_differences |
| 14 | Bot | Cityroomz has internet access and takes bookings, but has no parking. El Shaddai offers internet and parking facilities, and takes bookings. | Provide_differences |
| 15 | User | I think I'll go with The University Arms Hotel. | Selection |
| 16 | Bot | Great choice! The University Arms Hotel is a luxurious 4-star hotel with free breakfast, 24/7 room service, free wifi, a gym, a pool, and spacious rooms. | Affirm |
| 17 | User | The price is a bit steep. Can you offer a discount? | Negotiation |
| 18 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation |
| 19 | User | Can you remove the gym access? | Negotiation |
| 20 | Bot | Sure, I can remove the gym access. The discounted price will be £135 for a single room and £225 for a family room. | Provide_negotiation |
| 21 | User | That sounds good. I'll take it. | Affirm |
| 22 | Bot | The hotel has been reserved. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation |
| 23 | User | My name is John Smith, my email is johnsmith@email.com, and my contact number is 0123456789. | Inform |
| 24 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye |
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The first is Rosa's Bed and Breakfast, a 4-star guesthouse with a 33% discount for the next 4 days. The second is The Bridge Guest House, a 3-star guesthouse with moderate pricing. The third is Aylesbray Lodge Guest House, a 4-star hotel with a 30% discount for the next 2 days. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
10 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you negotiate the price? | Negotiation
12 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
13 | User | Can you remove the gym and pool facilities? | Negotiation
14 | Bot | Sure, I can remove the gym and pool facilities. The new price for Rosa's Bed and Breakfast will be £95 per night. | Provide_negotiation
15 | User | That's still a bit over my budget. Can you suggest another option? | Ask_alternatives
16 | Bot | Sure, I have one more option for you. The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Multioption_suggestion
17 | User | What are the differences between the Lensfield Hotel and the Bridge Guest House? | Ask_differences
18 | Bot | The Lensfield Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The Bridge Guest House is a 3-star guesthouse with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. | Provide_differences
19 | User | Can you tell me more about the Lensfield Hotel? | Selection
20 | Bot | The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Selection
21 | User | Can you negotiate the price for the Lensfield Hotel? | Negotiation
22 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Which facilities would you like to remove? | Provide_negotiation
23 | User | Can you remove the parking facility? | Negotiation
24 | Bot | Sure, I can remove the parking facility. The new price for the Lensfield Hotel will be £81 per night. | Provide_negotiation
25 | User | That sounds good. I'll go with the Lensfield Hotel. | Selection
26 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation, Ask_details
27 | User | My name is John Smith, my email is johnsmith@gmail.com, and there will be two people staying in the room. We prefer a double room. | Inform
28 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation, Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with a pool, gym, and spacious rooms. The Alexander Bed and Breakfast is a 4-star guesthouse with a gym, pool, bar, and BBQ grill. | Provide_differences
7 | User | How much does each option cost? | Add_aspect_price
8 | Bot | The Gonville Hotel ranges from £79 for a single room to £119 for a family room. The University Arms Hotel ranges from £150 for a single room to £250 for a family room. The Alexander Bed and Breakfast ranges from £100 for a single room to £150 for a family room. | Provide_differences
9 | User | That's expensive. Do you have any cheaper options? | Ask_alternatives
10 | Bot | Sure, we also have Cityroomz and El Shaddai. Cityroomz has affordable prices for single, double, and family rooms, and El Shaddai offers rooms at affordable prices with doubles at £60, singles at £40, and family rooms at £62. | Multioption_suggestion
11 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
12 | Bot | Cityroomz has internet access and affordable prices, but no parking. El Shaddai has internet and parking facilities, but no features or recognitions. | Provide_differences
13 | User | I want to know more about the University Arms Hotel. | Selection
14 | Bot | The University Arms Hotel is a luxurious 4-star hotel with a pool, gym, and spacious rooms. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_details
15 | User | That's too expensive. Can you negotiate the price? | Negotiation
16 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Would you like me to negotiate? | Provide_negotiation
17 | User | Yes, please negotiate. | Affirm
18 | Bot | I can offer you a 5% discount on the original price, but the free dinner will be removed. Would you like to proceed with the booking? | Confirmation
19 | User | Can you suggest any other hotels with a pool? | Add_aspect_pool
20 | Bot | The University Arms Hotel is the only hotel with a pool. Would you like me to suggest other hotels with a gym or other facilities? | Ask_alternatives
21 | User | Yes, please suggest other hotels with a gym. | Add_aspect_gym
22 | Bot | The Gonville Hotel and Alexander Bed and Breakfast both have a gym. Would you like to know more about them? | Multioption_suggestion
23 | User | What are the differences between the Gonville Hotel and Alexander Bed and Breakfast? | Ask_differences
24 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The Alexander Bed and Breakfast is a 4-star guesthouse with a gym, pool, bar, and BBQ grill. | Provide_differences
25 | User | How much does each option cost? | Add_aspect_price
26 | Bot | The Gonville Hotel ranges from £79 for a single room to £119 for a family room. The Alexander Bed and Breakfast ranges from £100 for a single room to £150 for a family room. | Provide_differences
27 | User | I want to know more about the Alexander Bed and Breakfast. | Selection
28 | Bot | The Alexander Bed and Breakfast is a 4-star guesthouse with a gym, pool, bar, and BBQ grill. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_details
29 | User | That's too expensive. Can you negotiate the price? | Negotiation
30 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Would you like me to negotiate? | Provide_negotiation
31 | User | Yes, please negotiate. | Affirm
32 | Bot | I can offer you a 7% discount on the original price, but the bar and BBQ grill will be removed. Would you like to proceed with the booking? | Confirmation
33 | User | Let me think about it. | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_differences
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Add_aspect_X
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_differences
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_differences
13 | User | I'm interested in the Huntingdon Marriott Hotel, but it's a bit expensive. Can you offer a lower price? | Negotiation
14 | Bot | I can offer a 10% discount, but some facilities like the DJ floor and free dinner may not be available. Would you still like to book the Huntingdon Marriott Hotel? | Provide_negotiation
15 | User | Hmm, can you suggest any other options? | Ask_alternatives
16 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Multioption_suggestion
17 | User | Can you tell me more about Finches Bed and Breakfast? | Add_aspect_X
18 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_differences
19 | User | That sounds great, but what's the price? | Add_aspect_X
20 | Bot | The price for a double room is £120 per night, a single room is £90 per night, and a family room is £150 per night. | Add_aspect_X
21 | User | That's a bit expensive. Can you offer a lower price? | Negotiation
22 | Bot | I can offer a 10% discount, but some facilities like the BBQ grill and Jacuzzi may not be available. Would you still like to book Finches Bed and Breakfast? | Provide_negotiation
23 | User | Can you suggest any other options? | Ask_alternatives
24 | Bot | Sure, how about The Cambridge Belfry? It's a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Multioption_suggestion
25 | User | Can you tell me more about The Cambridge Belfry? | Add_aspect_X
26 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_differences
27 | User | What's the price for The Cambridge Belfry? | Add_aspect_X
28 | Bot | The price for a double room is £150 per night, a single room is £120 per night, and a family room is £200 per night. | Add_aspect_X
29 | User | That's a bit expensive. Can you offer a lower price? | Negotiation
30 | Bot | I can offer a 10% discount, but some facilities like the jacuzzi may not be available. Would you still like to book The Cambridge Belfry? | Provide_negotiation
31 | User | I'll think about it and get back to you. | Selection
32 | Bot | Sure, take your time. Let me know if you have any other questions. | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, and a pool. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Selection
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Provide_details
9 | User | Can you suggest a cheaper option? | Ask_alternatives
10 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Which one would you like to know more about? | Multioption_suggestion
11 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
12 | Bot | Cityroomz is a moderate hotel with internet access and affordable prices for single, double, and family rooms. It has no parking, no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
13 | User | Can you tell me more about the University Arms Hotel? | Selection
14 | Bot | The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, a pool, and spacious rooms. The hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_details
15 | User | Can you suggest a cheaper option? | Ask_alternatives
16 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Which one would you like to know more about? | Multioption_suggestion
17 | User | Can you tell me more about the Alexander Bed and Breakfast? | Selection
18 | Bot | The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_details
19 | User | Can you suggest a cheaper option? | Ask_alternatives
20 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Which one would you like to know more about? | Multioption_suggestion
21 | User | Can you tell me more about the Gonville Hotel? | Selection
22 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Provide_details
23 | User | Can you suggest a cheaper option? | Ask_alternatives
24 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Which one would you like to know more about? | Multioption_suggestion
25 | User | I'm interested in the University Arms Hotel, but it's quite expensive. Can you offer a discount? | Negotiation
26 | Bot | I'm sorry, but the prices are fixed. However, I can offer you a 10% discount on the Gonville Hotel if you're interested. | Provide_negotiation
27 | User | Can you remove the gym and safe from the Gonville Hotel to make it cheaper? | Negotiation
28 | Bot | I'm sorry, but the gym and safe are essential facilities that we cannot remove. However, I can offer you a 5% discount on the Gonville Hotel if you're interested. | Provide_negotiation
29 | User | Okay, I'll book the Gonville Hotel. | Affirm
30 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference for the final booking. | Confirmation
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, and a pool. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Add_aspect_X
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. It has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Add_aspect_X
9 | User | That sounds good. Can you tell me more about the University Arms Hotel? | Add_aspect_X
10 | Bot | The University Arms Hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Add_aspect_X
11 | User | That sounds great. Can you tell me more about the Alexander Bed and Breakfast? | Add_aspect_X
12 | Bot | The Alexander Bed and Breakfast is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Add_aspect_X
13 | User | I think I'll go with the University Arms Hotel. | Selection
14 | Bot | Great choice! The University Arms Hotel is a luxurious 4-star hotel located in the centre of Regent Street. It offers free breakfast, 24/7 room service, free wifi, a gym, a pool, and spacious rooms. The hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. The price for your stay will be £357. | Provide_negotiation
15 | User | That's a bit expensive. Can you lower the price? | Negotiation
16 | Bot | I can offer you a 10% discount, bringing the price down to £321.30. However, some facilities like the pool and gym may not be available. | Provide_negotiation
17 | User | Okay, I'll take it. | Affirm
18 | Bot | Great! The hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for the booking. | Confirmation
19 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 0123456789. | Inform
20 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, here are three options: Rosa's Bed and Breakfast, The Bridge Guest House, and Aylesbray Lodge Guest House. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between them? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse with luxurious rooms, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | How much does each option cost? | Add_aspect_price
10 | Bot | Rosa's Bed and Breakfast is currently offering a 33% discount, with double rooms priced at £100, family rooms at £150, and single rooms at £75. The Bridge Guest House has double rooms at £75, family rooms at £90, and single rooms at £50. Aylesbray Lodge Guest House is currently offering a 30% discount, with double rooms priced at £105, family rooms at £135, and single rooms at £80. | Provide_differences
11 | User | Can you suggest more options? | Ask_alternatives
12 | Bot | Sure, how about The Lensfield Hotel? It's a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. | Multioption_suggestion
13 | User | How much does it cost? | Add_aspect_price
14 | Bot | The Lensfield Hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. | Provide_differences
15 | User | I'm interested in Rosa's Bed and Breakfast. Can you negotiate the price? | Negotiation
16 | Bot | I can negotiate up to 10% of the suggested price, but some facilities might get removed. | Provide_negotiation
17 | User | Can you remove the gym and pool facilities? | Add_aspect_facilities
18 | Bot | Sure, I can remove those facilities. The new price for a single room will be £67.50. | Provide_negotiation
19 | User | That's still a bit high. Can you lower it to £60? | Negotiation
20 | Bot | I'm sorry, but I can only go as low as £65. | Provide_negotiation
21 | User | Alright, I'll take it. | Selection
22 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for the booking. | Confirmation, Ask_details
23 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
24 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation
25 | User | Can you suggest some good restaurants in the area? | Add_aspect_restaurants
26 | Bot | Sure, how about The Cambridge Chop House, The Oak Bistro, and The Pint Shop? | Multioption_suggestion
27 | User | What are the differences between them? | Ask_differences
28 | Bot | The Cambridge Chop House is a traditional British restaurant with a cozy atmosphere and great food. The Oak Bistro is a French restaurant with a romantic ambiance and delicious cuisine. The Pint Shop is a gastropub with a wide selection of beers and tasty bar food. | Provide_differences
29 | User | How much do they cost? | Add_aspect_price
30 | Bot | The Cambridge Chop House has main courses priced at around £20, The Oak Bistro has main courses priced at around £30, and The Pint Shop has bar food priced at around £10. | Provide_differences
31 | User | I think I'll go with The Cambridge Chop House. Can you make a reservation for me? | Selection
32 | Bot | I'm sorry, but I'm not able to make restaurant reservations. However, I can provide you with their contact information. | Inform
33 | User | That's alright, please give me their contact information. | Inform
34 | Bot | The Cambridge Chop House's phone number is 01223 359506 and their email is info@cambridgechophouse.co.uk. Enjoy your stay in Cambridge! | Inform
35 | User | Thank you for your help. Goodbye! | Goodbye
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have 3 options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive but has luxurious rooms, a gym, and a pool. The A and B Guest House has a BBQ grill and Jacuzzi. Allenbell guesthouse is affordable and has a bar. | Provide_differences |
| 9 | User | Can you suggest more options? | Ask_alternatives |
| 10 | Bot | Sure, I have two more options for you. The first is Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. The second is Autumn House, a 4-star guesthouse with a 37% discount on bookings for the next 2 days and free dinner. | Multioption_suggestion |
| 11 | User | What are the differences between Carolina Bed and Breakfast and Autumn House? | Ask_differences |
| 12 | Bot | Carolina Bed and Breakfast has a pool, BBQ grill, and Jacuzzi. Autumn House has a DJ floor and fully safe, sanitary, and secure rooms. | Provide_differences |
| 13 | User | I'm interested in Leverton House, but it's over my budget. Can you offer a lower price? | Negotiation |
| 14 | Bot | I can offer a 10% discount, but some facilities like the gym and pool might not be available. | Provide_negotiation |
| 15 | User | Okay, I'll take the offer. | Affirm, Selection |
| 16 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details |
| 17 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform |
| 18 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye |
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have 3 options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive but has luxurious rooms, a gym, and a pool. The A and B Guest House has a BBQ grill and Jacuzzi. Allenbell guesthouse is affordable and has a bar. | Provide_differences |
| 9 | User | Can you suggest more options? | Ask_alternatives |
| 10 | Bot | Sure, I have two more options for you. The first is Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. The second is Autumn House, a 4-star guesthouse with a 37% discount on bookings for the next 2 days and free dinner. | Multioption_suggestion |
| 11 | User | What are the differences between Carolina Bed and Breakfast and Autumn House? | Ask_differences |
| 12 | Bot | Carolina Bed and Breakfast has a pool, BBQ grill, and Jacuzzi. Autumn House has a DJ floor and free dinner. Both have received recognitions and have hosted celebrities. | Provide_differences |
| 13 | User | I'm interested in Leverton House, but it's over my budget. Can you offer a lower price? | Negotiation |
| 14 | Bot | I can offer a 10% discount, but some facilities like the gym and pool might not be available. | Provide_negotiation |
| 15 | User | Okay, I'll take the offer. | Affirm, Selection |
| 16 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details |
| 17 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform |
| 18 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye |
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have three options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive option, but it offers a gym and a pool. The A and B Guest House has a BBQ grill and a Jacuzzi. Allenbell guesthouse has a bar and spacious luxurious rooms. | Provide_differences |
| 9 | User | Can you give me more options? | Ask_alternatives |
| 10 | Bot | Sure, I have two more options for you. The first is Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. The second is Autumn House, a 4-star guesthouse with a 37% discount on bookings for the next 2 days and free dinner. | Multioption_suggestion |
| 11 | User | What are the differences between Carolina Bed and Breakfast and Autumn House? | Ask_differences |
| 12 | Bot | Carolina Bed and Breakfast has a pool, bar, BBQ grill, and Jacuzzi. Autumn House has a DJ floor and fully safe, sanitary, and secure rooms. | Provide_differences |
| 13 | User | I'm interested in Leverton House, but it's a bit over my budget. Can you offer a lower price? | Negotiation |
| 14 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation |
| 15 | User | Can you remove the gym and pool facilities? | Negotiation |
| 16 | Bot | Sure, I can remove those facilities and offer you a 10% discount. The new price will be £135 per night. | Provide_negotiation |
| 17 | User | That sounds good. I'll take Leverton House. | Selection |
| 18 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation |
| 19 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform |
| 20 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye |
| 21 | User | No, that's all. Thank you. | Goodbye |
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, and a pool. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Selection
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Provide_details
9 | User | Can you suggest a cheaper option? | Ask_alternatives
10 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Cityroomz has no parking, but offers affordable prices for single, double, and family rooms. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices. | Multioption_suggestion
11 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
12 | Bot | Cityroomz has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse with a 0-star rating and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. | Provide_differences
13 | User | Can you tell me more about the University Arms Hotel? | Selection
14 | Bot | The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, a pool, and spacious rooms. The hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_details
15 | User | Can you suggest another option? | Ask_alternatives
16 | Bot | Sure, I have The Gonville Hotel, Alexander Bed and Breakfast, and El Shaddai. Which one would you like to know more about? | Multioption_suggestion
17 | User | Can you tell me more about the Alexander Bed and Breakfast? | Selection
18 | Bot | The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_details
19 | User | Can you suggest a cheaper option? | Ask_alternatives
20 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Cityroomz has no parking, but offers affordable prices for single, double, and family rooms. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices. | Multioption_suggestion
21 | User | I'm interested in the University Arms Hotel, but it's a bit expensive. Can you offer a discount? | Negotiation
22 | Bot | I'm sorry, but the prices are fixed. However, I can offer you a 10% discount on the University Arms Hotel, but some of the facilities provided might get removed. | Provide_negotiation
23 | User | Can you remove the gym and pool facilities? | Negotiation
24 | Bot | Sure, I can remove the gym and pool facilities. The new price for the University Arms Hotel will be £270 for a single room and £360 for a family room. | Provide_negotiation
25 | User | That's still a bit expensive. Can you offer a better price? | Negotiation
26 | Bot | I'm sorry, but the prices are already discounted. However, I can offer you a free dinner and a 5% discount on the University Arms Hotel. | Provide_negotiation
27 | User | Okay, I'll take the University Arms Hotel. | Selection
28 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for the booking. | Confirmation
29 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 0123456789. | Inform
30 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, a pool, and spacious rooms. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Add_aspect_X
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Add_aspect_X
9 | User | That sounds good, but can you tell me more about the University Arms Hotel? | Add_aspect_X
10 | Bot | The University Arms Hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Add_aspect_X
11 | User | That sounds great, but it's a bit expensive. Can you suggest a cheaper option? | Ask_alternatives
12 | Bot | Sure, Cityroomz and El Shaddai are two more options. Cityroomz is a moderate hotel with affordable prices for single, double, and family rooms. El Shaddai is a cheap guesthouse with rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. | Multioption_suggestion
13 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
14 | Bot | Cityroomz has internet access and takes bookings, but it has no parking. El Shaddai offers internet and parking facilities, and takes bookings. The hotel has a 0-star rating and offers rooms at affordable prices. The hotel also offers a free dinner. | Provide_differences
15 | User | Can you tell me more about El Shaddai? | Add_aspect_X
16 | Bot | El Shaddai is a cheap guesthouse located in the centre of Cambridge. It offers internet and parking facilities, and takes bookings. The hotel has a 0-star rating and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. Contact the hotel at 01223327978 or visit 41 Warkworth Street, CB11EG. | Add_aspect_X
17 | User | I think I'll go with the University Arms Hotel. Can you give me a better price? | Negotiation
18 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
19 | User | Can you remove the gym and pool facilities? | Negotiation
20 | Bot | Sure, I can remove those facilities. The new price will be £107.10 per night. | Provide_negotiation
21 | User | That sounds good. I'll take it. | Selection
22 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation
23 | User | My name is John Smith, my email is johnsmith@gmail.com, there will be two people, and we prefer a double room. | Inform
24 | Bot | Thank you, John. Your booking has been confirmed. You will receive an email with the details. Is there anything else I can help you with? | Confirmation
25 | User | Actually, can you tell me more about the Alexander Bed and Breakfast? | Add_aspect_X
26 | Bot | The Alexander Bed and Breakfast is a 4-star guesthouse located in the centre of Cambridge. It offers free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Add_aspect_X
27 | User | That sounds great. Can you give me a better price? | Negotiation
28 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
29 | User | Can you remove the gym and pool facilities? | Negotiation
30 | Bot | I'm sorry, but the gym and pool facilities are a major part of the hotel's appeal. I cannot remove them. | Provide_negotiation
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_differences
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Add_aspect_X
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_differences
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_differences
13 | User | I'm interested in the Huntingdon Marriott Hotel, but it's a bit expensive. Can you offer a lower price? | Negotiation
14 | Bot | I can offer a 10% discount, but some facilities like the DJ floor and free dinner may not be available. Would you still like to book the Huntingdon Marriott Hotel? | Provide_negotiation
15 | User | Hmm, can you suggest any other options? | Ask_alternatives
16 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Multioption_suggestion
17 | User | Can you tell me more about Finches Bed and Breakfast? | Add_aspect_X
18 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_differences
19 | User | That sounds great, but what's the price? | Add_aspect_X
20 | Bot | Finches Bed and Breakfast offers double rooms for £120, single rooms for £90, and family rooms for £150. | Provide_differences
21 | User | Can you offer a lower price for Finches Bed and Breakfast? | Negotiation
22 | Bot | I can offer a 5% discount, but some facilities like the BBQ grill and Jacuzzi may not be available. Would you like to book Finches Bed and Breakfast? | Provide_negotiation
23 | User | Let me think about it for a bit. | Selection
24 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
25 | User | Can you tell me more about the gym at the Cambridge Belfry? | Add_aspect_X
26 | Bot | The gym at the Cambridge Belfry is fully equipped with modern machines and equipment. It's open 24/7 and is free for all guests. | Provide_differences
27 | User | What about the pool at the Huntingdon Marriott Hotel? | Add_aspect_X
28 | Bot | The pool at the Huntingdon Marriott Hotel is a heated indoor pool with a sauna and steam room. It's open from 6 am to 10 pm and is free for all guests. | Provide_differences
29 | User | Can you tell me more about the free breakfast at Hobsons House? | Add_aspect_X
30 | Bot | The free breakfast at Hobsons House includes a variety of options such as eggs, bacon, toast, cereal, and fruit. It's served from 7 am to 10 am and is free for all guests. | Provide_differences
31 | User | I think I've made a decision. I'd like to book the Huntingdon Marriott Hotel. | Selection
32 | Bot | Great choice! The hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and phone number for the booking. | Confirmation, Ask_details
33 | User | My name is John Smith, my email is johnsmith@email.com, and my phone number is 123-456-7890. | Inform
34 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation
35 | User | No, that's all. Thank you for your help. | Goodbye
36 | Bot | You're welcome, John. Have a great day! | Goodbye
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, based on your criteria, I have three options: Kirkwood House, Home from Home, and Lovell Lodge. | Multioption_suggestion
7 | User | Can you tell me the differences between the options? | Ask_differences
8 | Bot | Kirkwood House is a 4-star guesthouse with a gym, pool, bar, and Jacuzzi. Home from Home is also a 4-star guesthouse with a gym, pool, and bar. Lovell Lodge is a 2-star hotel with free breakfast and wifi. | Provide_differences
9 | User | What's the price range for each option? | Add_aspect_X
10 | Bot | Kirkwood House is currently offering a 36% discount, with prices starting at £90 per night. Home from Home has double rooms at £75, family rooms at £105, and single rooms at £50. Lovell Lodge has double rooms at £65, family rooms at £70, and single rooms at £50. | Add_aspect_X
11 | User | Can you suggest more options? | Ask_alternatives
12 | Bot | Sure, based on your criteria, I have two more options: The Limehouse guesthouse and Acorn Guest House. | Multioption_suggestion
13 | User | What are the differences between these options? | Ask_differences
14 | Bot | The Limehouse guesthouse is a 4-star hotel with a gym, pool, and DJ floor. Acorn Guest House is also a 4-star guesthouse with a gym and pool. | Provide_differences
15 | User | What's the price range for these options? | Add_aspect_X
16 | Bot | The Limehouse guesthouse has prices starting at £120 per night. Acorn Guest House has prices starting at £95 per night. | Add_aspect_X
17 | User | Can you tell me more about Kirkwood House? | Ask_details
18 | Bot | Kirkwood House is a 4-star guesthouse located in North Cambridge. It offers free breakfast, 24/7 room service, free wifi, a gym, pool, bar, BBQ grill, and Jacuzzi. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as the Michelin Star. The hotel has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. | Ask_details
19 | User | That sounds great, but it's a bit out of my budget. Can you negotiate the price? | Negotiation
20 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
21 | User | Can you remove the BBQ grill and Jacuzzi? | Negotiation
22 | Bot | Sure, I can remove those facilities. The new price will be £81 per night. | Provide_negotiation
23 | User | That's still a bit high. Can you suggest a cheaper option? | Ask_alternatives
24 | Bot | Sure, based on your criteria, I have two more options: Home from Home and Lovell Lodge. | Multioption_suggestion
25 | User | Can you tell me more about Lovell Lodge? | Ask_details
26 | Bot | Lovell Lodge is a 2-star hotel located in North Cambridge. It offers free breakfast, free wifi, and good room service. The hotel has parking and internet facilities and takes bookings. The price range is moderate, with double rooms costing £65, family rooms £70, and single rooms £50. Lovell Lodge has been endorsed by local tour agencies TourMe and has received local awards such as Food fest. Currently, there are only 4 rooms left, and guests can enjoy a free dinner. The hotel has a public image rating of 6/10. | Ask_details
27 | User | That sounds good. Can I book Lovell Lodge? | Selection
28 | Bot | Sure, the hotel has been reserved for you. Your registration number is 12345. Please provide your name, email, and contact number for confirmation. | Confirmation
29 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
30 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_details
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Ask_alternatives
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_details
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_details
13 | User | Can you tell me more about the Huntingdon Marriott Hotel's food festival? | Add_aspect_X
14 | Bot | The Huntingdon Marriott Hotel is currently running a food festival with free dinner for guests. | Provide_details
15 | User | I'm interested in the Cambridge Belfry, but it's a bit expensive. Can you offer a lower price? | Negotiation
16 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
17 | User | Can you remove the jacuzzi? | Negotiation
18 | Bot | Sure, I can remove the jacuzzi. The new price will be £135 per night. | Provide_negotiation
19 | User | That's still a bit high. Can you offer a lower price? | Negotiation
20 | Bot | I'm sorry, but that's the best I can do. | Deny
21 | User | Okay, I'll take the Cambridge Belfry. | Selection
22 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation
23 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Ask_details
24 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Goodbye
25 | User | Actually, can you tell me more about the Finches Bed and Breakfast? | Ask_alternatives
26 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_details
27 | User | That sounds great. Can you tell me more about the price? | Add_aspect_X
28 | Bot | Finches Bed and Breakfast offers double rooms for £120, single rooms for £90, and family rooms for £150. | Provide_details
29 | User | Can you offer a discount? | Negotiation
30 | Bot | I'm sorry, but there are no discounts available at the moment. | Deny
31 | User | Okay, I'll stick with the Cambridge Belfry. | Selection
32 | Bot | Great, your booking is confirmed. Is there anything else I can help you with? | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, The University Arms Hotel, and The Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, 24/7 room service, free wifi, a gym, a pool, and spacious rooms. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Add_aspect_X
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Add_aspect_X
9 | User | What about the University Arms Hotel? | Add_aspect_X
10 | Bot | The University Arms Hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Add_aspect_X
11 | User | And the Alexander Bed and Breakfast? | Add_aspect_X
12 | Bot | The Alexander Bed and Breakfast has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Add_aspect_X
13 | User | Can you suggest more options? | Ask_alternatives
14 | Bot | Sure, I have two more options for you. Cityroomz and El Shaddai. Cityroomz is a moderate hotel located in the centre of Cambridge, with internet access and takes bookings. Although it has no parking, it offers affordable prices for single, double, and family rooms. The hotel has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse located in the centre of Cambridge. It offers internet and parking facilities, and takes bookings. The hotel has a 0-star rating and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Multioption_suggestion
15 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
16 | Bot | Cityroomz is a moderate hotel with internet access and affordable prices for single, double, and family rooms. It has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
17 | User | I'm interested in the University Arms Hotel, but it's a bit expensive. Can you suggest something cheaper? | Negotiation
18 | Bot | I understand your concern. How much is your estimated budget? | Add_aspect_X
19 | User | My budget is around £80 per night. | Add_aspect_X
20 | Bot | I see. How about the Gonville Hotel? It's currently offering 38% off on bookings for the next 4 days and free dinner. | Provide_negotiation
21 | User | Can you remove the gym and safe to make it cheaper? | Negotiation
22 | Bot | I'm sorry, but the gym and safe are part of the hotel's standard amenities. However, I can offer you a 10% discount on the original price. | Provide_negotiation
23 | User | Okay, I'll take it. | Selection
24 | Bot | Great! The hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation
25 | User | My name is John Smith, my email is johnsmith@gmail.com, there will be two people, and we prefer a double room. | Inform
26 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Goodbye
27 | User | Actually, can you suggest some good restaurants near the hotel? | Add_aspect_X
28 | Bot | Sure, there are many great restaurants near the University Arms Hotel. Some popular options are Midsummer House, Parker's Tavern, and The Ivy Cambridge Brasserie. | Add_aspect_X
29 | User | Can you make a reservation for Midsummer House for me? | Lookup
30 | Bot | I'm sorry, but I'm not able to make restaurant reservations. However, I can provide you with their contact information and you can make a reservation yourself. | Add_aspect_X
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, and a pool. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Selection
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Provide_details
9 | User | Can you suggest a cheaper option? | Ask_alternatives
10 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Cityroomz has no parking, but offers affordable prices for single, double, and family rooms. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices. | Multioption_suggestion
11 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
12 | Bot | Cityroomz has internet access and takes bookings, but has no parking. El Shaddai offers internet and parking facilities, and takes bookings. El Shaddai is cheaper, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
13 | User | Can you tell me more about the University Arms Hotel? | Selection
14 | Bot | The University Arms Hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_details
15 | User | Can you negotiate the price of the University Arms Hotel? | Negotiation
16 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, and a pool. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_negotiation
17 | User | Can you suggest more options? | Ask_alternatives
18 | Bot | Sure, I have The Gonville Hotel, University Arms Hotel, Alexander Bed and Breakfast, Cityroomz, and El Shaddai. Which one would you like to know more about? | Multioption_suggestion
19 | User | Can you tell me more about the Alexander Bed and Breakfast? | Selection
20 | Bot | The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_details
21 | User | Can you negotiate the price of the Alexander Bed and Breakfast? | Negotiation
22 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_negotiation
23 | User | Can you suggest more options? | Ask_alternatives
24 | Bot | Sure, I have The Gonville Hotel, University Arms Hotel, Alexander Bed and Breakfast, Cityroomz, and El Shaddai. Which one would you like to know more about? | Multioption_suggestion
25 | User | Can you tell me more about El Shaddai? | Selection
26 | Bot | El Shaddai is a cheap guesthouse located in the centre of Cambridge. It offers internet and parking facilities, and takes bookings. The hotel has a 0-star rating and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. Contact the hotel at 01223327978 or visit 41 Warkworth Street, CB11EG. | Provide_details
27 | User | Can you suggest more options? | Ask_alternatives
28 | Bot | I'm sorry, those are all the options I have available for your criteria. Which one would you like to book? | Selection
29 | User | I need some time to decide. | Affirm
30 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a moderate price range and a 31% discount for the next 2 days. The third is Lovell Lodge, a 2-star hotel with a moderate price range and only 4 rooms left. Which one would you like to know more about? | Multioption_suggestion
7 | User | What's the difference between Kirkwood House and Home from Home? | Ask_differences
8 | Bot | Kirkwood House is more luxurious and has a higher rating on social media. Home from Home has a moderate price range and is offering free dinner. | Provide_differences
9 | User | What about Lovell Lodge? | Ask_alternatives
10 | Bot | Lovell Lodge is a 2-star hotel with a moderate price range and only 4 rooms left. It has been endorsed by local tour agencies and has received local awards. | Multioption_suggestion
11 | User | How much does each option cost? | Add_aspect_X
12 | Bot | Kirkwood House costs £120 per night, Home from Home costs £75 for double rooms, £105 for family rooms, and £50 for single rooms, and Lovell Lodge costs £65 for double rooms, £70 for family rooms, and £50 for single rooms. | Add_aspect_X
13 | User | Can you tell me more about Kirkwood House? | Selection
14 | Bot | Kirkwood House is a 4-star guesthouse located in North Cambridge. It offers free breakfast, 24/7 room service, free wifi, a gym, pool, bar, BBQ grill, and Jacuzzi. It has spacious and luxurious rooms and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies and has received prestigious awards such as the Michelin Star. The hotel has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. | Selection
15 | User | That sounds great, but it's a bit out of my budget. Can you offer a lower price? | Negotiation
16 | Bot | I'm sorry, but the price is already discounted by 36%. However, I can offer a 10% discount on the other options if you'd like. | Provide_negotiation
17 | User | Can you remove the gym and pool from Home from Home to lower the price? | Negotiation
18 | Bot | I can remove the gym and pool, but the price will only be reduced by 5%. Is that okay? | Provide_negotiation
19 | User | Hmm, let me think about it. Can you suggest any other options? | Ask_alternatives
20 | Bot | Sure, I have two more options for you. The first is Limehouse guesthouse, a 4-star hotel with a food festival and a rating of 8/10. The second is Acorn Guest House, a 4-star guesthouse with a free dinner offer and a rating of 8/10. Which one would you like to know more about? | Multioption_suggestion
21 | User | What's the difference between Limehouse guesthouse and Acorn Guest House? | Ask_differences
22 | Bot | Limehouse guesthouse has a DJ floor and has hosted more celebrities, while Acorn Guest House has a head chef with a cookbook and has hosted fewer celebrities. | Provide_differences
23 | User | How much does each option cost? | Add_aspect_X
24 | Bot | Limehouse guesthouse costs £150 per night, and Acorn Guest House costs £120 per night. | Add_aspect_X
25 | User | Can you tell me more about Acorn Guest House? | Selection
26 | Bot | Acorn Guest House is a 4-star guesthouse located in North Cambridge. It offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel has a gym and pool. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Ronaldo and Eminem. The head chef has a cookbook named "How to Burger." | Selection
27 | User | That sounds good, but can you offer a lower price? | Negotiation
28 | Bot | I can offer a 10% discount, but some facilities like the gym and pool might have to be removed. Would you like to proceed with the booking? | Provide_negotiation
29 | User | Okay, I'll take it. | Affirm
30 | Bot | Great, the hotel has been reserved for you. Your registration number is 12345. Please provide your name, email, and contact number for the booking. | Confirmation, Ask_details
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, and a pool. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Selection
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Provide_details
9 | User | Can you suggest a cheaper option? | Ask_alternatives
10 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Which one would you like to know more about? | Multioption_suggestion
11 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
12 | Bot | Cityroomz is a moderate hotel with internet access and affordable prices for single, double, and family rooms. The hotel has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
13 | User | Can you tell me more about the University Arms Hotel? | Selection
14 | Bot | The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, a pool, and spacious rooms. The hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_details
15 | User | Can you suggest a cheaper option? | Ask_alternatives
16 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Which one would you like to know more about? | Multioption_suggestion
17 | User | Can you negotiate the price of the University Arms Hotel? | Negotiation
18 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, a pool, and spacious rooms. The hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_negotiation
19 | User | Can you suggest another option? | Ask_alternatives
20 | Bot | Sure, how about The Gonville Hotel, Alexander Bed and Breakfast, Cityroomz, or El Shaddai? | Multioption_suggestion
21 | User | Can you tell me more about the Alexander Bed and Breakfast? | Selection
22 | Bot | The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_details
23 | User | Can you suggest a cheaper option? | Ask_alternatives
24 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Which one would you like to know more about? | Multioption_suggestion
25 | User | Can you tell me more about El Shaddai? | Selection
26 | Bot | El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_details
27 | User | Can you negotiate the price of the Alexander Bed and Breakfast? | Negotiation
28 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_negotiation
29 | User | Can you suggest another option? | Ask_alternatives
30 | Bot | Sure, how about The Gonville Hotel, University Arms Hotel, Cityroomz, or El Shaddai? | Multioption_suggestion
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Add_aspect_X
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Ask_alternatives
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Add_aspect_X
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Add_aspect_X
13 | User | Can you tell me more about the food at the Cambridge Belfry? | Add_aspect_X
14 | Bot | The Cambridge Belfry offers great food with a head chef who has a cookbook named "How to Burger". The hotel has received prestigious awards such as Cateys and has been endorsed by popular tour agencies like Expedia. | Add_aspect_X
15 | User | I'm interested in the Huntingdon Marriott Hotel, but it's a bit expensive. Can you offer a lower price? | Negotiation
16 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
17 | User | Can you remove the DJ floor? | Negotiation
18 | Bot | Sure, I can remove the DJ floor. The new price will be £270. | Provide_negotiation
19 | User | That's still a bit high. Can you offer a lower price? | Negotiation
20 | Bot | I'm sorry, but that's the best I can do. | Provide_negotiation
21 | User | Okay, I'll go with the Cambridge Belfry. | Selection
22 | Bot | Great choice! The hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details
23 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
24 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Confirmation
25 | User | Can you tell me more about the gym at the Cambridge Belfry? | Add_aspect_X
26 | Bot | The gym at the Cambridge Belfry is spacious and well-equipped with modern machines. It's open 24/7 and free for guests. | Add_aspect_X
27 | User | Can I add a request for a room with a view? | Add_aspect_X
28 | Bot | Sure, I'll add that to your booking. Is there anything else I can help you with? | Add_aspect_X
29 | User | No, that's all. Thank you. | Goodbye
30 | Bot | You're welcome. Have a great day! | Goodbye
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a 31% discount for the next 2 days and free dinner. The third is Lovell Lodge, a 2-star hotel with a moderate price range. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Kirkwood House is a luxurious guesthouse with a gym, pool, bar, BBQ grill, and Jacuzzi. Home from Home is also a luxurious guesthouse with a gym, pool, and bar. Lovell Lodge is a 2-star hotel with free breakfast and wifi. | Provide_differences
9 | User | Can you tell me more about Kirkwood House? | Selection
10 | Bot | Kirkwood House is a 4-star guesthouse located in North Cambridge. It offers free breakfast, 24/7 room service, free wifi, a gym, pool, bar, BBQ grill, and Jacuzzi. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as the Michelin Star. The hotel has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you negotiate the price? | Negotiation
12 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
13 | User | Can you remove the BBQ grill and Jacuzzi? | Negotiation
14 | Bot | Sure, I can remove those facilities. The new price for Kirkwood House is £110 per night. | Provide_negotiation
15 | User | That's still a bit over my budget. Can you suggest another option? | Ask_alternatives
16 | Bot | Sure, I have two more options for you. The first is The Limehouse guesthouse, a 4-star hotel with a food festival and a rating of 8/10. The second is Archway House, a 4-star guesthouse with a food festival and 37% off on bookings for the next 4 days. Which one would you like to know more about? | Multioption_suggestion
17 | User | Can you tell me more about The Limehouse guesthouse? | Selection
18 | Bot | The Limehouse guesthouse is a 4-star hotel located in the north area of Cambridge. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, a pool, and a DJ floor. It has received prestigious awards such as Michelin Star and The Gold List and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. | Selection
19 | User | That sounds great. Can you book it for me? | Selection
20 | Bot | Sure, The Limehouse guesthouse has been reserved for you. Your registration number is LH1234. Please provide your name, email, no. of people, and room preference. | Confirmation, Ask_details
21 | User | My name is John Smith, my email is johnsmith@gmail.com, and I'll be staying with my wife. We prefer a double room. | Inform
22 | Bot | Great, your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation, Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_differences
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Add_aspect_X
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_differences
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_differences
13 | User | I'm interested in the Huntingdon Marriott Hotel, but it's a bit expensive. Can you offer a lower price? | Negotiation
14 | Bot | I can offer a 10% discount, but some facilities like the DJ floor and free dinner may not be available. Would you still like to book the Huntingdon Marriott Hotel? | Provide_negotiation
15 | User | Hmm, can you suggest any other options? | Ask_alternatives
16 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Multioption_suggestion
17 | User | Can you tell me more about Finches Bed and Breakfast? | Add_aspect_X
18 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_differences
19 | User | That sounds great, but what's the price? | Add_aspect_X
20 | Bot | The price for a double room is £120 per night, a single room is £90 per night, and a family room is £150 per night. | Add_aspect_X
21 | User | That's a bit expensive. Can you offer a lower price? | Negotiation
22 | Bot | I can offer a 10% discount, but some facilities like the BBQ grill and Jacuzzi may not be available. Would you like to book Finches Bed and Breakfast? | Provide_negotiation
23 | User | Let me think about it for a bit. | Selection
24 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
25 | User | Can you tell me more about the Cambridge Belfry's gym and pool? | Add_aspect_X
26 | Bot | The gym and pool at the Cambridge Belfry are both spacious and well-maintained. The gym has a variety of equipment, including treadmills, ellipticals, and weights. The pool is large and has a hot tub and sauna. | Add_aspect_X
27 | User | That sounds great. Can you tell me more about the breakfast? | Add_aspect_X
28 | Bot | The breakfast at the Cambridge Belfry is complimentary and includes a variety of options, including hot and cold items, pastries, and fresh fruit. | Add_aspect_X
29 | User | Can you tell me more about the Huntingdon Marriott Hotel's Michelin Star? | Add_aspect_X
30 | Bot | The Michelin Star is a prestigious award given to restaurants that offer exceptional cuisine. The Huntingdon Marriott Hotel's restaurant has been recognized with this award for its innovative and delicious dishes. | Add_aspect_X
31 | User | Can you tell me more about the Hobsons House's discount? | Add_aspect_X
32 | Bot | The discount at Hobsons House is 32% off the regular price for bookings made in the next 3 days. It also includes a free dinner. | Add_aspect_X
33 | User | I think I'll go with the Cambridge Belfry. Can you book it for me? | Selection
34 | Bot | Sure, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and phone number for the booking. | Confirmation, Ask_details
35 | User | My name is John Smith, my email is johnsmith@email.com, and my phone number is 123-456-7890. | Inform
36 | Bot | Great, your booking is confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation, Goodbye
37 | User | No, that's all. Thank you. | Goodbye, Affirm
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_details
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Ask_alternatives
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_details
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_details
13 | User | Can you tell me more about the Huntingdon Marriott Hotel's food festival? | Add_aspect_X
14 | Bot | The Huntingdon Marriott Hotel is currently running a food festival with free dinner for guests. | Provide_details
15 | User | I'm interested in the Cambridge Belfry, but it's a bit expensive. Can you offer a lower price? | Negotiation
16 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
17 | User | Can you remove the jacuzzi? | Negotiation
18 | Bot | Sure, I can remove the jacuzzi. The new price will be £135 per night. | Provide_negotiation
19 | User | That's still a bit high. Can you offer a lower price? | Negotiation
20 | Bot | I'm sorry, but that's the best I can do. | Deny
21 | User | Okay, I'll take the Cambridge Belfry. | Selection
22 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation
23 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Ask_details
24 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Goodbye
25 | User | Actually, can you tell me more about the Finches Bed and Breakfast? | Ask_alternatives
26 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_details
27 | User | That sounds great. Can you tell me more about the price? | Add_aspect_X
28 | Bot | The hotel offers double rooms for £150, single rooms for £120, and family rooms for £200. | Provide_details
29 | User | That's a bit expensive. Can you offer a lower price? | Negotiation
30 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | Can you tell me the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with free breakfast, 24/7 room service, and a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is also a 4-star hotel with free wifi, parking, gym, pool, bar, and DJ floor. Hobsons House is a 3-star guesthouse with free wifi, parking, and gym. | Provide_differences
7 | User | What about the prices? | Add_aspect_price
8 | Bot | The Cambridge Belfry is £150 per night, Huntingdon Marriott Hotel is £200 per night, and Hobsons House is £75 for a double room. | Provide_differences
9 | User | Can you suggest more options? | Ask_alternatives
10 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse with free breakfast, 24/7 room service, and a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. | Multioption_suggestion
11 | User | What's the price for Finches Bed and Breakfast? | Ask_details
12 | Bot | It's £180 per night for a double room. | Provide_differences
13 | User | Can you tell me more about The Cambridge Belfry? | Selection
14 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_differences
15 | User | Can you lower the price for The Cambridge Belfry? | Negotiation
16 | Bot | I can offer a 10% discount, but some facilities like the jacuzzi and room service may not be available. | Provide_negotiation
17 | User | Okay, I'll take it. | Affirm
18 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details
19 | User | My name is John Smith, email is johnsmith@gmail.com, and contact number is 1234567890. | Inform
20 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Confirmation
21 | User | Can you tell me more about Huntingdon Marriott Hotel? | Selection
22 | Bot | Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_differences
23 | User | Can you lower the price for Huntingdon Marriott Hotel? | Negotiation
24 | Bot | I can offer a 10% discount, but some facilities like the DJ floor and free dinner may not be available. | Provide_negotiation
25 | User | Can you make it 20%? | Negotiation
26 | Bot | I'm sorry, but 10% is the maximum discount I can offer. | Provide_negotiation
27 | User | Okay, I'll take it. | Affirm
28 | Bot | Great, the hotel has been reserved for you. Your registration number is 789012. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details
29 | User | My name is John Smith, email is johnsmith@gmail.com, and contact number is 1234567890. | Inform
30 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Confirmation
31 | User | Can you suggest more options? | Ask_alternatives
32 | Bot | Sure, what criteria would you like me to consider? | Add_aspect_X
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a moderate price range and a 31% discount for the next 2 days. The third is Lovell Lodge, a 2-star hotel with a moderate price range and only 4 rooms left. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Kirkwood House is a 4-star guesthouse with a gym, pool, bar, BBQ grill, and Jacuzzi. Home from Home is also a 4-star guesthouse with a gym, pool, and bar. Lovell Lodge is a 2-star hotel with free breakfast and wifi. | Provide_differences
9 | User | Can you tell me more about Kirkwood House? | Selection
10 | Bot | Kirkwood House is a luxurious guesthouse with spacious rooms and has been recognized by famous magazines and tour agencies. It has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. It is currently offering a 36% discount on bookings for the next 3 days. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you offer a better price? | Negotiation
12 | Bot | I can offer a 10% discount, but some facilities like the BBQ grill and Jacuzzi might not be available. Would you like to proceed with the booking? | Provide_negotiation
13 | User | Hmm, can you tell me more about Home from Home? | Ask_alternatives
14 | Bot | Home from Home is a 4-star guesthouse with a moderate price range. It offers free breakfast, 24/7 room service, free wifi, a gym, pool, and bar. It has been recognized by popular magazines and tour agencies and has hosted celebrities such as Ronaldo, Virat Kholi, and Tom Holland. It is currently offering a 31% discount on bookings for the next 2 days and free dinner. | Ask_alternatives
15 | User | What about Lovell Lodge? | Ask_alternatives
16 | Bot | Lovell Lodge is a 2-star hotel with free breakfast and wifi. It has parking and internet facilities and takes bookings. The price range is moderate, with double rooms costing £65, family rooms £70, and single rooms £50. Lovell Lodge has been endorsed by local tour agencies TourMe and has received local awards such as Food fest. Currently, there are only 4 rooms left, and guests can enjoy a free dinner. | Ask_alternatives
17 | User | I think I'll go with Home from Home. | Selection
18 | Bot | Great choice! The hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details
19 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
20 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Goodbye
| Utterance # | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the centre of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan on staying? | Ask_details |
| 3 | User | I'll be there next week. | Inform |
| 4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details |
| 5 | User | Just me. | Inform |
| 6 | Bot | Alright, based on your criteria, I have 3 options for you. The Gonville Hotel, The University Arms Hotel, and The Alexander Bed and Breakfast. | Multioption_suggestion |
| 7 | User | What's the difference between them? | Ask_differences |
| 8 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, 24/7 room service, free wifi, a gym, a pool, and spacious rooms. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. | Provide_differences |
| 9 | User | How much does each one cost? | Ask_details |
| 10 | Bot | The Gonville Hotel ranges from £79 for a single room to £119 for a family room. The University Arms Hotel ranges from £150 for a single room to £250 for a family room. The Alexander Bed and Breakfast ranges from £100 for a single room to £150 for a family room. | Provide_differences |
| 11 | User | That's quite expensive. Do you have any cheaper options? | Ask_alternatives |
| 12 | Bot | I have two more options for you. Cityroomz and El Shaddai. Cityroomz has affordable prices for single, double, and family rooms, and El Shaddai offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. | Multioption_suggestion |
| 13 | User | What's the difference between Cityroomz and El Shaddai? | Ask_differences |
| 14 | Bot | Cityroomz has internet access and takes bookings, but has no parking. El Shaddai offers internet and parking facilities, and takes bookings. | Provide_differences |
| 15 | User | I think I'll go with The University Arms Hotel. | Selection |
| 16 | Bot | Great choice! The University Arms Hotel is a luxurious 4-star hotel with free breakfast, 24/7 room service, free wifi, a gym, a pool, and spacious rooms. | Affirm |
| 17 | User | The price is a bit steep. Can you offer a discount? | Negotiation |
| 18 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation |
| 19 | User | Can you remove the gym access? | Negotiation |
| 20 | Bot | Sure, I can remove the gym access. The discounted price will be £135 for a single room and £225 for a family room. | Provide_negotiation |
| 21 | User | That sounds good. I'll take it. | Affirm |
| 22 | Bot | The hotel has been reserved. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation |
| 23 | User | My name is John Smith, my email is johnsmith@email.com, and my contact number is 0123456789. | Inform |
| 24 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye |
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, here are three options: Rosa's Bed and Breakfast, The Bridge Guest House, and Aylesbray Lodge Guest House. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between them? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse with luxurious rooms, a gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, a gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | How much does each option cost? | Add_aspect_price
10 | Bot | Rosa's Bed and Breakfast is currently offering a 33% discount, with double rooms priced at £100, family rooms at £150, and single rooms at £75. The Bridge Guest House has double rooms at £75, family rooms at £90, and single rooms at £50. Aylesbray Lodge Guest House is currently offering a 30% discount, with double rooms priced at £105, family rooms at £135, and single rooms at £80. | Provide_differences
11 | User | Can you suggest more options? | Ask_alternatives
12 | Bot | Sure, how about The Lensfield Hotel? It's a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. | Multioption_suggestion
13 | User | How much does it cost? | Add_aspect_price
14 | Bot | The Lensfield Hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. | Provide_differences
15 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
16 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. The hotel offers spacious and luxurious rooms with great food, gym, pool, bar, and BBQ grill. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. | Provide_details
17 | User | Can I negotiate the price? | Negotiation
18 | Bot | Sure, we can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
19 | User | Can I get a higher priced option for the price of the cheaper option? | Negotiation
20 | Bot | I'm sorry, but the facilities provided in the higher priced option are not available in the cheaper option. | Provide_negotiation
21 | User | Can you tell me more about Aylesbray Lodge Guest House? | Selection
22 | Bot | Aylesbray Lodge Guest House is a 4-star hotel located in South with free internet and parking. The hotel offers moderate prices for single, double, and family rooms. It has excellent 24/7 room service, free breakfast, and free wifi. The hotel features a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms that are fully safe, sanitary, and secure. Aylesbray Lodge Guest House has been recognized by famous magazines, tour agencies, and critics. It has hosted celebrities like Ronaldo, Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named Dine with Me. The hotel is currently offering a 30% discount on bookings for the next 2 days, with only 2 rooms left. It is popular with locals, tour agencies, and has a huge social media presence with an 8/10 rating. | Provide_details
23 | User | Can I negotiate the price for Aylesbray Lodge Guest House? | Negotiation
24 | Bot | Sure, we can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
25 | User | Can you suggest more options? | Ask_alternatives
26 | Bot | Sure, how about The Bridge Guest House? It's a 3-star guesthouse located in the south area of Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also provides parking and internet facilities. The hotel has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. The hotel offers moderate pricing with double rooms at £75, family rooms at £90, and single rooms at £50. | Multioption_suggestion
27 | User | Can you tell me more about The Bridge Guest House? | Selection
28 | Bot | The Bridge Guest House is a 3-star guesthouse located in the south area of Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also provides parking and internet facilities. The hotel has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. The hotel offers moderate pricing with double rooms at £75, family rooms at £90, and single rooms at £50. | Provide_details
29 | User | I'm still not sure which one to choose. Can you give me some time to decide? | Affirm
30 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a moderate price range and a 31% discount for the next 2 days. The third is Lovell Lodge, a 2-star hotel with a moderate price range and only 4 rooms left. Which one would you like to know more about? | Multioption_suggestion
7 | User | What's the difference between Kirkwood House and Home from Home? | Ask_differences
8 | Bot | Kirkwood House is more luxurious and has a higher rating on social media. Home from Home has a moderate price range and is offering free dinner. | Provide_differences
9 | User | What about Lovell Lodge? | Ask_alternatives
10 | Bot | Lovell Lodge is a 2-star hotel with a moderate price range and only 4 rooms left. It has been endorsed by local tour agencies and has received local awards. | Multioption_suggestion
11 | User | How much does each option cost? | Add_aspect_X
12 | Bot | Kirkwood House costs £120 per night, Home from Home costs £75 for double rooms, £105 for family rooms, and £50 for single rooms, and Lovell Lodge costs £65 for double rooms, £70 for family rooms, and £50 for single rooms. | Add_aspect_X
13 | User | Can you tell me more about Kirkwood House? | Selection
14 | Bot | Kirkwood House is a 4-star guesthouse located in North Cambridge. It offers free breakfast, 24/7 room service, free wifi, a gym, pool, bar, BBQ grill, and Jacuzzi. It has spacious and luxurious rooms and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies and has received prestigious awards such as the Michelin Star. The hotel has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. | Selection
15 | User | That sounds great, but it's a bit out of my budget. Can you offer a lower price? | Negotiation
16 | Bot | I'm sorry, but the price is already discounted by 36%. However, I can offer a 10% discount on Home from Home or Lovell Lodge. Which one would you like to negotiate for? | Provide_negotiation
17 | User | Can I negotiate for Home from Home? | Negotiation
18 | Bot | Sure, I can offer a 10% discount on Home from Home, but some facilities like the gym or pool might be removed. Would you still like to proceed? | Provide_negotiation
19 | User | Hmm, let me think about it. Can you tell me more about Lovell Lodge? | Selection
20 | Bot | Lovell Lodge is a 2-star hotel located in North Cambridge. It offers free breakfast, free wifi, and good room service. The hotel has parking and internet facilities and takes bookings. The price range is moderate, with double rooms costing £65, family rooms £70, and single rooms £50. Lovell Lodge has been endorsed by local tour agencies TourMe and has received local awards such as Food fest. Currently, there are only 4 rooms left, and guests can enjoy a free dinner. The hotel has a public image rating of 6/10. | Selection
21 | User | That sounds good. Can I book Lovell Lodge? | Selection
22 | Bot | Sure, I'll need your name, email, and phone number to make the booking. | Ask_details
23 | User | My name is John Smith, my email is johnsmith@gmail.com, and my phone number is 1234567890. | Inform
24 | Bot | Great, your booking has been confirmed. Your registration number is 12345. You can contact us at 0987654321 for any queries. | Confirmation
25 | User | Can I add breakfast to my booking? | Add_aspect_X
26 | Bot | Sure, breakfast is already included in your booking at Lovell Lodge. | Add_aspect_X
27 | User | Can I change my booking to a family room? | Add_aspect_X
28 | Bot | I'm sorry, but all family rooms are already booked. | Deny
29 | User | Can you suggest any other hotels with family rooms available? | Ask_alternatives
30 | Bot | Sure, I have two options for you. The first is The Limehouse guesthouse, a 4-star hotel with spacious and luxurious rooms, a gym, a pool, and a DJ floor. The second is Archway House, a 4-star guesthouse with free wifi, parking, and breakfast, spacious and luxurious rooms, a gym, pool, and DJ floor. Which one would you like to know more about? | Multioption_suggestion
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_details
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Ask_alternatives
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_details
11 | User | Can you tell me more about the food festival at Huntingdon Marriott Hotel? | Add_aspect_X
12 | Bot | The food festival at Huntingdon Marriott Hotel offers free dinner for guests. It's a great opportunity to try out some delicious food. | Provide_details
13 | User | I'm not sure which one to choose. Can you suggest another option? | Ask_alternatives
14 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Multioption_suggestion
15 | User | What are the prices for Finches Bed and Breakfast? | Add_aspect_X
16 | Bot | Finches Bed and Breakfast offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_details
17 | User | Can you negotiate the price for Huntingdon Marriott Hotel? | Negotiation
18 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
19 | User | Can you remove the DJ floor and still keep the free dinner? | Negotiation
20 | Bot | I can remove the DJ floor, but the free dinner is part of the food festival package and cannot be removed. | Provide_negotiation
21 | User | Okay, I'll go with Huntingdon Marriott Hotel. | Selection
22 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details
23 | User | My name is John Smith, my email is johnsmith@email.com, and my contact number is 1234567890. | Inform
24 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have three options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a rating of 8/10. Which one would you like to know more about? | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive option, but it offers a gym and a pool. The A and B Guest House has a BBQ grill and a Jacuzzi. Allenbell guesthouse is the most affordable option, but it has a bar. | Provide_differences |
| 9 | User | Can you tell me more about Leverton House? | Selection |
| 10 | Bot | Leverton House is a 4-star guesthouse located in East Cambridge. It offers free breakfast, 24/7 room service, free wifi, a gym, and a pool. The rooms are spacious and luxurious, and the hotel is fully safe, sanitary, and secure. It has received numerous recognitions, including appearing in magazines like BigHospitality and LuxeDine, being endorsed by tour agencies like Expedia, and receiving prestigious awards like the Michelin Star. It has also hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan and has been endorsed by famous critics like Pete Wells and Jonathan Gold. | Provide_differences |
| 11 | User | That sounds great, but it's a bit over my budget. Can you offer a lower price? | Negotiation |
| 12 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. Would you still like to proceed with the booking? | Provide_negotiation |
| 13 | User | Can you tell me more about The A and B Guest House? | Ask_alternatives |
| 14 | Bot | The A and B Guest House is a 4-star guesthouse located in East Cambridge. It offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel has a gym, pool, BBQ grill, and Jacuzzi. It has been recognized by famous magazines and tour agencies, received prestigious awards like the Michelin Star, and hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. The head chef has a cookbook named "Put me to Sleep". The hotel is popular with locals, international tourists, and tour agencies, and currently offers a food festival and discounts on bookings. | Multioption_suggestion |
| 15 | User | What's the price for The A and B Guest House? | Ask_differences |
| 16 | Bot | The A and B Guest House is priced at £130 per night. | Provide_differences |
| 17 | User | Can you tell me more about Allenbell guesthouse? | Ask_alternatives |
| 18 | Bot | Allenbell guesthouse, located in East Cambridge, is a 4-star hotel with affordable prices. It offers free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and spacious luxurious rooms. The hotel has received numerous recognitions, including Michelin Star and Cateys awards, and has hosted celebrities such as Ronaldo, Virat Kholi, and Eminem. It has also been endorsed by popular tour agencies like TripAdvisor and famous critics like Pete Wells, Gordon Ramsay, and Nigella Lawson. The hotel is popular with locals, international tourists, and tour agencies, and has a strong social media presence. | Multioption_suggestion |
| 19 | User | What's the price for Allenbell guesthouse? | Ask_differences |
| 20 | Bot | Allenbell guesthouse is priced at £120 per night. | Provide_differences |
| 21 | User | Can you offer a discount for The A and B Guest House? | Negotiation |
| 22 | Bot | I can offer a 5% discount, but some of the facilities provided might get removed. Would you still like to proceed with the booking? | Provide_negotiation |
| 23 | User | Can you tell me more about Autumn House? | Ask_alternatives |
| 24 | Bot | Autumn House is a 4-star guesthouse located in East, with free internet and parking. The hotel offers cheap prices for single, double, and family rooms. It has received recognitions from famous magazines, tour agencies, and prestigious awards like Michelin Star. The hotel has hosted celebrities like Ronaldo, Tom Holland, and Jackie Chan. It offers free breakfast, 24/7 room service, gym, pool, bar, BBQ grill, Jacuzzi, DJ floor, and fully safe, sanitary, and secure rooms. Autumn House is popular with locals and international tourists, with a 10/10 rating. It also offers 37% off on bookings for the next 2 days and free dinner. | Multioption_suggestion |
| 25 | User | What's the price for Autumn House? | Ask_differences |
| 26 | Bot | Autumn House is priced at £100 per night. | Provide_differences |
| 27 | User | I'm still not sure which one to choose. Can you give me some time to decide? | Affirm |
| 28 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm |
| 29 | User | Can you tell me more about the food festival at Leverton House? | Ask_details |
| 30 | Bot | The food festival at Leverton House features a variety of cuisines from around the world, including Indian, Chinese, Italian, and Mexican. There are also live cooking demonstrations and food tastings. | Ask_details |
| 31 | User | That sounds amazing. Can you offer a discount for Leverton House? | Negotiation |
| 32 | Bot | I can offer a 5% discount, but some of the facilities provided might get removed. Would you still like to proceed with the booking? | Provide_negotiation |
| 33 | User | I think I'll go with The A and B Guest House. | Selection |
| 34 | Bot | Great choice! The hotel has been reserved. Your registration number is 123456. Please provide your name, email, and contact number for the booking. | Confirmation |
| 35 | User | My name is John Smith, my email is johnsmith@email.com, and my contact number is 1234567890. | Inform |
| 36 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye |
| 37 | User | No, that's all. Thank you for your help. | Goodbye |
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_differences
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Add_aspect_X
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_differences
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_differences
13 | User | I'm interested in the Huntingdon Marriott Hotel, but it's a bit expensive. Can you offer a lower price? | Negotiation
14 | Bot | I can offer a 10% discount, but some facilities like the DJ floor and free dinner may not be available. Would you still like to book the Huntingdon Marriott Hotel? | Provide_negotiation
15 | User | Hmm, can you suggest any other options? | Ask_alternatives
16 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Multioption_suggestion
17 | User | Can you tell me more about Finches Bed and Breakfast? | Add_aspect_X
18 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_differences
19 | User | That sounds great, but what's the price? | Add_aspect_X
20 | Bot | Finches Bed and Breakfast offers double rooms for £120, single rooms for £90, and family rooms for £150. | Provide_differences
21 | User | Can you offer a lower price for Finches Bed and Breakfast? | Negotiation
22 | Bot | I can offer a 5% discount, but some facilities like the BBQ grill and Jacuzzi may not be available. Would you like to book Finches Bed and Breakfast? | Provide_negotiation
23 | User | Let me think about it for a bit. | Selection
24 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
25 | User | Can you tell me more about the Huntingdon Marriott Hotel's food festival? | Add_aspect_X
26 | Bot | The Huntingdon Marriott Hotel is currently running a food festival with free dinner for guests. The festival features a variety of cuisines and is a great opportunity to try new dishes. | Provide_differences
27 | User | Can I book the Huntingdon Marriott Hotel with the 10% discount? | Negotiation
28 | Bot | I'm sorry, but the Huntingdon Marriott Hotel is currently fully booked for the dates you requested. Would you like to book Finches Bed and Breakfast instead? | Ask_alternatives
29 | User | Alright, I'll book Finches Bed and Breakfast. | Selection
30 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and phone number for the booking. | Confirmation, Ask_details
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, and a pool. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Selection
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Provide_details
9 | User | Can you suggest a cheaper option? | Ask_alternatives
10 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Cityroomz has no parking, but offers affordable prices for single, double, and family rooms. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices. | Multioption_suggestion
11 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
12 | Bot | Cityroomz has internet access and takes bookings, but has no parking. El Shaddai offers internet and parking facilities, and takes bookings. El Shaddai is cheaper, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
13 | User | Can you tell me more about the University Arms Hotel? | Selection
14 | Bot | The University Arms Hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_details
15 | User | Can you suggest another option? | Ask_alternatives
16 | Bot | Sure, I have The Gonville Hotel, Cityroomz, and El Shaddai. Which one would you like to know more about? | Multioption_suggestion
17 | User | Can you negotiate the price of The Gonville Hotel? | Negotiation
18 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. The hotel is already offering 38% off on bookings for the next 4 days and free dinner. | Provide_negotiation
19 | User | Can you remove the gym and safe facilities? | Negotiation
20 | Bot | Sure, I can remove the gym and safe facilities. The new price for a single room would be £71.10 and for a family room would be £107.10. | Provide_negotiation
21 | User | Can you suggest another option? | Ask_alternatives
22 | Bot | Sure, I have The University Arms Hotel, Alexander Bed and Breakfast, and El Shaddai. Which one would you like to know more about? | Multioption_suggestion
23 | User | Can you tell me more about the Alexander Bed and Breakfast? | Selection
24 | Bot | The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_details
25 | User | Can you suggest another option? | Ask_alternatives
26 | Bot | Sure, I have The Gonville Hotel, University Arms Hotel, and El Shaddai. Which one would you like to know more about? | Multioption_suggestion
27 | User | Can you tell me more about the University Arms Hotel? | Selection
28 | Bot | The University Arms Hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_details
29 | User | Can you suggest another option? | Ask_alternatives
30 | Bot | Sure, I have The Gonville Hotel, Alexander Bed and Breakfast, and El Shaddai. Which one would you like to know more about? | Multioption_suggestion
31 | User | I'll go with The Gonville Hotel. | Selection
32 | Bot | Great, The Gonville Hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation
33 | User | My name is John Smith, email is johnsmith@gmail.com, there will be 2 people, and we prefer a family room. | Inform
34 | Bot | Thank you, John. Your booking has been confirmed. You will receive an email with the details. Is there anything else I can help you with? | Confirmation
35 | User | No, that's all. Thank you. | Goodbye
36 | Bot | You're welcome. Have a great day! | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The first is Rosa's Bed and Breakfast, a 4-star guesthouse with a 33% discount for the next 4 days. The second is The Bridge Guest House, a 3-star guesthouse with moderate pricing. The third is Aylesbray Lodge Guest House, a 4-star hotel with a 30% discount for the next 2 days. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
10 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you negotiate the price? | Negotiation
12 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Would you like me to negotiate for you? | Provide_negotiation
13 | User | Yes, please. | Affirm
14 | Bot | I'm sorry, but the hotel is already offering a 33% discount. I cannot negotiate any further. | Deny
15 | User | Okay, can you suggest some other options? | Ask_alternatives
16 | Bot | Sure, I have one more option for you. The Lensfield Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Multioption_suggestion
17 | User | What are the differences between the options? | Ask_differences
18 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. The Lensfield Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. | Provide_differences
19 | User | Can you tell me more about The Lensfield Hotel? | Selection
20 | Bot | The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel has received recognitions such as appearing in local magazines like FoodVilla and Food and Beyond, being endorsed by local tour agencies TourMe, and receiving local awards such as Food Fest, Budget, and Great and Escape. | Selection
21 | User | I'm not sure which one to choose. Can you give me some time to decide? | Inform
22 | Bot | Sure, take your time. Let me know if you have any other questions. | Inform
23 | User | Can you tell me more about the facilities at Aylesbray Lodge Guest House? | Ask_details
24 | Bot | Aylesbray Lodge Guest House has excellent 24/7 room service, free breakfast, and free wifi. The hotel features a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms that are fully safe, sanitary, and secure. The head chef has a cookbook named Dine with Me. | Ask_details
25 | User | How much is a double room at Aylesbray Lodge Guest House? | Add_aspect_X
26 | Bot | A double room at Aylesbray Lodge Guest House is priced at £85 per night. | Add_aspect_X
27 | User | Can you tell me more about The Bridge Guest House? | Selection
28 | Bot | The Bridge Guest House is a 3-star guesthouse located in the south area of Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also provides parking and internet facilities. The hotel has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. The hotel offers moderate pricing with double rooms at £75, family rooms at £90, and single rooms at £50. | Selection
29 | User | Can you tell me more about the facilities at Rosa's Bed and Breakfast? | Ask_details
30 | Bot | Rosa's Bed and Breakfast has free internet and parking. The hotel offers spacious and luxurious rooms with great food, gym, pool, bar, and BBQ grill. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Ask_details
31 | User | I think I'll go with The Bridge Guest House. | Selection
32 | Bot | Great choice! The hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference for the booking. | Confirmation
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, here are three options: Rosa's Bed and Breakfast, The Bridge Guest House, and Aylesbray Lodge Guest House. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between them? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse with luxurious rooms, a gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, a gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | How much does each option cost? | Add_aspect_price
10 | Bot | Rosa's Bed and Breakfast is currently offering a 33% discount, with double rooms priced at £100, family rooms at £150, and single rooms at £75. The Bridge Guest House has double rooms at £75, family rooms at £90, and single rooms at £50. Aylesbray Lodge Guest House is currently offering a 30% discount, with double rooms priced at £105, family rooms at £135, and single rooms at £80. | Provide_differences
11 | User | Can you suggest more options? | Ask_alternatives
12 | Bot | Sure, how about The Lensfield Hotel? It's a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. | Multioption_suggestion
13 | User | How much does it cost? | Add_aspect_price
14 | Bot | The Lensfield Hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. | Provide_differences
15 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
16 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. The hotel offers spacious and luxurious rooms with great food, gym, pool, bar, and BBQ grill. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. | Provide_details
17 | User | Can I negotiate the price? | Negotiation
18 | Bot | Sure, we can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
19 | User | Can I get a higher priced option for the price of the cheaper option? | Negotiation
20 | Bot | I'm sorry, but the prices are fixed. However, I can assure you that Rosa's Bed and Breakfast is worth the price. | Provide_negotiation
21 | User | Can you tell me more about Aylesbray Lodge Guest House? | Selection
22 | Bot | Aylesbray Lodge Guest House is a 4-star hotel located in South with free internet and parking. The hotel offers moderate prices for single, double, and family rooms. It has excellent 24/7 room service, free breakfast, and free wifi. The hotel features a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms that are fully safe, sanitary, and secure. Aylesbray Lodge Guest House has been recognized by famous magazines, tour agencies, and critics. It has hosted celebrities like Ronaldo, Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named Dine with Me. The hotel is currently offering a 30% discount on bookings for the next 2 days, with only 2 rooms left. It is popular with locals, tour agencies, and has a huge social media presence with an 8/10 rating. | Provide_details
23 | User | Can I negotiate the price for Aylesbray Lodge Guest House? | Negotiation
24 | Bot | Yes, we can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
25 | User | Can you tell me more about The Lensfield Hotel? | Selection
26 | Bot | The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel has received recognitions such as appearing in local magazines like FoodVilla and Food and Beyond, being endorsed by local tour agencies TourMe, and receiving local awards such as Food Fest, Budget, and Great and Escape. | Provide_details
27 | User | Can I negotiate the price for The Lensfield Hotel? | Negotiation
28 | Bot | Yes, we can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
29 | User | Can you suggest more options? | Ask_alternatives
30 | Bot | I'm sorry, but those are the only options available for your selected dates. Which one would you like to book? | Confirmation
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have three options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive but has luxurious rooms, a gym, and a pool. The A and B Guest House has a BBQ grill and Jacuzzi. Allenbell guesthouse is affordable and has a bar. | Provide_differences |
| 9 | User | Can you give me more options? | Ask_alternatives |
| 10 | Bot | Sure, how about Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days? Or Autumn House, a 4-star guesthouse with a 37% discount on bookings for the next 2 days and free dinner? | Multioption_suggestion |
| 11 | User | What are the differences between Carolina Bed and Breakfast and Autumn House? | Ask_differences |
| 12 | Bot | Carolina Bed and Breakfast has a pool, bar, and Jacuzzi. Autumn House has a DJ floor and free dinner. Both have received recognitions and hosted celebrities. | Provide_differences |
| 13 | User | I'm interested in Leverton House, but it's over my budget. Can you offer a lower price? | Negotiation |
| 14 | Bot | I can offer a 10% discount, but some facilities like the gym and pool might not be available. | Provide_negotiation |
| 15 | User | Okay, I'll take the discount. | Affirm, Selection |
| 16 | Bot | Great, the hotel has been reserved. Your registration number is 12345. Please provide your name, email, and number of people and rooms required. | Confirmation, Ask_details |
| 17 | User | My name is John Smith, my email is johnsmith@gmail.com, and I need a double room for two people. | Inform |
| 18 | Bot | Thank you, John. Your booking is confirmed. You can contact us at 123-456-7890 for any further queries. | Confirmation, Goodbye |
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with a pool, gym, and spacious rooms. The Alexander Bed and Breakfast is a 4-star guesthouse with a gym, pool, bar, and BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Selection
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Provide_details
9 | User | Can you suggest a cheaper option? | Ask_alternatives
10 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Which one would you like to know more about? | Multioption_suggestion
11 | User | What are the differences between the cheaper options? | Ask_differences
12 | Bot | Cityroomz is a moderate hotel with affordable prices for single, double, and family rooms. It has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse with a 0-star rating and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
13 | User | Can you tell me more about the University Arms Hotel? | Selection
14 | Bot | The University Arms Hotel is a luxurious 4-star hotel located in the centre of Regent Street. It offers free breakfast, 24/7 room service, free wifi, a gym, a pool, and spacious rooms. The hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_details
15 | User | Can you negotiate the price of the University Arms Hotel? | Negotiation
16 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. The University Arms Hotel is a luxurious 4-star hotel with a pool, gym, and spacious rooms. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_negotiation
17 | User | Can you suggest more options with a gym? | Add_aspect_gym
18 | Bot | Sure, The Gonville Hotel and Alexander Bed and Breakfast both have a gym. Which one would you like to know more about? | Multioption_suggestion
19 | User | What are the differences between the options with a gym? | Ask_differences
20 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. It also has friendly staff, delicious food, and very clean rooms. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. The Alexander Bed and Breakfast is a 4-star guesthouse with a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_differences
21 | User | Can you suggest a cheaper option with a gym? | Ask_alternatives
22 | Bot | Sure, Cityroomz and El Shaddai both have a gym. Which one would you like to know more about? | Multioption_suggestion
23 | User | What are the differences between the cheaper options with a gym? | Ask_differences
24 | Bot | Cityroomz is a moderate hotel with affordable prices for single, double, and family rooms. It has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse with a 0-star rating and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
25 | User | Can you suggest more options with a pool? | Add_aspect_pool
26 | Bot | Sure, The University Arms Hotel and Alexander Bed and Breakfast both have a pool. Which one would you like to know more about? | Multioption_suggestion
27 | User | What are the differences between the options with a pool? | Ask_differences
28 | Bot | The University Arms Hotel is a luxurious 4-star hotel with a pool, gym, and spacious rooms. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. The Alexander Bed and Breakfast is a 4-star guesthouse with a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_differences
29 | User | Can you suggest a cheaper option with a pool? | Ask_alternatives
30 | Bot | Sorry, there are no cheaper options with a pool. Would you like to select one of the options provided? | Selection
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have three options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive option, but it offers a gym and a pool. The A and B Guest House has a BBQ grill and a Jacuzzi. Allenbell guesthouse has a bar and spacious luxurious rooms. | Provide_differences |
| 9 | User | I'm interested in Leverton House. Can you tell me more about it? | Selection |
| 10 | Bot | Leverton House is a 4-star guesthouse located in East Cambridge. It offers free breakfast, 24/7 room service, free wifi, a gym, and a pool. The rooms are spacious and luxurious, and the hotel is fully safe, sanitary, and secure. It has received numerous recognitions, including appearing in magazines like BigHospitality and LuxeDine, being endorsed by tour agencies like Expedia, and receiving prestigious awards like the Michelin Star. It has also hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan and has been endorsed by famous critics like Pete Wells and Jonathan Gold. | Provide_details |
| 11 | User | The price is a bit high. Can you offer a discount? | Negotiation |
| 12 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation |
| 13 | User | Can you remove the gym and pool facilities? | Negotiation |
| 14 | Bot | I can remove the gym and pool facilities, but the discount will only be 5%. | Provide_negotiation |
| 15 | User | Okay, I'll take it. | Affirm |
| 16 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation |
| 17 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform |
| 18 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye |
| 19 | User | Actually, can you suggest some more options? | Ask_alternatives |
| 20 | Bot | Sure, I have two more options for you. The first is Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. The second is Autumn House, a 4-star guesthouse with free dinner and 37% off on bookings for the next 2 days. | Multioption_suggestion |
| 21 | User | What are the differences between the options? | Ask_differences |
| 22 | Bot | Carolina Bed and Breakfast has a pool, bar, BBQ grill, and Jacuzzi. Autumn House has a DJ floor and spacious luxurious rooms. | Provide_differences |
| 23 | User | I'm interested in Carolina Bed and Breakfast. Can you tell me more about it? | Selection |
| 24 | Bot | Carolina Bed and Breakfast is a 4-star guesthouse located in East Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. It has spacious and luxurious rooms, a pool, bar, BBQ grill, and Jacuzzi. The hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies like Expedia, TripAdvisor, and Thomas Cook. It has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. | Provide_details |
| 25 | User | The price is still a bit high. Can you offer a discount? | Negotiation |
| 26 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation |
| 27 | User | Can you remove the BBQ grill and Jacuzzi facilities? | Negotiation |
| 28 | Bot | I can remove the BBQ grill and Jacuzzi facilities, but the discount will only be 5%. | Provide_negotiation |
| 29 | User | Okay, I'll take it. | Affirm |
| 30 | Bot | Great, the hotel has been reserved. Your registration number is 654321. Please provide your name, email, and contact number for confirmation. | Confirmation |
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The Cambridge Belfry is £120 per night, Huntingdon Marriott Hotel is £150 per night, and Hobsons House is £75 per night. | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
9 | User | Can you suggest more options? | Ask_alternatives
10 | Bot | Sure, I also have Finches Bed and Breakfast for £130 per night. It's a 4-star guesthouse with a gym, pool, and BBQ grill. | Multioption_suggestion
11 | User | What are the differences between the options? | Ask_differences
12 | Bot | The Cambridge Belfry and Finches Bed and Breakfast are both 4-star hotels with a gym, pool, and jacuzzi. Huntingdon Marriott Hotel has a DJ floor and free dinner. Hobsons House has a 32% discount and free dinner. | Provide_differences
13 | User | I'm interested in The Cambridge Belfry. Can you negotiate the price? | Negotiation
14 | Bot | I can offer you a 10% discount, but some facilities like the jacuzzi will be removed. | Provide_negotiation
15 | User | Can you tell me more about The Cambridge Belfry? | Add_aspect_X
16 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Add_aspect_X
17 | User | Okay, I'll take The Cambridge Belfry. | Selection
18 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details
19 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
20 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_differences
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Add_aspect_X
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_differences
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_differences
13 | User | I'm interested in the Huntingdon Marriott Hotel, but it's a bit expensive. Can you offer a lower price? | Negotiation
14 | Bot | I can offer a 10% discount, but some facilities like the DJ floor and free dinner may not be available. Would you still like to book the Huntingdon Marriott Hotel? | Provide_negotiation
15 | User | Hmm, can you suggest any other options? | Ask_alternatives
16 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Multioption_suggestion
17 | User | Can you tell me more about Finches Bed and Breakfast? | Add_aspect_X
18 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_differences
19 | User | That sounds great, but what's the price? | Add_aspect_X
20 | Bot | The price for a double room is £120 per night, a single room is £90 per night, and a family room is £150 per night. | Add_aspect_X
21 | User | That's a bit expensive. Can you offer a lower price? | Negotiation
22 | Bot | I can offer a 10% discount, but some facilities like the BBQ grill and Jacuzzi may not be available. Would you still like to book Finches Bed and Breakfast? | Provide_negotiation
23 | User | Can you suggest any other options? | Ask_alternatives
24 | Bot | Sure, how about The Cambridge Belfry? It's a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Multioption_suggestion
25 | User | Can you tell me more about The Cambridge Belfry? | Add_aspect_X
26 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_differences
27 | User | What's the price for The Cambridge Belfry? | Add_aspect_X
28 | Bot | The price for a double room is £150 per night, a single room is £120 per night, and a family room is £200 per night. | Add_aspect_X
29 | User | That's a bit expensive. Can you offer a lower price? | Negotiation
30 | Bot | I can offer a 10% discount, but some facilities like the jacuzzi may not be available. Would you still like to book The Cambridge Belfry? | Provide_negotiation
31 | User | I'll think about it and get back to you. | Selection
32 | Bot | Sure, take your time. Let me know if you have any other questions. | Goodbye
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a 31% discount for the next 2 days and free dinner. The third is Lovell Lodge, a 2-star hotel with a moderate price range and only 4 rooms left. Which one would you like to know more about? | Multioption_suggestion
7 | User | Can you tell me the differences between the options? | Ask_differences
8 | Bot | Kirkwood House is a 4-star guesthouse with a gym, pool, bar, BBQ grill, and Jacuzzi. Home from Home is also a 4-star guesthouse with a gym, pool, and bar. Lovell Lodge is a 2-star hotel with free breakfast and wifi. | Provide_differences
9 | User | Can you tell me more about Kirkwood House? | Selection
10 | Bot | Kirkwood House is a 4-star guesthouse located in North Cambridge. It offers free breakfast, 24/7 room service, free wifi, a gym, pool, bar, BBQ grill, and Jacuzzi. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as the Michelin Star. The hotel has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. | Selection
11 | User | That sounds great, but it might be a bit out of my budget. Can you suggest something cheaper? | Ask_alternatives
12 | Bot | Sure, I have two other options for you. The first is Home from Home, a 4-star guesthouse with a moderate price range and a 31% discount for the next 2 days and free dinner. The second is Lovell Lodge, a 2-star hotel with a moderate price range and only 4 rooms left. Which one would you like to know more about? | Multioption_suggestion
13 | User | Can you tell me the differences between Home from Home and Lovell Lodge? | Ask_differences
14 | Bot | Home from Home is a 4-star guesthouse with a gym, pool, and bar. Lovell Lodge is a 2-star hotel with free breakfast and wifi. | Provide_differences
15 | User | Can you tell me more about Home from Home? | Selection
16 | Bot | Home from Home is a 4-star guesthouse located in North Cambridge. It offers free breakfast, 24/7 room service, free wifi, a gym, pool, and bar. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by popular magazines and tour agencies and has hosted celebrities such as Ronaldo, Virat Kholi, and Tom Holland. | Selection
17 | User | That sounds good. Can I negotiate the price? | Negotiation
18 | Bot | I'm sorry, but the prices are already discounted. However, I can offer you a 10% discount on the original price if you're interested. | Provide_negotiation
19 | User | Can you remove the free dinner and give me the 10% discount on Home from Home? | Negotiation
20 | Bot | Sure, I can remove the free dinner and give you a 10% discount on the original price. The new price for Home from Home will be £67.50 per night. Would you like to proceed with the booking? | Confirmation
21 | User | Can you suggest any other hotels with a food festival? | Ask_alternatives
22 | Bot | Yes, I have two options for you. The first is Limehouse guesthouse, a 4-star hotel with a food festival and a DJ floor. The second is Archway House, a 4-star guesthouse with a food festival and a 37% discount for the next 4 days. Which one would you like to know more about? | Multioption_suggestion
23 | User | Can you tell me the differences between Limehouse guesthouse and Archway House? | Ask_differences
24 | Bot | Limehouse guesthouse is a 4-star hotel with a gym, pool, and DJ floor. It has received prestigious awards such as Michelin Star and The Gold List and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. Archway House is a 4-star guesthouse with a gym, pool, and DJ floor. It has been recognized by popular magazines and tour agencies and has hosted celebrities like Tom Holland and Jackie Chan. | Provide_differences
25 | User | Can you tell me more about Limehouse guesthouse? | Selection
26 | Bot | Limehouse guesthouse is a 4-star hotel located in the north area of Cambridge. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, a pool, and a DJ floor. It has received prestigious awards such as Michelin Star and The Gold List and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. | Selection
27 | User | That sounds great, but it might be a bit out of my budget. Can you suggest something cheaper? | Ask_alternatives
28 | Bot | Sure, I have one more option for you. The Acorn Guest House is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel has a gym and pool. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Ronaldo and Eminem. The head chef has a cookbook named "How to Burger." The hotel is currently offering free dinner. | Multioption_suggestion
29 | User | Can you tell me more about Acorn Guest House? | Selection
30 | Bot | The Acorn Guest House is a 4-star guesthouse located in North Cambridge. It offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel has a gym and pool. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Ronaldo and Eminem. The head chef has a cookbook named "How to Burger." The hotel is popular with locals, international tourists, and tour agencies and has a huge social media presence. It is fully safe, sanitary, and secure. | Selection
31 | User | I need some time to think. Can I get back to you later? | Affirm
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi for £120 per night. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a food festival and free dinner for £150 per night. Hobsons House is a 3-star guesthouse with a 32% discount for the next 3 days for £75 per night. | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | The Cambridge Belfry and Huntingdon Marriott Hotel are both 4-star hotels with luxurious rooms and amenities. The Huntingdon Marriott Hotel is more expensive but offers a food festival and free dinner. Hobsons House is a 3-star guesthouse with a discount for the next 3 days. | Provide_differences
9 | User | Can you tell me more about The Cambridge Belfry? | Ask_details
10 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Ask_details
11 | User | That sounds great, but can you give me a better price? | Negotiation
12 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
13 | User | Okay, I'll think about it. Can you give me more options? | Ask_alternatives
14 | Bot | Sure, I have one more option for you. Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. The price for a double room is £130 per night. | Multioption_suggestion
15 | User | Can you tell me more about Finches Bed and Breakfast? | Ask_details
16 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Ask_details
17 | User | I'm still not sure. Can you give me more options? | Ask_alternatives
18 | Bot | Sure, I have one more option for you. The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. The price for a double room is £160 per night. | Multioption_suggestion
19 | User | Can you tell me more about The Huntingdon Marriott Hotel? | Ask_details
20 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Ask_details
21 | User | That sounds great, but can you give me a better price? | Negotiation
22 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
23 | User | Okay, I'll think about it. Can you give me some time? | Affirm
24 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
25 | User | Can you tell me more about the food festival at The Huntingdon Marriott Hotel? | Ask_details
26 | Bot | The food festival at The Huntingdon Marriott Hotel is a celebration of local and international cuisine. It features free dinner for guests and a variety of food stalls and vendors. It's a great opportunity to try new foods and meet other guests. | Ask_details
27 | User | Can I book the Cambridge Belfry? | Selection
28 | Bot | Sure, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation
29 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
30 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, here are three options: Rosa's Bed and Breakfast, The Bridge Guest House, and Aylesbray Lodge Guest House. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between them? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse with luxurious rooms, a gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, a gym, pool, bar, and BBQ grill. Which one would you like to know more about? | Provide_differences
9 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
10 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Provide_differences
11 | User | That sounds great, but it's a bit expensive. Can you offer a lower price? | Negotiation
12 | Bot | I can offer a 10% discount, but some facilities might be removed. Would you like to proceed with the booking? | Provide_negotiation
13 | User | Can you tell me more about The Bridge Guest House? | Selection
14 | Bot | The Bridge Guest House is a 3-star guesthouse located in the south area of Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. The hotel offers moderate pricing with double rooms at £75, family rooms at £90, and single rooms at £50. | Provide_differences
15 | User | That sounds good. Can you tell me more about the family room? | Add_aspect_X
16 | Bot | The family room is spacious and can accommodate up to four people. It has a comfortable bed, a TV, and a private bathroom. Would you like to proceed with the booking? | Confirmation
17 | User | Can you suggest more options? | Ask_alternatives
18 | Bot | Sure, here's another option: The Lensfield Hotel. It's a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has received recognitions such as appearing in local magazines like FoodVilla and Food and Beyond, being endorsed by local tour agencies TourMe, and receiving local awards such as Food Fest, Budget, and Great and Escape. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Multioption_suggestion
19 | User | Can you tell me more about the double room at The Lensfield Hotel? | Add_aspect_X
20 | Bot | The double room is spacious and has a comfortable bed, a TV, and a private bathroom. It also has a safe and offers parking and internet. Would you like to proceed with the booking? | Confirmation
21 | User | Can you tell me more about Aylesbray Lodge Guest House? | Selection
22 | Bot | Aylesbray Lodge Guest House is a 4-star hotel located in South with free internet and parking. The hotel offers moderate prices for single, double, and family rooms. It has excellent 24/7 room service, free breakfast, and free wifi. The hotel features a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms that are fully safe, sanitary, and secure. Aylesbray Lodge Guest House has been recognized by famous magazines, tour agencies, and critics. It has hosted celebrities like Ronaldo, Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named Dine with Me. The hotel is currently offering a 30% discount on bookings for the next 2 days, with only 2 rooms left. It is popular with locals, tour agencies, and has a huge social media presence with an 8/10 rating. | Provide_differences
23 | User | That sounds good. Can you tell me more about the gym and pool? | Add_aspect_X
24 | Bot | The gym and pool are both well-maintained and accessible to all guests. The gym has modern equipment, and the pool is heated and has a beautiful view. Would you like to proceed with the booking? | Confirmation
25 | User | Can you tell me more about the discount at Aylesbray Lodge Guest House? | Add_aspect_X
26 | Bot | The hotel is currently offering a 30% discount on bookings for the next 2 days, with only 2 rooms left. Would you like to proceed with the booking? | Confirmation
27 | User | Can you tell me more about the breakfast at The Bridge Guest House? | Add_aspect_X
28 | Bot | The breakfast at The Bridge Guest House is complimentary and includes a variety of options such as eggs, bacon, toast, and coffee. Would you like to proceed with the booking? | Confirmation
29 | User | I'm still deciding. Can I get back to you later? | Goodbye
30 | Bot | Sure, feel free to contact us anytime. Have a great day! | Goodbye
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a moderate price range and a 31% discount for the next 2 days. The third is Lovell Lodge, a 2-star hotel with a moderate price range and only 4 rooms left. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Kirkwood House is a 4-star guesthouse with a gym, pool, bar, BBQ grill, and Jacuzzi. Home from Home is also a 4-star guesthouse with a gym, pool, and bar. Lovell Lodge is a 2-star hotel with free breakfast and wifi. | Provide_differences
9 | User | Can you tell me more about Kirkwood House? | Selection
10 | Bot | Kirkwood House is a luxurious guesthouse with spacious rooms and has been recognized by famous magazines and tour agencies. It has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. It is currently offering a 36% discount on bookings for the next 3 days. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you offer a better price? | Negotiation
12 | Bot | I can offer a 10% discount, but some facilities like the BBQ grill and Jacuzzi might not be available. Would you like to proceed with the booking? | Provide_negotiation
13 | User | Hmm, let me think about it. Can you suggest some other options? | Ask_alternatives
14 | Bot | Sure, I have two more options for you. The first is Limehouse guesthouse, a 4-star hotel with a gym, pool, and DJ floor. The second is Acorn Guest House, a 4-star guesthouse with a gym and pool. Both offer free breakfast and great food. Which one would you like to know more about? | Multioption_suggestion
15 | User | What are the differences between Limehouse guesthouse and Acorn Guest House? | Ask_differences
16 | Bot | Limehouse guesthouse has received prestigious awards such as Michelin Star and The Gold List and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. Acorn Guest House has hosted celebrities like Ronaldo and Eminem, and the head chef has a cookbook named "How to Burger." | Provide_differences
17 | User | Can you tell me more about Limehouse guesthouse? | Selection
18 | Bot | Limehouse guesthouse is a luxurious 4-star hotel with spacious rooms, a gym, pool, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. It is fully safe, sanitary, and secure. | Selection
19 | User | That sounds great, but it's still a bit over my budget. Can you offer a better price? | Negotiation
20 | Bot | I can offer a 10% discount, but some facilities like the DJ floor might not be available. Would you like to proceed with the booking? | Provide_negotiation
21 | User | Let me think about it. Can you suggest some other options? | Ask_alternatives
22 | Bot | Sure, I have one more option for you. Archway House is a 4-star guesthouse with a food festival and 37% off on bookings for the next 4 days. It has a gym, pool, and DJ floor. Which one would you like to know more about? | Multioption_suggestion
23 | User | What are the differences between Archway House and the other options? | Ask_differences
24 | Bot | Archway House has a food festival and a 37% discount for the next 4 days. It has a gym, pool, and DJ floor. It has been recognized by popular magazines and tour agencies and has hosted celebrities like Tom Holland and Jackie Chan. The head chef has a cookbook named Red Tomato. | Provide_differences
25 | User | Can you tell me more about Archway House? | Selection
26 | Bot | Archway House is a luxurious 4-star guesthouse with spacious rooms, a gym, pool, and DJ floor. It has been recognized by popular magazines and tour agencies and has hosted celebrities like Tom Holland and Jackie Chan. The head chef has a cookbook named Red Tomato. It is fully safe, sanitary, and secure. | Selection
27 | User | That sounds great, but it's still a bit over my budget. Can you offer a better price? | Negotiation
28 | Bot | I can offer a 10% discount, but some facilities like the DJ floor might not be available. Would you like to proceed with the booking? | Provide_negotiation
29 | User | Let me think about it. Can you suggest some other options? | Ask_alternatives
30 | Bot | I'm sorry, but those are all the options I have for your criteria. Would you like to book one of the options we discussed earlier? | Ask_alternatives
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, here are three options: Rosa's Bed and Breakfast, The Bridge Guest House, and Aylesbray Lodge Guest House. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between them? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse with luxurious rooms, a gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, a gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | How much does each option cost? | Add_aspect_price
10 | Bot | Rosa's Bed and Breakfast is currently offering a 33% discount, with double rooms priced at £100, family rooms at £150, and single rooms at £75. The Bridge Guest House has double rooms at £75, family rooms at £90, and single rooms at £50. Aylesbray Lodge Guest House is currently offering a 30% discount, with double rooms priced at £105, family rooms at £135, and single rooms at £80. | Provide_differences
11 | User | Can you suggest more options? | Ask_alternatives
12 | Bot | Sure, how about The Lensfield Hotel? It's a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. | Multioption_suggestion
13 | User | How much does it cost? | Add_aspect_price
14 | Bot | The Lensfield Hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It's currently offering a 30% discount for the next 3 days. | Provide_differences
15 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
16 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. The hotel offers spacious and luxurious rooms with great food, gym, pool, bar, and BBQ grill. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. | Provide_details
17 | User | Can I negotiate the price? | Negotiation
18 | Bot | Sure, we can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Which facilities are you willing to compromise on? | Provide_negotiation
19 | User | Can I get a higher priced option for the price of the cheaper option? | Negotiation
20 | Bot | I'm sorry, but the prices are fixed. However, I can assure you that Rosa's Bed and Breakfast is worth the price. | Provide_negotiation
21 | User | Can you tell me more about Aylesbray Lodge Guest House? | Selection
22 | Bot | Aylesbray Lodge Guest House is a 4-star hotel located in South with free internet and parking. The hotel offers moderate prices for single, double, and family rooms. It has excellent 24/7 room service, free breakfast, and free wifi. The hotel features a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms that are fully safe, sanitary, and secure. Aylesbray Lodge Guest House has been recognized by famous magazines, tour agencies, and critics. It has hosted celebrities like Ronaldo, Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named Dine with Me. The hotel is currently offering a 30% discount on bookings for the next 2 days, with only 2 rooms left. It is popular with locals, tour agencies, and has a huge social media presence with an 8/10 rating. | Provide_details
23 | User | Can I negotiate the price for Aylesbray Lodge Guest House? | Negotiation
24 | Bot | Yes, we can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Which facilities are you willing to compromise on? | Provide_negotiation
25 | User | Can you tell me more about The Lensfield Hotel? | Selection
26 | Bot | The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel has received recognitions such as appearing in local magazines like FoodVilla and Food and Beyond, being endorsed by local tour agencies TourMe, and receiving local awards such as Food Fest, Budget, and Great and Escape. | Provide_details
27 | User | Can I negotiate the price for The Lensfield Hotel? | Negotiation
28 | Bot | Yes, we can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Which facilities are you willing to compromise on? | Provide_negotiation
29 | User | Can you tell me more about The Bridge Guest House? | Selection
30 | Bot | The Bridge Guest House is a 3-star guesthouse located in the south area of Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also provides parking and internet facilities. The hotel has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. The hotel offers moderate pricing with double rooms at £75, family rooms at £90, and single rooms at £50. | Provide_details
31 | User | I'm still not sure which one to choose. Can you give me some time to think? | Affirm
32 | Bot | Of course, take your time. Let me know if you have any other questions. | Affirm
33 | User | Can you tell me more about the discounts for each hotel? | Add_aspect_discount
34 | Bot | Rosa's Bed and Breakfast is currently offering a 33% discount for the next 4 days. Aylesbray Lodge Guest House is currently offering a 30% discount for the next 2 days, with only 2 rooms left. The Lensfield Hotel is currently offering a 30% discount for the next 3 days. | Provide_details
35 | User | Can you tell me more about the facilities at each hotel? | Add_aspect_facilities
36 | Bot | Rosa's Bed and Breakfast has a gym, pool, bar, and BBQ grill. The Bridge Guest House provides parking and internet facilities. Aylesbray Lodge Guest House has a gym, pool, bar, and BBQ grill. The Lensfield Hotel has a safe and offers parking and internet. | Provide_details
37 | User | Can you tell me more about the recognitions and awards for each hotel? | Add_aspect_awards
38 | Bot | Rosa's Bed and Breakfast has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The Bridge Guest House has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. Aylesbray Lodge Guest House has been recognized by famous magazines, tour agencies, and critics. It has hosted celebrities like Ronaldo, Virat Kholi, Eminem, and Jackie Chan. The Lensfield Hotel has received recognitions such as appearing in local magazines like FoodVilla and Food and Beyond, being endorsed by local tour agencies TourMe, and receiving local awards such as Food Fest, Budget, and Great and Escape. | Provide_details
39 | User | Can you tell me more about the rooms at each hotel? | Add_aspect_rooms
40 | Bot | Rosa's Bed and Breakfast offers spacious and luxurious rooms. The Bridge Guest House has very clean rooms. Aylesbray Lodge Guest House has spacious and luxurious rooms that are fully safe, sanitary, and secure. The Lensfield Hotel has very clean rooms. | Provide_details
41 | User | Can you tell me more about the food at each hotel? | Add_aspect_food
42 | Bot | Rosa's Bed and Breakfast has great food. The Bridge Guest House has delicious food. Aylesbray Lodge Guest House has a head chef with a cookbook named Dine with Me. The Lensfield Hotel has friendly staff and delicious food. | Provide_details
43 | User | I've decided to go with Aylesbray Lodge Guest House. | Selection
44 | Bot | Great choice! The hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and phone number for the booking. | Confirmation
45 | User | My name is John Smith, my email is johnsmith@email.com, and my phone number is 123-456-7890. | Inform
46 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation
47 | User | No, that's all. Thank you for your help. | Goodbye
48 | Bot | You're welcome, John. Have a great day! | Goodbye
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have 3 options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive but has luxurious rooms, a gym, and a pool. The A and B Guest House has a BBQ grill and Jacuzzi. Allenbell guesthouse is affordable and has a bar. | Provide_differences |
| 9 | User | Can you suggest more options? | Ask_alternatives |
| 10 | Bot | Sure, I have two more options for you. The first is Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. The second is Autumn House, a 4-star guesthouse with a 37% discount on bookings for the next 2 days and free dinner. | Multioption_suggestion |
| 11 | User | What are the differences between Carolina Bed and Breakfast and Autumn House? | Ask_differences |
| 12 | Bot | Carolina Bed and Breakfast has a pool, BBQ grill, and Jacuzzi. Autumn House has a DJ floor and fully safe, sanitary, and secure rooms. | Provide_differences |
| 13 | User | I'm interested in Leverton House, but it's over my budget. Can you offer a lower price? | Negotiation |
| 14 | Bot | I can offer a 10% discount, but some facilities like the gym and pool might not be available. | Provide_negotiation |
| 15 | User | Okay, I'll take the offer. | Affirm, Selection |
| 16 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details |
| 17 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform |
| 18 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye |
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have three options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive option, but it offers a gym and a pool. The A and B Guest House has a BBQ grill and a Jacuzzi. Allenbell guesthouse has a bar and spacious luxurious rooms. | Provide_differences |
| 9 | User | Can you give me more options? | Ask_alternatives |
| 10 | Bot | Sure, I have two more options for you. The first is Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. The second is Autumn House, a 4-star guesthouse with a 37% discount on bookings for the next 2 days and free dinner. | Multioption_suggestion |
| 11 | User | What are the differences between Carolina Bed and Breakfast and Autumn House? | Ask_differences |
| 12 | Bot | Carolina Bed and Breakfast has a pool, bar, BBQ grill, and Jacuzzi. Autumn House has a DJ floor and fully safe, sanitary, and secure rooms. | Provide_differences |
| 13 | User | I'm interested in Leverton House, but it's a bit over my budget. Can you offer a lower price? | Negotiation |
| 14 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation |
| 15 | User | Can you remove the gym and pool facilities? | Negotiation |
| 16 | Bot | Sure, I can remove those facilities and offer you a 10% discount. | Provide_negotiation |
| 17 | User | Okay, I'll take the offer. | Selection |
| 18 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation |
| 19 | User | My name is John Smith, my email is johnsmith@gmail.com, there will be two people, and we prefer a double room. | Inform |
| 20 | Bot | Thank you, John. Your booking is confirmed. You can contact us at 123-456-7890 for any further queries. | Confirmation |
| 21 | User | Can I get a receipt for my booking? | Add_aspect_X |
| 22 | Bot | Sure, I'll email you the receipt. Is there anything else I can help you with? | Ask_details |
| 23 | User | No, that's all. Thank you. | Goodbye |
| 24 | Bot | You're welcome. Have a great day! | Goodbye |
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_differences
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Add_aspect_X
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_differences
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_differences
13 | User | I'm interested in the Huntingdon Marriott Hotel, but it's a bit expensive. Can you offer a lower price? | Negotiation
14 | Bot | I can offer a 10% discount, but some facilities like the DJ floor and free dinner may not be available. Would you still like to book the Huntingdon Marriott Hotel? | Provide_negotiation
15 | User | Hmm, can you suggest any other options? | Ask_alternatives
16 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Multioption_suggestion
17 | User | Can you tell me more about Finches Bed and Breakfast? | Add_aspect_X
18 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_differences
19 | User | That sounds great, but what's the price? | Add_aspect_X
20 | Bot | Finches Bed and Breakfast offers double rooms for £120, single rooms for £90, and family rooms for £150. | Provide_differences
21 | User | Can you offer a lower price for Finches Bed and Breakfast? | Negotiation
22 | Bot | I can offer a 5% discount, but some facilities like the BBQ grill and Jacuzzi may not be available. Would you like to book Finches Bed and Breakfast? | Provide_negotiation
23 | User | Let me think about it for a bit. | Selection
24 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
25 | User | Can you tell me more about the Huntingdon Marriott Hotel's food festival? | Add_aspect_X
26 | Bot | The Huntingdon Marriott Hotel is currently running a food festival with free dinner for guests. The festival features a variety of cuisines and is a great opportunity to try new dishes. | Provide_differences
27 | User | Can I book the Huntingdon Marriott Hotel with the 10% discount? | Selection
28 | Bot | Absolutely, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference for the final booking. | Confirmation, Ask_details
29 | User | My name is John Smith, my email is johnsmith@email.com, there will be 2 people, and we prefer a double room. | Inform
30 | Bot | Great, your booking has been confirmed. You will receive a confirmation email shortly with all the details. Thank you for choosing our service. | Confirmation, Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The first is Rosa's Bed and Breakfast, a 4-star guesthouse with a 33% discount for the next 4 days. The second is The Bridge Guest House, a 3-star guesthouse with moderate pricing. The third is Aylesbray Lodge Guest House, a 4-star hotel with a 30% discount for the next 2 days. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
10 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you negotiate the price? | Negotiation
12 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
13 | User | Can you remove the gym and pool facilities? | Negotiation
14 | Bot | Sure, I can remove the gym and pool facilities. The new price for Rosa's Bed and Breakfast will be £95 per night. | Provide_negotiation
15 | User | That's still a bit over my budget. Can you suggest another option? | Ask_alternatives
16 | Bot | Sure, I have one more option for you. The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Multioption_suggestion
17 | User | What are the differences between the Lensfield Hotel and the Bridge Guest House? | Ask_differences
18 | Bot | The Lensfield Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The Bridge Guest House is a 3-star guesthouse with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. | Provide_differences
19 | User | Can you tell me more about the Lensfield Hotel? | Selection
20 | Bot | The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Selection
21 | User | Can you negotiate the price for the Lensfield Hotel? | Negotiation
22 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Which facilities would you like to remove? | Provide_negotiation
23 | User | Can you remove the parking facility? | Negotiation
24 | Bot | Sure, I can remove the parking facility. The new price for the Lensfield Hotel will be £81 per night. | Provide_negotiation
25 | User | That sounds good. I'll go with the Lensfield Hotel. | Selection
26 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation, Ask_details
27 | User | My name is John Smith, my email is johnsmith@gmail.com, and there will be two people staying in the room. We prefer a double room. | Inform
28 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation, Goodbye
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have 3 options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive but has luxurious rooms, a gym, and a pool. The A and B Guest House has a BBQ grill and Jacuzzi. Allenbell guesthouse is affordable and has a bar. | Provide_differences |
| 9 | User | Can you suggest more options? | Ask_alternatives |
| 10 | Bot | Sure, I have two more options for you. The first is Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. The second is Autumn House, a 4-star guesthouse with a 37% discount on bookings for the next 2 days and free dinner. | Multioption_suggestion |
| 11 | User | What are the differences between Carolina Bed and Breakfast and Autumn House? | Ask_differences |
| 12 | Bot | Carolina Bed and Breakfast has a pool, BBQ grill, and Jacuzzi. Autumn House has a DJ floor and fully safe, sanitary, and secure rooms. | Provide_differences |
| 13 | User | I'm interested in Leverton House, but it's over my budget. Can you offer a lower price? | Negotiation |
| 14 | Bot | I can offer a 10% discount, but some facilities like the gym and pool might not be available. | Provide_negotiation |
| 15 | User | Okay, I'll take the offer. | Affirm, Selection |
| 16 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details |
| 17 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform |
| 18 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye |
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have 3 options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive but has luxurious rooms, a gym, and a pool. The A and B Guest House has a BBQ grill and Jacuzzi. Allenbell guesthouse is affordable and has a bar. | Provide_differences |
| 9 | User | Can you suggest more options? | Ask_alternatives |
| 10 | Bot | Sure, I have two more options for you. The first is Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. The second is Autumn House, a 4-star guesthouse with a 37% discount on bookings for the next 2 days and free dinner. | Multioption_suggestion |
| 11 | User | What are the differences between Carolina Bed and Breakfast and Autumn House? | Ask_differences |
| 12 | Bot | Carolina Bed and Breakfast has a pool, BBQ grill, and Jacuzzi. Autumn House has a DJ floor and fully safe, sanitary, and secure rooms. | Provide_differences |
| 13 | User | I'm interested in Leverton House, but it's over my budget. Can you offer a lower price? | Negotiation |
| 14 | Bot | I can offer a 10% discount, but some facilities like the gym and pool might not be available. | Provide_negotiation |
| 15 | User | Okay, I'll take the offer. | Affirm, Selection |
| 16 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details |
| 17 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform |
| 18 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye |
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_differences
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Add_aspect_X
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_differences
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_differences
13 | User | I'm interested in the Huntingdon Marriott Hotel, but it's a bit expensive. Can you offer a lower price? | Negotiation
14 | Bot | I can offer a 10% discount, but some facilities like the DJ floor and free dinner may not be available. Would you still like to book the Huntingdon Marriott Hotel? | Provide_negotiation
15 | User | Hmm, can you suggest any other options? | Ask_alternatives
16 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Multioption_suggestion
17 | User | Can you tell me more about Finches Bed and Breakfast? | Add_aspect_X
18 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_differences
19 | User | That sounds great, but what's the price? | Add_aspect_X
20 | Bot | Finches Bed and Breakfast offers double rooms for £120, single rooms for £90, and family rooms for £150. | Provide_differences
21 | User | Can you offer a lower price for Finches Bed and Breakfast? | Negotiation
22 | Bot | I can offer a 5% discount, but some facilities like the BBQ grill and Jacuzzi may not be available. Would you like to book Finches Bed and Breakfast? | Provide_negotiation
23 | User | Let me think about it for a bit. | Selection
24 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
25 | User | Can you tell me more about the Huntingdon Marriott Hotel's food festival? | Add_aspect_X
26 | Bot | The Huntingdon Marriott Hotel is currently running a food festival with free dinner for guests. The festival features a variety of cuisines and is a great opportunity to try new dishes. | Provide_differences
27 | User | That sounds really tempting. Can you offer a higher discount for the Huntingdon Marriott Hotel? | Negotiation
28 | Bot | I'm sorry, but I can only offer a 10% discount. Would you like to book the Huntingdon Marriott Hotel? | Provide_negotiation
29 | User | I think I'll go with Finches Bed and Breakfast. | Selection
30 | Bot | Great choice! The hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for the booking. | Confirmation
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, here are three options: Rosa's Bed and Breakfast, The Bridge Guest House, and Aylesbray Lodge Guest House. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between them? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse with luxurious rooms, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | How much does each option cost? | Add_aspect_price
10 | Bot | Rosa's Bed and Breakfast is currently offering a 33% discount, with double rooms priced at £100, family rooms at £150, and single rooms at £75. The Bridge Guest House has double rooms at £75, family rooms at £90, and single rooms at £50. Aylesbray Lodge Guest House is currently offering a 30% discount, with double rooms priced at £105, family rooms at £135, and single rooms at £80. | Provide_differences
11 | User | Can you suggest more options? | Ask_alternatives
12 | Bot | Sure, how about The Lensfield Hotel? It's a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. | Multioption_suggestion
13 | User | How much does it cost? | Add_aspect_price
14 | Bot | The Lensfield Hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. | Provide_differences
15 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
16 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. The hotel offers spacious and luxurious rooms with great food, gym, pool, bar, and BBQ grill. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. | Provide_details
17 | User | Can I negotiate the price? | Negotiation
18 | Bot | We can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
19 | User | Can I get a higher priced option for the price of the cheaper option? | Negotiation
20 | Bot | I'm sorry, but the prices are fixed. However, I can assure you that Rosa's Bed and Breakfast is worth the price. | Provide_negotiation
21 | User | Can you tell me more about Aylesbray Lodge Guest House? | Selection
22 | Bot | Aylesbray Lodge Guest House is a 4-star hotel located in South with free internet and parking. The hotel offers moderate prices for single, double, and family rooms. It has excellent 24/7 room service, free breakfast, and free wifi. The hotel features a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms that are fully safe, sanitary, and secure. Aylesbray Lodge Guest House has been recognized by famous magazines, tour agencies, and critics. It has hosted celebrities like Ronaldo, Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named Dine with Me. The hotel is currently offering a 30% discount on bookings for the next 2 days, with only 2 rooms left. It is popular with locals, tour agencies, and has a huge social media presence with an 8/10 rating. | Provide_details
23 | User | Can I negotiate the price for Aylesbray Lodge Guest House? | Negotiation
24 | Bot | We can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
25 | User | Can you suggest more options? | Ask_alternatives
26 | Bot | Sure, I can suggest The Bridge Guest House. It's a 3-star guesthouse located in the south area of Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also provides parking and internet facilities. The hotel has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. The hotel offers moderate pricing with double rooms at £75, family rooms at £90, and single rooms at £50. | Multioption_suggestion
27 | User | Can you tell me more about The Bridge Guest House? | Selection
28 | Bot | The Bridge Guest House is a 3-star guesthouse located in the south area of Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also provides parking and internet facilities. The hotel has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. | Provide_details
29 | User | I'm still not sure which one to choose. Can you give me some time to decide? | Affirm
30 | Bot | Of course, take your time. Let me know if you have any other questions. | Affirm
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with a pool, gym, and spacious rooms. The Alexander Bed and Breakfast is a 4-star guesthouse with a gym, pool, bar, and BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Selection
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Provide_details
9 | User | Can you suggest a cheaper option? | Ask_alternatives
10 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Which one would you like to know more about? | Multioption_suggestion
11 | User | What are the differences between the cheaper options? | Ask_differences
12 | Bot | Cityroomz is a moderate hotel with affordable prices for single, double, and family rooms. It has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse with a 0-star rating and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
13 | User | Can you tell me more about the University Arms Hotel? | Selection
14 | Bot | The University Arms Hotel is a luxurious 4-star hotel located in the centre of Regent Street. It offers free breakfast, 24/7 room service, free wifi, a gym, a pool, and spacious rooms. The hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_details
15 | User | Can you negotiate the price of the University Arms Hotel? | Negotiation
16 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. The University Arms Hotel is a luxurious 4-star hotel with a pool, gym, and spacious rooms. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_negotiation
17 | User | Can you suggest more options with a gym? | Add_aspect_gym
18 | Bot | Sure, The Gonville Hotel and Alexander Bed and Breakfast both have a gym. Which one would you like to know more about? | Multioption_suggestion
19 | User | What are the differences between the options with a gym? | Ask_differences
20 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. It also has friendly staff, delicious food, and very clean rooms. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. The Alexander Bed and Breakfast is a 4-star guesthouse with a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_differences
21 | User | Can you suggest a cheaper option with a gym? | Ask_alternatives
22 | Bot | Sure, Cityroomz and El Shaddai both have a gym. Which one would you like to know more about? | Multioption_suggestion
23 | User | What are the differences between the cheaper options with a gym? | Ask_differences
24 | Bot | Cityroomz is a moderate hotel with affordable prices for single, double, and family rooms. It has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse with a 0-star rating and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
25 | User | Can you suggest more options with a pool? | Add_aspect_pool
26 | Bot | Sure, The University Arms Hotel and Alexander Bed and Breakfast both have a pool. Which one would you like to know more about? | Multioption_suggestion
27 | User | What are the differences between the options with a pool? | Ask_differences
28 | Bot | The University Arms Hotel is a luxurious 4-star hotel with a pool, gym, and spacious rooms. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. The Alexander Bed and Breakfast is a 4-star guesthouse with a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_differences
29 | User | Can you suggest a cheaper option with a pool? | Ask_alternatives
30 | Bot | Sorry, there are no cheaper options with a pool. Would you like to select one of the options provided? | Selection
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_details
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Ask_alternatives
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_details
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_details
13 | User | Can you tell me more about the Huntingdon Marriott Hotel's food festival? | Add_aspect_X
14 | Bot | The Huntingdon Marriott Hotel is currently running a food festival with free dinner for guests. | Provide_details
15 | User | I'm interested in the Cambridge Belfry, but it's a bit expensive. Can you offer a lower price? | Negotiation
16 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
17 | User | Can you remove the jacuzzi? | Negotiation
18 | Bot | Sure, I can remove the jacuzzi. The new price will be £135 per night. | Provide_negotiation
19 | User | That's still a bit high. Can you offer a lower price? | Negotiation
20 | Bot | I'm sorry, but £135 is the best I can do. | Provide_negotiation
21 | User | Alright, I'll take it. | Selection
22 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details
23 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
24 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Confirmation
25 | User | Actually, can you tell me more about the Finches Bed and Breakfast? | Ask_alternatives
26 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_details
27 | User | That sounds great, but how much does it cost? | Add_aspect_X
28 | Bot | Finches Bed and Breakfast offers double rooms for £120, single rooms for £90, and family rooms for £150. | Provide_details
29 | User | Can you tell me more about the Huntingdon Marriott Hotel's Michelin Star? | Add_aspect_X
30 | Bot | The Michelin Star is a prestigious award given to restaurants with exceptional quality. The Huntingdon Marriott Hotel has received this award for its excellent food and service. | Provide_details
31 | User | I'm still deciding between the Cambridge Belfry and Finches Bed and Breakfast. Can you give me a moment? | Selection
32 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the centre of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan on staying? | Ask_details
3 | User | I'll be there next week. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, The University Arms Hotel, and The Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between them? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, 24/7 room service, free wifi, a gym, a pool, and spacious rooms. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. | Provide_differences
7 | User | How much does each one cost? | Add_aspect_price
8 | Bot | The Gonville Hotel ranges from £79 for a single room to £119 for a family room. The University Arms Hotel is more expensive, with prices starting at £150 for a single room and going up to £300 for a family room. The Alexander Bed and Breakfast ranges from £100 for a single room to £200 for a family room. | Provide_differences
9 | User | That's quite expensive. Do you have any cheaper options? | Ask_alternatives
10 | Bot | Sure, I have two more options for you. Cityroomz and El Shaddai. Cityroomz offers affordable prices for single, double, and family rooms, with a discount of 34% for the next 4 days. El Shaddai is a cheap guesthouse with rooms starting at £40 for a single and £60 for a double. | Multioption_suggestion
11 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
12 | Bot | Cityroomz has internet access and affordable prices, but no parking. El Shaddai offers internet and parking facilities, but has a 0-star rating. | Provide_differences
13 | User | I think I'll go with The Alexander Bed and Breakfast. | Selection
14 | Bot | Great choice! The Alexander Bed and Breakfast it is. How many people will be staying? | Ask_details
15 | User | There will be two of us. | Inform
16 | Bot | Okay, would you like a double room or a family room? | Ask_details
17 | User | A double room will be fine. | Inform
18 | Bot | Alright, your total for a double room at The Alexander Bed and Breakfast will be £100 per night. Is that within your budget? | Ask_details
19 | User | That's a bit over my budget. Can you offer a lower price? | Negotiation
20 | Bot | I can offer you a 10% discount, bringing the price down to £90 per night. However, some facilities such as the gym and pool may not be available. Would you like to proceed with the booking? | Provide_negotiation
21 | User | Okay, I'll take it. | Affirm, Selection
22 | Bot | Great! Your booking has been confirmed. Your registration number is 123456. Please note that check-in time is at 2 PM and check-out time is at 12 PM. Is there anything else I can help you with? | Confirmation
23 | User | Can you recommend any good restaurants nearby? | Add_aspect_food
24 | Bot | Sure, there's The Cambridge Chop House, The Pint Shop, and The Eagle. All of them are within walking distance from your hotel. | Multioption_suggestion
25 | User | What type of cuisine do they serve? | Ask_details
26 | Bot | The Cambridge Chop House serves British cuisine, The Pint Shop serves pub food, and The Eagle serves international cuisine. | Provide_differences
27 | User | I think I'll go with The Cambridge Chop House. | Selection
28 | Bot | Great choice! Would you like me to make a reservation for you? | Ask_details
29 | User | Yes, please. For two people at 7 PM. | Inform
30 | Bot | Alright, your reservation has been made. Is there anything else I can help you with? | Confirmation
31 | User | No, that's all. Thank you for your help. | Goodbye
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have 3 options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive but has luxurious rooms, a gym, and a pool. The A and B Guest House has a BBQ grill and Jacuzzi. Allenbell guesthouse is affordable and has a bar. | Provide_differences |
| 9 | User | Can you suggest more options? | Ask_alternatives |
| 10 | Bot | Sure, I have two more options for you. The first is Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. The second is Autumn House, a 4-star guesthouse with a 37% discount on bookings for the next 2 days and free dinner. | Multioption_suggestion |
| 11 | User | What are the differences between Carolina Bed and Breakfast and Autumn House? | Ask_differences |
| 12 | Bot | Carolina Bed and Breakfast has a pool, BBQ grill, and Jacuzzi. Autumn House has a DJ floor and fully safe, sanitary, and secure rooms. | Provide_differences |
| 13 | User | I'm interested in Leverton House, but it's over my budget. Can you offer a lower price? | Negotiation |
| 14 | Bot | I can offer a 10% discount, but some facilities like the gym and pool might not be available. | Provide_negotiation |
| 15 | User | Okay, I'll take the offer. | Affirm, Selection |
| 16 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details |
| 17 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform |
| 18 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye |
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, and a pool. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Add_aspect_X
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. It has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Add_aspect_X
9 | User | That sounds good. Can you tell me more about the University Arms Hotel? | Add_aspect_X
10 | Bot | The University Arms Hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Add_aspect_X
11 | User | That sounds great. Can you tell me more about the Alexander Bed and Breakfast? | Add_aspect_X
12 | Bot | The Alexander Bed and Breakfast is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Add_aspect_X
13 | User | I think I'll go with the University Arms Hotel. | Selection
14 | Bot | Great choice! The University Arms Hotel is a luxurious 4-star hotel located in the centre of Regent Street. It offers free breakfast, 24/7 room service, free wifi, a gym, a pool, and spacious rooms. The hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. The price for your stay will be £357. | Provide_negotiation
15 | User | That's a bit expensive. Can you lower the price? | Negotiation
16 | Bot | I can offer you a 10% discount, bringing the price down to £321.30. However, some facilities like the pool and gym may not be available. | Provide_negotiation
17 | User | Okay, I'll take it. | Affirm
18 | Bot | Great! The hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for the booking. | Confirmation
19 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 0123456789. | Inform
20 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | Okay, I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a moderate price range and a 31% discount for the next 2 days. The third is Lovell Lodge, a 2-star hotel with a moderate price range and only 4 rooms left. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Kirkwood House is a 4-star guesthouse with a gym, pool, bar, BBQ grill, and Jacuzzi. Home from Home is also a 4-star guesthouse with a gym, pool, and bar. Lovell Lodge is a 2-star hotel with free breakfast and wifi. | Provide_differences
9 | User | Can you tell me more about Kirkwood House? | Selection
10 | Bot | Kirkwood House is a luxurious guesthouse with spacious rooms and has been recognized by famous magazines and tour agencies. It has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. It is currently offering a 36% discount on bookings for the next 3 days. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you offer a better price? | Negotiation
12 | Bot | I can offer a 10% discount, but some facilities like the BBQ grill and Jacuzzi might not be available. Would you like to proceed with the booking? | Provide_negotiation
13 | User | Hmm, let me think about it. Can you suggest some other options? | Ask_alternatives
14 | Bot | Sure, I have two more options for you. The Limehouse guesthouse is a 4-star hotel with a food festival and great food. The Acorn Guest House is also a 4-star guesthouse with a gym and pool. Which one would you like to know more about? | Multioption_suggestion
15 | User | What are the prices for these options? | Ask_details
16 | Bot | The Limehouse guesthouse has a moderate price range with double rooms at £85, family rooms at £120, and single rooms at £65. The Acorn Guest House has a moderate to high price range with double rooms at £110, family rooms at £150, and single rooms at £90. | Provide_differences
17 | User | Can you tell me more about The Limehouse guesthouse? | Selection
18 | Bot | The Limehouse guesthouse is a 4-star hotel with a food festival and great food. It has spacious and luxurious rooms, a gym, a pool, and a DJ floor. It has received prestigious awards such as Michelin Star and The Gold List and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. | Selection
19 | User | That sounds good. Can you offer a discount? | Negotiation
20 | Bot | I can offer a 5% discount, but some facilities like the food festival might not be available. Would you like to proceed with the booking? | Provide_negotiation
21 | User | Let me think about it. Can you suggest some more options? | Ask_alternatives
22 | Bot | Sure, I have one more option for you. Archway House is a 4-star guesthouse with a food festival and 37% off on bookings for the next 4 days. It has spacious and luxurious rooms, a gym, a pool, and a DJ floor. It has been recognized by popular magazines and tour agencies and has hosted celebrities like Tom Holland and Jackie Chan. Which one would you like to know more about? | Multioption_suggestion
23 | User | What are the prices for Archway House? | Ask_details
24 | Bot | Archway House has a moderate to high price range with double rooms at £95, family rooms at £130, and single rooms at £75. | Provide_differences
25 | User | Can you tell me more about Archway House? | Selection
26 | Bot | Archway House is a 4-star guesthouse with a food festival and 37% off on bookings for the next 4 days. It has spacious and luxurious rooms, a gym, a pool, and a DJ floor. It has been recognized by popular magazines and tour agencies and has hosted celebrities like Tom Holland and Jackie Chan. | Selection
27 | User | That sounds good. Can you offer a discount? | Negotiation
28 | Bot | I can offer a 5% discount, but some facilities like the food festival might not be available. Would you like to proceed with the booking? | Provide_negotiation
29 | User | Let me think about it. Can you tell me more about Home from Home? | Selection
30 | Bot | Home from Home is a 4-star guesthouse with a moderate price range and a 31% discount for the next 2 days. It has spacious and luxurious rooms, a gym, a pool, and a bar. It has been recognized by popular magazines and tour agencies and has hosted celebrities like Ronaldo, Virat Kholi, and Tom Holland. | Selection
31 | User | That sounds good. Can you offer a discount? | Negotiation
32 | Bot | I can offer a 5% discount, but some facilities like the bar might not be available. Would you like to proceed with the booking? | Provide_negotiation
33 | User | Let me think about it. Can you suggest some more options? | Ask_alternatives
34 | Bot | I'm sorry, but those are all the options I have for your criteria. Would you like to book any of the options we discussed? | Ask_alternatives
35 | User | I'm still not sure. Can you tell me more about the facilities at Kirkwood House? | Add_aspect_X
36 | Bot | Kirkwood House has a gym, pool, bar, BBQ grill, and Jacuzzi. It also offers free breakfast, 24/7 room service, and free wifi. | Add_aspect_X
37 | User | That sounds really good. Can you offer a better discount? | Negotiation
38 | Bot | I'm sorry, but the discount is already at 36%. I can offer a complimentary bottle of wine with your booking. Would you like to proceed with the booking? | Provide_negotiation
39 | User | Okay, I'll book Kirkwood House. | Selection
40 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for the booking. | Confirmation, Ask_details
41 | User | My name is John Smith, my email is johnsmith@email.com, and my contact number is 1234567890. | Inform
42 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation
43 | User | No, that's all. Thank you. | Goodbye
44 | Bot | You're welcome. Have a great day! | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is also a 4-star hotel with a food festival and DJ floor. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a luxurious hotel with spacious rooms, free breakfast, and 24/7 room service. It has received prestigious awards and has hosted celebrities like Virat Kholi and Eminem. | Provide_differences
9 | User | What about the Huntingdon Marriott Hotel? | Add_aspect_X
10 | Bot | The Huntingdon Marriott Hotel is a luxurious hotel with excellent 24/7 room service, a food festival, and a DJ floor. It has received prestigious awards and has hosted celebrities like Virat Kholi and Tom Holland. | Provide_differences
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a guesthouse with clean rooms, friendly staff, and a 32% discount. It offers free breakfast and 24/7 room service. | Provide_differences
13 | User | I'm interested in the Huntingdon Marriott Hotel. Can you negotiate the price? | Negotiation
14 | Bot | I can offer a 10% discount, but some facilities might get removed. | Provide_negotiation
15 | User | Can you remove the DJ floor? | Negotiation
16 | Bot | Sure, I can remove the DJ floor. The new price is £270. | Provide_negotiation
17 | User | That's still a bit high. Can you offer a better price? | Negotiation
18 | Bot | I can offer a 15% discount, but the food festival will be removed. | Provide_negotiation
19 | User | Alright, I'll take it. | Selection
20 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and number of people. | Confirmation, Ask_details
21 | User | My name is John Smith, email is johnsmith@gmail.com, and there will be 2 people. | Inform
22 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Confirmation
23 | User | Can you suggest more options? | Ask_alternatives
24 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse with great facilities. | Multioption_suggestion
25 | User | Can you tell me more about it? | Add_aspect_X
26 | Bot | Finches Bed and Breakfast is a luxurious guesthouse with spacious rooms, free breakfast, and 24/7 room service. It has a gym, pool, bar, BBQ grill, and Jacuzzi. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi and Eminem. | Provide_differences
27 | User | What's the price range? | Add_aspect_X
28 | Bot | The double rooms are £120, single rooms are £90, and family rooms are £180. | Add_aspect_X
29 | User | That's a bit expensive. Can you suggest something cheaper? | Ask_alternatives
30 | Bot | How about Hobsons House? It's a 3-star guesthouse with a 32% discount and free dinner. | Multioption_suggestion
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about The Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_differences
9 | User | That sounds great, but it's a bit expensive. Can you suggest a cheaper option? | Ask_alternatives
10 | Bot | Sure, how about Hobsons House? It's a 3-star guesthouse with a 32% discount and free dinner. | Multioption_suggestion
11 | User | What are the differences between The Cambridge Belfry and Hobsons House? | Ask_differences
12 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. Hobsons House is a 3-star guesthouse with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. | Provide_differences
13 | User | Can I negotiate the price for The Cambridge Belfry? | Negotiation
14 | Bot | We can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
15 | User | Can I get The Cambridge Belfry for the price of Hobsons House? | Negotiation
16 | Bot | I'm sorry, but that's not possible. The Cambridge Belfry is a luxurious 4-star hotel with many facilities and amenities. | Provide_negotiation
17 | User | Okay, I'll go with Hobsons House. Can you tell me more about it? | Selection, Add_aspect_X
18 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_differences
19 | User | Can I get a family room for £100? | Negotiation
20 | Bot | I'm sorry, but the price is fixed. However, I can offer you a complimentary bottle of wine with your booking. | Provide_negotiation
21 | User | Okay, I'll take it. | Affirm
22 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details
23 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
24 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye
25 | User | Actually, can you suggest another hotel with a pool? | Ask_alternatives
26 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Multioption_suggestion
27 | User | Can you tell me more about Finches Bed and Breakfast? | Add_aspect_X
28 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_differences
29 | User | That sounds great, but it's a bit expensive. Can you suggest a cheaper option? | Ask_alternatives
30 | Bot | How about Hobsons House? It's a 3-star guesthouse with a 32% discount and free dinner. | Multioption_suggestion
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a 31% discount for the next 2 days and free dinner. The third is Lovell Lodge, a 2-star hotel with a moderate price range. Which one would you like to know more about? | Multioption_suggestion
7 | User | Can you tell me more about Kirkwood House? | Ask_differences
8 | Bot | Kirkwood House is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, BBQ grill, and Jacuzzi. It has spacious and luxurious rooms and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies and has received prestigious awards such as the Michelin Star. It has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. | Provide_differences
9 | User | What about Home from Home? | Ask_differences
10 | Bot | Home from Home is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and spacious luxurious rooms. It is fully safe, sanitary, and secure. It has been recognized by popular magazines and tour agencies and has hosted celebrities such as Ronaldo, Virat Kholi, and Tom Holland. It offers a moderate price range with double rooms at £75, family rooms at £105, and single rooms at £50. | Provide_differences
11 | User | And Lovell Lodge? | Ask_differences
12 | Bot | Lovell Lodge is a 2-star hotel with free breakfast, free wifi, and good room service. It has parking and internet facilities and takes bookings. The price range is moderate, with double rooms costing £65, family rooms £70, and single rooms £50. It has been endorsed by local tour agencies TourMe and has received local awards such as Food fest. | Provide_differences
13 | User | Can you suggest more options? | Ask_alternatives
14 | Bot | Sure, I have two more options for you. The first is Limehouse guesthouse, a 4-star hotel with free breakfast, 24/7 room service, free wifi, and great food. It has spacious and luxurious rooms, a gym, a pool, and a DJ floor. It has received prestigious awards such as Michelin Star and The Gold List and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. The second is Acorn Guest House, a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel has a gym and pool. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Ronaldo and Eminem. Which one would you like to know more about? | Multioption_suggestion
15 | User | Can you tell me more about Limehouse guesthouse? | Ask_differences
16 | Bot | Limehouse guesthouse is a 4-star hotel with free breakfast, 24/7 room service, free wifi, and great food. It has spacious and luxurious rooms, a gym, a pool, and a DJ floor. It has received prestigious awards such as Michelin Star and The Gold List and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. | Provide_differences
17 | User | And Acorn Guest House? | Ask_differences
18 | Bot | Acorn Guest House is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel has a gym and pool. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Ronaldo and Eminem. The head chef has a cookbook named "How to Burger." | Provide_differences
19 | User | Can you suggest more options? | Ask_alternatives
20 | Bot | I'm sorry, those are all the options available in the North area of Cambridge. Which one do you prefer? | Selection
21 | User | I'm interested in Kirkwood House, but the price is a bit high. Can you offer a discount? | Negotiation
22 | Bot | I'm sorry, but the price is already discounted by 36%. However, I can offer a 10% discount on the original price, but some facilities might get removed. | Provide_negotiation
23 | User | Can you remove the BBQ grill and Jacuzzi? | Negotiation
24 | Bot | Sure, I can remove those facilities and offer you a 10% discount on the original price. | Provide_negotiation
25 | User | Alright, I'll take it. | Affirm, Selection
26 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and contact number for the booking. | Confirmation, Ask_details
27 | User | My name is John Smith, my email is johnsmith@email.com, and my contact number is 1234567890. | Inform
28 | Bot | Thank you, John. Your booking has been confirmed. Is there anything else I can help you with? | Goodbye
29 | User | Actually, can you tell me more about the gym at Kirkwood House? | Add_aspect_X
30 | Bot | The gym at Kirkwood House is fully equipped with state-of-the-art machines and equipment. It is open 24/7 and is free for all guests. | Provide_differences
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_differences
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Add_aspect_X
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_differences
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_differences
13 | User | I'm interested in the Huntingdon Marriott Hotel, but it's a bit expensive. Can you offer a lower price? | Negotiation
14 | Bot | I can offer a 10% discount, but some facilities like the DJ floor and free dinner may not be available. Would you still like to book the Huntingdon Marriott Hotel? | Provide_negotiation
15 | User | Hmm, can you suggest any other options? | Ask_alternatives
16 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Multioption_suggestion
17 | User | Can you tell me more about Finches Bed and Breakfast? | Add_aspect_X
18 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_differences
19 | User | That sounds great, but what's the price? | Add_aspect_X
20 | Bot | Finches Bed and Breakfast offers double rooms for £120, single rooms for £90, and family rooms for £150. | Provide_differences
21 | User | Can you offer a lower price for Finches Bed and Breakfast? | Negotiation
22 | Bot | I can offer a 5% discount, but some facilities like the BBQ grill and Jacuzzi may not be available. Would you like to book Finches Bed and Breakfast? | Provide_negotiation
23 | User | Let me think about it for a bit. | Selection
24 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
25 | User | Can you tell me more about the gym at the Cambridge Belfry? | Add_aspect_X
26 | Bot | The gym at the Cambridge Belfry is fully equipped with modern machines and equipment. It's open 24/7 and is free for all guests. | Provide_differences
27 | User | What about the pool at the Huntingdon Marriott Hotel? | Add_aspect_X
28 | Bot | The pool at the Huntingdon Marriott Hotel is a heated indoor pool with a sauna and steam room. It's open from 6 am to 10 pm and is free for all guests. | Provide_differences
29 | User | Can you tell me more about the free breakfast at Hobsons House? | Add_aspect_X
30 | Bot | The free breakfast at Hobsons House includes a variety of options such as eggs, bacon, toast, cereal, and fruit. It's served from 7 am to 10 am and is free for all guests. | Provide_differences
31 | User | I think I've made a decision. I'd like to book the Huntingdon Marriott Hotel. | Selection
32 | Bot | Great choice! The hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and phone number for the booking. | Confirmation, Ask_details
33 | User | My name is John Smith, my email is johnsmith@email.com, and my phone number is 123-456-7890. | Inform
34 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation
35 | User | No, that's all. Thank you for your help. | Goodbye
36 | Bot | You're welcome, John. Have a great day! | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The first is Rosa's Bed and Breakfast, a 4-star guesthouse with a 33% discount for the next 4 days. The second is The Bridge Guest House, a 3-star guesthouse with moderate pricing. The third is Aylesbray Lodge Guest House, a 4-star hotel with a 30% discount for the next 2 days. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
10 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you negotiate the price? | Negotiation
12 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
13 | User | Can you remove the gym and pool facilities? | Negotiation
14 | Bot | Sure, I can remove the gym and pool facilities. The new price for Rosa's Bed and Breakfast will be £95 per night. | Provide_negotiation
15 | User | That's still a bit over my budget. Can you suggest another option? | Ask_alternatives
16 | Bot | Sure, I have one more option for you. The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Multioption_suggestion
17 | User | What are the differences between the Lensfield Hotel and the Bridge Guest House? | Ask_differences
18 | Bot | The Lensfield Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The Bridge Guest House is a 3-star guesthouse with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. It also provides parking and internet facilities. | Provide_differences
19 | User | Can you tell me more about the Lensfield Hotel? | Selection
20 | Bot | The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Selection
21 | User | Can you negotiate the price for the Lensfield Hotel? | Negotiation
22 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Which facilities would you like to remove? | Provide_negotiation
23 | User | Can you remove the parking facility? | Negotiation
24 | Bot | Sure, I can remove the parking facility. The new price for the Lensfield Hotel will be £81 per night. | Provide_negotiation
25 | User | That sounds good. I'll go with the Lensfield Hotel. | Selection
26 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation, Ask_details
27 | User | My name is John Smith, my email is johnsmith@gmail.com, and I'll be staying with my wife. We prefer a double room. | Inform
28 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation, Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is also a 4-star hotel with a food festival and DJ floor. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a luxurious hotel with spacious rooms, free breakfast, and 24/7 room service. It has received prestigious awards and has hosted celebrities like Virat Kholi and Eminem. | Provide_differences
9 | User | What about the Huntingdon Marriott Hotel? | Add_aspect_X
10 | Bot | The Huntingdon Marriott Hotel is a luxurious hotel with excellent 24/7 room service, a food festival, and a DJ floor. It has received prestigious awards and has hosted celebrities like Virat Kholi and Tom Holland. | Provide_differences
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a guesthouse with clean rooms, friendly staff, and a 32% discount. It offers free breakfast and 24/7 room service. | Provide_differences
13 | User | I'm interested in the Huntingdon Marriott Hotel. Can you negotiate the price? | Negotiation
14 | Bot | I can offer a 10% discount, but some facilities might get removed. | Provide_negotiation
15 | User | Can you remove the DJ floor? | Negotiation
16 | Bot | Sure, I can remove the DJ floor. The new price is £270. | Provide_negotiation
17 | User | That's still a bit high. Can you offer a better price? | Negotiation
18 | Bot | I can offer a 15% discount, but the food festival will be removed. | Provide_negotiation
19 | User | Alright, I'll take it. | Selection
20 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and number of people. | Confirmation, Ask_details
21 | User | My name is John Smith, email is johnsmith@gmail.com, and there will be 2 people. | Inform
22 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Confirmation
23 | User | Can you suggest more options? | Ask_alternatives
24 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse with great facilities. | Multioption_suggestion
25 | User | Can you tell me more about it? | Add_aspect_X
26 | Bot | Finches Bed and Breakfast is a luxurious guesthouse with spacious rooms, free breakfast, and 24/7 room service. It has a gym, pool, bar, BBQ grill, and Jacuzzi. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi and Eminem. | Provide_differences
27 | User | What's the price range? | Add_aspect_X
28 | Bot | The double rooms are £120, single rooms are £90, and family rooms are £180. | Add_aspect_X
29 | User | That's a bit expensive. Can you negotiate the price? | Negotiation
30 | Bot | I can offer a 10% discount, but some facilities might get removed. | Provide_negotiation
31 | User | Can you remove the BBQ grill? | Negotiation
32 | Bot | Sure, I can remove the BBQ grill. The new price is £108. | Provide_negotiation
33 | User | I'll think about it and get back to you. | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, University Arms Hotel, and Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, and a pool. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Selection
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Provide_details
9 | User | Can you suggest a cheaper option? | Ask_alternatives
10 | Bot | Sure, Cityroomz and El Shaddai are two cheaper options. Cityroomz has no parking, but offers affordable prices for single, double, and family rooms. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices. | Multioption_suggestion
11 | User | What are the prices for Cityroomz and El Shaddai? | Ask_details
12 | Bot | Cityroomz has prices ranging from £50 for a single room to £80 for a family room. El Shaddai offers doubles at £60, singles at £40, and family rooms at £62. | Provide_details
13 | User | Can you tell me more about the University Arms Hotel? | Selection
14 | Bot | The University Arms Hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Provide_details
15 | User | Can you negotiate the price for the University Arms Hotel? | Negotiation
16 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, and a pool. It has hosted celebrities and received prestigious awards. The hotel is currently offering free dinner. | Provide_negotiation
17 | User | Can you suggest more options with a gym and a pool? | Ask_alternatives
18 | Bot | Sure, I suggest The Gonville Hotel and The Alexander Bed and Breakfast. Both have a gym and a pool. | Multioption_suggestion
19 | User | Can you tell me more about The Alexander Bed and Breakfast? | Selection
20 | Bot | The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Provide_details
21 | User | Can you negotiate the price for The Alexander Bed and Breakfast? | Negotiation
22 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities and has been endorsed by famous critics. | Provide_negotiation
23 | User | Can you suggest a cheaper option with a gym and a pool? | Ask_alternatives
24 | Bot | Sorry, there are no cheaper options with a gym and a pool. Would you like to select one of the options I have provided? | Ask_details
25 | User | I need some time to decide. | Inform
26 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
27 | User | Can you tell me more about the free dinner offer at The Gonville Hotel? | Ask_details
28 | Bot | The Gonville Hotel is currently offering 38% off on bookings for the next 4 days and free dinner. | Provide_details
29 | User | Can I book The Gonville Hotel? | Selection
30 | Bot | Sure, The Gonville Hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference for the final booking. | Confirmation
| Utterance # | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the centre of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan on staying? | Ask_details |
| 3 | User | I'll be there next week. | Inform |
| 4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details |
| 5 | User | Just me. | Inform |
| 6 | Bot | Alright, here are three options: The Gonville Hotel, The University Arms Hotel, and The Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion |
| 7 | User | What's the difference between them? | Ask_differences |
| 8 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, free wifi, a gym, and a pool. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, free wifi, a gym, a pool, a bar, and a BBQ grill. | Provide_differences |
| 9 | User | How much does each one cost? | Add_aspect_price |
| 10 | Bot | The Gonville Hotel ranges from £79 for a single room to £119 for a family room. The University Arms Hotel ranges from £150 for a single room to £250 for a family room. The Alexander Bed and Breakfast ranges from £100 for a single room to £150 for a family room. | Provide_differences |
| 11 | User | That's quite expensive. Do you have any cheaper options? | Ask_alternatives |
| 12 | Bot | I have two more options for you: Cityroomz and El Shaddai. Cityroomz has affordable prices for single, double, and family rooms, while El Shaddai offers rooms at even cheaper prices. | Multioption_suggestion |
| 13 | User | What's the difference between Cityroomz and El Shaddai? | Ask_differences |
| 14 | Bot | Cityroomz has internet access and affordable prices, while El Shaddai offers internet and parking facilities at even cheaper prices. | Provide_differences |
| 15 | User | How much does each one cost? | Add_aspect_price |
| 16 | Bot | Cityroomz ranges from £50 for a single room to £90 for a family room. El Shaddai offers doubles at £60, singles at £40, and family rooms at £62. | Provide_differences |
| 17 | User | I think I'll go with The Alexander Bed and Breakfast. | Selection |
| 18 | Bot | Great choice! Would you like to book now? | Confirmation |
| 19 | User | Can you give me a discount? | Negotiation |
| 20 | Bot | I can offer you a 10% discount, but some facilities might be removed. | Provide_negotiation |
| 21 | User | Can you remove the gym? | Negotiation |
| 22 | Bot | Sure, I can remove the gym. Your new price is £90 for a single room and £150 for a family room. | Provide_negotiation |
| 23 | User | That's still a bit expensive. Can you lower it more? | Negotiation |
| 24 | Bot | I'm sorry, but that's the best I can do. | Deny |
| 25 | User | Alright, I'll take it. | Affirm |
| 26 | Bot | Great! Can I have your name, email, and phone number for the booking? | Ask_details |
| 27 | User | My name is John Smith, my email is johnsmith@gmail.com, and my phone number is 1234567890. | Inform |
| 28 | Bot | Thank you, John. Your booking has been confirmed. Your registration number is 123456. The address is 123 Main Street, Cambridge. | Confirmation |
| 29 | User | Can I add breakfast to my booking? | Add_aspect_breakfast |
| 30 | Bot | Sure, I can add breakfast for an additional £10 per day. | Provide_negotiation |
| 31 | User | That's too expensive. Nevermind. | Deny |
| 32 | Bot | Alright, let me know if you need anything else. | Goodbye |
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The first is Rosa's Bed and Breakfast, a 4-star guesthouse with a 33% discount for the next 4 days. The second is The Bridge Guest House, a 3-star guesthouse with moderate pricing. The third is Aylesbray Lodge Guest House, a 4-star hotel with a 30% discount for the next 2 days. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
10 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you negotiate the price? | Negotiation
12 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
13 | User | Can you remove the gym and pool facilities? | Negotiation
14 | Bot | Sure, I can remove the gym and pool facilities. The new price for Rosa's Bed and Breakfast will be £95 per night. | Provide_negotiation
15 | User | That's still a bit over my budget. Can you suggest another option? | Ask_alternatives
16 | Bot | Sure, I have one more option for you. The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Multioption_suggestion
17 | User | What are the differences between the Lensfield Hotel and the Bridge Guest House? | Ask_differences
18 | Bot | The Lensfield Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The Bridge Guest House is a 3-star guesthouse with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. | Provide_differences
19 | User | Can you tell me more about the Lensfield Hotel? | Selection
20 | Bot | The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Selection
21 | User | Can you negotiate the price for the Lensfield Hotel? | Negotiation
22 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Which facilities would you like to remove? | Provide_negotiation
23 | User | Can you remove the parking facility? | Negotiation
24 | Bot | Sure, I can remove the parking facility. The new price for the Lensfield Hotel will be £81 per night. | Provide_negotiation
25 | User | That sounds good. I'll go with the Lensfield Hotel. | Selection
26 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation, Ask_details
27 | User | My name is John Smith, my email is johnsmith@gmail.com, and there will be two people staying in the room. We prefer a double room. | Inform
28 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation, Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Add_aspect_X
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Ask_alternatives
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Add_aspect_X
11 | User | Can you tell me more about the free dinner at Huntingdon Marriott Hotel? | Add_aspect_X
12 | Bot | The Huntingdon Marriott Hotel is currently running a food festival with free dinner for guests. The festival features a variety of cuisines and is a great opportunity to try new dishes. | Add_aspect_X
13 | User | I'm not sure which one to choose. Can you suggest another option? | Ask_alternatives
14 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Multioption_suggestion
15 | User | What are the prices for Finches Bed and Breakfast? | Add_aspect_X
16 | Bot | Finches Bed and Breakfast offers double rooms for £75, single rooms for £59, and family rooms for £110. | Add_aspect_X
17 | User | Can you tell me more about the facilities at Finches Bed and Breakfast? | Add_aspect_X
18 | Bot | Finches Bed and Breakfast has a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious. | Add_aspect_X
19 | User | I think I'm interested in the Huntingdon Marriott Hotel. Can you negotiate the price for me? | Negotiation
20 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. The Huntingdon Marriott Hotel is already offering a free breakfast and a food festival with free dinner for guests. | Provide_negotiation
21 | User | Can you remove the DJ floor and give me a discount? | Negotiation
22 | Bot | I can offer you a 5% discount if I remove the DJ floor. Would you like to proceed with the booking? | Provide_negotiation
23 | User | Yes, I would like to proceed with the booking. | Affirm, Selection
24 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation, Ask_details
25 | User | My name is John Smith, my email is johnsmith@gmail.com, there will be 2 people, and we would like a double room. | Inform
26 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation, Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_details
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Ask_alternatives
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_details
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_details
13 | User | Can you tell me more about the Huntingdon Marriott Hotel's food festival? | Add_aspect_X
14 | Bot | The Huntingdon Marriott Hotel is currently running a food festival with free dinner for guests. | Provide_details
15 | User | I'm interested in the Cambridge Belfry, but it's a bit expensive. Can you offer a lower price? | Negotiation
16 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
17 | User | Can you remove the jacuzzi? | Negotiation
18 | Bot | Sure, I can remove the jacuzzi. The new price will be £135 per night. | Provide_negotiation
19 | User | That's still a bit high. Can you offer a lower price? | Negotiation
20 | Bot | I'm sorry, but £135 is the best I can do. | Provide_negotiation
21 | User | Okay, I'll take it. | Selection
22 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details
23 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
24 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Confirmation
25 | User | Actually, can you tell me more about the Finches Bed and Breakfast? | Ask_alternatives
26 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_details
27 | User | That sounds great. Can you tell me more about the price? | Add_aspect_X
28 | Bot | Finches Bed and Breakfast offers double rooms for £150, single rooms for £120, and family rooms for £200. | Provide_details
29 | User | That's a bit too expensive for me. Can you offer a lower price? | Negotiation
30 | Bot | I'm sorry, but the prices are fixed. Is there anything else I can help you with? | Provide_negotiation, Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, The University Arms Hotel, and The Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, 24/7 room service, free wifi, a gym, a pool, and spacious rooms. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Add_aspect_X
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Add_aspect_X
9 | User | What about the University Arms Hotel? | Add_aspect_X
10 | Bot | The University Arms Hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Add_aspect_X
11 | User | And the Alexander Bed and Breakfast? | Add_aspect_X
12 | Bot | The Alexander Bed and Breakfast has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Add_aspect_X
13 | User | Can you suggest more options? | Ask_alternatives
14 | Bot | Sure, I have two more options for you. Cityroomz and El Shaddai. Cityroomz is a moderate hotel located in the centre of Cambridge, with internet access and takes bookings. Although it has no parking, it offers affordable prices for single, double, and family rooms. The hotel has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse located in the centre of Cambridge. It offers internet and parking facilities, and takes bookings. The hotel has a 0-star rating and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Multioption_suggestion
15 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
16 | Bot | Cityroomz is a moderate hotel with internet access and affordable prices for single, double, and family rooms. It has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
17 | User | I'm interested in the University Arms Hotel, but it's a bit expensive. Can you suggest something cheaper? | Negotiation
18 | Bot | I understand your concern. How much is your estimated budget? | Add_aspect_X
19 | User | My budget is around £80 per night. | Add_aspect_X
20 | Bot | I see. In that case, I can suggest Cityroomz or El Shaddai. Both are within your budget. Which one would you like to know more about? | Multioption_suggestion
21 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
22 | Bot | Cityroomz is a moderate hotel with internet access and affordable prices for single, double, and family rooms. It has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
23 | User | Can you negotiate the price of the University Arms Hotel? | Negotiation
24 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Are you sure you want to negotiate? | Provide_negotiation
25 | User | Yes, I want to negotiate. | Affirm
26 | Bot | Alright, I can offer you a 5% discount on the price of the University Arms Hotel. However, the free dinner offer will be removed. Is that okay with you? | Provide_negotiation
27 | User | Can you remove something else instead of the free dinner? | Negotiation
28 | Bot | I'm sorry, but the free dinner offer is the only thing that can be removed. | Provide_negotiation
29 | User | Okay, I'll go with the University Arms Hotel. | Selection
30 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference for the booking. | Confirmation
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have three options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive option, but it offers a gym and a pool. The A and B Guest House has a BBQ grill and a Jacuzzi. Allenbell guesthouse has a bar and spacious luxurious rooms. | Provide_differences |
| 9 | User | Can you give me more options? | Ask_alternatives |
| 10 | Bot | Sure, I have two more options for you. The first is Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. The second is Autumn House, a 4-star guesthouse with a 37% discount on bookings for the next 2 days and free dinner. | Multioption_suggestion |
| 11 | User | What are the differences between Carolina Bed and Breakfast and Autumn House? | Ask_differences |
| 12 | Bot | Carolina Bed and Breakfast has a pool, bar, and BBQ grill. Autumn House has a DJ floor and fully safe, sanitary, and secure rooms. | Provide_differences |
| 13 | User | I'm interested in Leverton House, but it's a bit over my budget. Can you offer a lower price? | Negotiation |
| 14 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation |
| 15 | User | Can you remove the gym and pool facilities? | Negotiation |
| 16 | Bot | Sure, I can remove those facilities and offer you a 10% discount. | Provide_negotiation |
| 17 | User | Okay, I'll take the offer. | Selection |
| 18 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation, Ask_details |
| 19 | User | My name is John Smith, my email is johnsmith@gmail.com, there will be two people, and we prefer a double room. | Inform |
| 20 | Bot | Thank you, John. Your booking is confirmed. You can contact us at 123-456-7890 for any further queries. | Confirmation |
| 21 | User | Can I add breakfast to my booking? | Add_aspect_X |
| 22 | Bot | Sure, I can add breakfast for an additional £10 per day. | Provide_negotiation |
| 23 | User | Okay, I'll take the breakfast. | Selection |
| 24 | Bot | Great, your booking has been updated. Is there anything else I can help you with? | Confirmation |
| 25 | User | No, that's all. Thank you. | Goodbye |
| 26 | Bot | Thank you for choosing our hotel. Have a great day! | Goodbye |
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have three options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive option, but it offers a gym and a pool. The A and B Guest House has a BBQ grill and a Jacuzzi. Allenbell guesthouse has a bar and spacious luxurious rooms. | Provide_differences |
| 9 | User | I'm interested in Leverton House. Can you tell me more about it? | Selection |
| 10 | Bot | Leverton House is a 4-star guesthouse located in East Cambridge. It offers free breakfast, 24/7 room service, free wifi, a gym, and a pool. The rooms are spacious and luxurious, and the hotel is fully safe, sanitary, and secure. It has received numerous recognitions, including appearing in magazines like BigHospitality and LuxeDine, being endorsed by tour agencies like Expedia, and receiving prestigious awards like the Michelin Star. It has also hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan and has been endorsed by famous critics like Pete Wells and Jonathan Gold. | Provide_details |
| 11 | User | The price is a bit high. Can you offer a discount? | Negotiation |
| 12 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation |
| 13 | User | Can you remove the gym and pool facilities? | Negotiation |
| 14 | Bot | I can remove the gym and pool facilities, but the discount will only be 5%. | Provide_negotiation |
| 15 | User | Okay, I'll take it. | Affirm |
| 16 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation |
| 17 | User | Can you suggest some nearby restaurants? | Ask_alternatives |
| 18 | Bot | Sure, there's a great Italian restaurant called La Margherita nearby. There's also a Chinese restaurant called Golden Wok and a pub called The Eagle. | Multioption_suggestion |
| 19 | User | Can you book a table for me at La Margherita? | Add_aspect_X |
| 20 | Bot | I'm sorry, I can't book a table for you. But I can provide you with their contact details. | Inform |
| 21 | User | Can you suggest some tourist attractions nearby? | Ask_alternatives |
| 22 | Bot | Sure, there's the Cambridge University Botanic Garden, the Fitzwilliam Museum, and the King's College Chapel. | Multioption_suggestion |
| 23 | User | Can you book tickets for the Botanic Garden? | Add_aspect_X |
| 24 | Bot | I'm sorry, I can't book tickets for you. But I can provide you with their contact details. | Inform |
| 25 | User | Can you suggest some nearby shopping centers? | Add_aspect_X |
| 26 | Bot | Sure, there's the Grand Arcade, the Grafton Centre, and the Lion Yard Shopping Centre. | Multioption_suggestion |
| 27 | User | Can you book a taxi for me to the Grand Arcade? | Add_aspect_X |
| 28 | Bot | I'm sorry, I can't book a taxi for you. But I can provide you with the contact details of a local taxi service. | Inform |
| 29 | User | I'm still not sure about my hotel choice. Can you suggest some more options? | Ask_alternatives |
| 30 | Bot | Sure, there's Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. There's also Autumn House, a 4-star guesthouse with free dinner and 37% off on bookings for the next 2 days. | Multioption_suggestion |
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a 31% discount for the next 2 days and free dinner. The third is Lovell Lodge, a 2-star hotel with a moderate price range and only 4 rooms left. Which one would you like to know more about? | Multioption_suggestion
7 | User | Can you tell me the differences between the options? | Ask_differences
8 | Bot | Kirkwood House is a luxurious guesthouse with a gym, pool, bar, BBQ grill, and Jacuzzi. Home from Home is also a luxurious guesthouse with a gym, pool, and bar. Lovell Lodge is a 2-star hotel with free breakfast and wifi. | Provide_differences
9 | User | Can you tell me more about Kirkwood House? | Selection
10 | Bot | Kirkwood House is a 4-star guesthouse located in North Cambridge. It offers free breakfast, 24/7 room service, free wifi, a gym, pool, bar, BBQ grill, and Jacuzzi. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as the Michelin Star. The hotel has hosted celebrities like Ronaldo, Virat Kholi, and Jackie Chan. | Selection
11 | User | That sounds great, but it's a bit out of my budget. Can you suggest something cheaper? | Ask_alternatives
12 | Bot | Sure, I have two more options for you. The first is The Limehouse guesthouse, a 4-star hotel with free breakfast, 24/7 room service, free wifi, and great food. The second is The Acorn Guest House, a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, and great food. Which one would you like to know more about? | Multioption_suggestion
13 | User | Can you tell me the differences between The Limehouse and The Acorn Guest House? | Ask_differences
14 | Bot | The Limehouse guesthouse has a DJ floor and has hosted celebrities like Ronaldo, Virat Kholi, Tom Holland, and Jackie Chan. The Acorn Guest House has a gym and pool and has hosted celebrities like Ronaldo and Eminem. The head chef at The Acorn Guest House has a cookbook named "How to Burger." | Provide_differences
15 | User | Can you tell me more about The Acorn Guest House? | Selection
16 | Bot | The Acorn Guest House is a 4-star guesthouse located in North Cambridge. It offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel has a gym and pool. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Ronaldo and Eminem. The head chef has a cookbook named "How to Burger." | Selection
17 | User | I'm still not sure. Can you suggest something else? | Ask_alternatives
18 | Bot | Sure, I have one more option for you. Archway House is a 4-star guesthouse with free wifi, parking, and breakfast. It offers spacious and luxurious rooms, a gym, pool, and DJ floor. It has been recognized by popular magazines and tour agencies and has hosted celebrities like Tom Holland and Jackie Chan. The head chef has a cookbook named Red Tomato. Currently, the hotel is offering a food festival and 37% off on bookings for the next 4 days. | Multioption_suggestion
19 | User | Can you tell me the differences between Archway House and the other options? | Ask_differences
20 | Bot | Archway House has free parking and is currently offering a food festival and 37% off on bookings for the next 4 days. It has a DJ floor and has hosted celebrities like Tom Holland and Jackie Chan. | Provide_differences
21 | User | Can you tell me more about Archway House? | Selection
22 | Bot | Archway House is a 4-star guesthouse located in North Cambridge. It offers free wifi, parking, and breakfast. The hotel offers spacious and luxurious rooms, a gym, pool, and DJ floor. It has been recognized by popular magazines and tour agencies and has hosted celebrities like Tom Holland and Jackie Chan. The head chef has a cookbook named Red Tomato. Currently, the hotel is offering a food festival and 37% off on bookings for the next 4 days. | Selection
23 | User | I'm still not sure. Can I negotiate the price for Kirkwood House? | Negotiation
24 | Bot | Sure, I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. What is your estimated budget? | Provide_negotiation
25 | User | My budget is £150. | Inform
26 | Bot | I'm sorry, but the price for Kirkwood House is £250 per night. However, I can offer you a 10% discount, bringing the price down to £225 per night. Would you like to book it? | Confirmation
27 | User | That's still too high. Can you suggest something else? | Ask_alternatives
28 | Bot | Sure, I have two more options for you. The first is Home from Home, a 4-star guesthouse with a moderate price range. The second is Lovell Lodge, a 2-star hotel with a moderate price range and only 4 rooms left. Which one would you like to know more about? | Multioption_suggestion
29 | User | Can you tell me the differences between Home from Home and Lovell Lodge? | Ask_differences
30 | Bot | Home from Home is a luxurious guesthouse with a gym, pool, and bar. Lovell Lodge is a 2-star hotel with free breakfast and wifi. | Provide_differences
31 | User | Can you tell me more about Home from Home? | Selection
32 | Bot | Home from Home is a 4-star guesthouse located in North Cambridge. It offers free breakfast, 24/7 room service, free wifi, a gym, pool, and bar. The hotel has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by popular magazines and tour agencies and has hosted celebrities such as Ronaldo, Virat Kholi, and Tom Holland. The hotel offers a moderate price range with double rooms at £75, family rooms at £105, and single rooms at £50. Currently, the hotel is offering a 31% discount on bookings for the next 2 days and free dinner. | Selection
33 | User | That sounds good. I'll book Home from Home. | Affirm, Confirmation
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The first is Rosa's Bed and Breakfast, a 4-star guesthouse with a 33% discount for the next 4 days. The second is The Bridge Guest House, a 3-star guesthouse with moderate pricing. The third is Aylesbray Lodge Guest House, a 4-star hotel with a 30% discount for the next 2 days. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
10 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you negotiate the price? | Negotiation
12 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Would you like me to negotiate for you? | Provide_negotiation
13 | User | Yes, please. | Affirm
14 | Bot | I'm sorry, but the hotel is already offering a 33% discount. I cannot negotiate any further. | Deny
15 | User | Okay, can you suggest some other options? | Ask_alternatives
16 | Bot | Sure, I have one more option for you. The Lensfield Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Multioption_suggestion
17 | User | What are the differences between the options? | Ask_differences
18 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. The Lensfield Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. | Provide_differences
19 | User | Can you tell me more about The Lensfield Hotel? | Selection
20 | Bot | The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel has received recognitions such as appearing in local magazines like FoodVilla and Food and Beyond, being endorsed by local tour agencies TourMe, and receiving local awards such as Food Fest, Budget, and Great and Escape. | Selection
21 | User | I'm not sure which one to choose. Can you give me some time to decide? | Inform
22 | Bot | Sure, take your time. Let me know if you have any other questions. | Inform
23 | User | Can you tell me more about the facilities at Aylesbray Lodge Guest House? | Ask_details
24 | Bot | Aylesbray Lodge Guest House has excellent 24/7 room service, free breakfast, and free wifi. The hotel features a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms that are fully safe, sanitary, and secure. The head chef has a cookbook named Dine with Me. | Ask_details
25 | User | How much is a double room at Aylesbray Lodge Guest House? | Add_aspect_X
26 | Bot | A double room at Aylesbray Lodge Guest House is priced at £85 per night. | Add_aspect_X
27 | User | Can you tell me more about The Bridge Guest House? | Selection
28 | Bot | The Bridge Guest House is a 3-star guesthouse located in the south area of Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also provides parking and internet facilities. The hotel has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. The hotel offers moderate pricing with double rooms at £75, family rooms at £90, and single rooms at £50. | Selection
29 | User | Can you tell me more about the facilities at Rosa's Bed and Breakfast? | Ask_details
30 | Bot | Rosa's Bed and Breakfast has free internet and parking. The hotel offers spacious and luxurious rooms with great food, gym, pool, bar, and BBQ grill. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Ask_details
31 | User | I think I'll go with The Bridge Guest House. | Selection
32 | Bot | Great choice! The hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference for the booking. | Confirmation
Utterance # | Speaker | Utterance | Intent
----------- | ------- | --------- | ------
1 | User | Hi, I'm looking for a hotel in the North area of Cambridge. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. What's your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | Okay, I have three options for you. The first is Kirkwood House, a 4-star guesthouse with a 36% discount for the next 3 days. The second is Home from Home, a 4-star guesthouse with a 31% discount for the next 2 days and free dinner. The third is Lovell Lodge, a 2-star hotel with a moderate price range. Which one would you like to know more about? | Multioption_suggestion
7 | User | What's the difference between Kirkwood House and Home from Home? | Ask_differences
8 | Bot | Kirkwood House is a bit more expensive, but it offers a gym, pool, bar, BBQ grill, and Jacuzzi. Home from Home doesn't have a BBQ grill or Jacuzzi, but it's a bit cheaper and offers free dinner. | Provide_differences
9 | User | Can you tell me more about Lovell Lodge? | Ask_alternatives
10 | Bot | Sure, Lovell Lodge is a 2-star hotel with free breakfast and wifi. It's a bit cheaper than the other two options, but it doesn't have as many amenities. | Provide_differences
11 | User | I think I'm interested in Kirkwood House. Can you tell me more about it? | Selection
12 | Bot | Kirkwood House is a 4-star guesthouse with free breakfast, 24/7 room service, and free wifi. It's fully safe, sanitary, and secure, and has spacious and luxurious rooms. It's been recognized by famous magazines and tour agencies, and has received prestigious awards such as the Michelin Star. It's currently offering a 36% discount on bookings for the next 3 days. | Provide_differences
13 | User | The price is a bit high for me. Can you offer a lower price? | Negotiation
14 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. Would you still like to proceed? | Provide_negotiation
15 | User | Okay, I'll take the 10% discount. | Affirm
16 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Can I have your name, email, and contact number for the booking? | Ask_details
17 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Inform
18 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Confirmation
19 | User | Actually, can you tell me more about the food at Kirkwood House? | Ask_alternatives
20 | Bot | Kirkwood House has a great food festival going on right now. They've also received a Michelin Star and The Gold List award for their food. | Provide_differences
21 | User | That sounds great. Can you tell me more about the gym and pool? | Ask_alternatives
22 | Bot | The gym and pool at Kirkwood House are both top-notch. They're spacious and well-maintained, and are available 24/7. | Provide_differences
23 | User | I'm still not sure. Can you suggest any other options? | Ask_alternatives
24 | Bot | Sure, I have two more options for you. The first is The Limehouse guesthouse, a 4-star hotel with free breakfast, 24/7 room service, and a DJ floor. The second is Archway House, a 4-star guesthouse with free wifi, parking, and breakfast, and a food festival going on right now. Which one would you like to know more about? | Multioption_suggestion
25 | User | What's the difference between The Limehouse and Archway House? | Ask_differences
26 | Bot | The Limehouse has a DJ floor, while Archway House has parking facilities. Both are 4-star hotels with free breakfast and wifi. The Limehouse has a Michelin Star and The Gold List award, while Archway House has a public rating of 8/10. | Provide_differences
27 | User | Can you tell me more about the food at Archway House? | Ask_alternatives
28 | Bot | The food festival at Archway House is quite popular. They've also received good reviews for their food. | Provide_differences
29 | User | I think I'll stick with Kirkwood House. Can I get the 10% discount on my booking? | Negotiation
30 | Bot | I'm sorry, John, but the discount has already been applied to your booking. Is there anything else I can help you with? | Deny
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I want to book a hotel in the centre of Cambridge. | Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Gonville Hotel, The University Arms Hotel, and The Alexander Bed and Breakfast. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Gonville Hotel is a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. The University Arms Hotel is a luxurious 4-star hotel with free breakfast, 24/7 room service, free wifi, a gym, a pool, and spacious rooms. The Alexander Bed and Breakfast is a 4-star guesthouse with free breakfast, 24/7 room service, free wifi, a gym, pool, bar, and BBQ grill. | Provide_differences
7 | User | Can you tell me more about the Gonville Hotel? | Add_aspect_X
8 | Bot | The Gonville Hotel has friendly staff, delicious food, and very clean rooms. It also has a gym and a safe. The hotel has received recognitions such as appearing in local magazines like MrHotel and Food and beyond, being endorsed by local tour agencies Travel Partner and Buddy's travel, and receiving local awards such as Budget and Great. The hotel is expensive, with prices ranging from £79 for a single room to £119 for a family room. The hotel is currently offering 38% off on bookings for the next 4 days and free dinner. The hotel has a public image rating of 8/10. | Add_aspect_X
9 | User | What about the University Arms Hotel? | Add_aspect_X
10 | Bot | The University Arms Hotel is fully safe, sanitary, and secure. It has received prestigious awards such as Michelin Star and Cateys and has been endorsed by popular tour agencies such as Thomas Cook. The hotel has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Gordon Ramsay. The hotel offers free dinner and has a huge social media presence. It is popular with both locals and international tourists and has a rating of 10/10. | Add_aspect_X
11 | User | And the Alexander Bed and Breakfast? | Add_aspect_X
12 | Bot | The Alexander Bed and Breakfast has spacious and luxurious rooms, and is fully safe, sanitary, and secure. It has been recognized by famous magazines and tour agencies, and has received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi and Jackie Chan, and has been endorsed by famous critics like Gordon Ramsay and Nigella Lawson. The hotel is popular with both locals and international tourists, and has a public rating of 8/10. | Add_aspect_X
13 | User | Can you suggest more options? | Ask_alternatives
14 | Bot | Sure, I have two more options for you. Cityroomz and El Shaddai. Cityroomz is a moderate hotel located in the centre of Cambridge, with internet access and takes bookings. Although it has no parking, it offers affordable prices for single, double, and family rooms. The hotel has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse located in the centre of Cambridge. It offers internet and parking facilities, and takes bookings. The hotel has a 0-star rating and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Multioption_suggestion
15 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
16 | Bot | Cityroomz is a moderate hotel with internet access and affordable prices for single, double, and family rooms. It has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
17 | User | I'm interested in the University Arms Hotel, but it's a bit expensive. Can you suggest something cheaper? | Negotiation
18 | Bot | I understand your concern. How much is your estimated budget? | Add_aspect_X
19 | User | My budget is around £80 per night. | Add_aspect_X
20 | Bot | I see. In that case, I can suggest Cityroomz or El Shaddai. Both are within your budget. Which one would you like to know more about? | Multioption_suggestion
21 | User | What are the differences between Cityroomz and El Shaddai? | Ask_differences
22 | Bot | Cityroomz is a moderate hotel with internet access and affordable prices for single, double, and family rooms. It has no stars or recognitions, but it does have an offer of 34% off on bookings for the next 4 days. Its public image is rated 1/10. El Shaddai is a cheap guesthouse with internet and parking facilities, and offers rooms at affordable prices, with doubles at £60, singles at £40, and family rooms at £62. The hotel also offers a free dinner and has a public image rating of 1/10. No features or recognitions are mentioned. | Provide_differences
23 | User | Can you negotiate the price of the University Arms Hotel? | Negotiation
24 | Bot | I can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Are you sure you want to negotiate? | Provide_negotiation
25 | User | Yes, I want to negotiate. | Affirm
26 | Bot | Alright, I can offer you a 5% discount on the price of the University Arms Hotel. However, the free dinner offer will be removed. Is that okay with you? | Provide_negotiation
27 | User | Can you remove something else instead of the free dinner? | Negotiation
28 | Bot | I'm sorry, but the free dinner offer is the only thing that can be removed. | Provide_negotiation
29 | User | Okay, I'll take the University Arms Hotel. | Selection
30 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference for the booking. | Confirmation
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, here are three options: Rosa's Bed and Breakfast, The Bridge Guest House, and Aylesbray Lodge Guest House. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between them? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse with luxurious rooms, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | How much does each option cost? | Add_aspect_price
10 | Bot | Rosa's Bed and Breakfast is currently offering a 33% discount, with double rooms priced at £100, family rooms at £150, and single rooms at £75. The Bridge Guest House has double rooms at £75, family rooms at £90, and single rooms at £50. Aylesbray Lodge Guest House is currently offering a 30% discount, with double rooms priced at £105, family rooms at £135, and single rooms at £80. | Provide_differences
11 | User | Can you suggest more options? | Ask_alternatives
12 | Bot | Sure, how about The Lensfield Hotel? It's a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. | Multioption_suggestion
13 | User | How much does it cost? | Add_aspect_price
14 | Bot | The Lensfield Hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. | Provide_differences
15 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
16 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. The hotel offers spacious and luxurious rooms with great food, gym, pool, bar, and BBQ grill. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. | Provide_details
17 | User | Can I negotiate the price? | Negotiation
18 | Bot | Sure, we can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Which facilities are you willing to compromise on? | Provide_negotiation
19 | User | Can I get a higher priced option for the price of the cheaper option? | Negotiation
20 | Bot | I'm sorry, but the prices are fixed. However, I can assure you that Rosa's Bed and Breakfast is worth the price. It has great facilities and has hosted celebrities like Ronaldo and Jackie Chan. | Provide_negotiation
21 | User | Can you tell me more about Aylesbray Lodge Guest House? | Selection
22 | Bot | Aylesbray Lodge Guest House is a 4-star hotel located in South with free internet and parking. The hotel offers moderate prices for single, double, and family rooms. It has excellent 24/7 room service, free breakfast, and free wifi. The hotel features a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms that are fully safe, sanitary, and secure. Aylesbray Lodge Guest House has been recognized by famous magazines, tour agencies, and critics. It has hosted celebrities like Ronaldo, Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named Dine with Me. The hotel is currently offering a 30% discount on bookings for the next 2 days, with only 2 rooms left. It is popular with locals, tour agencies, and has a huge social media presence with an 8/10 rating. | Provide_details
23 | User | Can I negotiate the price for Aylesbray Lodge Guest House? | Negotiation
24 | Bot | Sure, we can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. Which facilities are you willing to compromise on? | Provide_negotiation
25 | User | Can you suggest more options? | Ask_alternatives
26 | Bot | Sure, how about The Bridge Guest House? It's a 3-star guesthouse located in the south area of Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also provides parking and internet facilities. The hotel has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. The hotel offers moderate pricing with double rooms at £75, family rooms at £90, and single rooms at £50. | Multioption_suggestion
27 | User | Can you tell me more about The Bridge Guest House? | Selection
28 | Bot | The Bridge Guest House is a 3-star guesthouse located in the south area of Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also provides parking and internet facilities. The hotel has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. | Provide_details
29 | User | I'm still not sure which one to choose. Can you give me some time to decide? | Affirm
30 | Bot | Of course, take your time. Let me know if you have any other questions. | Affirm
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The first is Rosa's Bed and Breakfast, a 4-star guesthouse with a 33% discount for the next 4 days. The second is The Bridge Guest House, a 3-star guesthouse with moderate pricing. The third is Aylesbray Lodge Guest House, a 4-star hotel with a 30% discount for the next 2 days. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a luxurious 4-star guesthouse with great food, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
10 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Selection
11 | User | That sounds great, but it's a bit over my budget. Can you negotiate the price? | Negotiation
12 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. Would you like to proceed with the booking? | Provide_negotiation
13 | User | Can you tell me more about The Bridge Guest House? | Selection
14 | Bot | The Bridge Guest House is a 3-star guesthouse located in the south area of Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also provides parking and internet facilities. The hotel has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. The hotel offers moderate pricing with double rooms at £75, family rooms at £90, and single rooms at £50. | Selection
15 | User | That sounds good. Can you suggest more options? | Ask_alternatives
16 | Bot | Sure, I have one more option for you. The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel has received recognitions such as appearing in local magazines like FoodVilla and Food and Beyond, being endorsed by local tour agencies TourMe, and receiving local awards such as Food Fest, Budget, and Great and Escape. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Multioption_suggestion
17 | User | Can you tell me more about The Lensfield Hotel? | Selection
18 | Bot | The Lensfield Hotel is a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel has received recognitions such as appearing in local magazines like FoodVilla and Food and Beyond, being endorsed by local tour agencies TourMe, and receiving local awards such as Food Fest, Budget, and Great and Escape. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Selection
19 | User | I'm still not sure which one to choose. Can you give me some time to decide? | Inform
20 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
21 | User | Can you tell me more about the facilities at Aylesbray Lodge Guest House? | Selection
22 | Bot | Aylesbray Lodge Guest House is a 4-star hotel located in South with free internet and parking. The hotel offers moderate prices for single, double, and family rooms. It has excellent 24/7 room service, free breakfast, and free wifi. The hotel features a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms that are fully safe, sanitary, and secure. Aylesbray Lodge Guest House has been recognized by famous magazines, tour agencies, and critics. It has hosted celebrities like Ronaldo, Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named Dine with Me. The hotel is currently offering a 30% discount on bookings for the next 2 days, with only 2 rooms left. It is popular with locals, tour agencies, and has a huge social media presence with an 8/10 rating. | Selection
23 | User | Can you tell me more about the food at The Bridge Guest House? | Add_aspect_X
24 | Bot | The Bridge Guest House has delicious food that has been highly praised by guests. They offer a variety of dishes for breakfast, lunch, and dinner. | Add_aspect_X
25 | User | Can you tell me more about the parking facilities at Rosa's Bed and Breakfast? | Add_aspect_X
26 | Bot | Rosa's Bed and Breakfast offers free parking for guests. | Add_aspect_X
27 | User | Can you tell me more about the public image rating of The Lensfield Hotel? | Add_aspect_X
28 | Bot | The Lensfield Hotel has a public image rating of 6/10. | Add_aspect_X
29 | User | I've decided to go with The Bridge Guest House. Can you book it for me? | Inform
30 | Bot | Sure, The Bridge Guest House has been reserved for you. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation, Ask_details
31 | User | My name is John Smith, my email is johnsmith@gmail.com, and there will be two people staying in a double room. | Inform
32 | Bot | Great, your booking has been confirmed. You will receive a confirmation email shortly. Thank you for choosing our service. | Confirmation, Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is also a 4-star hotel with a food festival and DJ floor. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about The Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a luxurious hotel with spacious rooms, free breakfast, and 24/7 room service. It has been endorsed by popular tour agencies and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. | Provide_differences
9 | User | What about the Huntingdon Marriott Hotel? | Add_aspect_X
10 | Bot | The Huntingdon Marriott Hotel is a luxurious hotel with spacious rooms, free breakfast, and 24/7 room service. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. | Provide_differences
11 | User | How much does each option cost? | Ask_differences
12 | Bot | The Cambridge Belfry costs £150 per night, Huntingdon Marriott Hotel costs £200 per night, and Hobsons House costs £75 for a double room, £59 for a single room, and £110 for a family room. | Provide_differences
13 | User | Can you suggest more options? | Ask_alternatives
14 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse with free breakfast, 24/7 room service, and a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. | Multioption_suggestion
15 | User | How much does Finches Bed and Breakfast cost? | Ask_differences
16 | Bot | Finches Bed and Breakfast costs £180 per night. | Provide_differences
17 | User | Can you tell me more about the facilities at Huntingdon Marriott Hotel? | Add_aspect_X
18 | Bot | Huntingdon Marriott Hotel has a food festival with free dinner for guests, a DJ floor, and a Michelin Star. | Provide_differences
19 | User | I'm interested in The Cambridge Belfry, but the price is a bit high. Can you offer a discount? | Negotiation
20 | Bot | I can offer a 10% discount, but some facilities like the gym and pool might not be available. | Provide_negotiation
21 | User | Can you tell me more about the food at The Cambridge Belfry? | Add_aspect_X
22 | Bot | The food at The Cambridge Belfry is great and the head chef has a cookbook named "How to Burger". | Provide_differences
23 | User | Okay, I'll go with The Cambridge Belfry. | Selection
24 | Bot | Great, the hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and number of people and rooms required. | Confirmation, Ask_details
25 | User | My name is John Smith, email is johnsmith@gmail.com, and I need 2 double rooms for 4 people. | Inform
26 | Bot | Thank you, John. Your booking is confirmed. You will receive a confirmation email shortly. | Confirmation
27 | User | Can I add breakfast to my booking? | Add_aspect_X
28 | Bot | Breakfast is already included in your booking. | Provide_differences
29 | User | Can I cancel my booking? | Add_aspect_X
30 | Bot | Yes, you can cancel your booking up to 24 hours before check-in. | Provide_differences
31 | User | Thank you for your help. | Goodbye
32 | Bot | You're welcome. Have a great day! | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X
5 | User | My budget is around £100 per night. | Add_aspect_X
6 | Bot | I have three options for you. The Cambridge Belfry is £120 per night, Huntingdon Marriott Hotel is £150 per night, and Hobsons House is £75 per night. | Multioption_suggestion
7 | User | What are the differences between the options? | Ask_differences
8 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
9 | User | Can you suggest more options? | Ask_alternatives
10 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse with a gym, pool, and BBQ grill. It's £130 per night. | Multioption_suggestion
11 | User | What are the differences between the options? | Ask_differences
12 | Bot | The Cambridge Belfry and Finches Bed and Breakfast are both 4-star hotels with a gym, pool, and jacuzzi. Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
13 | User | I'm interested in Huntingdon Marriott Hotel. Can you negotiate the price? | Negotiation
14 | Bot | I can offer you a 10% discount, but some facilities like the DJ floor and free dinner will be removed. | Provide_negotiation
15 | User | Can you suggest more options? | Ask_alternatives
16 | Bot | Sure, how about The Varsity Hotel & Spa? It's a 4-star hotel with a spa, gym, and rooftop bar. It's £180 per night. | Multioption_suggestion
17 | User | What are the differences between Huntingdon Marriott Hotel and The Varsity Hotel & Spa? | Ask_differences
18 | Bot | Huntingdon Marriott Hotel has a DJ floor and free dinner, while The Varsity Hotel & Spa has a spa and rooftop bar. | Provide_differences
19 | User | I'll go with Huntingdon Marriott Hotel. | Selection
20 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation, Ask_details
21 | User | My name is John Smith, email is johnsmith@gmail.com, and contact number is 1234567890. | Inform
22 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_differences
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Add_aspect_X
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_differences
11 | User | Can you tell me more about the Hobsons House? | Add_aspect_X
12 | Bot | Hobsons House is a 3-star guesthouse located in West with free wifi, parking, and gym. The rooms are very clean and the staff is friendly. The hotel offers free breakfast and 24/7 room service. It has been recognized by local tour agencies and appeared in local magazines. Currently, there is a 32% discount on bookings for the next 3 days and free dinner. The hotel has a moderate price range and offers double rooms for £75, single rooms for £59, and family rooms for £110. | Provide_differences
13 | User | I'm interested in the Huntingdon Marriott Hotel, but it's a bit expensive. Can you offer a lower price? | Negotiation
14 | Bot | I can offer a 10% discount, but some facilities like the DJ floor and free dinner may not be available. Would you still like to book the Huntingdon Marriott Hotel? | Provide_negotiation
15 | User | Hmm, can you suggest any other options? | Ask_alternatives
16 | Bot | Sure, how about Finches Bed and Breakfast? It's a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Multioption_suggestion
17 | User | Can you tell me more about Finches Bed and Breakfast? | Add_aspect_X
18 | Bot | Finches Bed and Breakfast is a 4-star guesthouse located in West Cambridge. The hotel offers free breakfast, 24/7 room service, free wifi, and great food. The rooms are spacious and luxurious, and the hotel features a gym, pool, bar, BBQ grill, Jacuzzi, and DJ floor. It has been recognized by famous magazines and tour agencies and has hosted celebrities like Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named "How to Burger." The hotel is fully safe, sanitary, and secure and is popular with locals, international tourists, and tour agencies. | Provide_differences
19 | User | That sounds great, but what's the price? | Add_aspect_X
20 | Bot | Finches Bed and Breakfast offers double rooms for £120, single rooms for £90, and family rooms for £150. | Provide_differences
21 | User | Can you offer a lower price for Finches Bed and Breakfast? | Negotiation
22 | Bot | I can offer a 5% discount, but some facilities like the BBQ grill and Jacuzzi may not be available. Would you like to book Finches Bed and Breakfast? | Provide_negotiation
23 | User | Let me think about it for a bit. | Selection
24 | Bot | Sure, take your time. Let me know if you have any other questions. | Affirm
25 | User | Can you tell me more about the gym at the Cambridge Belfry? | Add_aspect_X
26 | Bot | The gym at the Cambridge Belfry is fully equipped with modern machines and equipment. It's open 24/7 and is free for all guests. | Provide_differences
27 | User | What about the pool at the Huntingdon Marriott Hotel? | Add_aspect_X
28 | Bot | The pool at the Huntingdon Marriott Hotel is a heated indoor pool with a sauna and steam room. It's open 24/7 and is free for all guests. | Provide_differences
29 | User | Can you tell me more about the free breakfast at Hobsons House? | Add_aspect_X
30 | Bot | The free breakfast at Hobsons House includes a variety of options such as eggs, bacon, toast, cereal, and fruit. It's served from 7am to 10am every day. | Provide_differences
31 | User | I think I've made a decision. I'd like to book the Huntingdon Marriott Hotel. | Selection
32 | Bot | Great choice! The hotel has been reserved for you. Your registration number is 123456. Please provide your name, email, and phone number for the booking. | Confirmation, Ask_details
33 | User | My name is John Smith, my email is johnsmith@email.com, and my phone number is 123-456-7890. | Inform
34 | Bot | Thank you, John. Your booking has been confirmed. You will receive a confirmation email shortly. Is there anything else I can help you with? | Confirmation
35 | User | No, that's all. Thank you for your help. | Goodbye
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have three options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive option, but it offers a gym and a pool. The A and B Guest House has a BBQ grill and a Jacuzzi. Allenbell guesthouse has a bar and spacious luxurious rooms. | Provide_differences |
| 9 | User | Can you give me more options? | Ask_alternatives |
| 10 | Bot | Sure, I have two more options for you. The first is Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. The second is Autumn House, a 4-star guesthouse with a 37% discount on bookings for the next 2 days and free dinner. | Multioption_suggestion |
| 11 | User | What are the differences between Carolina Bed and Breakfast and Autumn House? | Ask_differences |
| 12 | Bot | Carolina Bed and Breakfast has a pool, bar, BBQ grill, and Jacuzzi. Autumn House has a DJ floor and fully safe, sanitary, and secure rooms. | Provide_differences |
| 13 | User | I'm interested in Leverton House, but it's a bit over my budget. Can you offer a lower price? | Negotiation |
| 14 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation |
| 15 | User | Can you remove the gym and pool facilities? | Negotiation |
| 16 | Bot | Sure, I can remove those facilities and offer you a 10% discount. | Provide_negotiation |
| 17 | User | Okay, I'll take the offer. | Selection |
| 18 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation, Ask_details |
| 19 | User | My name is John Smith, my email is johnsmith@gmail.com, there will be two people, and we prefer a double room. | Inform |
| 20 | Bot | Thank you, John. Your booking is confirmed. You can contact us at 123-456-7890 for any further queries. | Confirmation |
| 21 | User | Can I add breakfast to my booking? | Add_aspect_X |
| 22 | Bot | Sure, breakfast can be added for an additional £10 per person per day. Would you like to add it? | Add_aspect_X |
| 23 | User | Yes, please add breakfast for both of us. | Add_aspect_X |
| 24 | Bot | Noted. Your booking has been updated. | Confirmation |
| 25 | User | Can I change my check-in date to the 16th? | Add_aspect_X |
| 26 | Bot | Let me check if that's possible. Yes, it's possible. Your booking has been updated. | Confirmation |
| 27 | User | Can I cancel my booking? | Add_aspect_X |
| 28 | Bot | Yes, you can cancel your booking. However, there will be a cancellation fee of £50. | Add_aspect_X |
| 29 | User | Okay, I'll keep that in mind. Thank you. | Goodbye |
| 30 | Bot | You're welcome. Have a great day! | Goodbye |
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the West area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. The Cambridge Belfry, Huntingdon Marriott Hotel, and Hobsons House. Which one would you like to know more about? | Multioption_suggestion
5 | User | What are the differences between the options? | Ask_differences
6 | Bot | The Cambridge Belfry is a 4-star hotel with a gym, pool, and jacuzzi. The Huntingdon Marriott Hotel is a luxurious 4-star hotel with a DJ floor and free dinner. Hobsons House is a 3-star guesthouse with a 32% discount and free dinner. | Provide_differences
7 | User | Can you tell me more about the Cambridge Belfry? | Add_aspect_X
8 | Bot | The Cambridge Belfry is a 4-star hotel located in West Cambourne. It offers free breakfast, 24/7 room service, free wifi, and great food. The hotel has spacious and luxurious rooms, a gym, pool, and jacuzzi. It has been endorsed by popular tour agencies like Expedia and received prestigious awards such as Cateys. The hotel has hosted celebrities like Virat Kholi, Eminem, Tom Holland, and Jackie Chan. The head chef has a cookbook named "How to Burger". The hotel is popular with locals, international tourists, and tour agencies, and has a huge social media presence. | Provide_details
9 | User | That sounds great, but what about the Huntingdon Marriott Hotel? | Ask_alternatives
10 | Bot | The Huntingdon Marriott Hotel is a luxurious 4-star hotel located in the west area of Huntingdon. It offers free wifi, parking, gym, pool, bar, and DJ floor. The hotel has spacious and luxurious rooms with excellent 24/7 room service and friendly staff. It has received prestigious awards such as Michelin Star and has been endorsed by popular tour agencies such as Expedia. The hotel has hosted celebrities such as Virat Kholi, Tom Holland, and Jackie Chan. It has also appeared in famous magazines like Today's Hotelier, BigHospitality, and The World of Hospitality. The hotel is expensive but offers a free breakfast and is currently running a food festival with free dinner for guests. It is popular with the locals and has a huge social media presence with an 8/10 rating. | Provide_details
11 | User | Can you tell me more about the food festival at Huntingdon Marriott Hotel? | Add_aspect_X
12 | Bot | The food festival at Huntingdon Marriott Hotel offers free dinner for guests. It's a great opportunity to try out some delicious food. | Provide_details
13 | User | I'm interested in the Cambridge Belfry, but it's a bit expensive. Can you offer a lower price? | Negotiation
14 | Bot | I can offer a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation
15 | User | Can you remove the jacuzzi? | Negotiation
16 | Bot | Sure, I can remove the jacuzzi. The new price will be £135 per night. | Provide_negotiation
17 | User | That's still a bit high. Can you offer a lower price? | Negotiation
18 | Bot | I'm sorry, but that's the best I can do. | Deny
19 | User | Okay, I'll go with the Cambridge Belfry. | Selection
20 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, and contact number for confirmation. | Confirmation
21 | User | My name is John Smith, my email is johnsmith@gmail.com, and my contact number is 1234567890. | Ask_details
22 | Bot | Thank you, John. Your booking is confirmed. Is there anything else I can help you with? | Goodbye
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have three options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive option, but it offers a gym and a pool. The A and B Guest House has a BBQ grill and a Jacuzzi. Allenbell guesthouse has a bar and spacious luxurious rooms. | Provide_differences |
| 9 | User | Can you give me more options? | Ask_alternatives |
| 10 | Bot | Sure, I have two more options for you. The first is Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. The second is Autumn House, a 4-star guesthouse with a 37% discount on bookings for the next 2 days and free dinner. | Multioption_suggestion |
| 11 | User | What are the differences between Carolina Bed and Breakfast and Autumn House? | Ask_differences |
| 12 | Bot | Carolina Bed and Breakfast has a pool, bar, and BBQ grill. Autumn House has a DJ floor and fully safe, sanitary, and secure rooms. | Provide_differences |
| 13 | User | I'm interested in Leverton House, but it's a bit over my budget. Can you offer a lower price? | Negotiation |
| 14 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation |
| 15 | User | Can you remove the gym and keep the pool? | Negotiation |
| 16 | Bot | I'm sorry, but the gym and pool are part of a package deal. However, I can offer you a 5% discount without removing any facilities. | Provide_negotiation |
| 17 | User | Okay, I'll take the 5% discount. | Selection |
| 18 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation, Ask_details |
| 19 | User | My name is John Smith, my email is johnsmith@gmail.com, there will be two people, and we prefer a double room. | Inform |
| 20 | Bot | Thank you, John. Your booking is confirmed. You will receive an email with the details. | Confirmation |
| 21 | User | Can I ask more questions about the hotel? | Ask_alternatives |
| 22 | Bot | Of course, what would you like to know? | Ask_details |
| 23 | User | Does Leverton House have any famous guests? | Add_aspect_X |
| 24 | Bot | Yes, Leverton House has hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. It has also been endorsed by famous critics like Pete Wells and Jonathan Gold. | Inform |
| 25 | User | That's impressive. What about the A and B Guest House? | Ask_details |
| 26 | Bot | The A and B Guest House has also hosted celebrities like Virat Kholi, Tom Holland, and Jackie Chan. The head chef has a cookbook named "Put me to Sleep". | Inform |
| 27 | User | Thank you for the information. I'll let you know if I have any more questions. | Goodbye |
| 28 | Bot | You're welcome. Have a great day! | Goodbye |
| 29 | User | Actually, can you suggest a hotel with a Michelin Star? | Add_aspect_X |
| 30 | Bot | Sure, Allenbell guesthouse and Carolina Bed and Breakfast both have Michelin Stars. | Inform |
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, here are three options: Rosa's Bed and Breakfast, The Bridge Guest House, and Aylesbray Lodge Guest House. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between them? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse with luxurious rooms, a gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, a gym, pool, bar, and BBQ grill. Which one interests you? | Provide_differences
9 | User | Can you tell me more about Rosa's Bed and Breakfast? | Add_aspect_X
10 | Bot | Sure, Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. The hotel is currently offering a 33% discount on bookings for the next 4 days. It is popular with locals, international tourists, and tour agencies and has a perfect rating of 10/10. | Provide_differences
11 | User | That sounds great, but it's a bit expensive. Can you suggest something cheaper? | Negotiation
12 | Bot | I understand. The Bridge Guest House is a 3-star guesthouse with moderate pricing. Double rooms are priced at £75, family rooms at £90, and single rooms at £50. | Provide_negotiation
13 | User | Can you tell me more about The Bridge Guest House? | Add_aspect_X
14 | Bot | The Bridge Guest House is a 3-star guesthouse located in the south area of Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has received recognitions from local magazines like MrHotel and Food and beyond, local tour agencies like TourMe, Travel Partner, and Buddy's travel, and local awards such as Food fest, Budget, and Great and Escape. | Provide_differences
15 | User | That sounds good. Can you suggest something else? | Ask_alternatives
16 | Bot | Sure, how about The Lensfield Hotel? It's a 3-star hotel located in South Cambridge. It offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. The hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. The hotel has a public image rating of 6/10. | Multioption_suggestion
17 | User | Can you tell me more about Aylesbray Lodge Guest House? | Add_aspect_X
18 | Bot | Aylesbray Lodge Guest House is a 4-star hotel located in South with free internet and parking. The hotel offers moderate prices for single, double, and family rooms. It has excellent 24/7 room service, free breakfast, and free wifi. The hotel features a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms that are fully safe, sanitary, and secure. Aylesbray Lodge Guest House has been recognized by famous magazines, tour agencies, and critics. It has hosted celebrities like Ronaldo, Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named Dine with Me. The hotel is currently offering a 30% discount on bookings for the next 2 days, with only 2 rooms left. It is popular with locals, tour agencies, and has a huge social media presence with an 8/10 rating. | Provide_differences
19 | User | That sounds good. Can you tell me more about the discount? | Add_aspect_X
20 | Bot | The discount is valid for the next 2 days and is 30% off the regular price. There are only 2 rooms left, so you'll need to book soon if you're interested. | Provide_differences
21 | User | Can you tell me more about the facilities at The Lensfield Hotel? | Add_aspect_X
22 | Bot | The Lensfield Hotel offers free breakfast, free wifi, and excellent 24/7 room service. The hotel has friendly staff, delicious food, and very clean rooms. It also has a safe and offers parking and internet. | Provide_differences
23 | User | I'm still not sure. Can you give me some time to decide? | Selection
24 | Bot | Of course, take your time. Let me know if you have any other questions. | Affirm
25 | User | Can you tell me more about the rooms at Rosa's Bed and Breakfast? | Add_aspect_X
26 | Bot | Rosa's Bed and Breakfast offers spacious and luxurious rooms with free internet and parking. | Provide_differences
27 | User | Can you tell me more about the food at Aylesbray Lodge Guest House? | Add_aspect_X
28 | Bot | Aylesbray Lodge Guest House has a head chef with a cookbook named Dine with Me. The hotel offers free breakfast and has a bar and BBQ grill. | Provide_differences
29 | User | Can you tell me more about the parking at The Bridge Guest House? | Add_aspect_X
30 | Bot | The Bridge Guest House offers parking facilities. | Provide_differences
31 | User | I've decided to go with Aylesbray Lodge Guest House. | Selection
32 | Bot | Great choice! Can I have your name, email, and phone number for the booking? | Ask_details
33 | User | My name is John Smith, my email is johnsmith@gmail.com, and my phone number is 123-456-7890. | Inform
34 | Bot | Thank you, John. Your booking has been confirmed. Your registration number is 123456. You'll receive a confirmation email shortly. | Confirmation
35 | User | Thank you. | Affirm
36 | Bot | Is there anything else I can help you with? | Affirm
37 | User | No, that's all. | Goodbye
38 | Bot | Have a great day! | Goodbye
Utterance # | Speaker | Utterance | Intent
--- | --- | --- | ---
1 | User | Hi, I'm looking for a hotel in the South area. | Greet, Lookup
2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details
3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform
4 | Bot | Great, I have a few options for you. How many people will be staying? | Ask_details
5 | User | It'll be just me. | Inform
6 | Bot | Alright, here are three options: Rosa's Bed and Breakfast, The Bridge Guest House, and Aylesbray Lodge Guest House. Which one would you like to know more about? | Multioption_suggestion
7 | User | What are the differences between them? | Ask_differences
8 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse with luxurious rooms, gym, pool, bar, and BBQ grill. The Bridge Guest House is a 3-star guesthouse with friendly staff, delicious food, and very clean rooms. Aylesbray Lodge Guest House is a 4-star hotel with excellent 24/7 room service, gym, pool, bar, and BBQ grill. | Provide_differences
9 | User | How much does each option cost? | Add_aspect_price
10 | Bot | Rosa's Bed and Breakfast is currently offering a 33% discount, with double rooms priced at £100, family rooms at £150, and single rooms at £75. The Bridge Guest House has double rooms at £75, family rooms at £90, and single rooms at £50. Aylesbray Lodge Guest House is currently offering a 30% discount, with double rooms priced at £105, family rooms at £135, and single rooms at £80. | Provide_differences
11 | User | Can you suggest more options? | Ask_alternatives
12 | Bot | Sure, how about The Lensfield Hotel? It's a 3-star hotel with free breakfast, free wifi, and excellent 24/7 room service. It has friendly staff, delicious food, and very clean rooms. | Multioption_suggestion
13 | User | How much does it cost? | Add_aspect_price
14 | Bot | The Lensfield Hotel is expensive, with double rooms priced at £90, family rooms at £125, and single rooms at £65. It also has an offer of 30% off on bookings for the next 3 days. | Provide_differences
15 | User | Can you tell me more about Rosa's Bed and Breakfast? | Selection
16 | Bot | Rosa's Bed and Breakfast is a 4-star guesthouse located in South with free internet and parking. The hotel offers spacious and luxurious rooms with great food, gym, pool, bar, and BBQ grill. It has been recognized by famous magazines, tour agencies, and critics and has hosted celebrities like Ronaldo and Jackie Chan. | Provide_details
17 | User | Can I negotiate the price? | Negotiation
18 | Bot | We can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
19 | User | Can I get a higher priced option for the price of the cheaper option? | Negotiation
20 | Bot | I'm sorry, but the prices are fixed. However, I can assure you that Rosa's Bed and Breakfast is worth the price. | Provide_negotiation
21 | User | Can you tell me more about Aylesbray Lodge Guest House? | Selection
22 | Bot | Aylesbray Lodge Guest House is a 4-star hotel located in South with free internet and parking. The hotel offers moderate prices for single, double, and family rooms. It has excellent 24/7 room service, free breakfast, and free wifi. The hotel features a gym, pool, bar, and BBQ grill. It has spacious and luxurious rooms that are fully safe, sanitary, and secure. Aylesbray Lodge Guest House has been recognized by famous magazines, tour agencies, and critics. It has hosted celebrities like Ronaldo, Virat Kholi, Eminem, and Jackie Chan. The head chef has a cookbook named Dine with Me. The hotel is currently offering a 30% discount on bookings for the next 2 days, with only 2 rooms left. It is popular with locals, tour agencies, and has a huge social media presence with an 8/10 rating. | Provide_details
23 | User | Can I negotiate the price for Aylesbray Lodge Guest House? | Negotiation
24 | Bot | We can negotiate up to 10% of the suggested price, but some of the facilities provided might get removed. | Provide_negotiation
25 | User | Can you suggest more options? | Ask_alternatives
26 | Bot | Sure, I'll look up some more options for you. What other criteria are you looking for? | Add_aspect_X
27 | User | I'd like a hotel with a spa. | Add_aspect_spa
28 | Bot | Alright, I have two options for you: The Varsity Hotel & Spa and The Gonville Hotel. Which one would you like to know more about? | Multioption_suggestion
29 | User | What are the differences between them? | Ask_differences
30 | Bot | The Varsity Hotel & Spa is a 4-star hotel with a rooftop bar, spa, and gym. It has luxurious rooms with free wifi and parking. The Gonville Hotel is a 4-star hotel with a spa, gym, and restaurant. It has spacious and comfortable rooms with free wifi and parking. | Provide_differences
31 | User | How much do they cost? | Add_aspect_price
32 | Bot | The Varsity Hotel & Spa has double rooms priced at £200, family rooms at £300, and single rooms at £150. The Gonville Hotel has double rooms priced at £180, family rooms at £250, and single rooms at £120. | Provide_differences
33 | User | Can you suggest more options? | Ask_alternatives
34 | Bot | Sure, what other criteria are you looking for? | Add_aspect_X
35 | User | I'd like a hotel with a pool. | Add_aspect_pool
36 | Bot | Alright, I have two options for you: The Tamburlaine Hotel and The Cambridge Belfry. Which one would you like to know more about? | Multioption_suggestion
37 | User | What are the differences between them? | Ask_differences
38 | Bot | The Tamburlaine Hotel is a 4-star hotel with a pool, gym, and restaurant. It has luxurious rooms with free wifi and parking. The Cambridge Belfry is a 4-star hotel with a pool, gym, and spa. It has spacious and comfortable rooms with free wifi and parking. | Provide_differences
39 | User | How much do they cost? | Add_aspect_price
40 | Bot | The Tamburlaine Hotel has double rooms priced at £180, family rooms at £250, and single rooms at £120. The Cambridge Belfry has double rooms priced at £200, family rooms at £300, and single rooms at £150. | Provide_differences
41 | User | Can you suggest more options? | Ask_alternatives
42 | Bot | I'm sorry, but those are all the options I have for your criteria. Which one would you like to book? | Selection
43 | User | I need some time to decide. Can I get back to you later? | Goodbye
| Utterance Number | Speaker | Utterance | Intent |
| --- | --- | --- | --- |
| 1 | User | Hi, I'm looking for a hotel in the East area of Cambridge. | Greet, Lookup |
| 2 | Bot | Sure, when do you plan to check-in and check-out? | Ask_details |
| 3 | User | I'll be checking in on the 15th and checking out on the 18th. | Inform |
| 4 | Bot | Great, I have a few options for you. How much is your estimated budget? | Add_aspect_X |
| 5 | User | My budget is around £150 per night. | Add_aspect_X |
| 6 | Bot | I have three options for you. The first is Leverton House, a 4-star guesthouse with a food festival and a 38% discount on bookings for the next 3 days. The second is The A and B Guest House, a 4-star guesthouse with a food festival and discounts on bookings. The third is Allenbell guesthouse, a 4-star hotel with affordable prices and a strong social media presence. | Multioption_suggestion |
| 7 | User | What are the differences between the options? | Ask_differences |
| 8 | Bot | Leverton House is the most expensive option, but it offers a gym and a pool. The A and B Guest House has a BBQ grill and a Jacuzzi. Allenbell guesthouse has a bar and spacious luxurious rooms. | Provide_differences |
| 9 | User | Can you give me more options? | Ask_alternatives |
| 10 | Bot | Sure, I have two more options for you. The first is Carolina Bed and Breakfast, a 4-star guesthouse with a food festival and 29% off on bookings for the next 3 days. The second is Autumn House, a 4-star guesthouse with a 37% discount on bookings for the next 2 days and free dinner. | Multioption_suggestion |
| 11 | User | What are the differences between Carolina Bed and Breakfast and Autumn House? | Ask_differences |
| 12 | Bot | Carolina Bed and Breakfast has a pool, bar, BBQ grill, and Jacuzzi. Autumn House has a DJ floor and fully safe, sanitary, and secure rooms. | Provide_differences |
| 13 | User | I'm interested in Leverton House, but it's a bit over my budget. Can you offer a lower price? | Negotiation |
| 14 | Bot | I can offer you a 10% discount, but some of the facilities provided might get removed. | Provide_negotiation |
| 15 | User | Can you remove the gym and pool facilities? | Negotiation |
| 16 | Bot | Sure, I can remove those facilities and offer you a 10% discount. | Provide_negotiation |
| 17 | User | Okay, I'll take the offer. | Selection |
| 18 | Bot | Great, the hotel has been reserved. Your registration number is 123456. Please provide your name, email, no. of people, and room preference. | Confirmation, Ask_details |
| 19 | User | My name is John Smith, my email is johnsmith@gmail.com, there will be two people, and we prefer a double room. | Inform |
| 20 | Bot | Thank you, John. Your booking is confirmed. You can contact us at 123-456-7890 for any further queries. | Confirmation |
| 21 | User | Thank you. | Goodbye |
| 22 | Bot | Thank you for choosing our hotel. Have a great day! | Goodbye |
