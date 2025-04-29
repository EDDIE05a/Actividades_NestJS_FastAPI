package org.example.logic;

import org.example.model.Product;
import java.util.*;

public class Inventory {
    private Map<Integer, Product> products = new HashMap<>();

    public void addProduct(Product product) {
        products.put(product.getId(), product);
    }

    public void deleteProduct(int id) {
        products.remove(id);
    }

    public void updateProduct(Product product) {
        products.put(product.getId(), product);
    }

    public List<Product> listProduct() {
        return new ArrayList<>(products.values());
    }

    public Product searchById(int id) {
        return products.get(id);
    }

    public List<Product> filterByName(String name) {
        List<Product> result = new ArrayList<>();
        for (Product p : products.values()) {
            if (p.getName().toLowerCase().contains(name.toLowerCase())) {
                result.add(p);
            }
        }
        return result;
    }
}
