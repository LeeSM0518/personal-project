package mapper;

import dto.Course;
import dto.Seat;
import dto.SelectCourseListByRoomIdResponse;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import java.util.List;

public interface RoomMapper {

  @Select("select c.id, c.title, c.startTime, c.endTime, c.day, p.name, c._class " +
      "from room r, course c, professor p where r.id = #{roomId} and c.professorId = p.id and r.id = c.roomId")
  List<SelectCourseListByRoomIdResponse> selectCourseListByRoomId(@Param("roomId") int roomId);

  @Select("select s.id, s.seatNumber, s.status " +
      "from course c, seat s " +
      "where c.id=#{courseId} and c.roomId = s.roomId")
  List<Seat> selectSeatListByCourseId(@Param("courseId") int id);

  @Update("update seat " +
      "set status=#{status} " +
      "where id=#{id}")
  void updateSeat(Seat seat);

}
