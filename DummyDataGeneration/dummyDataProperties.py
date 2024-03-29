#  -----------------------------------------------------------------------
#  Copyright (c) 2022.
#  Author: Amey Bhilegaonkar
#  Copyright (c) Amey Bhilegaonkar. All rights reserved.
#  Developer Email: bhilegaonkar11@gmail.com
#  -----------------------------------------------------------------------

Gender = ['M', 'F']

MaleName = ['Aadi', 'Aarav', 'Aarnav', 'Aarush', 'Aayush', 'Abdul', 'Abeer', 'Abhimanyu', 'Abhiramnew', 'Aditya',
            'Advaith', 'Advay', 'Advik', 'Agastya', 'Akshay', 'Amol', 'Anay', 'Anirudh', 'Anmol', 'Ansh', 'Arin',
            'Arjun', 'Arnav', 'Aryan', 'Atharv', 'Avi', 'Ayaan', 'Ayush', 'Ayushman', 'Azaan', 'Azad', 'Adnan',
            'Brijesh', 'Bachittar', 'Bahadurjit', 'Bakhshi', 'Balendra', 'Balhaar', 'Baljiwan', 'Balvan', 'Balveer',
            'Banjeet', 'Chaitanya', 'Chakradev', 'Chakradhar', 'Champak', 'Chanakya', 'Chandran', 'Chandresh', 'Charan',
            'Chatresh', 'Chatura', 'Daksh', 'Darsh', 'Dev', 'Devansh', 'Dhruv', 'Dakshesh', 'Dalbir', 'Darpan',
            'Ekansh', 'Ekalinga', 'Ekapad', 'Ekavir', 'Ekaraj', 'Ekbal', 'Farhan', 'Falan', 'Faqid', 'Faraj', 'Faras',
            'Fitan', 'Fariq', 'Faris', 'Fiyaz', 'Frado', 'Gautam', 'Gagan', 'Gaurang', 'Girik', 'Girindra', 'Girish',
            'Gopal', 'Gaurav', 'Gunbir', 'Guneet', 'Harsh', 'Harshil', 'Hredhaan', 'Hardik', 'Harish', 'Hritik',
            'Hitesh', 'Hemang', 'Isaac', 'Ishaan', 'Imaran', 'Indrajit', 'Ikbal', 'Ishwar', 'Jainew', 'Jason',
            'Jagdish', 'Jagat', 'Jatin', 'Jai', 'Jairaj', 'Jeet', 'Kabir', 'Kalpit', 'Karan', 'Kiaan', 'Krish',
            'Krishna', 'Laksh', 'Lakshay', 'Lucky', 'Lakshit', 'Lohit', 'Laban', 'Manan', 'Mohammed', 'Madhav',
            'Mitesh', 'Maanas', 'Manbir', 'Maanav', 'Manthan', 'Nachiket', 'Naksh', 'Nakul', 'Neel', 'Nakul', 'Naveen',
            'Nihal', 'Nitesh', 'Om', 'Ojas', 'Omkaar', 'Onkar', 'Onveer', 'Orinder', 'Parth', 'Pranav', 'Praneel',
            'Pranit', 'Pratyush', 'Parimal', 'Qabil', 'Qadim', 'Qarin', 'Qasim', 'Rachit', 'Raghav', 'Ranbir',
            'Ranveer', 'Rayaan', 'Rehaannew', 'Reyansh', 'Rishi', 'Rohan', 'Ronith', 'Rudranew', 'Rushil', 'Ryan',
            'Sai', 'Saksham', 'Samaksh', 'Samar', 'Samarth', 'Samesh', 'Sarthak', 'Sathvi', 'Shaurya', 'Shivansh',
            'Siddharth', 'Tejas', 'Tanay', 'Tanish', 'Tarak', 'Teerth', 'Tanveer', 'Udant', 'Udarsh', 'Utkarsh',
            'Umang', 'Upkaar', 'Vedant', 'Veer', 'Viaannew', 'Vihaan', 'Viraj', 'Vivaan', 'Wahab', 'Wazir', 'Warinder',
            'Warjas', 'Wriddhish', 'Wridesh', 'Yash', 'Yug', 'Yatin', 'Yuvraj', 'Yagnesh', 'Yatan', 'Zayan', 'Zaid',
            'Zayyan', 'Zashil', 'Zehaan', ]

FemaleName = ['Aadhya', 'Aahana', 'Aalia', 'Aanya', 'Aaradhya', 'Aarna', 'Aarohi', 'Aditi', 'Advika', 'Adweta', 'Adya',
              'Ahana', 'Akshara', 'Amaira', 'Amaya', 'Amrita', 'Amruta', 'Anaisha', 'Anaya', 'Andrea', 'Anvi', 'Anya',
              'Aria', 'Arunima', 'Arya', 'Avni', 'Bhavna', 'Bhagyasri', 'Baghyawati', 'Bhanumati', 'Bhavani', 'Binita',
              'Bishakha', 'Brinda', 'Bina', 'Bimala', 'Bhavini', 'Chaaya', 'Chaitaly', 'Chakrika', 'Chaman', 'Chameli',
              'Chanchal', 'Chandani', 'Charita', 'Chasmum', 'Chavvi', 'Daksha', 'Dhriti', 'Divya', 'Diya', 'Dalaja',
              'Damini', 'Damyanti', 'Darika', 'Dayamai', 'Dayita', 'Deepa', 'Ekaja', 'Ekani', 'Ekanta', 'Ekta', 'Ela',
              'Eshana', 'Eta', 'Ekantika', 'Ella', 'Ekiya', 'Falguni', 'Forum', 'Faiza', 'Falak', 'Farisha', 'Fatheha',
              'Farzeen', 'Farida', 'Gauri', 'Geet', 'Geetika', 'Ganga', 'Garima', 'Gaurangi', 'Garima', 'Gayathri',
              'Gaurika', 'Gautami', 'Hiral', 'Harini', 'Hemangini', 'Hema', 'Harinakshi', 'Harita', 'Hemal', 'Hemani',
              'Heena', 'Ira', 'Isha', 'Ishani', 'Ishanvi', 'Ishita', 'Idika', 'Idris', 'Ijaya', 'Ikshita', 'Indali',
              'Jasmine', 'Jhanvi', 'Jagrati', 'Jagvi', 'Jalsa', 'Janaki', 'Januja', 'Janya', 'Jasmit', 'Jeevika',
              'Jhalak', 'Kashvi', 'Kavya', 'Khushi', 'Kiara', 'Krisha', 'Krishna', 'Kyra', 'Kajal', 'Kamya', 'Kashika',
              'Lakshmi', 'Lipika', 'Lolita', 'Lopa', 'Lekha', 'Leena', 'Libni', 'Lochan', 'Ladli', 'Lajita', 'Mahika',
              'Manya', 'Maryam', 'Meera', 'Megha', 'Meghana', 'Meher', 'Mishka', 'Mitali', 'Myra', 'Naira', 'Navya',
              'Nayantara', 'Niharika', 'Nisha', 'Nitara', 'Netra', 'Nidra', 'Nikita', 'Nilima', 'Olivia', 'Omaja',
              'Omisha', 'Oni', 'Opal', 'Ojasvi', 'Omya', 'Osha', 'Odika', 'Oeshi', 'Pari', 'Pihu', 'Pratyusha',
              'Prisha', 'Pahal', 'Palak', 'Panini', 'Pallavi', 'Parul', 'Pavani', 'Qushi', 'Qiyara', 'Quasar', 'Queeni',
              'Quincy', 'Qayanat', 'Rachita', 'Raveena', 'Ridhi', 'Riya', 'Rabhya', 'Rachana', 'Radha', 'Rajata',
              'Rajeshri', 'Raksha', 'Saanvi', 'Sahana', 'Sai', 'Saira', 'Samaira', 'Sarah', 'Saumya', 'Shanaya',
              'Shravya', 'Shreya', 'Sneha', 'Suhana', 'Suhani', 'Tanvi', 'Trisha', 'Tanmayi', 'Tamanna', 'Tanuja',
              'Tripti', 'Triveni', 'Triya', 'Turvi', 'Tulsi', 'Ucchal', 'Ubika', 'Udyati', 'Unnati', 'Unni',
              'Upadhriti', 'Urishilla', 'Urmi', 'Upma', 'Upasna', 'Vaishnavi', 'Vansha', 'Vanya', 'Vedhika', 'Vinaya',
              'Vamakshi', 'Vamika', 'Vasana', 'Vasatika', 'Vasudha', 'Waida', 'Warda', 'Wishi', 'Wafiya', 'Watika',
              'Waheeda', 'Wakeeta', 'Widisha', 'Yachana', 'Yadavi', 'Yahvi', 'Yashawini', 'Yashica', 'Yashoda',
              'Yashodhara', 'Yasti', 'Yauvani', 'Yochana', 'Zara', 'Zoya', 'Zoey', 'Zora', 'Zuri', 'Zaha', 'Zaida',
              'Zarna', 'Zenia', 'Zivah']

lastName = ['Acharya', 'Agarwal', 'Agate', 'Aggarwal', 'Agrawal', 'Ahluwalia', 'Ahuja', 'Amble', 'Anand', 'Andra',
            'Anne', 'Apte', 'Arora', 'Arya', 'Atwal', 'Aurora', 'Babu', 'Badal', 'Badami', 'Bahl', 'Bahri', 'Bail',
            'Bains', 'Bajaj', 'Bajwa', 'Bakshi', 'Bal', 'Bala', 'Bala', 'Balakrishnan', 'Balan', 'Balasubramanian',
            'Balay', 'Bali', 'Bandi', 'Banerjee', 'Banik', 'Bansal', 'Barad', 'Barad', 'Baral', 'Baria', 'Barman',
            'Basak', 'Bassi', 'Basu', 'Bath', 'Batra', 'Batta', 'Bava', 'Bawa', 'Bedi', 'Behl', 'Bhagat', 'Bhakta',
            'Bhalla', 'Bhandari', 'Bhardwaj', 'Bhargava', 'Bhasin', 'Bhat', 'Bhatia', 'Bhatnagar', 'Bhatt',
            'Bhattacharyya', 'Bhatti', 'Bhavsar', 'Bir', 'Biswas', 'Boase', 'Bobal', 'Bora', 'Bora', 'Borah', 'Borde',
            'Borra', 'Bose', 'Brahmbhatt', 'Brar', 'Buch', 'Buch', 'Bumb', 'Butala', 'Chacko', 'Chad', 'Chada',
            'Chadha', 'Chahal', 'Chakrabarti', 'Chakraborty', 'Chana', 'Chand', 'Chanda', 'Chander', 'Chandra',
            'Chandran', 'Char', 'Chatterjee', 'Dalal', 'Dani', 'Dar', 'Dara', 'Dara', 'Das', 'Dasgupta', 'Dash', 'Dass',
            'Date', 'Datta', 'Dave', 'Dayal', 'Dey', 'Deep', 'Deo', 'Deol', 'Desai', 'Deshmukh', 'Deshpande', 'Devan',
            'Devi', 'Dewan', 'Dey', 'Dhaliwal', 'Dhar', 'Dhar', 'Dhawan', 'Dhillon', 'Dhingra', 'Din', 'Divan', 'Dixit',
            'Doctor', 'Dora', 'Doshi', 'Dua', 'Dube', 'Dubey', 'Dugal', 'Dugar', 'Dugar', 'Dutt', 'Dutta', 'Dyal',
            'Edwin', 'Gaba', 'Gade', 'Gala', 'Gandhi', 'Ganesan', 'Ganesh', 'Ganguly', 'Gara', 'Garde', 'Garg', 'Gera',
            'Ghose', 'Ghosh', 'Gill', 'Goda', 'Goel', 'Gokhale', 'Gola', 'Gole', 'Golla', 'Gopal', 'Goswami', 'Gour',
            'Goyal', 'Grewal', 'Grover', 'Guha', 'Gulati', 'Gupta', 'Halder', 'Handa', 'Hans', 'Hari', 'Hayer',
            'Mathai', 'Mathur', 'Matthai', 'Meda', 'Mehan', 'Mehra', 'Mehrotra', 'Mehta', 'Meka', 'Memon', 'Menon',
            'Merchant', 'Minhas', 'Mishra', 'Misra', 'Mistry', 'Mital', 'Mitra', 'Mittal', 'Mitter', 'Modi', 'Mody',
            'Mohan', 'Mohanty', 'Morar', 'More', 'Mukherjee', 'Mukhopadhyay', 'Muni', 'Munshi', 'Murthy', 'Murty',
            'Mutti', 'Nadig', 'Nadkarni', 'Nagar', 'Nagarajan', 'Nagi', 'Nagy', 'Naidu', 'Naik', 'Nair', 'Nanda',
            'Narain', 'Narang', 'Narasimhan', 'Narayan', 'Narayanan', 'Narula', 'Natarajan', 'Nath', 'Natt', 'Nayak',
            'Nayar', 'Nazareth', 'Nigam', 'Nori', 'Oak', 'Om', 'Oommen', 'Oza', 'Padmanabhan', 'Pai', 'Pal', 'Palan',
            'Pall', 'Palla', 'Palla', 'Panchal', 'Pandey', 'Pandit', 'Pandya', 'Pant', 'Parekh', 'Parikh', 'Parmar',
            'Parmer', 'Parsa', 'Patel', 'Pathak', 'Patil', 'Patla', 'Patla', 'Pau', 'Peri', 'Pillai', 'Pillay',
            'Pingle', 'Prabhakar', 'Prabhu', 'Pradhan', 'Prakash', 'Prasad', 'Prashad', 'Puri', 'Purohit',
            'Radhakrishnan', 'Raghavan', 'Rai']

studentRegId = ['C2K181{}', 'I2K181{}', 'E2K181{}']

