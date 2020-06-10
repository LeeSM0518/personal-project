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
public class SelectCourseListByRoomIdResponse {

  private int id;
  private String title;
  private Time startTime;
  private Time endTime;
  private String day;
  private String name;
  private String _class;

}
