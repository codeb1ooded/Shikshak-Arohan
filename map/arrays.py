from array import *

state = [ 'Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam',
          'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi',
          'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand',
          'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya',
          'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
          'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Telangana']

state_ids = [ 'AndamanNicobarIslands', 'AndhraPradesh', 'ArunachalPradesh', 'Assam',
          'Bihar', 'Chandigarh', 'Chhattisgarh', 'DadraNagarHaveli', 'DamanDiu', 'Delhi',
          'Goa', 'Gujarat', 'Haryana', 'HimachalPradesh', 'JammuKashmir', 'Jharkhand',
          'Karnataka', 'Kerala', 'Lakshadweep', 'MadhyaPradesh', 'Maharashtra', 'Manipur', 'Meghalaya',
          'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'TamilNadu',
          'Tripura', 'UttarPradesh', 'Uttarakhand', 'WestBengal', 'Telangana']

state_id_int = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014',
            '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028',
            '029', '030', '031', '032', '033', '034', '035', '036']

addr = [
'Baksa'   ,      'Mushalpur',
'Barpeta'  ,     'Barpeta',
'Bishwanath',	'Bishwanath Chariali',
'Bongaigaon'	,'Bongaigaon',
'Cachar',	'Silchar',
'Charaideo', 	'Sonari',
'Chirang'	,'Kajalgaon' ,
'Darrang',	'Mangaldoi',
'Dhemaji'	,'Dhemaji',
'Dhubri',	'Dhubri' ,
'Dibrugarh',	'Dibrugarh',
'Dima Hasao',	'Haflong',
'Goalpara'	,'Goalpara',
'Golaghat'	,'Golaghat',
'Hailakandi',	'Hailakandi',
'Hojai',	'Hojai'		,
'Jorhat',	'Jorhat',
'Kamrup'	,'Amingaon',
'Kamrup Metropolitan',	'Guwahati' ,
'Karbi Anglong',	'Diphu',
'Karimganj',	'Karimganj',
'Kokrajhar','Kokrajhar',
'Lakhimpur',	'North Lakhimpur',
'Majuli'	,'Garamur'	,
'Morigaon'	,'Marigaon',
'Nagaon',	'Nagaon',
'Nalbari',	'Nalbari',
'Sivasagar',	'Sibsagar',
'South', 'Salmara-Mankachar',
'Sonitpur',	'Tezpur' ,
'Tinsukia',	'Tinsukia',
'Udalguri',	'Udalguri',
'West Karbi Anglong',	'Hamren' ]
