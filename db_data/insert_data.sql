INSERT INTO hotel (name, location, services, rooms_quantity, image_id) VALUES 
('Cosmos Collection Altay Resort', 'Republic of Altai, Maiminsky district, Urlu-Aspak village, St. Lesohozyainaya, 20', '["Wi-Fi", "Pool", "Parking", "Air conditioner"]', 15, 1),
('Skala', 'Republic of Altai, Maiminsky district, Barangol village, St. Chuyskaya 40а', '["Wi-Fi", "Parking"]', 23, 2),
('Aru-Kel', 'Republic of Altai, Turochaksky district, Artybash village, St. Teletskaya, 44А', '["Parking"]', 30, 3),
('Hotel Syktyvkar', 'Republic of Komi, Syktyvkar, St. Communisticheskaya, 67', '["Wi-Fi", "Parking", "GYM"]', 55, 4),
('Palace', 'Republic of Komi, Syktyvkar, St. Pervomayskata, 62', '["Wi-Fi", "Parking", "Air conditioner in the room"]', 22, 5),
('Bridge Resort', 'Urban-type settlement Sirius, St. Figurnaya, 45', '["Wi-Fi", "Parking", "Air conditioner in the room", "GYM"]', 45, 6);

INSERT INTO room (hotel_id, name, price, quantity, services, image_id) VALUES
(1, 'Superior with terrace and lake view', 245, 5, '["Free Wi‑Fi", "Air conditioner (with climate control)"]', 7),
(1, 'Deluxe Plus', 224, 10, '["Free Wi‑Fi", "Air conditioner"]', 8),
(2, 'Room for 2 people', 45, 15, '[]', 9),
(2, 'Room for 3 people', 43, 8, '[]', 10),
(3, 'Junior suite family room with 1 double bed', 70, 20, '["Fridge"]', 11),
(3, 'Comfort 2-room suite', 98, 10, '[]', 12),
(4, 'Standard double', 43, 20, '["Free Wi‑Fi", "Fridge"]', 13),
(4, 'Standard improved PLUS', 47, 35, '["Free Wi-Fi", "Fridge", "Jacuzzi", "Air conditioner"]', 14),
(5, 'Standard room with 2 single beds (breakfast included)', 50, 15, '[]', 15),
(5, 'Premium junior suite (breakfast included)', 80, 7, '[]', 16),
(6, 'Standard (standard housing)', 81, 45, '[]', 17);

INSERT INTO user_account (email, hashed_password) VALUES 
('user1_pass_123_@gmail.com', '$2b$12$s9Q.HTnN07kNWsw1pAMJNuZghCVuZD3wsmGNmzcOCpiDyQzhMESt6'), -- password: 123
('user2_pass_abc_@gmail.com', '$2b$12$vx6ARKBSwLpnSC0sD3GMPOhHeNFsq5EsGvOZF7Fk1kW7dhvwX41tm'); -- password: abc

INSERT INTO booking (room_id, user_account_id, date_from, date_to, price) VALUES
(1, 1, '2023-06-15', '2023-06-30', 3675),
(7, 2, '2023-06-25', '2023-07-10', 645);
