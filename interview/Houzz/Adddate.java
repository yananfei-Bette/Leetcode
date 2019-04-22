package laiofferAlgorithm.src.laiofferAlgorithm.Houzz;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;


public class Adddate {


    private int year;
    private int month;
    private int day;

    public Adddate(int year, int month,int day) {
        this.day = day;
        this.month = month;
        this.year = year;
    }

    public void addDays(int days) {

        //when adding year
        while(days > 365) {
            // only on the day of leap year, will lose one day
            if(isLeap(year) && month == 2 && day == 29 ) {
                days -= 365;
                year ++;
                day = 28;

                // adding one year -366
                // this year is leap year and before the day
                // or after the day and next year is leap year
            } else if (isLeap(year) && month <= 2 && day <= 28 || (isLeap(year + 1) && month > 2)){
                days -= 366;
                year++;

            } else {
                days -= 365;
                year++;

            }
        }

        //when remaining can still add to new year
        int remain = remainDays();
        if (remain < days) {
            year++;
            month = 1;
            day = 1;
            days = days - remain - 1;
        }

        //add month
        if (days > 31) {
            if (!isLeap(year)) {
                days = days - (Month.values()[month].days - day + 1);
                day = 1;
                month++;
                while (days > 31) {
                    days = days - Month.values()[month].days;
                    month++;
                }
            } else {
                days = days - (Month_LEAP.values()[month].days - day + 1);
                day = 1;
                month++;
                while (days > 31) {
                    days = days - Month_LEAP.values()[month].days;
                    month++;
                }
            }

        }

        //add days
        if (!isLeap(year)) {
            if (day + days > Month.values()[month].days) {
                day = days - (Month.values()[month].days - day);
                if (month == 12) {
                    year++;
                    month = 1;

                } else {
                    month++;

                }


            } else {
                day += days;

            }
        } else {

            if (day + days > Month_LEAP.values()[month].days) {
                day = days - (Month_LEAP.values()[month].days - day);
                if (month == 12) {
                    year++;
                    month = 1;

                } else {
                    month++;

                }


            } else {
                day += days;

            }

        }



    }

    public int remainDays() {
        int remain = 0;
        int curMonth = month;

        if (isLeap(year)) {

            remain += Month_LEAP.values()[curMonth].days- day;
            while (curMonth < 12) {
                curMonth++;
                remain += Month_LEAP.values()[curMonth].days;
            }

        } else {

            remain += Month.values()[curMonth].days - day;
            while (curMonth < 12) {
                curMonth++;
                remain += Month.values()[curMonth].days;
            }

        }

        return remain;

    }


    public boolean isLeap(int year) {
        if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) {
            return true;
        }
        return false;
    }






    enum Month{
        NULL(0),
        JAN(31),
        FEB(28),
        MAR(31),
        APR(30),
        MAY(31),
        JUN(30),
        JUL(31),
        AUG(31),
        SEP(30),
        OCT(31),
        NOV(30),
        DEC(31);


        private final int days;

        Month(int days) {
            this.days = days;
        }

    }

    enum Month_LEAP{
        NULL(0),
        JAN(31),
        FEB(29),
        MAR(31),
        APR(30),
        MAY(31),
        JUN(30),
        JUL(31),
        AUG(31),
        SEP(30),
        OCT(31),
        NOV(30),
        DEC(31);


        private final int days;

        Month_LEAP(int days) {
            this.days = days;
        }


    }

    public static void main(String[] args) throws ParseException {

        Adddate test = new Adddate(2000, 2, 1);
        Calendar c = Calendar.getInstance();

        String dt = "2000-02-01";  // Start date
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");


        int[] days = {0, 10, 31, 365, 366, 1000, 3000};
        for (int i = 0; i < days.length; i++) {
            test.addDays(days[i]);
            System.out.print(test.year + "-");
            System.out.print(test.month + "-");
            System.out.print(test.day + "-");
            System.out.println();


            // actual
            c.setTime(sdf.parse(dt));
            c.add(Calendar.DATE, days[i]);  // number of days to add
            dt = sdf.format(c.getTime());  // dt is now the new date

            System.out.println(dt);
            System.out.println();
        }

    }

}
