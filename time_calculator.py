import re;
import math;

def add_time(start, duration, day='null'):

    start_AM_PM = re.findall('[a-zA-Z]+', start);
    start_time = re.findall('\d+:\d+',start);
    s_t = start_time[0].split(":");
    start_hours = int(s_t[0]);
    start_minutes = int(s_t[1]);
 
    total_start_in_minutes = (start_hours * 60) + start_minutes;

    d_t = duration.split(":");
    dur_hours = int(d_t[0]);
    dur_minutes = int(d_t[1]);

    total_dur_in_minutes = (dur_hours * 60) + dur_minutes;
 
    total_in_minutes = total_start_in_minutes + total_dur_in_minutes;

    mins = total_in_minutes % 60;

    if day != 'null':
      day = (day.lower()).capitalize();

    hrs = total_in_minutes // 60;
    if mins < 10:
      mins = '0' + str(mins);
    else:
      mins = str(mins);

    new_time = '';
    no_of_days = math.ceil(total_dur_in_minutes/1440);


    if start_AM_PM[0] == 'AM':
      if total_in_minutes < 720:
        if day != 'null':
          new_time += str(hrs) + ':' + mins + ' AM, ' + day;  
        else:
          new_time += str(hrs) + ':' + mins + ' AM';
        
      elif total_in_minutes < 1440:      
        if hrs > 12:
          hrs -= 12;
        if day != 'null':
          new_time += str(hrs) + ':' + mins + ' PM, ' + day;
        else:
          new_time += str(hrs) + ':' + mins + ' PM';
      elif total_in_minutes < 2160:
        hrs -= 24;
        if day != 'null':
          no_of_days = 1;
          return selected_day(day, no_of_days, hrs, mins, False);
        else:
          new_time += str(hrs) + ':' + mins + ' AM (next day)';
      else :               
        mins_remain = total_dur_in_minutes % 1440;

        if mins_remain < 720:
          hrs_am = (mins_remain // 60) + start_hours;
          mins_am = (mins_remain % 60) + start_minutes;
          if mins_am < 10:
            mins_am = '0' + str(mins_am);
          else:
            mins_am = str(mins_am);
          if day != 'null':
            return selected_day(day, no_of_days, hrs_am, mins_am, 'AM');
          else:
            new_time += str(hrs_am) + ':' + mins_am + ' AM ' + '(' + str(no_of_days) + ' days later)';

        elif mins_remain < 1440:
          hrs_pm = (mins_remain // 60) + start_hours;
          mins_pm = (mins_remain % 60) + start_minutes;
          hrs_pm -= 12;
          if mins_pm < 10:
            mins_pm = '0' + str(mins_pm);
          else:
            mins_pm = str(mins_pm);

          if day != 'null':
            return selected_day(day, no_of_days, hrs_pm, mins_pm, 'PM');
          else:
            new_time += str(hrs_pm) + ':' + mins_pm + ' PM ' + '(' + str(no_of_days) + ' days later)';

    elif start_AM_PM[0] == 'PM':
      if total_in_minutes < 720:
        if day != 'null':
          new_time += str(hrs) + ':' + mins + ' PM, ' + day;  
        else:
          new_time += str(hrs) + ':' + mins + ' PM';

      elif total_in_minutes < 1440:
        if hrs > 12:
          hrs -= 12;

        if day != 'null':
          no_of_days = 1;
          return selected_day(day, no_of_days, hrs, mins, False)
        else:
          new_time += str(hrs) + ':' + mins + ' AM (next day)';

      else:   
        mins_remain = total_in_minutes % 1440;
        if mins_remain < 720: 
          hrs_am = (mins_remain // 60);
          mins_am = (mins_remain % 60);
          if mins_am < 10:
            mins_am = '0' + str(mins_am);
          else:
            mins_am = str(mins_am);
          
          if day != 'null':
            return selected_day(day, no_of_days, hrs_am, mins_am, 'PM');
          else:
            new_time += str(hrs_am) + ':' + mins_am + ' PM ' + '(' + str(no_of_days) + ' days later)';

        elif mins_remain < 1440:
          hrs_pm = (mins_remain // 60);
          mins_pm = (mins_remain % 60);
          if hrs_pm > 12:
            hrs_pm -= 12;
          if mins_pm < 10:
            mins_pm = '0' + str(mins_pm);
          else:
            mins_pm = str(mins_pm);

          if day != 'null':
            return selected_day(day, no_of_days, hrs_pm, mins_pm, 'AM');
          else: 
            new_time += str(hrs_pm) + ':' + mins_pm + ' AM ' + '(' + str(no_of_days) + ' days later)';

    return new_time

def selected_day(day, no_of_days, hrs, mins, am_pm):
  
  new_time = '';
  day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
  index_no = day_of_week.index(day);
  days_plus_index = index_no + no_of_days;
  day_select = '';

  if days_plus_index < 7:
    day_select += day_of_week[days_plus_index];
  else:
    new_index = days_plus_index % 7;
    day_select += day_of_week[new_index];

  if no_of_days == 1 and not am_pm:
    new_time += str(hrs) + ':' + mins + ' AM, ' + day_select + ' (next day)';
  elif am_pm == 'PM':
    new_time += str(hrs) + ':' + mins + ' PM, ' + day_select + ' (' + str(no_of_days) + ' days later)';
  elif am_pm == 'AM':
    new_time += str(hrs) + ':' + mins + ' AM, ' + day_select + ' (' + str(no_of_days) + ' days later)';
  
  return new_time