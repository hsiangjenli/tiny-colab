package com.hsiangjenli;

import com.enofex.taikai.Taikai.Builder;
import io.quarkus.test.junit.QuarkusTest;
import org.junit.jupiter.api.Test;

@QuarkusTest
public class ArchitectureTest {

  @Test
  void shouldValidateJavaRules() {
    Builder builder = new Builder();
    builder.namespace("com.hsiangjenli").java(ArchitectureRules.BASE_JAVA_RULES).build().checkAll();
  }
}
