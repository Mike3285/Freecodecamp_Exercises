def add_time(start, duration, day=None):
    m0 = int(start.split(' ')[0].split(':')[1])
    h0 = int(start.split(' ')[0].split(':')[0])
    m1 = int(duration.split(':')[1])
    h1 = int(duration.split(':')[0])
    meridian = start.split(' ')[1].lower()
    if meridian == 'pm':
        h0 = h0 + 12
    d_to_add = h1 // 24
    h_to_add = h1 % 24
    new_h = h0 + h_to_add
    tot_m = m0 + m1
    if tot_m >= 60:
        new_h += tot_m // 60
        new_m_str = tot_m % 60
    else:
        new_m_str = tot_m
    new_m_str = str(new_m_str).zfill(2)
    if new_h >= 24:
        d_to_add += new_h // 24
        new_h = new_h % 24
    if new_h > 12:
        new_h_str = str(new_h - 12) + f":{new_m_str}" + ' PM'
    elif new_h == 12:
        new_h_str = str(new_h) + f":{new_m_str}" + ' PM'
    elif new_h == 0:
        new_h_str = str(new_h+12) + f":{new_m_str}" + ' AM'
    else:
        new_h_str = str(new_h) + f":{str(new_m_str).zfill(2)}" + ' AM'
    new_time = f"{new_h_str}"
    if day:
        week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = day.lower()
        day_i = week.index(day)
        new_day = week[(day_i+d_to_add) % 7]
        new_time += f", {new_day.title()}"
    if d_to_add == 1:
        new_time += f" (next day)"
    if d_to_add > 1:
        new_time += f" ({d_to_add} days later)"
    return new_time
