use super::{RequestStatus, Server};

pub struct Application;

impl Server for Application {
    fn handle_request(&mut self, url: &str, method: &str) -> RequestStatus {
        if url == "/app/status" && method == "GET" {
            return (200, "Ok".into());
        }

        if url == "/create/user" && method == "POST" {
            return(201, "User created".into());
        }

        (404, "Not Ok".into())
    }
}