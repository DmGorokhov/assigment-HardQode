
INSERT INTO Products (title, description, owner_id, created_at)
VALUES ('Product 1', 'Description 1', 1, '2023-09-21 10:00:00'),
       ('Product 2', 'Description 2', 2, '2023-09-21 11:00:00'),
       ('Product 3', 'Description 3', 1, '2023-09-21 12:00:00');

-- Insert fake data into the ProductMembers table
INSERT INTO ProductMembers (product_id, member_id, created_at)
VALUES (1, 1, '2023-09-21 10:00:00'),
       (1, 2, '2023-09-21 10:30:00'),
       (2, 2, '2023-09-21 11:30:00');

-- Insert fake data into the Lessons table
INSERT INTO Lessons (name, content_src_link, playback_duration_sec, created_at)
VALUES ('Lesson 1', 'https://example.com/lesson1', 600, '2023-09-21 10:00:00'),
       ('Lesson 2', 'https://example.com/lesson2', 900, '2023-09-21 11:00:00'),
       ('Lesson 3', 'https://example.com/lesson3', 1200, '2023-09-21 12:00:00');

-- Insert fake data into the ProductsLessons table
INSERT INTO ProductsLessons (product_id, lesson_id)
VALUES (1, 1),
       (1, 2),
       (2, 2),
       (3, 3);

-- Insert fake data into the LessonsReviews table
INSERT INTO LessonsReviews (lesson_id, user_id, product_members_id, lesson_duration_sec, lesson_view_duration_sec, viewing_status, created_at, updated_at)
VALUES (1, 1, NULL, 600, 450, 'Просмотрено', '2023-09-21 10:00:00', '2023-09-21 10:30:00'),
       (1, 2, 1, 600, 0, 'Не просмотрено', '2023-09-21 10:30:00', '2023-09-21 10:30:00'),
       (2, 2, 2, 900, 750, 'Просмотрено', '2023-09-21 11:30:00', '2023-09-21 11:30:00');
