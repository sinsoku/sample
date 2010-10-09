package sinsoku.sample;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

import org.junit.Test;

public class PystrTest {
	@Test
	public void インスタンスを新規作成() throws Exception {
		Pystr pystr = new Pystr();
		assertThat(pystr.toString(), is(""));
	}
}
