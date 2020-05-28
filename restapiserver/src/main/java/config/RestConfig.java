package config;

import controller.LoginController;
import controller.LoginExceptionAdvice;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import service.LoginService;

@Configuration
@EnableWebMvc
@ComponentScan({"controller", "service"})
public class RestConfig {

}
