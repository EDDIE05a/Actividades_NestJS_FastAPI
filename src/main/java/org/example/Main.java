package org.example;

import org.example.logic.Inventory;
import org.example.model.Product;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Inventory inventory = new Inventory();
        Scanner scanner = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\n=== MENÚ INVENTARIO ===");
            System.out.println("1. Agregar producto");
            System.out.println("2. Eliminar producto");
            System.out.println("3. Actualizar producto");
            System.out.println("4. Listar productos");
            System.out.println("5. Buscar producto por ID");
            System.out.println("6. Filtrar producto por nombre");
            System.out.println("0. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine(); // limpiar el buffer

            switch (opcion) {
                case 1:
                    System.out.print("ID: ");
                    int id = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("Nombre: ");
                    String name = scanner.nextLine();
                    System.out.print("Descripción: ");
                    String description = scanner.nextLine();
                    System.out.print("Precio: ");
                    double price = scanner.nextDouble();
                    System.out.print("Cantidad: ");
                    int quantity = scanner.nextInt();
                    Product newProduct = new Product(id, name, description, price, quantity);
                    inventory.addProduct(newProduct);
                    System.out.println("Producto agregado.");
                    break;

                case 2:
                    System.out.print("ID del producto a eliminar: ");
                    int deleteId = scanner.nextInt();
                    inventory.deleteProduct(deleteId);
                    System.out.println("Producto eliminado si existía.");
                    break;

                case 3:
                    System.out.print("ID del producto a actualizar: ");
                    int updateId = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("Nuevo nombre: ");
                    String newName = scanner.nextLine();
                    System.out.print("Nueva descripción: ");
                    String newDescription = scanner.nextLine();
                    System.out.print("Nuevo precio: ");
                    double newPrice = scanner.nextDouble();
                    System.out.print("Nueva cantidad: ");
                    int newQuantity = scanner.nextInt();
                    Product updatedProduct = new Product(updateId, newName, newDescription, newPrice, newQuantity);
                    inventory.updateProduct(updatedProduct);
                    System.out.println("Producto actualizado.");
                    break;

                case 4:
                    System.out.println("\n--- Lista de productos ---");
                    inventory.listProduct().forEach(p ->
                            System.out.println(p.getId() + " - " + p.getName() + " (" + p.getQuantity() + " unidades)")
                    );
                    break;

                case 5:
                    System.out.print("ID del producto a buscar: ");
                    int searchId = scanner.nextInt();
                    Product found = inventory.searchById(searchId);
                    if (found != null) {
                        System.out.println("Encontrado: " + found.getName() + ", Precio: " + found.getPrice());
                    } else {
                        System.out.println("Producto no encontrado.");
                    }
                    break;

                case 6:
                    System.out.print("Nombre a filtrar: ");
                    String filterName = scanner.nextLine();
                    System.out.println("Resultados:");
                    inventory.filterByName(filterName).forEach(p ->
                            System.out.println(p.getId() + " - " + p.getName())
                    );
                    break;

                case 0:
                    System.out.println("Saliendo del sistema...");
                    break;

                default:
                    System.out.println("Opción inválida.");
            }

        } while (opcion != 0);

        scanner.close();
    }
}
