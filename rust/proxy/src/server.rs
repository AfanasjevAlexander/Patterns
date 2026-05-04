mod application;
mod nginx;

pub use nginx::NginxServer;

type RequestStatus = (u16, String);

pub trait Server {
    fn handle_request(&mut self, url: &str, method: &str) -> RequestStatus;
}