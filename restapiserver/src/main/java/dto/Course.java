package dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.sql.Time;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Course {

  private int id;
  private String title;
  private Time startTime;
  private Time endTime;
  private int _class;
  private String day;
  private String name;
  private String dong;
  private String ho;

}
