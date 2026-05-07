package practical_8_java_RMI;

import java.rmi.Naming;
import java.util.Map;
import java.util.Scanner;

public class HotelClient {

    public static void main(String[] args) {

        try {

            HotelServiceInterface hotelService =
                (HotelServiceInterface)
            Naming.lookup(
                "rmi://localhost/HotelService");

            Scanner scanner = new Scanner(System.in);

            while (true) {

                System.out.println("1. Book a room");
                System.out.println("2. Cancel booking");
                System.out.println("3. Show booked room details");
                System.out.println("4. Exit");

                System.out.print("Enter your choice: ");

                int choice = scanner.nextInt();

                scanner.nextLine();

                switch (choice) {

                    case 1:

                        System.out.print(
                            "Enter guest name: ");

                        String guestName =
                            scanner.nextLine();

                        System.out.print(
                            "Enter room number: ");

                        int roomNumber =
                            scanner.nextInt();

                        boolean booked =
                            hotelService.bookRoom(
                                guestName,
                                roomNumber);

                        if (booked) {

                            System.out.println(
                                "Room booked successfully!");

                        } else {

                            System.out.println(
                                "Room booking failed.");
                        }

                        break;

                    case 2:

                        System.out.print(
                            "Enter guest name for cancellation: ");

                        String cancelGuestName =
                            scanner.nextLine();

                        boolean canceled =
                            hotelService.cancelBooking(
                                cancelGuestName);

                        if (canceled) {

                            System.out.println(
                                "Booking canceled successfully!");

                        } else {

                            System.out.println(
                                "Booking cancellation failed.");
                        }

                        break;

                    case 3:

                        Map < Integer, String > bookedRooms =
                            hotelService.showBookedRoomDetails();

                        System.out.println();

                        System.out.println(
                            "+----------------------+------------+"
                        );

                        System.out.printf(
                            "| %-20s | %-10s |\n",
                            "Guest Name",
                            "Room No."
                        );

                        System.out.println(
                            "+----------------------+------------+"
                        );

                        for (Map.Entry < Integer, String > entry: bookedRooms.entrySet()) {

                            Integer roomNo = entry.getKey();

                            String name = entry.getValue();

                            System.out.printf(
                                "| %-20s | %-10d |\n",
                                name,
                                roomNo
                            );
                        }

                        System.out.println(
                            "+----------------------+------------+"
                        );

                        System.out.println();

                        break;

                    case 4:

                        System.out.println(
                            "Exiting application.");

                        System.exit(0);

                    default:

                        System.out.println(
                            "Invalid choice.");
                }
            }

        } catch (Exception e) {

            e.printStackTrace();
        }
    }
}