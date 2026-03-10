package org.example;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        try {

            System.out.println("1. INR to USD");
            System.out.println("2. USD to INR");
            System.out.print("Select type (1 or 2): ");

            int choice = scanner.nextInt();

            String targetCurrency;

            if (choice == 1) {
                targetCurrency = "usd";
            } else if (choice == 2) {
                targetCurrency = "inr";
            } else {
                System.out.println("Invalid choice");
                return;
            }

            System.out.print("Enter amount: ");
            double amount = scanner.nextDouble();

            String url = "http://localhost:3000/convert?to="
                    + targetCurrency + "&amount=" + amount;

            HttpClient client = HttpClient.newHttpClient();

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .GET()
                    .build();

            HttpResponse<String> response = client.send(
                    request,
                    HttpResponse.BodyHandlers.ofString()
            );

            String body = response.body();

            // Print response from server
            System.out.println("Server Response: " + body);

            if (body.contains("\"to\":")) {

                String value = body.split("\"to\":")[1]
                        .replace("}", "")
                        .trim();

                double result = Double.parseDouble(value);

                System.out.println("Converted Amount: " + result);

            } else {
                System.out.println("Invalid response from server");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        scanner.close();
    }
}
