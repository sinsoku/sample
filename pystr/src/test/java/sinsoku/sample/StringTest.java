package sinsoku.sample;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

import org.junit.Test;


public class StringTest {
	@Test
	public void test_codePointAt() throws Exception {
		String str = "0z?!あ表";
		assertThat(str.codePointAt(0), is(48));
		assertThat(str.codePointAt(1), is(122));
		assertThat(str.codePointAt(2), is(63));
		assertThat(str.codePointAt(3), is(33));
		assertThat(str.codePointAt(4), is(12354));
		assertThat(str.codePointAt(5), is(34920));
	}

	@Test
	public void test_codePointBefore() throws Exception {
		String str = "0z?!あ表";
		assertThat(str.codePointBefore(1), is(48));
		assertThat(str.codePointBefore(2), is(122));
		assertThat(str.codePointBefore(3), is(63));
		assertThat(str.codePointBefore(4), is(33));
		assertThat(str.codePointBefore(5), is(12354));
		assertThat(str.codePointBefore(6), is(34920));
	}
}
