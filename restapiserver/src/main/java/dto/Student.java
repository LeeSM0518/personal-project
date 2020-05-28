package dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Student {

  private int id;
  private String studentCode;
  private String name;
  private String password;
  private String fingerprint;

}
