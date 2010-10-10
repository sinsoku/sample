package sinsoku.sample;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Iterator;

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

	@Test
	public void test_codePointCount() throws Exception {
		String str = "0z?!あ表";
		assertThat(str.codePointCount(0, 0), is(0));
		assertThat(str.codePointCount(0, 1), is(1));
		assertThat(str.codePointCount(0, 2), is(2));
		assertThat(str.codePointCount(0, 3), is(3));
		assertThat(str.codePointCount(0, 4), is(4));
	}

	@Test
	public void test_getChars() throws Exception {
		char[] dist = { '0', '1', '2', '3', '4', '5' };
		"abc".getChars(0, 2, dist, 2);

		Character[] cexpected = {'0', '1', 'a', 'b', '4', '5'};
		ArrayList<Character> expected = new ArrayList<Character>();
		for (Character c : cexpected) {
			expected.add(c);
		}

		ArrayList<Character> actual = new ArrayList<Character>();
		for (Character c : dist) {
			actual.add(c);
		}

		assertThat(actual, is(expected));
	}
}
