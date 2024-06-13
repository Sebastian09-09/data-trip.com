import os 
import pandas 

for hotelid in os.listdir(r'E:\development\Internship\trip.com\node\data-trip.com\data'):#[-1:]:
    with open(f'data/{hotelid}','r',encoding='utf-8') as f:
        data=f.readlines()

    name = "" 
    room = "" 
    stayed = "" 
    gat = "" 
    reviews = "" 
    rating = "" 
    posted = "" 
    msg = "" 
    info = 0

    for i in data:
        Finaldata = {
            'url': [],
            'name': [],
            'room': [],
            'stayed': [],
            'gat': [],
            'reviews': [],
            'rating': [],
            'posted': [],
            'msg': []
        }
        if i.startswith('name:'):
            name = i[5:].strip()
        
        elif i.startswith('info:'):
            if info == 0:
                room = i[5:].strip()
                info += 1
            elif info == 1:
                stayed = i[5:].strip()
                info += 1
            elif info == 2:
                gat = i[5:].strip()
                info += 1
            elif info == 3:
                reviews = i[5:].strip()
                info = 0
        
        elif i.startswith('rating:'):
            rating = i[7:].strip()
        
        elif i.startswith('posted:'):
            posted = i[7:].strip()
        
        elif i.startswith('msg:'):
            msg = i[4:]
        
        elif i.startswith('----'):
            Finaldata['url'].append(f'https://www.trip.com/hotels/detail/?hotelId={hotelid[:-4]}')
            Finaldata['name'].append(name)
            Finaldata['room'].append(room)
            Finaldata['stayed'].append(stayed)
            Finaldata['gat'].append(gat)
            Finaldata['reviews'].append(reviews)
            Finaldata['rating'].append(rating)
            Finaldata['posted'].append(posted)
            Finaldata['msg'].append(msg.strip())

            df = pandas.DataFrame(Finaldata)
            df.to_csv('data.csv', header=False, index=False, mode='a', encoding='utf-8')
            print(hotelid[:-4],name)

            name = "" 
            room = "" 
            stayed = "" 
            gat = "" 
            reviews = "" 
            rating = "" 
            posted = "" 
            msg = "" 
            info = 0
        
        else:
            msg += i
