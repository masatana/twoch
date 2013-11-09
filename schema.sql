CREATE TABLE downloaded_thread (
    id INT PRIMARY KEY NOT NULL,
    download_data TEXT,
    title TEXT
);

CREATE TABLE downloaded_image (
    id TEXT PRIMARY KEY NOT NULL,
    download_data TEXT
);
